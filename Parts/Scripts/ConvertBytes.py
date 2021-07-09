def convertBytes(text : str, subject = r'\xXY'):
    if not text or not subject: return text
    
    newText, passTimes = '', 0
    
    for char in range(3, len(text)):
        if passTimes > 0:
            passTimes -= 1
            continue
        if text[char - 3] == '\\' and text[char - 2] == 'x':
            byte = subject.replace('X', text[char - 1]).replace('Y', text[char])
            newText += byte
            passTimes = 3
        else: newText += text[char - 3]
    
    z = 3 - passTimes
    newText += text[len(text)-z : len(text)]
    return newText