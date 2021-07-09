def Width(text : str, charmap : dict):
    textWidth = 0
    for char in text:
        if char not in charmap: continue
        textWidth += charmap[char][2] + charmap[char][6]
    return textWidth

def OffsetTextWithSpaces(text : str, charsNum : int, textOffset : int):
    spacesNum = charsNum - len(text)
    if   textOffset == 0: #first
        return ' ' * spacesNum
    elif textOffset == 1: #middle
        halfSpaces = spacesNum // 2
        return ' ' * halfSpaces + text + ' ' * (spacesNum - halfSpaces)
    elif textOffset == 2: #last
        return ' ' * spacesNum + text

def OffsetLineWithSpaces(line : str, charmap : dict, LineMaxWidth : int, lineOffset : int):
    if ' ' not in charmap:
        print('(Space) have no width.')
        return line
    
    lineWidth = Width(line, charmap)
    
    SpacesNum = int((LineMaxWidth - lineWidth) / (charmap[' '][2] + charmap[' '][6]))
    
    if   lineOffset == 0: # إزاحة من اليمين لليسار
        return line + (' ' * SpacesNum)
    elif lineOffset == 1: # إزاحة من اليسار لليمين
        return (' ' * SpacesNum) + line
    elif lineOffset == 2: # إزاحة من اليمين للوسط
        return (' ' * (SpacesNum // 2)) + line
    elif lineOffset == 3: # إزاحة من اليسار للوسط
        return (' ' * (SpacesNum // 2)) + line + (' ' * (SpacesNum - (SpacesNum // 2)))

def OffsetLineWithCommands(line : str, charmap : dict, LineMaxWidth : int, lineOffset : int, command : str): #  : (px) should be in command
    lineWidth = Width(line, charmap)
    freeSpace = LineMaxWidth - lineWidth
    
    if   lineOffset == 0: # إزاحة من اليمين لليسار
        command = command.replace('(px)', str(freeSpace), 1)
        return line + command
    elif lineOffset == 1: # إزاحة من اليسار لليمين
        command = command.replace('(px)', str(freeSpace), 1)
        return command + line
    elif lineOffset == 2: # إزاحة من اليمين للوسط
        command = command.replace('(px)', str(freeSpace // 2), 1)
        return command + line
    elif lineOffset == 3: # إزاحة من اليسار للوسط
        return command.replace('(px)', str(freeSpace // 2), 1) + line + command.replace('(px)', str(freeSpace // 2 + 1), 1)