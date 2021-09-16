from Parts.Scripts.FreezeArabic import Freeze

charmap = {}
charmapParent = {
        'ً'  : ['', '', '', ''],
        'َ'  : ['', '', '', ''],
        'ٌ'  : ['', '', '', ''],
        'ُ'  : ['', '', '', ''],
        'ٍ'  : ['', '', '', ''],
        'ِ'  : ['', '', '', ''],
        'ّ'  : ['', '', '', ''],
        'ْ'  : ['', '', '', ''],
        'ء' : ['', '', '', ''],
        'آ' : ['', '', '', ''],
        'أ' : ['', '', '', ''],
		'ؤ' : ['', '', '', ''],
		'إ' : ['', '', '', ''],
		'ئ' : ['', '', '', ''],
		'ا' : ['', '', '', ''],
		'ب' : ['', '', '', ''],
		'ة' : ['', '', '', ''],
		'ت' : ['', '', '', ''],
		'ث' : ['', '', '', ''],
		'ج' : ['', '', '', ''],
		'ح' : ['', '', '', ''],
		'خ' : ['', '', '', ''],
		'د' : ['', '', '', ''],
		'ذ' : ['', '', '', ''],
		'ر' : ['', '', '', ''],
		'ز' : ['', '', '', ''],
		'س' : ['', '', '', ''],
		'ش' : ['', '', '', ''],
		'ص' : ['', '', '', ''],
		'ض' : ['', '', '', ''],
		'ط' : ['', '', '', ''],
		'ظ' : ['', '', '', ''],
		'ع' : ['', '', '', ''],
		'غ' : ['', '', '', ''],
		'ف' : ['', '', '', ''],
		'ق' : ['', '', '', ''],
		'ك' : ['', '', '', ''],
		'ل' : ['', '', '', ''],
		'م' : ['', '', '', ''],
		'ن' : ['', '', '', ''],
		'ه' : ['', '', '', ''],
		'و' : ['', '', '', ''],
		'ى' : ['', '', '', ''],
		'ي' : ['', '', '', ''],
		'لآ' : ['', '', '', ''],
		'لأ' : ['', '', '', ''],
		'لإ' : ['', '', '', ''],
		'لا' : ['', '', '', ''],
		'پ' : ['', '', '', ''],
		'چ' : ['', '', '', ''],
		'ڤ' : ['', '', '', ''],
    }

