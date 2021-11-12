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
charsList = (('ﺁ', 'ﺂ', '', ''), ('ﺃ', 'ﺄ', '', ''), ('ﺅ', 'ﺆ', '', ''), ('ﺇ', 'ﺈ', '', ''), ('ﺉ', 'ﺊ', 'ﺌ', 'ﺋ'), ('ﺍ', 'ﺎ', '', ''),
    ('ﺏ', 'ﺐ', 'ﺒ', 'ﺑ'), ('ﺓ', 'ﺔ', '', ''), ('ﺕ', 'ﺖ', 'ﺘ', 'ﺗ'), ('ﺙ', 'ﺚ', 'ﺜ', 'ﺛ'), ('ﺝ', 'ﺞ', 'ﺠ', 'ﺟ'), ('ﺡ', 'ﺢ', 'ﺤ', 'ﺣ'),
    ('ﺥ', 'ﺦ', 'ﺨ', 'ﺧ'), ('ﺩ', 'ﺪ', '', ''), ('ﺫ', 'ﺬ', '', ''), ('ﺭ', 'ﺮ', '', ''), ('ﺯ', 'ﺰ', '', ''), ('ﺱ', 'ﺲ', 'ﺴ', 'ﺳ'),
    ('ﺵ', 'ﺶ', 'ﺸ', 'ﺷ'), ('ﺹ', 'ﺺ', 'ﺼ', 'ﺻ'), ('ﺽ', 'ﺾ', 'ﻀ', 'ﺿ'), ('ﻁ', 'ﻂ', 'ﻄ', 'ﻃ'), ('ﻅ', 'ﻆ', 'ﻈ', 'ﻇ'), ('ﻉ', 'ﻊ', 'ﻌ', 'ﻋ'),
    ('ﻍ', 'ﻎ', 'ﻐ', 'ﻏ'), ('ﻑ', 'ﻒ', 'ﻔ', 'ﻓ'), ('ﻕ', 'ﻖ', 'ﻘ', 'ﻗ'), ('ﻙ', 'ﻚ', 'ﻜ', 'ﻛ'), ('ﻝ', 'ﻞ', 'ﻠ', 'ﻟ'), ('ﻡ', 'ﻢ', 'ﻤ', 'ﻣ'),
    ('ﻥ', 'ﻦ', 'ﻨ', 'ﻧ'), ('ﻩ', 'ﻪ', 'ﻬ', 'ﻫ'), ('ﻭ', 'ﻮ', '', ''), ('ﻯ', 'ﻰ', '', ''), ('ﻱ', 'ﻲ', 'ﻴ', 'ﻳ'), ('ﻵ', 'ﻶ', '', ''),
    ('ﻷ', 'ﻸ', '', ''), ('ﻹ', 'ﻺ', '', ''), ('ﻻ', 'ﻼ', '', ''), ('ﭖ', 'ﭗ', 'ﭙ', 'ﭘ'), ('ﭺ', 'ﭻ', 'ﭽ', 'ﭼ'), ('ﭪ', 'ﭫ', 'ﭭ', 'ﭬ')
    )

def sort(char, convertTo):
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

def sortACT(tableContent, _SEPARATOR_): # table content with no description
    global charmap
    charmap = dict(charmapParent) # dict ليساوي المتغير الجديد قيمة القديم وليس القديم نفسه كي لا يتغير احدهما بتغير الاخر
    newTable = ''
    
    lines = tableContent.split('\n')
    
    for line in lines:
        if not line: continue
        if line.endswith(_SEPARATOR_*4):
            newTable += Freeze(line[0:-4], False) + '\n'
        
        items = line.split(_SEPARATOR_)
        sort(items[0], items[4])
    
    for k, v in charmap.items():
        if not k: continue
        if ''.join(v):
            newTable += k + _SEPARATOR_ + _SEPARATOR_.join(v) + '\n'
        
    return newTable

def fillHalfs(Charmap : dict, chars : tuple):
    if chars[1] not in Charmap and chars[0] in Charmap: Charmap[chars[1]] = Charmap[chars[0]]
    if chars[0] not in Charmap and chars[1] in Charmap: Charmap[chars[0]] = Charmap[chars[1]]
    
    if chars[3] not in Charmap and chars[2] in Charmap: Charmap[chars[3]] = Charmap[chars[2]]
    if chars[2] not in Charmap and chars[3] in Charmap: Charmap[chars[2]] = Charmap[chars[3]]
    
    return Charmap

def fillEmptyCells(Charmap : dict, chars : tuple):
    if chars[0] in Charmap and chars[1] in Charmap and chars[2] in Charmap and chars[3] in Charmap: return Charmap
    
    Charmap = fillHalfs(Charmap, chars)
    if chars[1] not in Charmap and chars[2] in Charmap: Charmap[chars[1]] = Charmap[chars[2]]
    if chars[0] not in Charmap and chars[3] in Charmap: Charmap[chars[0]] = Charmap[chars[3]]
    Charmap = fillHalfs(Charmap, chars)
    
    return Charmap

