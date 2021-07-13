import re

bows_list = ['()', '[]', '{}', '<>']
Arabic_letters = 'ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي' + '؟،؛ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼ'

def swap(text, char1, char2, unused_char = u'\uffff'):
    return text.replace(char1, unused_char).replace(char2, char1).replace(unused_char, char2)

def swap_edges_spaces(text):
    if len(text) < 2: return text
    beforeSpaces, afterSpaces = 0, 0
    
    while text[0] == ' ':
        beforeSpaces += 1
        text = text[1:len(text)]
    while text[-1] == ' ':
        afterSpaces += 1
        text = text[0:-1]
    
    return (beforeSpaces * ' ') + text + (afterSpaces * ' ')

def reverse_arabic(text):
    words = text.split(' ')
    for w in range(len(words)):
        if not words[w]: continue
        if words[w][-1] in Arabic_letters:
            words[w] = words[w][::-1]
    
    return swap_edges_spaces(' '.join(words[::-1]))

def Reverse(text, case = True):
    if case:
        for bow in bows_list:
            text = swap(text, bow[0], bow[1])
            text = text[::-1]
    else: text = reverse_arabic(text)
    
    return text