import re
from Parts.Scripts.UsefulLittleFunctions import hexToString, fixRegexPattert, stringToHex

def convertBytes(text : str, subFrom, subTo, key = 'hextohex', table = {}, useTable = False):
    # if not text or not subFrom or not subTo: return text
    
    subFromXindexes = [m.start(0) for m in re.finditer('X', subFrom)]
    subFromYindexes = [m.start(0) for m in re.finditer('Y', subFrom)]
    
    regexSubFrom = fixRegexPattert(subFrom)
    regexSubFrom = regexSubFrom.replace('X', '[A-Z, a-z, 0-9]').replace('Y', '[A-Z, a-z, 0-9]')
    Bytes = re.findall(regexSubFrom, text)
    
    subFromindexes = [m.start(0) for m in re.finditer(regexSubFrom, text)]
    
    
    if key == 'hextohex':
        for uni in Bytes:
            newUni = subTo
            for x in subFromXindexes:
                newUni = newUni.replace('X', uni[x], 1)
            for y in subFromYindexes:
                newUni = newUni.replace('Y', uni[y], 1)
            text = text.replace(uni, newUni)
        
    elif key == 'hextotext':
        bytes = mergBytes(text, subFrom, subFromindexes, subFromXindexes, subFromYindexes)
        for byte in bytes:
            string = hexToString(convertByte(byte, table, useTable))
            num = len(byte)//2
            text = re.sub(regexSubFrom*num, string, text, 1)
        
    elif key == 'texttohex':
        hexText = stringToHex(convertString(text, table, useTable))
        text = ''
        for n in range(0, len(hexText), 2):
            text += subFrom.replace('X', hexText[n]).replace('Y', hexText[n+1])
    
    return text

def mergBytes(text, subFrom, subFromindexes, subFromXindexes, subFromYindexes):
    bytes = []
    for i in range(len(subFromindexes)):
        byte = ''
        if subFromindexes[i] - subFromindexes[i-1] == len(subFrom):
            for x in subFromXindexes:
                byte += text[subFromindexes[i]+x]
            for y in subFromYindexes:
                byte += text[subFromindexes[i]+y]
            bytes[-1] += byte
        else:
            for x in subFromXindexes:
                byte += text[subFromindexes[i]+x]
            for y in subFromYindexes:
                byte += text[subFromindexes[i]+y]
            bytes.append(byte)
    return bytes

def convertString(string, table, useTable):
    if not table or not useTable: return string
    for k, v in table.items():
        if string != k: continue
        string = v
        break
    return string

def convertByte(byte, table, useTable):
    if not table or not useTable: return byte
    byte = hexToString(byte)
    for k, v in table.items():
        if byte != v: continue
        byte = k
        break
    else:
        s = ''
        for b in byte:
            for k, v in table.items():
                if b != v: continue
                s += k
                break
        byte = s
    return stringToHex(byte)
