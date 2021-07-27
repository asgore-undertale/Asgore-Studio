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
    if mergedCharLen[0] < 2 or mergedCharLen[0] > mergedCharLen[1]: return [], ''
    # resultsNum = resultsNum // (mergedCharLen[1] - mergedCharLen[0])
    
    text = Freeze(text, True, False)
    _text = text
    for char in ignoredChars: _text = _text.replace(char, '')
    chars = "".join(dict.fromkeys(_text))
    
    dteList = []
    for k in range(mergedCharLen[1] - mergedCharLen[0] + 1):
        _List = []
        for i in range(mergedCharLen[0] - 1 + k):
            _List = makeDTE(text, _List, chars)
            if not _List: break
        _List = _List[0:resultsNum]
        
        for item in _List:
            dteList.append(item)
    
    log = 'المجموعات البصرية المقترحة وعدد ورودها:\n'
    for dte in dteList:
        log += f'{dte[0]}\t\t[{dte[1]}]\n'
    
    return dteList, log