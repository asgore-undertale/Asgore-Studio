from Parts.Scripts.UsefulLittleFunctions import getRegexPattern, Split
from Parts.Scripts.FreezeArabic import Freeze
import re

def increase_y(y : int, text : str):
    if y == fit.linesNum - 1: return 0, fit.newPage + text
    else: return y + 1, fit.newLine + text

def handle_xy(x : int, y : int, textWidth : int, newtext : str):
    if x + textWidth > fit.boxWidth:
        x += textWidth
        y, newtext = increase_y(y, newtext)
    else: x += textWidth
    return x, y, newtext

def checkChar(char : str):
    if char not in fit.charmap:
        print(f'{char} not in charmap.')
        return True
    if fit.charmap[char][2] + fit.charmap[char][6] > fit.boxWidth:
        print(f'{char} is wider than Textzone.')
        return True

def checkWord(word : str, x : int, y : int, case : bool, newword = ''):
    if case:
        for char in word:
            if checkChar(char): continue
            x, y, newword = handle_xy(x, y, fit.charmap[char][2] + fit.charmap[char][6], newword)
            newword += char
    else:
        for char in word:
            if checkChar(char): continue
            newword += char
        x = getTextWidth(newword)
        y, newword = increase_y(y, newword)
    return newword, x, y

def getTextWidth(text : str, width = 0):
    for char in text:
        if checkChar(char): continue
        width += fit.charmap[char][2] + fit.charmap[char][6]
    return width

def splitTo(text : str, case : bool, beforeCom = '', afterCom = ''):
    if case:
        if beforeCom and afterCom:
            partsList = re.split(getRegexPattern(beforeCom, afterCom), text)
        else: partsList = [text]
        
    else:
        partsList = text.split(' ')
        for i in range(len(partsList) - 1): partsList.insert(i * 2 + 1, ' ')
    
    return partsList

def fit(text : str, charmap : dict, boxWidth : int, linesNum : int, newLine : str, newPage : str, beforeCom : str, afterCom : str):
    if not linesNum: return ''
    x, y, fit.newtext = 0, 0, ''
    fit.boxWidth, fit.linesNum, fit.newLine, fit.newPage = boxWidth, linesNum, newLine, newPage
    fit.charmap = charmap
    
    pages = Split(text, newPage)
    for p in range(len(pages)):
        sentences = Split(pages[p], newLine)
        for s in range(len(sentences)):
            if p and not s: fit.newtext += newPage
            if s: fit.newtext += newLine
            parts = splitTo(sentences[s], True, beforeCom, afterCom)
            for c in range(len(parts)):
                if not parts[c]: continue
                if c % 2:
                    fit.newtext += beforeCom + parts[c] + afterCom
                    if parts[c] == newPage: x, y = 0, 0
                    elif parts[c] == newLine: x, y = 0, increase_y(y)
                    continue
                
                parts[c] = Freeze(parts[c])
                wordsList = splitTo(parts[c], False)
                
                for word in wordsList:
                    if not word: continue
                    wordWidth = getTextWidth(word)
                    if x + wordWidth > boxWidth and wordWidth < boxWidth:
                        word, x, y = checkWord(word, x, y, False)
                    elif x + wordWidth > boxWidth:
                        word, x, y = checkWord(word, x, y, True)
                    else:
                        word, x, y = checkWord(word, x, y, True)
                    fit.newtext += word
    
    return fit.newtext