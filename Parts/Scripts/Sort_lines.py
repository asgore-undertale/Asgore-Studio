def Sort(text, lineCom = '\n', case = True):
    if not lineCom: lineCom = '\n'

    lines_list = text.split(lineCom)
    lines_list.sort(key=len)
    
    if not case: lines_list = lines_list[::-1]
    text = lineCom.join(lines_list)
    
    return text