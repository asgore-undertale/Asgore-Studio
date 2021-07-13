import re

bowslist = ['()', '[]', '{}', '<>']
ArabicLetters = 'ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيپچڤ' + '؟،؛ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼﭬﭭﭫﭪﭼﭽﭻﭺﭘﭙﭗﭖ'

def swap(text, char1, char2, unused_char = u'\uffff'):
    return text.replace(char1, unused_char).replace(char2, char1).replace(unused_char, char2)

def swapSpacesOnEdges(text):
    if len(text) < 2: return text
    beforeSpaces, afterSpaces = 0, 0
    
    while text[0] == ' ':
        beforeSpaces += 1
        text = text[1:len(text)]
    while text[-1] == ' ':
        afterSpaces += 1
        text = text[0:-1]
    
    return (beforeSpaces * ' ') + text + (afterSpaces * ' ')

def reverseArabic(text):
    container = ''
    for char in text:
        if char in ArabicLetters:
            container += char
        else:
            if not container: continue
            text = text.replace(container, container[::-1], 1)
            container = ''
    
    return swapSpacesOnEdges(text)

def Reverse(text, case = True):
    if case:
        for bow in bowslist:
            text = swap(text, bow[0], bow[1])
            text = text[::-1]
    else: text = reverseArabic(text)
    
    return text