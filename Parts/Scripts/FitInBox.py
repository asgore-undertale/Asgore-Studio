from Parts.Scripts.UsefulLittleFunctions import splitTextByCommands, getRegexPattern
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
    
    sentences = splitTextByCommands((newPage, newLine), text)
    
    for s in range(len(sentences)):
        if s:
            if not s % (linesNum): fit.newtext += newPage
            else: fit.newtext += newLine
        
        sentence = splitTo(sentences[s], True, beforeCom, afterCom)
        for p in range(len(sentence)):
            if not sentence[p]: continue
            if p % 2:
                sentence[p] = beforeCom + sentence[p] + afterCom
                fit.newtext += sentence[p]
                if sentence[p] == newPage: x, y = 0, 0
                elif sentence[p] == newLine: x, y = 0, increase_y(y)
                continue
            
            sentence[p] = Freeze(sentence[p])
            words_list = splitTo(sentence[p], False)
            
            for word in words_list:
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