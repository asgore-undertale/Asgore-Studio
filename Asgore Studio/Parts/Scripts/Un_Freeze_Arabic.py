letters_Table = {'''  '<initial>' '<medial>' '<final>' '<isolated>' '''
                    "ء" : [u"\ufe80", u"\ufe80", u"\ufe80", u"\ufe80"], #Xإن محيت الهمزة من هنا فستحدث مشكلة
                    "آ" : [u"\ufe81", u"\ufe82", u"\ufe82", u"\ufe81"],
                    "أ" : [u"\ufe83", u"\ufe84", u"\ufe84", u"\ufe83"],
                    "ؤ" : [u"\ufe85", u"\ufe86", u"\ufe86", u"\ufe85"],
                    "إ" : [u"\ufe87", u"\ufe88", u"\ufe88", u"\ufe87"],
                    "ئ" : [u"\ufe8b", u"\ufe8c", u"\ufe8a", u"\ufe89"],
                    "ا" : [u"\ufe8d", u"\ufe8e", u"\ufe8e", u"\ufe8d"],
                    "ب" : [u"\ufe91", u"\ufe92", u"\ufe90", u"\ufe8f"],
                    "ة" : [u"\ufe93", u"\ufe94", u"\ufe94", u"\ufe93"],
                    "ت" : [u"\ufe97", u"\ufe98", u"\ufe96", u"\ufe95"],
                    "ث" : [u"\ufe9b", u"\ufe9c", u"\ufe9a", u"\ufe99"],
                    "ج" : [u"\ufe9f", u"\ufea0", u"\ufe9e", u"\ufe9d"],
                    "ح" : [u"\ufea3", u"\ufea4", u"\ufea2", u"\ufea1"],
                    "خ" : [u"\ufea7", u"\ufea8", u"\ufea6", u"\ufea5"],
                    "د" : [u"\ufea9", u"\ufeaa", u"\ufeaa", u"\ufea9"],
                    "ذ" : [u"\ufeab", u"\ufeac", u"\ufeac", u"\ufeab"],
                    "ر" : [u"\ufead", u"\ufeae", u"\ufeae", u"\ufead"],
                    "ز" : [u"\ufeaf", u"\ufeb0", u"\ufeb0", u"\ufeaf"],
                    "س" : [u"\ufeb3", u"\ufeb4", u"\ufeb2", u"\ufeb1"],
                    "ش" : [u"\ufeb7", u"\ufeb8", u"\ufeb6", u"\ufeb5"],
                    "ص" : [u"\ufebb", u"\ufebc", u"\ufeba", u"\ufeb9"],
                    "ض" : [u"\ufebf", u"\ufec0", u"\ufebe", u"\ufebd"],
                    "ط" : [u"\ufec3", u"\ufec4", u"\ufec2", u"\ufec1"],
                    "ظ" : [u"\ufec7", u"\ufec8", u"\ufec6", u"\ufec5"],
                    "ع" : [u"\ufecb", u"\ufecc", u"\ufeca", u"\ufec9"],
                    "غ" : [u"\ufecf", u"\ufed0", u"\ufece", u"\ufecd"],
                    "ف" : [u"\ufed3", u"\ufed4", u"\ufed2", u"\ufed1"],
                    "ق" : [u"\ufed7", u"\ufed8", u"\ufed6", u"\ufed5"],
                    "ك" : [u"\ufedb", u"\ufedc", u"\ufeda", u"\ufed9"],
                    "ل" : [u"\ufedf", u"\ufee0", u"\ufede", u"\ufedd"],
                    "م" : [u"\ufee3", u"\ufee4", u"\ufee2", u"\ufee1"],
                    "ن" : [u"\ufee7", u"\ufee8", u"\ufee6", u"\ufee5"],
                    "ه" : [u"\ufeeb", u"\ufeec", u"\ufeea", u"\ufee9"],
                    "و" : [u"\ufeed", u"\ufeee", u"\ufeee", u"\ufeed"],
                    "ى" : [u"\ufeef", u"\ufef0", u"\ufef0", u"\ufeef"],
                    "ي" : [u"\ufef3", u"\ufef4", u"\ufef2", u"\ufef1"],
                    "لآ" : [u"\ufef5", u"\ufef6", u"\ufef6", u"\ufef5"],
                    "لأ" : [u"\ufef7", u"\ufef8", u"\ufef8", u"\ufef7"],
                    "لإ" : [u"\ufef9", u"\ufefa", u"\ufefa", u"\ufef9"],
                    "لا" : [u"\ufefb", u"\ufefc", u"\ufefc", u"\ufefb"],
                    "پ" : [u"\ufb58", u"\ufb59", u"\ufb57", u"\ufb56"],
                    "چ" : [u"\ufb7c", u"\ufb7d", u"\ufb7b", u"\ufb7a"],
                    "ڤ" : [u"\ufb6c", u"\ufb6d", u"\ufb6b", u"\ufb6a"],
    }

