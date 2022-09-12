from Parts.Vars import Harakat, CharsConnectBoth, CharsConnectBefore, FreezedArabicTable, LaList

def Freeze(text, case = True, mergLA = True):
    if case:
        reshaped_text = ''
        textlist = ' '+text+' '

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

            if textlist[i] not in FreezedArabicTable:
                reshaped_text += textlist[i]
            else:
                if before == 0 and after == 1: #أول الكلمة
                    reshaped_text += FreezedArabicTable[textlist[i]][0]
                elif before == 1 and after == 1: #وسط الكلمة
                    reshaped_text += FreezedArabicTable[textlist[i]][1]
                elif before == 1 and after == 0: #آخر الكلمة
                    reshaped_text += FreezedArabicTable[textlist[i]][2]
                elif before == 0 and after == 0: #منفصل
                    reshaped_text += FreezedArabicTable[textlist[i]][3]

        if mergLA:
            for la in LaList:
                reshaped_text = reshaped_text.replace(la[0], la[1])
        
        return reshaped_text
    else:
        for k, v in FreezedArabicTable.items():
            for char in v:
                text = text.replace(char, k)

        return text