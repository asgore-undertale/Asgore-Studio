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

harakat = 'َﹰﹱﹲﹴﹶﹷﹸﹹﹺﹻﹼﹽﹾﹿًٌٍَُِّْ'
list1 = 'ئبتثجحخسشصضطظعغفقكلمنهيپچڤـ'
list2 = 'آأؤإاةدذرزوى'

def Reshape(text):
    reshaped_text = ''
    textlist = list(' '+text+' ')

    for i in range(1, len(textlist)-1):
        aroundbefore = 1
        while textlist[i-aroundbefore] in harakat: aroundbefore += 1
        if (textlist[i] in list1 or textlist[i] in list2 or textlist[i] in harakat) and (textlist[i-aroundbefore] in list1):
            before = 1
        else:
            before = 0
        
        aroundafter = 1
        while textlist[i+aroundafter] in harakat: aroundafter += 1
        if (textlist[i] in list1 or textlist[i] in harakat) and (textlist[i+aroundafter] in list1 or textlist[i+aroundafter] in list2):
            after = 1
        else:
            after = 0
        
        if textlist[i] not in letters_Table:
            new_text = textlist[i]
        else:
            if before == 0 and after == 1: #أول الكلمة
                new_text = letters_Table[textlist[i]][0]
            elif before == 1 and after == 1: #وسط الكلمة
                new_text = letters_Table[textlist[i]][1]
            elif before == 1 and after == 0: #آخر الكلمة
                new_text = letters_Table[textlist[i]][2]
            elif before == 0 and after == 0: #منفصل
                new_text = letters_Table[textlist[i]][3]
        
        reshaped_text += str(new_text)
        new_text = ''
    
    return reshaped_text