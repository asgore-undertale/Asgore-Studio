from Parts.Vars import Harakat, CharsConnectBoth, CharsConnectBefore

letters_Table = {
                    "ً"  : ['ﹰ', 'ﹱ', 'ﹰ', 'ﹰ'],
                    "ﹰ"  : ['ﹰ', 'ﹱ', 'ﹰ', 'ﹰ'],
                    "ٌ"  : ['ﹲ', 'ﹲ', 'ﹲ', 'ﹲ'],
                    "ٍ"  : ['ﹴ', 'ﹴ', 'ﹴ', 'ﹴ'],
                    "َ"  : ['ﹶ', 'ﹷ', 'ﹶ', 'ﹶ'],
                    "ﹶ"  : ['ﹶ', 'ﹶ', 'ﹶ', 'ﹶ'],
                    "ُ"  : ['ﹸ', 'ﹹ', 'ﹸ', 'ﹸ'],
                    "ﹸ"  : ['ﹸ', 'ﹸ', 'ﹸ', 'ﹸ'],
                    "ِ"  : ['ﹺ', 'ﹻ', 'ﹺ','ﹺ'],
                    "ﹺ"  : ['ﹺ', 'ﹺ', 'ﹺ', 'ﹺ'],
                    "ّ"  : ['ﹼ', 'ﹽ', 'ﹼ', 'ﹼ'],
                    "ﹼ"  : ['ﹼ', 'ﹼ', 'ﹼ', 'ﹼ'],
                    "ْ"  : ['ﹾ', 'ﹿ', 'ﹾ', 'ﹾ'],
                    "ﹾ"  : ['ﹾ', 'ﹾ', 'ﹾ', 'ﹾ'],
    }

def Reshape(text):
    reshaped_text = ''
    textlist = list(' '+text+' ')

    for i in range(1, len(textlist)-1):
        aroundbefore = 1
        while textlist[i-aroundbefore] in Harakat: aroundbefore += 1
        if (textlist[i] in CharsConnectBoth or textlist[i] in CharsConnectBefore or textlist[i] in Harakat) and (textlist[i-aroundbefore] in CharsConnectBoth):
            before = 1
        else:
            before = 0
        
        aroundafter = 1
        while textlist[i+aroundafter] in Harakat: aroundafter += 1
        if (textlist[i] in CharsConnectBoth or textlist[i] in Harakat) and (textlist[i+aroundafter] in CharsConnectBoth or textlist[i+aroundafter] in CharsConnectBefore):
            after = 1
        else:
            after = 0
        
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
    
    return reshaped_text