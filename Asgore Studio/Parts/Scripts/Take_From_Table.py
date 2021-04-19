def Take_From_Table(ate_file):
    chars_table = {}
    rows = open(ate_file, 'r', encoding="utf-8").read().split('\n')
    
    VERSION = float(rows[1][9:-1])
    SEPARATOR = rows[2][11:-1]
    
    for row in range(5, len(rows)):
        if not rows[row]: continue
        cols = rows[row].split(SEPARATOR)
        if cols[0] == 'آ':
            chars_table['ﺁ'] = cols[4]
            chars_table['ﺂ'] = cols[3]
        elif cols[0] == 'أ':
            chars_table['ﺃ'] = cols[4]
            chars_table['ﺄ'] = cols[3]
        elif cols[0] == 'ؤ':
            chars_table['ﺅ'] = cols[4]
            chars_table['ﺆ'] = cols[3]
        elif cols[0] == 'إ':
            chars_table['ﺇ'] = cols[4]
            chars_table['ﺈ'] = cols[3]
        elif cols[0] == 'ئ':
            chars_table['ﺉ'] = cols[4]
            chars_table['ﺊ'] = cols[3]
            chars_table['ﺌ'] = cols[2]
            chars_table['ﺋ'] = cols[1]
        elif cols[0] == 'ا':
            chars_table['ﺍ'] = cols[4]
            chars_table['ﺎ'] = cols[3]
        elif cols[0] == 'ب':
            chars_table['ﺏ'] = cols[4]
            chars_table['ﺐ'] = cols[3]
            chars_table['ﺒ'] = cols[2]
            chars_table['ﺑ'] = cols[1]
        elif cols[0] == 'ة':
            chars_table['ﺓ'] = cols[4]
            chars_table['ﺔ'] = cols[3]
        elif cols[0] == 'ت':
            chars_table['ﺕ'] = cols[4]
            chars_table['ﺖ'] = cols[3]
            chars_table['ﺘ'] = cols[2]
            chars_table['ﺗ'] = cols[1]
        elif cols[0] == 'ث':
            chars_table['ﺙ'] = cols[4]
            chars_table['ﺚ'] = cols[3]
            chars_table['ﺜ'] = cols[2]
            chars_table['ﺛ'] = cols[1]
        elif cols[0] == 'ج':
            chars_table['ﺝ'] = cols[4]
            chars_table['ﺞ'] = cols[3]
            chars_table['ﺠ'] = cols[2]
            chars_table['ﺟ'] = cols[1]
        elif cols[0] == 'ح':
            chars_table['ﺡ'] = cols[4]
            chars_table['ﺢ'] = cols[3]
            chars_table['ﺤ'] = cols[2]
            chars_table['ﺣ'] = cols[1]
        elif cols[0] == 'خ':
            chars_table['ﺥ'] = cols[4]
            chars_table['ﺦ'] = cols[3]
            chars_table['ﺨ'] = cols[2]
            chars_table['ﺧ'] = cols[1]
        elif cols[0] == 'د':
            chars_table['ﺩ'] = cols[4]
            chars_table['ﺪ'] = cols[3]
        elif cols[0] == 'ذ':
            chars_table['ﺫ'] = cols[4]
            chars_table['ﺬ'] = cols[3]
        elif cols[0] == 'ر':
            chars_table['ﺭ'] = cols[4]
            chars_table['ﺮ'] = cols[3]
        elif cols[0] == 'ز':
            chars_table['ﺯ'] = cols[4]
            chars_table['ﺰ'] = cols[3]
        elif cols[0] == 'س':
            chars_table['ﺱ'] = cols[4]
            chars_table['ﺲ'] = cols[3]
            chars_table['ﺴ'] = cols[2]
            chars_table['ﺳ'] = cols[1]
        elif cols[0] == 'ش':
            chars_table['ﺵ'] = cols[4]
            chars_table['ﺶ'] = cols[3]
            chars_table['ﺸ'] = cols[2]
            chars_table['ﺷ'] = cols[1]
        elif cols[0] == 'ص':
            chars_table['ﺹ'] = cols[4]
            chars_table['ﺺ'] = cols[3]
            chars_table['ﺼ'] = cols[2]
            chars_table['ﺻ'] = cols[1]
        elif cols[0] == 'ض':
            chars_table['ﺽ'] = cols[4]
            chars_table['ﺾ'] = cols[3]
            chars_table['ﻀ'] = cols[2]
            chars_table['ﺿ'] = cols[1]
        elif cols[0] == 'ط':
            chars_table['ﻁ'] = cols[4]
            chars_table['ﻂ'] = cols[3]
            chars_table['ﻄ'] = cols[2]
            chars_table['ﻃ'] = cols[1]
        elif cols[0] == 'ظ':
            chars_table['ﻅ'] = cols[4]
            chars_table['ﻆ'] = cols[3]
            chars_table['ﻈ'] = cols[2]
            chars_table['ﻇ'] = cols[1]
        elif cols[0] == 'ع':
            chars_table['ﻉ'] = cols[4]
            chars_table['ﻊ'] = cols[3]
            chars_table['ﻋ'] = cols[2]
            chars_table['ﻌ'] = cols[1]
        elif cols[0] == 'غ':
            chars_table['ﻍ'] = cols[4]
            chars_table['ﻎ'] = cols[3]
            chars_table['ﻐ'] = cols[2]
            chars_table['ﻏ'] = cols[1]
        elif cols[0] == 'ف':
            chars_table['ﻑ'] = cols[4]
            chars_table['ﻒ'] = cols[3]
            chars_table['ﻔ'] = cols[2]
            chars_table['ﻓ'] = cols[1]
        elif cols[0] == 'ق':
            chars_table['ﻕ'] = cols[4]
            chars_table['ﻖ'] = cols[3]
            chars_table['ﻘ'] = cols[2]
            chars_table['ﻗ'] = cols[1]
        elif cols[0] == 'ك':
            chars_table['ﻙ'] = cols[4]
            chars_table['ﻚ'] = cols[3]
            chars_table['ﻜ'] = cols[2]
            chars_table['ﻛ'] = cols[1]
        elif cols[0] == 'ل':
            chars_table['ﻝ'] = cols[4]
            chars_table['ﻞ'] = cols[3]
            chars_table['ﻠ'] = cols[2]
            chars_table['ﻟ'] = cols[1]
        elif cols[0] == 'م':
            chars_table['ﻡ'] = cols[4]
            chars_table['ﻢ'] = cols[3]
            chars_table['ﻤ'] = cols[2]
            chars_table['ﻣ'] = cols[1]
        elif cols[0] == 'ن':
            chars_table['ﻥ'] = cols[4]
            chars_table['ﻦ'] = cols[3]
            chars_table['ﻨ'] = cols[2]
            chars_table['ﻧ'] = cols[1]
        elif cols[0] == 'ه':
            chars_table['ﻩ'] = cols[4]
            chars_table['ﻪ'] = cols[3]
            chars_table['ﻬ'] = cols[2]
            chars_table['ﻫ'] = cols[1]
        elif cols[0] == 'و':
            chars_table['ﻭ'] = cols[4]
            chars_table['ﻮ'] = cols[3]
        elif cols[0] == 'ى':
            chars_table['ﻯ'] = cols[4]
            chars_table['ﻰ'] = cols[3]
        elif cols[0] == 'ي':
            chars_table['ﻱ'] = cols[4]
            chars_table['ﻲ'] = cols[3]
            chars_table['ﻴ'] = cols[2]
            chars_table['ﻳ'] = cols[1]
        elif cols[0] == 'لآ':
            chars_table['ﻵ'] = cols[4]
            chars_table['ﻶ'] = cols[3]
        elif cols[0] == 'لأ':
            chars_table['ﻷ'] = cols[4]
            chars_table['ﻸ'] = cols[3]
        elif cols[0] == 'لإ':
            chars_table['ﻹ'] = cols[4]
            chars_table['ﻺ'] = cols[3]
        elif cols[0] == 'لا':
            chars_table['ﻻ'] = cols[4]
            chars_table['ﻼ'] = cols[3]
        else:
            if len(cols) == 5: chars_table[cols[0]] = cols[4]

    return chars_table