def check(char, convertTo):
    if   char == 'ﹰ': charmap['ً' ][3] = convertTo
    elif char == 'ﹶ': charmap['َ' ][3] = convertTo
    elif char == 'ﹲ': charmap['ٌ' ][3] = convertTo
    elif char == 'ﹸ': charmap['ُ' ][3] = convertTo
    elif char == 'ﹴ': charmap['ٍ' ][3] = convertTo
    elif char == 'ﹺ': charmap['ِ' ][3] = convertTo
    elif char == 'ﹼ': charmap['ّ' ][3] = convertTo
    elif char == 'ﹾ': charmap['ْ' ][3] = convertTo
    elif char == 'ﺀ': charmap['ء'][3] = convertTo
    elif char == 'ﺁ': charmap['آ'][3] = convertTo
    elif char == 'ﺂ': charmap['آ'][2] = convertTo
    elif char == 'ﺃ': charmap['أ'][3] = convertTo
    elif char == 'ﺄ': charmap['أ'][2] = convertTo
    elif char == 'ﺅ': charmap['ؤ'][3] = convertTo
    elif char == 'ﺆ': charmap['ؤ'][2] = convertTo
    elif char == 'ﺇ': charmap['إ'][3] = convertTo
    elif char == 'ﺈ': charmap['إ'][2] = convertTo
    elif char == 'ﺉ': charmap['ئ'][3] = convertTo
    elif char == 'ﺊ': charmap['ئ'][2] = convertTo
    elif char == 'ﺌ': charmap['ئ'][1] = convertTo
    elif char == 'ﺋ': charmap['ئ'][0] = convertTo
    elif char == 'ﺍ': charmap['ا'][3] = convertTo
    elif char == 'ﺎ': charmap['ا'][2] = convertTo
    elif char == 'ﺏ': charmap['ب'][3] = convertTo
    elif char == 'ﺐ': charmap['ب'][2] = convertTo
    elif char == 'ﺒ': charmap['ب'][1] = convertTo
    elif char == 'ﺑ': charmap['ب'][0] = convertTo
    elif char == 'ﺓ': charmap['ة'][3] = convertTo
    elif char == 'ﺔ': charmap['ة'][2] = convertTo
    elif char == 'ﺕ': charmap['ت'][3] = convertTo
    elif char == 'ﺖ': charmap['ت'][2] = convertTo
    elif char == 'ﺘ': charmap['ت'][1] = convertTo
    elif char == 'ﺗ': charmap['ت'][0] = convertTo
    elif char == 'ﺙ': charmap['ث'][3] = convertTo
    elif char == 'ﺚ': charmap['ث'][2] = convertTo
    elif char == 'ﺜ': charmap['ث'][1] = convertTo
    elif char == 'ﺛ': charmap['ث'][0] = convertTo
    elif char == 'ﺝ': charmap['ج'][3] = convertTo
    elif char == 'ﺞ': charmap['ج'][2] = convertTo
    elif char == 'ﺠ': charmap['ج'][1] = convertTo
    elif char == 'ﺟ': charmap['ج'][0] = convertTo
    elif char == 'ﺡ': charmap['ح'][3] = convertTo
    elif char == 'ﺢ': charmap['ح'][2] = convertTo
    elif char == 'ﺤ': charmap['ح'][1] = convertTo
    elif char == 'ﺣ': charmap['ح'][0] = convertTo
    elif char == 'ﺥ': charmap['خ'][3] = convertTo
    elif char == 'ﺦ': charmap['خ'][2] = convertTo
    elif char == 'ﺨ': charmap['خ'][1] = convertTo
    elif char == 'ﺧ': charmap['خ'][0] = convertTo
    elif char == 'ﺩ': charmap['د'][3] = convertTo
    elif char == 'ﺪ': charmap['د'][2] = convertTo
    elif char == 'ﺫ': charmap['ذ'][3] = convertTo
    elif char == 'ﺬ': charmap['ذ'][2] = convertTo
    elif char == 'ﺭ': charmap['ر'][3] = convertTo
    elif char == 'ﺮ': charmap['ر'][2] = convertTo
    elif char == 'ﺯ': charmap['ز'][3] = convertTo
    elif char == 'ﺰ': charmap['ز'][2] = convertTo
    elif char == 'ﺱ': charmap['س'][3] = convertTo
    elif char == 'ﺲ': charmap['س'][2] = convertTo
    elif char == 'ﺴ': charmap['س'][1] = convertTo
    elif char == 'ﺳ': charmap['س'][0] = convertTo
    elif char == 'ﺵ': charmap['ش'][3] = convertTo
    elif char == 'ﺶ': charmap['ش'][2] = convertTo
    elif char == 'ﺸ': charmap['ش'][1] = convertTo
    elif char == 'ﺷ': charmap['ش'][0] = convertTo
    elif char == 'ﺹ': charmap['ص'][3] = convertTo
    elif char == 'ﺺ': charmap['ص'][2] = convertTo
    elif char == 'ﺼ': charmap['ص'][1] = convertTo
    elif char == 'ﺻ': charmap['ص'][0] = convertTo
    elif char == 'ﺽ': charmap['ض'][3] = convertTo
    elif char == 'ﺾ': charmap['ض'][2] = convertTo
    elif char == 'ﻀ': charmap['ض'][1] = convertTo
    elif char == 'ﺿ': charmap['ض'][0] = convertTo
    elif char == 'ﻁ': charmap['ط'][3] = convertTo
    elif char == 'ﻂ': charmap['ط'][2] = convertTo
    elif char == 'ﻄ': charmap['ط'][1] = convertTo
    elif char == 'ﻃ': charmap['ط'][0] = convertTo
    elif char == 'ﻅ': charmap['ظ'][3] = convertTo
    elif char == 'ﻆ': charmap['ظ'][2] = convertTo
    elif char == 'ﻈ': charmap['ظ'][1] = convertTo
    elif char == 'ﻇ': charmap['ظ'][0] = convertTo
    elif char == 'ﻉ': charmap['ع'][3] = convertTo
    elif char == 'ﻊ': charmap['ع'][2] = convertTo
    elif char == 'ﻌ': charmap['ع'][1] = convertTo
    elif char == 'ﻋ': charmap['ع'][0] = convertTo
    elif char == 'ﻍ': charmap['غ'][3] = convertTo
    elif char == 'ﻎ': charmap['غ'][2] = convertTo
    elif char == 'ﻐ': charmap['غ'][1] = convertTo
    elif char == 'ﻏ': charmap['غ'][0] = convertTo
    elif char == 'ﻑ': charmap['ف'][3] = convertTo
    elif char == 'ﻒ': charmap['ف'][2] = convertTo
    elif char == 'ﻔ': charmap['ف'][1] = convertTo
    elif char == 'ﻓ': charmap['ف'][0] = convertTo
    elif char == 'ﻕ': charmap['ق'][3] = convertTo
    elif char == 'ﻖ': charmap['ق'][2] = convertTo
    elif char == 'ﻘ': charmap['ق'][1] = convertTo
    elif char == 'ﻗ': charmap['ق'][0] = convertTo
    elif char == 'ﻙ': charmap['ك'][3] = convertTo
    elif char == 'ﻚ': charmap['ك'][2] = convertTo
    elif char == 'ﻜ': charmap['ك'][1] = convertTo
    elif char == 'ﻛ': charmap['ك'][0] = convertTo
    elif char == 'ﻝ': charmap['ل'][3] = convertTo
    elif char == 'ﻞ': charmap['ل'][2] = convertTo
    elif char == 'ﻠ': charmap['ل'][1] = convertTo
    elif char == 'ﻟ': charmap['ل'][0] = convertTo
    elif char == 'ﻡ': charmap['م'][3] = convertTo
    elif char == 'ﻢ': charmap['م'][2] = convertTo
    elif char == 'ﻤ': charmap['م'][1] = convertTo
    elif char == 'ﻣ': charmap['م'][0] = convertTo
    elif char == 'ﻥ': charmap['ن'][3] = convertTo
    elif char == 'ﻦ': charmap['ن'][2] = convertTo
    elif char == 'ﻨ': charmap['ن'][1] = convertTo
    elif char == 'ﻧ': charmap['ن'][0] = convertTo
    elif char == 'ﻩ': charmap['ه'][3] = convertTo
    elif char == 'ﻪ': charmap['ه'][2] = convertTo
    elif char == 'ﻬ': charmap['ه'][1] = convertTo
    elif char == 'ﻫ': charmap['ه'][0] = convertTo
    elif char == 'ﻭ': charmap['و'][3] = convertTo
    elif char == 'ﻮ': charmap['و'][2] = convertTo
    elif char == 'ﻯ': charmap['ى'][3] = convertTo
    elif char == 'ﻰ': charmap['ى'][2] = convertTo
    elif char == 'ﻱ': charmap['ي'][3] = convertTo
    elif char == 'ﻲ': charmap['ي'][2] = convertTo
    elif char == 'ﻴ': charmap['ي'][1] = convertTo
    elif char == 'ﻳ': charmap['ي'][0] = convertTo
    elif char == 'ﻵ': charmap['لآ'][3] = convertTo
    elif char == 'ﻶ': charmap['لآ'][2] = convertTo
    elif char == 'ﻷ': charmap['لأ'][3] = convertTo
    elif char == 'ﻸ': charmap['لأ'][2] = convertTo
    elif char == 'ﻹ': charmap['لإ'][3] = convertTo
    elif char == 'ﻺ': charmap['لإ'][2] = convertTo
    elif char == 'ﻻ': charmap['لا'][3] = convertTo
    elif char == 'ﻼ': charmap['لا'][2] = convertTo
    elif char == 'ﭖ': charmap['پ'][3] = convertTo
    elif char == 'ﭗ': charmap['پ'][2] = convertTo
    elif char == 'ﭙ': charmap['پ'][1] = convertTo
    elif char == 'ﭘ': charmap['پ'][0] = convertTo
    elif char == 'ﭺ': charmap['چ'][3] = convertTo
    elif char == 'ﭻ': charmap['چ'][2] = convertTo
    elif char == 'ﭽ': charmap['چ'][1] = convertTo
    elif char == 'ﭼ': charmap['چ'][0] = convertTo
    elif char == 'ﭪ': charmap['ڤ'][3] = convertTo
    elif char == 'ﭫ': charmap['ڤ'][2] = convertTo
    elif char == 'ﭭ': charmap['ڤ'][1] = convertTo
    elif char == 'ﭬ': charmap['ڤ'][0] = convertTo
    else: charmap[char] = ['', '', '', convertTo]

