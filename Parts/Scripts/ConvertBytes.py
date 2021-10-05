import re
from Parts.Scripts.UsefulLittleFunctions import hexToString, fixRegexPattert, stringToHex
from Parts.Windows import StudioWindow

longestCharBytes = 2

def convertBytes(text : str, subFrom, subTo, readByteLength, resultByteLength, key = 'hextohex', table = {}, placeHolder = '', useTable = False):
    Bytesindexes = getIndexesList(text, subFrom, readByteLength)
    
    for m in re.finditer('X', subFrom):
        subFromXindex = m.start(0)
        break
    convertBytes.Report = []
    resultText = ''
    
    if key == 'hextohex':
        bytesList = mergBytes(text, subFrom, Bytesindexes, subFromXindex)
        resultText = ''.join(
            [subTo.replace('X', byte[b:b+(resultByteLength*2)], 1) for byte in bytesList for b in range(0, len(byte), resultByteLength*2)]
            )
    
    elif key == 'hextotext':
        bytesList = mergBytes(text, subFrom, Bytesindexes, subFromXindex)
        resultText = ''.join(hexToString(convertByte(byte, table, placeHolder, useTable)) for byte in bytesList)
        report()
    
    elif key == 'texttohex':
        hexText = stringToHex(convertString(text, table, placeHolder, useTable))
        resultText = ''.join(subTo.replace('X', hexText[n:n+(resultByteLength*2)]) for n in range(0, len(hexText), resultByteLength*2))
        report()
    
    elif key == 'unicodetotext':
        unicodes =  re.findall(r'\\u' + ('[A-Z, a-z, 0-9]'*4), text)
        resultText = text
        for uni in unicodes:
            uni = '\\' + uni
            resultText = re.sub(uni, chr(int(uni[3:], 16)), resultText)
    
    elif key == 'texttounicode':
        resultText = ''.join(r'\u{:04X}'.format(ord(char)) for char in text)
    
    return resultText

def getIndexesList(text, subFrom, readByteLength):
    Bytesindexes, indexesRom = [], []
    regexSubFrom = fixRegexPattert(subFrom)
    for i in range(readByteLength[0], readByteLength[1]+1):
        i = readByteLength[1]+1 - i
        _rSubFrom = regexSubFrom.replace('X', '[A-Z, a-z, 0-9]' * i*2)
        
        for m in re.finditer(_rSubFrom, text):
            if m.start(0) in indexesRom: continue
            indexesRom.append(m.start(0))
            Bytesindexes.append([m.start(0), i*2])
    
    return sorted(Bytesindexes, key=lambda x: x[0])

def report():
    strLog = '\n'.join(convertBytes.Report)
    StudioWindow.Report(f'({len(convertBytes.Report)}) عنصر غير موجود في التيبل', strLog)

def addToReport(value):
    if value in convertBytes.Report: return
    convertBytes.Report.append(value)

def mergBytes(text, subFrom, subFromindexes, subFromXindex):
    bytesList = []
    subFromLen = len(subFrom.replace('X', ''))
    for i in range(len(subFromindexes)):
        byte = text[subFromXindex+subFromindexes[i][0] : subFromXindex+subFromindexes[i][0]+subFromindexes[i][1]]
        
        # if subFromindexes[i][0] - subFromindexes[i-1][0] == subFromLen + subFromindexes[i-1][1]:
            # bytesList[-1] += byte
        # else:
        bytesList.append(byte)
    
    return bytesList

def convertString(string, table, placeHolder, useTable):
    if not table or not useTable: return string
    value = ''
    for char in string:
        for k, v in table.items():
            if char == k:
                value += v
                break
        else:
            value += placeHolder
            addToReport(char)
    return value

def convertByte(bytes, table, placeHolder, useTable):
    if not table or not useTable: return bytes
    value = ''
    passTimes = 0
    
    for i in range(0, len(bytes), 2):
        b = False
        if passTimes:
            passTimes -= 1
            continue
            
        for k, v in table.items():
            for j in range(0, longestCharBytes):
                j = longestCharBytes - j
                charBytes = bytes[i:i + (j*2)]
                if charBytes == stringToHex(v):
                    value += k
                    passTimes = j - 1
                    b = True
                    break
            if b: break
        else:
            value += placeHolder
            addToReport(hexToString(charBytes))
    
    return stringToHex(value)
