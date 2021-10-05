from Parts.Vars import bowsList, ASCII
from PyQt5.QtWidgets import QFileDialog
from os import path, walk
import re

def openFile(type : tuple, window = None, text = 'جدول حروف'):
    type = '*.'+' *.'.join(type)
    _open, _ = QFileDialog.getOpenFileName(window, text, '', type)
    return _open * (_open != '/') * (_open != '') * (path.exists(_open))

def saveFile(type : tuple, window = None, text = 'جدول حروف'):
    type = '*.'+' *.'.join(type)
    _save, _ = QFileDialog.getSaveFileName(window, text, '', type)
    return _save * (_save != '/') * (_save != '')

def selectFolder(window = None, text = 'اختر مجلداً'):
    _select = QFileDialog.getExistingDirectory(window, text, '')+'/'
    return _select * (_select != '/') * (_select != '') * (path.exists(_select))

def fixHexLength(hexstring):
    return '0'*(len(hexstring) % 2) + hexstring

def fixHexbite(hexstring):
    return '0'*(len(hexstring) % 4) + hexstring

def intToHex(num):
    hexstring = str(hex(num))[2:]
    return fixHexLength(hexstring)

# def hexToString(hexstring):
    # hexstring = '0'*(len(hexstring) % 2) + hexstring
    # try:
        # return bytearray.fromhex(hexstring).decode(encoding='utf8', errors='replace')
    # except:
        # return 'Error: Byte out of range.'

def hexToString(hexstring):
    string = ''
    hexstring = fixHexbite(hexstring)
    try:
        for c in range(0, len(hexstring), 4):
            string += chr(int(hexstring[c:c+4], 16))
    except:
        string = 'Error'
    return string

# def stringToHex(string):
    # return string.encode().hex()

def stringToHex(string):
    hexvalue = ''
    for char in string:
        v = str(hex(ord(char)))[2:]
        hexvalue += fixHexLength(v)
    return hexvalue

def hexLength(text):
    hexstring = text.encode().hex()
    return len(fixHexLength(hexstring)) // 2

def bytesToString(Bytes):
    try: Bytes = Bytes.decode()
    except:
        Bytes = str(Bytes)[2:-1].replace("\\'", "'").replace('\\"', '"').replace('\\\\', '\\').replace('\\r\\n', '\\n').replace('\\n', '\n')
    return Bytes

def sortDictByKeyLengh(Dict):
    newDict = {}
    for k in sorted(Dict, key=len, reverse=True):
        newDict[k] = Dict[k]
    return newDict

def tryTakeNum(string : str, defaultNum = 0, isInt = True):
    string = str(string)
    
    if not len(string): return defaultNum
    while string[0] == '0' and len(string) > 1:
        string = string[1:len(string)]
        if not len(string): return defaultNum
    
    try:
        if isInt:
            return int(eval(string))
        return float(eval(string))
    except:
        try:
            if isInt:
                return int(float(string))
            return float(string)
        except:
            return defaultNum

def checkForCommand(command : str, text : str, currentIndex : int):
    try:
        for i in range(len(command)):
            if command[i] != text[currentIndex+i]: return
        return True
    except: pass

def splitTextBySoperators(text : str, soperators : list):
    soperators = list(filter(lambda a: a, soperators))
    if not soperators: return [text]
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
def fixRegexPattert(Pattern):
    for char in commandsChars:
        toChar = '\\'+char
        if isinstance(Pattern, bytes):  char, toChar = char.encode(), toChar.encode()
        Pattern = Pattern.replace(char, toChar)
    return Pattern

def getRegexPattern(beforeCom, afterCom):
    beforeCom, afterCom = fixRegexPattert(beforeCom), fixRegexPattert(afterCom)
    middle = "(.*?)"
    if isinstance(beforeCom, bytes): middle = middle.encode()
    return beforeCom + middle + afterCom

def SortLines(text, lineCom = '\n', sortType = 'alphabet', reverse = False):
    if not lineCom: lineCom = '\n'

    linesList = text.split(lineCom)
    
    if sortType == 'alphabet':
        linesList.sort()
    elif sortType == 'length':
        linesList.sort(key=len)
    
    if reverse:
        linesList = linesList[::-1]
    
    return lineCom.join(linesList)

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

def ToModulePath(path):
    return path.replace('/', '.').replace('\\', '.').replace('.py', '')

def minimax(num, min, max):
    minType = getType(min)
    maxType = getType(max)
    if (minType == 'int' or minType == 'float') and num < min: return
    if (maxType == 'int' or maxType == 'float') and num > max: return
    return True
    
def filterAscii(text):
    t = text
    if isinstance(text, bytes):
        t = t.decode(errors='replace')
    
    for char in t:
        if char not in ASCII:
            return
    
    return text

def getType(value):
    return str(type(value))[8:-2]