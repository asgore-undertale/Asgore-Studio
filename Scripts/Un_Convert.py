def Convert(text, convert_dic, case = True, ANITC = True): # Add Not In Table Chars
    if len(convert_dic) == 0: return
    
    new_text = ''
    if case:
        for char in text:
            if char == '\n': new_text += char
            elif char in convert_dic: new_text += convert_dic[char]
            elif ANITC: new_text += char
    else:
        for char in text:
            for k, v in convert_dic.items():
                if v == char:
                    new_text += k
                    break

    return new_text