def sortACT(tableContent):
    global charmap
    charmap = dict(charmapParent) # dict ليساوي المتغير الجديد قيمة القديم وليس القديم نفسه كي لا يتغير احدهما بتغير الاخر
    newTable = ''
    
    lines = tableContent.split('\n')
    _SEPARATOR_ = lines[2][11:-1]
    
    for line in lines:
        if _SEPARATOR_ not in line or line == f'SEPARATOR="{_SEPARATOR_}"' or line == f'الحرف{_SEPARATOR_}أول{_SEPARATOR_}وسط{_SEPARATOR_}آخر{_SEPARATOR_}منفصل':
            newTable += line + '\n'
            continue
        if line.endswith(_SEPARATOR_*4):
            newTable += Freeze(line[0:-4], False) + '\n'
        
        items = line.split(_SEPARATOR_)
        check(items[0], items[4])
    
    for k, v in charmap.items():
        if not k: continue
        if ''.join(v):
            newTable += k + _SEPARATOR_ + _SEPARATOR_.join(v) + '\n'
        
    return newTable

def fillEmptyCells(Charmap : dict, chars : tuple):
    if chars[0] in Charmap and chars[1] in Charmap and chars[2] in Charmap and chars[3] in Charmap: return Charmap
    
    if chars[1] not in Charmap and chars[0] in Charmap: Charmap[chars[1]] = Charmap[chars[0]]
    if chars[0] not in Charmap and chars[1] in Charmap: Charmap[chars[0]] = Charmap[chars[1]]
    
    if chars[3] not in Charmap and chars[2] in Charmap: Charmap[chars[3]] = Charmap[chars[2]]
    if chars[2] not in Charmap and chars[3] in Charmap: Charmap[chars[2]] = Charmap[chars[3]]

    if chars[0] not in Charmap and chars[3] in Charmap: Charmap[chars[0]] = Charmap[chars[3]]
    if chars[1] not in Charmap and chars[2] in Charmap: Charmap[chars[1]] = Charmap[chars[2]]
    
    if chars[0] not in Charmap and chars[2] in Charmap: Charmap[chars[0]] = Charmap[chars[2]]
    if chars[1] not in Charmap and chars[3] in Charmap: Charmap[chars[1]] = Charmap[chars[3]]
    
    if chars[3] not in Charmap and chars[0] in Charmap: Charmap[chars[3]] = Charmap[chars[0]]
    if chars[2] not in Charmap and chars[1] in Charmap: Charmap[chars[2]] = Charmap[chars[1]]

    if chars[2] not in Charmap and chars[0] in Charmap: Charmap[chars[2]] = Charmap[chars[0]]
    if chars[3] not in Charmap and chars[1] in Charmap: Charmap[chars[3]] = Charmap[chars[1]]
    
    return Charmap