def takeFromArabic(Charmap : dict, cells : list):
    if cells[0] == 'ً':
        Charmap['ﹰ'] = cells[4]
    elif cells[0] == 'َ':
        Charmap['ﹶ'] = cells[4]
    elif cells[0] == 'ٌ':
        Charmap['ﹲ'] = cells[4]
    elif cells[0] == 'ُ':
        Charmap['ﹸ'] = cells[4]
    elif cells[0] == 'ٍ':
        Charmap['ﹴ'] = cells[4]
    elif cells[0] == 'ِ':
        Charmap['ﹺ'] = cells[4]
    elif cells[0] == 'ّ':
        Charmap['ﹼ'] = cells[4]
    elif cells[0] == 'ْ':
        Charmap['ﹾ'] = cells[4]
    elif cells[0] == 'ء':
        Charmap['ﺀ'] = cells[4]
    elif cells[0] == 'آ':
        Charmap['ﺁ'] = cells[4]
        Charmap['ﺂ'] = cells[3]
    elif cells[0] == 'أ':
        Charmap['ﺃ'] = cells[4]
        Charmap['ﺄ'] = cells[3]
    elif cells[0] == 'ؤ':
        Charmap['ﺅ'] = cells[4]
        Charmap['ﺆ'] = cells[3]
    elif cells[0] == 'إ':
        Charmap['ﺇ'] = cells[4]
        Charmap['ﺈ'] = cells[3]
    elif cells[0] == 'ئ':
        Charmap['ﺉ'] = cells[4]
        Charmap['ﺊ'] = cells[3]
        Charmap['ﺌ'] = cells[2]
        Charmap['ﺋ'] = cells[1]
    elif cells[0] == 'ا':
        Charmap['ﺍ'] = cells[4]
        Charmap['ﺎ'] = cells[3]
    elif cells[0] == 'ب':
        Charmap['ﺏ'] = cells[4]
        Charmap['ﺐ'] = cells[3]
        Charmap['ﺒ'] = cells[2]
        Charmap['ﺑ'] = cells[1]
    elif cells[0] == 'ة':
        Charmap['ﺓ'] = cells[4]
        Charmap['ﺔ'] = cells[3]
    elif cells[0] == 'ت':
        Charmap['ﺕ'] = cells[4]
        Charmap['ﺖ'] = cells[3]
        Charmap['ﺘ'] = cells[2]
        Charmap['ﺗ'] = cells[1]
    elif cells[0] == 'ث':
        Charmap['ﺙ'] = cells[4]
        Charmap['ﺚ'] = cells[3]
        Charmap['ﺜ'] = cells[2]
        Charmap['ﺛ'] = cells[1]
    elif cells[0] == 'ج':
        Charmap['ﺝ'] = cells[4]
        Charmap['ﺞ'] = cells[3]
        Charmap['ﺠ'] = cells[2]
        Charmap['ﺟ'] = cells[1]
    elif cells[0] == 'ح':
        Charmap['ﺡ'] = cells[4]
        Charmap['ﺢ'] = cells[3]
        Charmap['ﺤ'] = cells[2]
        Charmap['ﺣ'] = cells[1]
    elif cells[0] == 'خ':
        Charmap['ﺥ'] = cells[4]
        Charmap['ﺦ'] = cells[3]
        Charmap['ﺨ'] = cells[2]
        Charmap['ﺧ'] = cells[1]
    elif cells[0] == 'د':
        Charmap['ﺩ'] = cells[4]
        Charmap['ﺪ'] = cells[3]
    elif cells[0] == 'ذ':
        Charmap['ﺫ'] = cells[4]
        Charmap['ﺬ'] = cells[3]
    elif cells[0] == 'ر':
        Charmap['ﺭ'] = cells[4]
        Charmap['ﺮ'] = cells[3]
    elif cells[0] == 'ز':
        Charmap['ﺯ'] = cells[4]
        Charmap['ﺰ'] = cells[3]
    elif cells[0] == 'س':
        Charmap['ﺱ'] = cells[4]
        Charmap['ﺲ'] = cells[3]
        Charmap['ﺴ'] = cells[2]
        Charmap['ﺳ'] = cells[1]
    elif cells[0] == 'ش':
        Charmap['ﺵ'] = cells[4]
        Charmap['ﺶ'] = cells[3]
        Charmap['ﺸ'] = cells[2]
        Charmap['ﺷ'] = cells[1]
    elif cells[0] == 'ص':
        Charmap['ﺹ'] = cells[4]
        Charmap['ﺺ'] = cells[3]
        Charmap['ﺼ'] = cells[2]
        Charmap['ﺻ'] = cells[1]
    elif cells[0] == 'ض':
        Charmap['ﺽ'] = cells[4]
        Charmap['ﺾ'] = cells[3]
        Charmap['ﻀ'] = cells[2]
        Charmap['ﺿ'] = cells[1]
    elif cells[0] == 'ط':
        Charmap['ﻁ'] = cells[4]
        Charmap['ﻂ'] = cells[3]
        Charmap['ﻄ'] = cells[2]
        Charmap['ﻃ'] = cells[1]
    elif cells[0] == 'ظ':
        Charmap['ﻅ'] = cells[4]
        Charmap['ﻆ'] = cells[3]
        Charmap['ﻈ'] = cells[2]
        Charmap['ﻇ'] = cells[1]
    elif cells[0] == 'ع':
        Charmap['ﻉ'] = cells[4]
        Charmap['ﻊ'] = cells[3]
        Charmap['ﻋ'] = cells[2]
        Charmap['ﻌ'] = cells[1]
    elif cells[0] == 'غ':
        Charmap['ﻍ'] = cells[4]
        Charmap['ﻎ'] = cells[3]
        Charmap['ﻐ'] = cells[2]
        Charmap['ﻏ'] = cells[1]
    elif cells[0] == 'ف':
        Charmap['ﻑ'] = cells[4]
        Charmap['ﻒ'] = cells[3]
        Charmap['ﻔ'] = cells[2]
        Charmap['ﻓ'] = cells[1]
    elif cells[0] == 'ق':
        Charmap['ﻕ'] = cells[4]
        Charmap['ﻖ'] = cells[3]
        Charmap['ﻘ'] = cells[2]
        Charmap['ﻗ'] = cells[1]
    elif cells[0] == 'ك':
        Charmap['ﻙ'] = cells[4]
        Charmap['ﻚ'] = cells[3]
        Charmap['ﻜ'] = cells[2]
        Charmap['ﻛ'] = cells[1]
    elif cells[0] == 'ل':
        Charmap['ﻝ'] = cells[4]
        Charmap['ﻞ'] = cells[3]
        Charmap['ﻠ'] = cells[2]
        Charmap['ﻟ'] = cells[1]
    elif cells[0] == 'م':
        Charmap['ﻡ'] = cells[4]
        Charmap['ﻢ'] = cells[3]
        Charmap['ﻤ'] = cells[2]
        Charmap['ﻣ'] = cells[1]
    elif cells[0] == 'ن':
        Charmap['ﻥ'] = cells[4]
        Charmap['ﻦ'] = cells[3]
        Charmap['ﻨ'] = cells[2]
        Charmap['ﻧ'] = cells[1]
    elif cells[0] == 'ه':
        Charmap['ﻩ'] = cells[4]
        Charmap['ﻪ'] = cells[3]
        Charmap['ﻬ'] = cells[2]
        Charmap['ﻫ'] = cells[1]
    elif cells[0] == 'و':
        Charmap['ﻭ'] = cells[4]
        Charmap['ﻮ'] = cells[3]
    elif cells[0] == 'ى':
        Charmap['ﻯ'] = cells[4]
        Charmap['ﻰ'] = cells[3]
    elif cells[0] == 'ي':
        Charmap['ﻱ'] = cells[4]
        Charmap['ﻲ'] = cells[3]
        Charmap['ﻴ'] = cells[2]
        Charmap['ﻳ'] = cells[1]
    elif cells[0] == 'لآ':
        Charmap['ﻵ'] = cells[4]
        Charmap['ﻶ'] = cells[3]
    elif cells[0] == 'لأ':
        Charmap['ﻷ'] = cells[4]
        Charmap['ﻸ'] = cells[3]
    elif cells[0] == 'لإ':
        Charmap['ﻹ'] = cells[4]
        Charmap['ﻺ'] = cells[3]
    elif cells[0] == 'لا':
        Charmap['ﻻ'] = cells[4]
        Charmap['ﻼ'] = cells[3]
    elif cells[0] == 'پ':
        Charmap['ﭖ'] = cells[4]
        Charmap['ﭗ'] = cells[3]
        Charmap['ﭙ'] = cells[2]
        Charmap['ﭘ'] = cells[1]
    elif cells[0] == 'چ':
        Charmap['ﭺ'] = cells[4]
        Charmap['ﭻ'] = cells[3]
        Charmap['ﭽ'] = cells[2]
        Charmap['ﭼ'] = cells[1]
    elif cells[0] == 'ڤ':
        Charmap['ﭪ'] = cells[4]
        Charmap['ﭫ'] = cells[3]
        Charmap['ﭭ'] = cells[2]
        Charmap['ﭬ'] = cells[1]
    else:
        Charmap[cells[0]] = cells[4]
    return Charmap

def fixCharmap(Charmap : dict):
    for char in charsList:
        Charmap = fillEmptyCells(Charmap, char)
    Charmap.pop('', None)
    return Charmap

def sameItemsLengh(Charmap : dict, lengh : int):
    remove = []
    for k, v in Charmap.items():
        if len(k) != len(v) != lengh:
            remove.append(k)
    for k in remove: Charmap.pop(k, None)
    return Charmap