def Un_Freeze(text, case = True):
    if case:
        harakat = "ًٌٍَُِّْ"
        list1 = 'ئبتثجحخسشصضطظعغفقكلمنهي'
        list2 = 'آأؤإاةدذرزوى'
        list3 = 'ء '

        reshaped_text = ''
        textlist = list(' '+text+' ') #هذه الخطوة ضرورية ليعمل الكود بشكل صحيح

        for i in range(1, len(textlist)-1):
            #تقرير إن كان الحرف متصلا بما قبله أم لا
            aroundbefore = 1
            while textlist[i-aroundbefore] in harakat:
                aroundbefore += 1
            if textlist[i-aroundbefore] in list1:
                before = 1
            else:
                before = 0

            #تقرير إن كان الحرف متصلا بما بعده أم لا
            aroundafter = 1
            while textlist[i+aroundafter] in harakat:
                aroundafter += 1
            if textlist[i] in list1 and textlist[i+aroundafter] in list1 or textlist[i] in list1 and textlist[i+aroundafter] in list2:
                after = 1
            else:
                after = 0

            if textlist[i] not in letters_Table: #إن لم يكن في الجدول
                if textlist[i] == 'ء':  #وضعت الهمزة هنا لأنها لم تعمل في الجدول
                    new_text = u"\ufe80"
                else:
                    new_text = textlist[i]  #إن لم يكن في الجدول اترك الحرف كما هو
            else:
                #إن كان في الجدول فحدد شكله
                if before == 0 and after == 1: #أول الكلمة
                    new_text = letters_Table[textlist[i]][0]
                if before == 1 and after == 1: #وسط الكلمة
                        new_text = letters_Table[textlist[i]][1]
                if before == 1 and after == 0: #آخر الكلمة
                    new_text = letters_Table[textlist[i]][2]
                if before == 0 and after == 0: #منفصل
                    new_text = letters_Table[textlist[i]][3]

            reshaped_text += str(new_text)  #أضف الحرف لمتغير واحد
            new_text = ''   #ارجع قيمة المتغير الذي يأخذ قيمة الحرف عدما كي لا تتراكم الأحرف فيه

        #لاستبدال الألف واللام المنفصلين بحرف متصل
        reshaped_text = reshaped_text.replace('ﻟﺂ', 'ﻵ')
        reshaped_text = reshaped_text.replace('ﻠﺂ', 'ﻶ')
        reshaped_text = reshaped_text.replace('ﻟﺄ', 'ﻷ')
        reshaped_text = reshaped_text.replace('ﻠﺄ', 'ﻸ')
        reshaped_text = reshaped_text.replace('ﻟﺈ', 'ﻹ')
        reshaped_text = reshaped_text.replace('ﻠﺈ', 'ﻺ')
        reshaped_text = reshaped_text.replace('ﻟﺎ', 'ﻻ')
        reshaped_text = reshaped_text.replace('ﻠﺎ', 'ﻼ')
        text = reshaped_text
    else:
        for char in text:
            for k, v in letters_Table.items():
                if char in v:
                    text = text.replace(char, k)
                    break

    return text