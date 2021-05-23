def DDL(text, lineCom = '\n'):
    if not lineCom: lineCom = '\n'
    
    lines_list = text.split(lineCom)
    deleted_lines_list = list(dict.fromkeys(lines_list))
    text = lineCom.join(deleted_lines_list)
    return text