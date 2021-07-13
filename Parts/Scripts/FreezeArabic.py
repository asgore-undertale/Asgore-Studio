from Parts.Vars import Harakat, CharsConnectBoth, CharsConnectBefore

letters_Table = {#<initial><medial><final><isolated>
                    "ء" : ['ﺀ', 'ﺀ', 'ﺀ', 'ﺀ'],
                    "آ" : ['ﺁ', 'ﺂ', 'ﺂ', 'ﺁ'],
                    "أ" : ['ﺃ', 'ﺄ', 'ﺄ', 'ﺃ'],
                    "ؤ" : ['ﺅ', 'ﺆ', 'ﺆ', 'ﺅ'],
                    "إ" : ['ﺇ', 'ﺈ', 'ﺈ', 'ﺇ'],
                    "ئ" : ['ﺋ', 'ﺌ', 'ﺊ', 'ﺉ'],
                    "ا" : ['ﺍ', 'ﺎ', 'ﺎ', 'ﺍ'],
                    "ب" : ['ﺑ', 'ﺒ', 'ﺐ', 'ﺏ'],
                    "ة" : ['ﺓ', 'ﺔ', 'ﺔ', 'ﺓ'],
                    "ت" : ['ﺗ', 'ﺘ', 'ﺖ', 'ﺕ'],
                    "ث" : ['ﺛ', 'ﺜ', 'ﺚ', 'ﺙ'],
                    "ج" : ['ﺟ', 'ﺠ', 'ﺞ', 'ﺝ'],
                    "ح" : ['ﺣ', 'ﺤ', 'ﺢ', 'ﺡ'],
                    "خ" : ['ﺧ', 'ﺨ', 'ﺦ', 'ﺥ'],
                    "د" : ['ﺩ', 'ﺪ', 'ﺪ', 'ﺩ'],
                    "ذ" : ['ﺫ', 'ﺬ', 'ﺬ', 'ﺫ'],
                    "ر" : ['ﺭ', 'ﺮ', 'ﺮ', 'ﺭ'],
                    "ز" : ['ﺯ', 'ﺰ', 'ﺰ', 'ﺯ'],
                    "س" : ['ﺳ', 'ﺴ', 'ﺲ', 'ﺱ'],
                    "ش" : ['ﺷ', 'ﺸ', 'ﺶ', 'ﺵ'],
                    "ص" : ['ﺻ', 'ﺼ', 'ﺺ', 'ﺹ'],
                    "ض" : ['ﺿ', 'ﻀ', 'ﺾ', 'ﺽ'],
                    "ط" : ['ﻃ', 'ﻄ', 'ﻂ', 'ﻁ'],
                    "ظ" : ['ﻇ', 'ﻈ', 'ﻆ', 'ﻅ'],
                    "ع" : ['ﻋ', 'ﻌ', 'ﻊ', 'ﻉ'],
                    "غ" : ['ﻏ', 'ﻐ', 'ﻎ', 'ﻍ'],
                    "ف" : ['ﻓ', 'ﻔ', 'ﻒ', 'ﻑ'],
                    "ق" : ['ﻗ', 'ﻘ', 'ﻖ', 'ﻕ'],
                    "ك" : ['ﻛ', 'ﻜ', 'ﻚ', 'ﻙ'],
                    "ل" : ['ﻟ', 'ﻠ', 'ﻞ', 'ﻝ'],
                    "م" : ['ﻣ', 'ﻤ', 'ﻢ', 'ﻡ'],
                    "ن" : ['ﻧ', 'ﻨ', 'ﻦ', 'ﻥ'],
                    "ه" : ['ﻫ', 'ﻬ', 'ﻪ', 'ﻩ'],
                    "و" : ['ﻭ', 'ﻮ', 'ﻮ', 'ﻭ'],
                    "ى" : ['ﻯ', 'ﻰ', 'ﻰ', 'ﻯ'],
                    "ي" : ['ﻳ', 'ﻴ', 'ﻲ', 'ﻱ'],
                    "لآ" : ['ﻵ', 'ﻶ', 'ﻶ', 'ﻵ'],
                    "لأ" : ['ﻷ', 'ﻸ', 'ﻸ', 'ﻷ'],
                    "لإ" : ['ﻹ', 'ﻺ', 'ﻺ', 'ﻹ'],
                    "لا" : ['ﻻ', 'ﻼ', 'ﻼ', 'ﻻ'],
                    "پ" : ['ﭘ', 'ﭙ', 'ﭗ', 'ﭖ'],
                    "چ" : ['ﭼ', 'ﭽ', 'ﭻ', 'ﭺ'],
                    "ڤ" : ['ﭬ', 'ﭭ', 'ﭫ', 'ﭪ'],
                    "ـ" : ['ـ', 'ـ', 'ـ', 'ـ'],
                    "ً"  : ['ﹰ', 'ﹰ', 'ﹰ', 'ﹰ'],
                    #"ً"  : ['ﹰ', 'ﹱ', 'ﹰ', 'ﹰ'],
                    "ٌ"  : ['ﹲ', 'ﹲ', 'ﹲ', 'ﹲ'],
                    "ٍ"  : ['ﹴ', 'ﹴ', 'ﹴ', 'ﹴ'],
                    "َ"  : ['ﹶ', 'ﹶ', 'ﹶ', 'ﹶ'],
                    #"َ"  : ['ﹶ', 'ﹷ', 'ﹶ', 'ﹶ'],
                    "ُ"  : ['ﹸ', 'ﹸ', 'ﹸ', 'ﹸ'],
                    #"ُ"  : ['ﹸ', 'ﹹ', 'ﹸ', 'ﹸ'],
                    "ِ"  : ['ﹺ', 'ﹺ', 'ﹺ', 'ﹺ'],
                    #"ِ"  : ['ﹺ', 'ﹻ', 'ﹺ','ﹺ'],
                    "ّ"  : ['ﹼ', 'ﹼ', 'ﹼ', 'ﹼ'],
                    #"ّ"  : ['ﹼ', 'ﹽ', 'ﹼ', 'ﹼ'],
                    "ْ"  : ['ﹾ', 'ﹾ', 'ﹾ', 'ﹾ'],
                    #"ْ"  : ['ﹾ', 'ﹿ', 'ﹾ', 'ﹾ'],
    }

