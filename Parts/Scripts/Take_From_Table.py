from Parts.Scripts.UsefulFunctions import sortDictByKeyLengh

def Take_From_Table(filePath):
    if filePath.endswith('.act'):
        return TakeFromACT(filePath)
    if filePath.endswith('.zts'):
        return TakeFromZTS(filePath)

def TakeFromZTS(ztsPath):
    charsTable = {}
    
    lines = open(ztsPath, 'r', encoding="utf-8").read().split('\n')
    string1, string2 = lines[0], lines[1]
    
    for i, j in zip(string1, string2): charsTable[j] = i
    
    return charsTable

def TakeFromACT(atePath):
    charsTable = {}
    rows = open(atePath, 'r', encoding="utf-8").read().split('\n')
    
    VERSION = float(rows[1][9:-1])
    SEPARATOR = rows[2][11:-1]
    
    for row in range(5, len(rows)):
        if not rows[row]: continue
        for i in range(4 - rows[row].count(SEPARATOR)): rows[row] += SEPARATOR
        cols = rows[row].split(SEPARATOR)
        
        if   cols[0] == 'ً':
            charsTable['ﹰ'] = cols[4]
        elif cols[0] == 'َ':
            charsTable['ﹶ'] = cols[4]
        elif cols[0] == 'ٌ':
            charsTable['ﹲ'] = cols[4]
        elif cols[0] == 'ُ':
            charsTable['ﹸ'] = cols[4]
        elif cols[0] == 'ٍ':
            charsTable['ﹴ'] = cols[4]
        elif cols[0] == 'ِ':
            charsTable['ﹺ'] = cols[4]
        elif cols[0] == 'ّ':
            charsTable['ﹼ'] = cols[4]
        elif cols[0] == 'ْ':
            charsTable['ﹾ'] = cols[4]
        elif cols[0] == 'ء':
            charsTable['ﺀ'] = cols[4]
        elif cols[0] == 'آ':
            charsTable['ﺁ'] = cols[4]
            charsTable['ﺂ'] = cols[3]
        elif cols[0] == 'أ':
            charsTable['ﺃ'] = cols[4]
            charsTable['ﺄ'] = cols[3]
        elif cols[0] == 'ؤ':
            charsTable['ﺅ'] = cols[4]
            charsTable['ﺆ'] = cols[3]
        elif cols[0] == 'إ':
            charsTable['ﺇ'] = cols[4]
            charsTable['ﺈ'] = cols[3]
        elif cols[0] == 'ئ':
            charsTable['ﺉ'] = cols[4]
            charsTable['ﺊ'] = cols[3]
            charsTable['ﺌ'] = cols[2]
            charsTable['ﺋ'] = cols[1]
        elif cols[0] == 'ا':
            charsTable['ﺍ'] = cols[4]
            charsTable['ﺎ'] = cols[3]
        elif cols[0] == 'ب':
            charsTable['ﺏ'] = cols[4]
            charsTable['ﺐ'] = cols[3]
            charsTable['ﺒ'] = cols[2]
            charsTable['ﺑ'] = cols[1]
        elif cols[0] == 'ة':
            charsTable['ﺓ'] = cols[4]
            charsTable['ﺔ'] = cols[3]
        elif cols[0] == 'ت':
            charsTable['ﺕ'] = cols[4]
            charsTable['ﺖ'] = cols[3]
            charsTable['ﺘ'] = cols[2]
            charsTable['ﺗ'] = cols[1]
        elif cols[0] == 'ث':
            charsTable['ﺙ'] = cols[4]
            charsTable['ﺚ'] = cols[3]
            charsTable['ﺜ'] = cols[2]
            charsTable['ﺛ'] = cols[1]
        elif cols[0] == 'ج':
            charsTable['ﺝ'] = cols[4]
            charsTable['ﺞ'] = cols[3]
            charsTable['ﺠ'] = cols[2]
            charsTable['ﺟ'] = cols[1]
        elif cols[0] == 'ح':
            charsTable['ﺡ'] = cols[4]
            charsTable['ﺢ'] = cols[3]
            charsTable['ﺤ'] = cols[2]
            charsTable['ﺣ'] = cols[1]
        elif cols[0] == 'خ':
            charsTable['ﺥ'] = cols[4]
            charsTable['ﺦ'] = cols[3]
            charsTable['ﺨ'] = cols[2]
            charsTable['ﺧ'] = cols[1]
        elif cols[0] == 'د':
            charsTable['ﺩ'] = cols[4]
            charsTable['ﺪ'] = cols[3]
        elif cols[0] == 'ذ':
            charsTable['ﺫ'] = cols[4]
            charsTable['ﺬ'] = cols[3]
        elif cols[0] == 'ر':
            charsTable['ﺭ'] = cols[4]
            charsTable['ﺮ'] = cols[3]
        elif cols[0] == 'ز':
            charsTable['ﺯ'] = cols[4]
            charsTable['ﺰ'] = cols[3]
        elif cols[0] == 'س':
            charsTable['ﺱ'] = cols[4]
            charsTable['ﺲ'] = cols[3]
            charsTable['ﺴ'] = cols[2]
            charsTable['ﺳ'] = cols[1]
        elif cols[0] == 'ش':
            charsTable['ﺵ'] = cols[4]
            charsTable['ﺶ'] = cols[3]
            charsTable['ﺸ'] = cols[2]
            charsTable['ﺷ'] = cols[1]
        elif cols[0] == 'ص':
            charsTable['ﺹ'] = cols[4]
            charsTable['ﺺ'] = cols[3]
            charsTable['ﺼ'] = cols[2]
            charsTable['ﺻ'] = cols[1]
        elif cols[0] == 'ض':
            charsTable['ﺽ'] = cols[4]
            charsTable['ﺾ'] = cols[3]
            charsTable['ﻀ'] = cols[2]
            charsTable['ﺿ'] = cols[1]
        elif cols[0] == 'ط':
            charsTable['ﻁ'] = cols[4]
            charsTable['ﻂ'] = cols[3]
            charsTable['ﻄ'] = cols[2]
            charsTable['ﻃ'] = cols[1]
        elif cols[0] == 'ظ':
            charsTable['ﻅ'] = cols[4]
            charsTable['ﻆ'] = cols[3]
            charsTable['ﻈ'] = cols[2]
            charsTable['ﻇ'] = cols[1]
        elif cols[0] == 'ع':
            charsTable['ﻉ'] = cols[4]
            charsTable['ﻊ'] = cols[3]
            charsTable['ﻋ'] = cols[2]
            charsTable['ﻌ'] = cols[1]
        elif cols[0] == 'غ':
            charsTable['ﻍ'] = cols[4]
            charsTable['ﻎ'] = cols[3]
            charsTable['ﻐ'] = cols[2]
            charsTable['ﻏ'] = cols[1]
        elif cols[0] == 'ف':
            charsTable['ﻑ'] = cols[4]
            charsTable['ﻒ'] = cols[3]
            charsTable['ﻔ'] = cols[2]
            charsTable['ﻓ'] = cols[1]
        elif cols[0] == 'ق':
            charsTable['ﻕ'] = cols[4]
            charsTable['ﻖ'] = cols[3]
            charsTable['ﻘ'] = cols[2]
            charsTable['ﻗ'] = cols[1]
        elif cols[0] == 'ك':
            charsTable['ﻙ'] = cols[4]
            charsTable['ﻚ'] = cols[3]
            charsTable['ﻜ'] = cols[2]
            charsTable['ﻛ'] = cols[1]
        elif cols[0] == 'ل':
            charsTable['ﻝ'] = cols[4]
            charsTable['ﻞ'] = cols[3]
            charsTable['ﻠ'] = cols[2]
            charsTable['ﻟ'] = cols[1]
        elif cols[0] == 'م':
            charsTable['ﻡ'] = cols[4]
            charsTable['ﻢ'] = cols[3]
            charsTable['ﻤ'] = cols[2]
            charsTable['ﻣ'] = cols[1]
        elif cols[0] == 'ن':
            charsTable['ﻥ'] = cols[4]
            charsTable['ﻦ'] = cols[3]
            charsTable['ﻨ'] = cols[2]
            charsTable['ﻧ'] = cols[1]
        elif cols[0] == 'ه':
            charsTable['ﻩ'] = cols[4]
            charsTable['ﻪ'] = cols[3]
            charsTable['ﻬ'] = cols[2]
            charsTable['ﻫ'] = cols[1]
        elif cols[0] == 'و':
            charsTable['ﻭ'] = cols[4]
            charsTable['ﻮ'] = cols[3]
        elif cols[0] == 'ى':
            charsTable['ﻯ'] = cols[4]
            charsTable['ﻰ'] = cols[3]
        elif cols[0] == 'ي':
            charsTable['ﻱ'] = cols[4]
            charsTable['ﻲ'] = cols[3]
            charsTable['ﻴ'] = cols[2]
            charsTable['ﻳ'] = cols[1]
        elif cols[0] == 'لآ':
            charsTable['ﻵ'] = cols[4]
            charsTable['ﻶ'] = cols[3]
        elif cols[0] == 'لأ':
            charsTable['ﻷ'] = cols[4]
            charsTable['ﻸ'] = cols[3]
        elif cols[0] == 'لإ':
            charsTable['ﻹ'] = cols[4]
            charsTable['ﻺ'] = cols[3]
        elif cols[0] == 'لا':
            charsTable['ﻻ'] = cols[4]
            charsTable['ﻼ'] = cols[3]
        elif cols[0] == 'پ':
            charsTable['ﭖ'] = cols[4]
            charsTable['ﭗ'] = cols[3]
            charsTable['ﭙ'] = cols[2]
            charsTable['ﭘ'] = cols[1]
        elif cols[0] == 'چ':
            charsTable['ﭺ'] = cols[4]
            charsTable['ﭻ'] = cols[3]
            charsTable['ﭽ'] = cols[2]
            charsTable['ﭼ'] = cols[1]
        elif cols[0] == 'ڤ':
            charsTable['ﭪ'] = cols[4]
            charsTable['ﭫ'] = cols[3]
            charsTable['ﭭ'] = cols[2]
            charsTable['ﭬ'] = cols[1]
        else:
            charsTable[cols[0]] = cols[4]
    
    return sortDictByKeyLengh(charsTable)