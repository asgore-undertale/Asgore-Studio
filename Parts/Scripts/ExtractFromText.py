from Parts.Scripts.UsefulLittleFunctions import getRegexPattern, filterAscii, minimax
from Parts.Vars import ASCII
import re

def Extract(text, before, after, addBeforeAfter = False, mini = False, maxi = False, onlyASCII = False):
    if not before or not after:
        if onlyASCII: return extractAscii(text)
        return
    
    _UnusedChar = (u'\uffff' * 4)
    _EnterChar  = '\n'
    
    if isinstance(before, bytes): _UnusedChar, _EnterChar = _UnusedChar.encode(), _EnterChar.encode()
    
    text = text.replace(_EnterChar, _UnusedChar)
    before = before.replace(_EnterChar, _UnusedChar)
    after = after.replace(_EnterChar, _UnusedChar)
    
    if before == after:
        extractedList = text.split(before)
        if len(extractedList) > 2:
            del extractedList[0]
            del extractedList[-1]
    else:
        extractedList = re.findall(getRegexPattern(before, after), text)
    
    if addBeforeAfter:
        extractedList = [(before+x+after).replace(_UnusedChar, _EnterChar) for x in extractedList]
    else:
        extractedList = [x.replace(_UnusedChar, _EnterChar) for x in extractedList]
    
    if onlyASCII:
        extractedList = list(map(filterAscii, extractedList))
        extractedList = list(filter(lambda a: a, extractedList))
    
    if mini or maxi:
        for i in range(len(extractedList)):
            extractedList[i] = minimax(extractedList[i], mini, maxi)
        extractedList = list(filter(lambda a: a, extractedList))
    
    return extractedList

def extractAscii(text):
    isBytes = isinstance(text, bytes)
    if isBytes: text = text.decode(errors='replace')
    
    extractedList, container = [], ''
    for char in text:
        if char in ASCII:
            container += char
        else:
            if not container: continue
            if isBytes: container = container.encode(errors='replace')
            extractedList.append(container)
            container = ''
    
    if container:
        if isBytes: container = container.encode(errors='replace')
        extractedList.append(container)
        container = ''
    
    return extractedList