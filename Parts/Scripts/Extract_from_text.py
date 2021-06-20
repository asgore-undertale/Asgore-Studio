import re

EnglishLetters = ' !"'+"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def minimax(text):
    if mini and len(text) < mini: return
    if maxi and len(text) > maxi: return
    return text
    
def inEnglish(text):
    for char in text:
        if char not in EnglishLetters:
            return
    return text

def Extract(text, before, after, mini = False, maxi = False, onlyEnglish = False):
    if not before or not after: return
    try:
        mini = int(mini)
        maxi = int(maxi)
    except:
        mini = False
        maxi = False
    if mini > maxi: return
    
    # المتغيرات
    commands_chars = '.[]{}*+?()^'
    text = text.replace('\n', u'\uffff' * 8)#الريجيكس يعاني مشاكل مع عودات السطر
    
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
    
    extracted_list = [x.replace(u'\uffff' * 8, '\n') for x in extracted_list]
    
    if onlyEnglish:
        extracted_list = list(map(inEnglish, extracted_list))
        extracted_list = list(filter(lambda a: a, extracted_list))
    
    if mini or maxi:
        extracted_list = list(map(minimax, extracted_list))
        extracted_list = list(filter(lambda a: a, extracted_list))
    
    return extracted_list