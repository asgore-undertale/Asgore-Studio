from Parts.Scripts.Un_Freeze_Arabic import Un_Freeze

def makeDTE(text):
    dteList = []
    for char in text:
        for _char in text:
            dte = f'{char}{_char}'
            count = text.count(dte)
            if not count: continue
            
            dteList.append([dte, str(count)])
    return dteList

def suggestDTE(text, resultsNum):
    dteList, _ = [], ''
    text = Un_Freeze(text, True, False)
    text = "".join(dict.fromkeys(text))
    _ += f'المجموعات البصرية المقترحة وعدد ورودها:\n'
    
    dteList = sorted(makeDTE(text), key=lambda x: x[1], reverse=True)
    dteList = dteList[0:resultsNum]
    
    for dte in dteList:
        _ += f'[{dte[0]}]\t\t[{dte[1]}]\n'
    
    return dteList, _