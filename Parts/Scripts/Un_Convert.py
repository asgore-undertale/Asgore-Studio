def Convert(text, convert_dic, case = True, ANITC = True): # Add Not In Table Chars
    if not len(convert_dic): return
    
    if case:
        for k, v in convert_dic.items():
            if not k: continue
            text = text.replace(k, v)
    else:
        for k, v in convert_dic.items():
            if not v: continue
            text = text.replace(v, k)

    return text
    
    # new_text = ''
    # if case:
        # for char in text:
            # if char == '\n': new_text += char
            # elif char in convert_dic: new_text += convert_dic[char]
            # elif ANITC: new_text += char
    # else:
        # for char in text:
            # for k, v in convert_dic.items():
                # if v == char:
                    # new_text += k
                    # break

    # return new_text