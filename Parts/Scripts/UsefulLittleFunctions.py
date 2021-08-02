from PyQt5.QtWidgets import QFileDialog
from os import path, walk
import re

def openFile(type : tuple, window, text = 'جدول حروف'):
    type = '*.'+' *.'.join(type)
    _open, _ = QFileDialog.getOpenFileName(window, text, '', type)
    return _open * (_open != '/') * (_open != '') * (path.exists(_open))

def saveFile(type : tuple, window, text = 'جدول حروف'):
    type = '*.'+' *.'.join(type)
    _save, _ = QFileDialog.getSaveFileName(window, text, '', type)
    return _save * (_save != '/') * (_save != '')

def selectFolder(window, text = 'اختر مجلداً'):
    _select = QFileDialog.getExistingDirectory(window, text, '')+'/'
    return _select * (_select != '/') * (_select != '') * (path.exists(_select))

def intToHex(num):
    hexstring = str(hex(num)).replace("0x","")
    return (len(hexstring) % 2 * '0') + hexstring

def hexToString(hexstring):
    hexstring = '0'*(len(hexstring) % 2) + hexstring
    return bytearray.fromhex(hexstring).decode(encoding='utf8', errors='replace')

def bytesToString(Bytes):
    try: Bytes = Bytes.decode()
    except:
        Bytes = str(Bytes)[2:-1].replace("\\'", "'").replace('\\"', '"').replace('\\\\', '\\').replace('\\r\\n', '\\n').replace('\\n', '\n')
    return Bytes

def stringToHex(string):
    return string.encode().hex()

def sortDictByKeyLengh(Dict):
    newDict = {}
    for k in sorted(Dict, key=len, reverse=True):
        newDict[k] = Dict[k]
    return newDict

def tryTakeNum(string : str, defaultNum = 0, isInt = True):
    try:
        num = float(string)
        if isInt: return int(num)
        return num
    except: return defaultNum

def checkForCommand(command : str, text : str, currentIndex : int):
    try:
        for i in range(len(command)):
            if command[i] != text[currentIndex+i]: return
        return True
    except: pass

def splitTextBySoperators(text : str, soperators : tuple):
    sentence, sentences, passTimes, Pass = '', [], 0, False
    try:
        for i in range(len(text)):
            if passTimes:
                passTimes -= 1
                continue
            
            for soperator in soperators:
                if checkForCommand(soperator, text, i):
                    sentences.append(sentence)
                    sentences.append(soperator)
                    sentence, Pass = '', True
                    passTimes = len(soperator) - 1
                    break
            if Pass:
                Pass = False
                continue
            
            sentence += text[i]
        
        sentences.append(sentence)
        return sentences
    
    except: return sentences

commandsChars = '\\.[]{}*+?()^'
def fixBeforAfterCommands(beforeCom, afterCom):
    for char in commandsChars:
        toChar = '\\'+char
        if isinstance(beforeCom, bytes):  char, toChar = char.encode(), toChar.encode()
        beforeCom = beforeCom.replace(char, toChar)
        afterCom = afterCom.replace(char, toChar)
    return beforeCom, afterCom

def getRegexPattern(beforeCom, afterCom):
    beforeCom, afterCom = fixBeforAfterCommands(beforeCom, afterCom)
    middle = "(.*?)"
    if isinstance(beforeCom, bytes):  middle = middle.encode()
    return beforeCom + middle + afterCom

def SortLines(text, lineCom = '\n', case = True):
    if not lineCom: lineCom = '\n'

    linesList = text.split(lineCom)
    linesList.sort(key=len)
    if not case: linesList = linesList[::-1]
    text = lineCom.join(linesList)
    
    return text

def DeleteDuplicatedLines(text, lineCom = '\n'):
    if not lineCom: lineCom = '\n'
    
    lines_list = text.split(lineCom)
    deleted_lines_list = list(dict.fromkeys(lines_list))
    text = lineCom.join(deleted_lines_list)
    return text

def dirList(path):
    if path[0] == '"' and path[-1] == '"': path = path[1:-1]
    return [root+'\\{}'.format(f) for root, dirs, files in walk(path) for f in files]

def splitByBeforeAfterComAndDo(text, beforeCom, afterCom, function, reverse = False):
    if beforeCom and afterCom:
        if beforeCom == afterCom:
            textList = text.replace(afterCom, beforeCom, text.count(beforeCom)).split(beforeCom)
        else:
            textList = re.split(getRegexPattern(beforeCom, afterCom), text)
        
        for i in range(len(textList)):
            textList[i] = (i%2 > 0) * (beforeCom + textList[i] + afterCom) + function((not i%2) * textList[i])
        
        if reverse: textList = textList[::-1]
        return ''.join(textList)
    else:
        return function(text)

def Split(text, splitter):
    if splitter: return text.split(splitter)
    else: return [text]

def byteInCell(text, subject = '[b]'):
    if not subject in text: return text
    return hexToString(text.replace(subject, ''))

bowsList = ['()', '[]', '{}', '<>']
def swap(text, bowsList, unused_char = u'\uffff'):
    for bow in bowsList:
        text.replace(bow[0], unused_char).replace(bow[1], bow[0]).replace(unused_char, bow[1])
    return

def fixSlashes(text):
    return text.replace(r'\n', '\n').replace(r'\r', '\r').replace(r'\t', '\t').replace(r'\0', '\0')

def swapCharsOnEdges(text, char):
    if len(text) < 2: return text
    charsBefore, charsAfter = 0, 0
    
    while text[0] == char:
        charsBefore += 1
        text = text[1:len(text)]
    while text[-1] == char:
        charsAfter += 1
        text = text[0:-1]
    
    return (charsBefore * char) + text + (charsAfter * char)