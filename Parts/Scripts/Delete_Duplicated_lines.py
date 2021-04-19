def DDL(text):
    lines_list = text.split('\n')
    deleted_lines_list = list(dict.fromkeys(lines_list))
    text = '\n'.join(deleted_lines_list)
    return text