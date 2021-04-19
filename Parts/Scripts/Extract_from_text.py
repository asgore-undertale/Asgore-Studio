import re

def Extract(text, case = True, before = '', after = '', mini = False, maxi = False):
    if before == '' or after == '': return
    if mini == '': mini = False
    if maxi == '': maxi = False
    if isinstance(mini, str): mini = int(mini)
    if isinstance(maxi, str): maxi = int(maxi)
    if mini > maxi: return
    
    # المتغيرات
    English_Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    Symbols = '1234567890-=!"£$%^&*()_+`[];"@\|:~{}<>?./,# ' + "'"
    commands_chars = '.[]{}*+?()^'
    
    text = text.replace('\n', ' ')#الريجيكس يعاني مشاكل مع عودات السطر
    ##
    
    def minimax(text):
        if mini != False and len(text) < mini: return
        if maxi != False and len(text) > maxi: return
        return text
    
    def in_letters(text):
        for char in text:
            if char not in English_Letters and char not in Symbols:
                return
        return text
    
    if before == after:
        extracted_list = text.split(before)
        if len(extracted_list) > 2:
            del extracted_list[0]
            del extracted_list[-1]
    else:
        for char in commands_chars:
            before = before.replace(char, '\\'+char)
            after = after.replace(char, '\\'+char)
        pattern = before + "(.*?)" + after
        extracted_list = re.findall(pattern, text)
    
    if mini != False or mini != False:
        extracted_list = list(map(minimax, extracted_list))
        extracted_list = list(filter(lambda a: a != None and a != '', extracted_list))#list() for python 2.x
    if case:
        extracted_list = list(map(in_letters, extracted_list))
        extracted_list = list(filter(lambda a: a != None and a != '', extracted_list))
    
    extracted_list = list(dict.fromkeys(extracted_list))
    return extracted_list