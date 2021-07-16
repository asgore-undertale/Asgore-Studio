from Parts.Scripts.FreezeArabic import Freeze

def makeDTE(text, chars):
    dteList = []
    for char in chars:
        for _char in chars:
            dte = char + _char
            count = text.count(dte)
            if not count: continue
            
            dteList.append([dte, str(count)])
    return dteList

def makeDTE2(text, dteList, chars):
    dteList3 = []
    for dte in dteList:
        for char in chars:
            dte3 = dte[0] + char
            count = text.count(dte3)
            if not count: continue
            
            dteList3.append([dte3, str(count)])
    
    return sorted(dteList3, key=lambda x: x[1], reverse=True)

def suggestDTE(text, ignoredChars, mergedCharLen, resultsNum):
    if mergedCharLen < 2: return [], ''
    
    text = Freeze(text, True, False)
    _text = text
    for char in ignoredChars: _text = _text.replace(char, '')
    chars = "".join(dict.fromkeys(_text))
    
    dteList = makeDTE(text, chars)
    for i in range(mergedCharLen - 2):
        dteList = makeDTE2(text, dteList, chars)
    dteList = dteList[0:resultsNum]
    
    log = 'المجموعات البصرية المقترحة وعدد ورودها:\n'
    for dte in dteList:
        log += f'[{dte[0]}]\t\t[{dte[1]}]\n'
    
    return dteList, log