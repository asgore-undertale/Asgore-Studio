from Parts.Scripts.FreezeArabic import Freeze
from Parts.Vars import mergedArabicChars

maxSampleLength = 2
# available = '﷼﷽'

def returnMostPrevalent(text, ignoredDtes):
    sample, num = '', 0
    for k in mergedArabicChars.keys():
        if len(k) > maxSampleLength or len(k) < 2: continue
        if mergedArabicChars[k] in ignoredDtes: continue
        
        counter = text.count(k)
        
        if len(k) > len(sample) and counter > 0: sample, num = k, counter
        elif counter > num: sample, num = k, counter # and sample in available
    
    return sample, num

def analyzeText(text, ignoredDtes, resultsNum):
    if not text: return
    if maxSampleLength < 2: return
    log, i = '', 0
    
    log += f'الطول الأصلي\t\t{len(text)}\n'
    text = Freeze(text)
    log += f'بعد التجميد\t\t{len(text)}\n\nالمجموعات البصرية وعدد ورودها:\n'
    
    while True:
        if i == resultsNum: break
        k, count = returnMostPrevalent(text, ignoredDtes)
        if not k: break
        
        i += 1
        text = text.replace(k, mergedArabicChars[k])
        log += f'[{mergedArabicChars[k]}]   [{count}]\tصار الطول   {len(text)} (-{count})\n'
    
    log += f'\nالطول بعد الاختزال\t{len(text)}'
    return text, log