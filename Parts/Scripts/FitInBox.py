from Parts.Scripts.UsefulLittleFunctions import getRegexPattern, splitTextBySoperators
from Parts.Scripts.FreezeArabic import Freeze
import re

def increase_y(y : int, text : str, before = False):
    if before: a, b = text + fit.newPage, text + fit.newLine
    else: a, b = fit.newPage + text, fit.newLine + text
    if y == fit.linesNum - 1: return 0, a
    else: return y + 1, b

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
            newword += char
            x, y, newword = handle_xy(x, y, fit.charmap[char][2] + fit.charmap[char][6], newword)
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
            return re.split(getRegexPattern(beforeCom, afterCom), text)
        else: return [text]
    else:
        return splitTextBySoperators(text, [' '])

def fit(text : str, charmap : dict, boxWidth : int, linesNum : int, newLine : str, newPage : str, beforeCom : str, afterCom : str):
    if not linesNum: return ''
    x, y, newtext = 0, 0, ''
    fit.boxWidth, fit.linesNum, fit.newLine, fit.newPage = boxWidth, linesNum, newLine, newPage
    fit.charmap = charmap
    
    sentences = splitTextBySoperators(text, (newPage, newLine))
    for s in range(len(sentences)):
        if s % 2:
            x = 0
            if sentences[s] == newPage: y, newtext = 0, newtext + sentences[s]
            elif sentences[s] == newLine: y, newtext = increase_y(y, newtext, True)
            continue
            
        parts = splitTo(sentences[s], True, beforeCom, afterCom)
        for c in range(len(parts)):
            if not parts[c]: continue
            if c % 2:
                newtext += beforeCom + parts[c] + afterCom
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
                newtext += word
    
    return newtext