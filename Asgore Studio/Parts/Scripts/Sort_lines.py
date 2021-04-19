def Sort(text, case = True):
    lines_list = text.split('\n')
    lines_list.sort(key=len)
    
    if case == False: lines_list = lines_list[::-1]
    text = '\n'.join(lines_list)
    
    return text