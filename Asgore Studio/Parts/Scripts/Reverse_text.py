import re

bows_list = ['()', '[]', '{}', '<>']
Arabic_letters = 'ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي' + '؟،؛ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼ'

def swap(text, char1, char2, unused_char = u'\uffff'):
    text = text.replace(char1, unused_char)
    text = text.replace(char2, char1)
    text = text.replace(unused_char, char2)
    return text

def swap_edges_spaces(text):
    text = list(text)
    counter = 0
    while text[counter] == ' ':
        counter += 1
    while text[-1] == ' ':
        del text[-1]
        text.insert(0, ' ')
    for _ in range(counter):
        del text[0]
        text.append(' ')
    return ''.join(text)

def reverse_arabic(text):
    word, spaces = '', ''
    for char in text:
        if char in Arabic_letters:
            word += spaces
            word += char
            spaces = ''
        elif char == ' ':
            if word != '': spaces += char
        else:
            text = text.replace(word, word[::-1])
            spaces = ''
            word = ''
    if word != '': text = text.replace(word, word[::-1])
    return text

def reverse_script(text, start_command, end_command, case = True):
    for bow in bows_list:
        if bow[0] not in (start_command + end_command) or bow[1] not in (start_command + end_command):
            text = swap(text, bow[0], bow[1])
    if start_command == '' or end_command == '':
        if case:
            text = text[::-1]
        else:
            text = reverse_arabic(text)
        return text
    else:
        commands_chars = '.[]{}*+?()^'
        re_start_command = start_command
        re_end_command = end_command
        for char in commands_chars:
            re_start_command = re_start_command.replace(char, '\\'+char)
            re_end_command = re_end_command.replace(char, '\\'+char)
        pattern = re_start_command + "(.*?)" + re_end_command
        text_list = re.split(pattern, text)
        
        for _ in range(len(text_list)):
            if _%2 == 1:
                text_list[_] = start_command + text_list[_] + end_command
            else:
                if case:
                    text_list[_] = text_list[_][::-1]
                else:
                    text_list[_] = reverse_arabic(text_list[_])
                    text_list[_] = swap_edges_spaces(text_list[_])
        text = ''.join(text_list[::-1])
        return text

def Reverse(text, start_command, end_command, new_page_command='', new_line_command='\n', case = True):
    if new_page_command != '': text_pages_list = text.split(new_page_command)
    else: text_pages_list = [text]
    if new_line_command != '':  text_pages_lines_list = [page.split(new_line_command) for page in text_pages_list]
    else: text_pages_lines_list = [text_pages_list]
   
    reversed_text = ''
    
    for page in range(len(text_pages_lines_list)):
        for line in range(len(text_pages_lines_list[page])):
            reversed_text += reverse_script(text_pages_lines_list[page][line], start_command, end_command, case)
            if len(text_pages_lines_list[page])-1 > line: reversed_text += new_line_command 
        if len(text_pages_lines_list)-1 > page : reversed_text += new_page_command 
    
    if case: reversed_text = '\n'.join(reversed_text.split('\n')[::-1])
    return reversed_text