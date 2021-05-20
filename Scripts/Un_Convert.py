import re

def Convert(text, convert_dic, case = True):
    if len(convert_dic) == 0: return
    
    new_text = ''
    if case:
        for char in text:
            if char in convert_dic and convert_dic[char]: new_text += convert_dic[char]
            elif char == '\n' or char == ' ': new_text += char
    else:
        for char in text:
            for k, v in convert_dic.items():
                if k == char: new_text += v

    return new_text