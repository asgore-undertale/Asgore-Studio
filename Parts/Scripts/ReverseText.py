import re

bows_list = ['()', '[]', '{}', '<>']
Arabic_letters = 'ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي' + '؟،؛ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼ'

def swap(text, char1, char2, unused_char = u'\uffff'):
    return text.replace(char1, unused_char).replace(char2, char1).replace(unused_char, char2)

def swap_edges_spaces(text):
    text = list(text)
    counter = 0
    while not text[counter]:
        counter += 1
    while not text[-1]:
        del text[-1]
        text.insert(0, ' ')
    for _ in range(counter):
        del text[0]
        text.append(' ')
    return ''.join(text)

def reverse_arabic(text):
    words = text.split(' ')
    for w in range(len(words)):
        if not words[w]: continue
        if words[w][0] in Arabic_letters:
            words[w] = words[w][::-1]
    return swap_edges_spaces(' '.join(words[::-1]))

def Reverse(text, case = True):
    for bow in bows_list:
        text = swap(text, bow[0], bow[1])
    
    if case: text = text[::-1]
    else: text = reverse_arabic(text)
    
    return text