def Freeze(text, case = True, mergLA = True):
    if case:
        reshaped_text = ''
        textlist = list(' '+text+' ')

        for i in range(1, len(textlist)-1):
            aroundbefore = 1
            while textlist[i-aroundbefore] in Harakat: aroundbefore += 1
            #if (textlist[i] in CharsConnectBoth or textlist[i] in CharsConnectBefore or textlist[i] in Harakat) and (textlist[i-aroundbefore] in CharsConnectBoth):
            if textlist[i-aroundbefore] in CharsConnectBoth:
                before = 1
            else: before = 0

            aroundafter = 1
            while textlist[i+aroundafter] in Harakat: aroundafter += 1
            #if (textlist[i] in CharsConnectBoth or textlist[i] in Harakat) and (textlist[i+aroundafter] in CharsConnectBoth or textlist[i+aroundafter] in CharsConnectBefore):
            if textlist[i] in CharsConnectBoth and (textlist[i+aroundafter] in CharsConnectBoth or textlist[i+aroundafter] in CharsConnectBefore):
                after = 1
            else: after = 0

            if textlist[i] not in letters_Table:
                reshaped_text += textlist[i]
            else:
                if before == 0 and after == 1: #أول الكلمة
                    reshaped_text += letters_Table[textlist[i]][0]
                elif before == 1 and after == 1: #وسط الكلمة
                    reshaped_text += letters_Table[textlist[i]][1]
                elif before == 1 and after == 0: #آخر الكلمة
                    reshaped_text += letters_Table[textlist[i]][2]
                elif before == 0 and after == 0: #منفصل
                    reshaped_text += letters_Table[textlist[i]][3]

        if mergLA:
            LaList = [
                ('ﻟﺂ', 'ﻵ'), ('ﻠﺂ', 'ﻶ'), ('ﻟﺄ', 'ﻷ'), ('ﻠﺄ', 'ﻸ'),
                ('ﻟﺈ', 'ﻹ'), ('ﻠﺈ', 'ﻺ'), ('ﻟﺎ', 'ﻻ'), ('ﻠﺎ', 'ﻼ')
            ]
            for la in LaList:
                reshaped_text = reshaped_text.replace(la[0], la[1])
        
        return reshaped_text
    else:
        for k, v in letters_Table.items():
            for char in v:
                text = text.replace(char, k)

        return text