def fixCharmap(Charmap : dict):
    Charmap = fillEmptyCells(Charmap, ('ﺁ', 'ﺂ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺃ', 'ﺄ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺅ', 'ﺆ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺇ', 'ﺈ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺉ', 'ﺊ', 'ﺌ', 'ﺋ'))
    Charmap = fillEmptyCells(Charmap, ('ﺍ', 'ﺎ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺏ', 'ﺐ', 'ﺒ', 'ﺑ'))
    Charmap = fillEmptyCells(Charmap, ('ﺓ', 'ﺔ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺕ', 'ﺖ', 'ﺘ', 'ﺗ'))
    Charmap = fillEmptyCells(Charmap, ('ﺙ', 'ﺚ', 'ﺜ', 'ﺛ'))
    Charmap = fillEmptyCells(Charmap, ('ﺝ', 'ﺞ', 'ﺠ', 'ﺟ'))
    Charmap = fillEmptyCells(Charmap, ('ﺡ', 'ﺢ', 'ﺤ', 'ﺣ'))
    Charmap = fillEmptyCells(Charmap, ('ﺥ', 'ﺦ', 'ﺨ', 'ﺧ'))
    Charmap = fillEmptyCells(Charmap, ('ﺩ', 'ﺪ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺫ', 'ﺬ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺭ', 'ﺮ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺯ', 'ﺰ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﺱ', 'ﺲ', 'ﺴ', 'ﺳ'))
    Charmap = fillEmptyCells(Charmap, ('ﺵ', 'ﺶ', 'ﺸ', 'ﺷ'))
    Charmap = fillEmptyCells(Charmap, ('ﺹ', 'ﺺ', 'ﺼ', 'ﺻ'))
    Charmap = fillEmptyCells(Charmap, ('ﺽ', 'ﺾ', 'ﻀ', 'ﺿ'))
    Charmap = fillEmptyCells(Charmap, ('ﻁ', 'ﻂ', 'ﻄ', 'ﻃ'))
    Charmap = fillEmptyCells(Charmap, ('ﻅ', 'ﻆ', 'ﻈ', 'ﻇ'))
    Charmap = fillEmptyCells(Charmap, ('ﻉ', 'ﻊ', 'ﻌ', 'ﻋ'))
    Charmap = fillEmptyCells(Charmap, ('ﻍ', 'ﻎ', 'ﻐ', 'ﻏ'))
    Charmap = fillEmptyCells(Charmap, ('ﻑ', 'ﻒ', 'ﻔ', 'ﻓ'))
    Charmap = fillEmptyCells(Charmap, ('ﻕ', 'ﻖ', 'ﻘ', 'ﻗ'))
    Charmap = fillEmptyCells(Charmap, ('ﻙ', 'ﻚ', 'ﻜ', 'ﻛ'))
    Charmap = fillEmptyCells(Charmap, ('ﻝ', 'ﻞ', 'ﻠ', 'ﻟ'))
    Charmap = fillEmptyCells(Charmap, ('ﻡ', 'ﻢ', 'ﻤ', 'ﻣ'))
    Charmap = fillEmptyCells(Charmap, ('ﻥ', 'ﻦ', 'ﻨ', 'ﻧ'))
    Charmap = fillEmptyCells(Charmap, ('ﻩ', 'ﻪ', 'ﻬ', 'ﻫ'))
    Charmap = fillEmptyCells(Charmap, ('ﻭ', 'ﻮ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﻯ', 'ﻰ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﻱ', 'ﻲ', 'ﻴ', 'ﻳ'))
    Charmap = fillEmptyCells(Charmap, ('ﻵ', 'ﻶ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﻷ', 'ﻸ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﻹ', 'ﻺ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﻻ', 'ﻼ', '', ''))
    Charmap = fillEmptyCells(Charmap, ('ﭖ', 'ﭗ', 'ﭙ', 'ﭘ'))
    Charmap = fillEmptyCells(Charmap, ('ﭺ', 'ﭻ', 'ﭽ', 'ﭼ'))
    Charmap = fillEmptyCells(Charmap, ('ﭪ', 'ﭫ', 'ﭭ', 'ﭬ'))
    Charmap.pop('', None)
    return Charmap

def sameItemsLengh(Charmap : dict, lengh : int):
    remove = []
    for k, v in Charmap.items():
        if len(k) != len(v) != lengh:
            remove.append(k)
    for k in remove: Charmap.pop(k, None)
    return Charmap