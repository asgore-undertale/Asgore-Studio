from Parts.Scripts.FreezeArabic import Freeze

def makeDTE(text, dteList, chars):
    if not dteList: dteList = chars
    newDteList = []
    
    for dte in dteList:
        for char in chars:
            newDte = dte[0] + char
            count = text.count(newDte)
            
            if not count: continue
            newDteList.append([newDte, str(count)])
    
    return sorted(newDteList, key=lambda x: x[1], reverse=True)

def suggestDTE(text, ignoredChars, mergedCharLen, resultsNum):
    if mergedCharLen < 2: return [], ''
    
    text = Freeze(text, True, False)
    _text = text
    for char in ignoredChars: _text = _text.replace(char, '')
    chars = "".join(dict.fromkeys(_text))
    
    dteList = []
    for i in range(mergedCharLen - 1):
        dteList = makeDTE(text, dteList, chars)
        if not dteList: break
    dteList = dteList[0:resultsNum]
    
    log = 'المجموعات البصرية المقترحة وعدد ورودها:\n'
    for dte in dteList:
        log += f'[{dte[0]}]\t\t[{dte[1]}]\n'
    
    return dteList, log