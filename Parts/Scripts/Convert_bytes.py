def convert_bytes(text : str, subject : str, new_text = '', x = 0):
    if not text or not subject: return text

    for char in range(3, len(text)):
        if x > 0:
            x -= 1
            continue
        if text[char - 3] == '\\' and text[char - 2] == 'x':
            byte = subject.replace('X', text[char - 1]).replace('Y', text[char])
            new_text += byte
            x = 3
        else: new_text += text[char - 3]
    
    z = 3 - x
    for i in range(0, z): new_text += text[i - z]
    return new_text