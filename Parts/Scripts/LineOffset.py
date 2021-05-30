def Width(text : str, charmap : dict):
    textWidth = 0
    for char in text:
        if char not in charmap: continue
        textWidth += charmap[char][2] + charmap[char][6]
    return textWidth

def OffsetLineWithSpaces(line : str, charmap : dict, LineMaxWidth : int, lineOffset : int):
    if ' ' not in charmap:
        print('(Space) have no width.')
        return line
    
    lineWidth = Width(line, charmap)
    
    SpacesNum = int((LineMaxWidth - lineWidth) / (charmap[' '][2] + charmap[' '][6]))
    
    if   lineOffset == 0: # إزاحة من اليمين لليسار
        line = line + (' ' * SpacesNum)
    elif lineOffset == 1: # إزاحة من اليسار لليمين
        line = (' ' * SpacesNum) + line
    elif lineOffset == 2: # إزاحة من اليمين للوسط
        line = (' ' * (SpacesNum // 2)) + line
    elif lineOffset == 3: # إزاحة من اليسار للوسط
        line = (' ' * (SpacesNum // 2)) + line + (' ' * (SpacesNum - (SpacesNum // 2)))
    
    return line

def OffsetLineWithCommands(line : str, charmap : dict, LineMaxWidth : int, lineOffset : int, command : str): #  : (px) should be in command
    lineWidth = Width(line, charmap)
    freeSpace = LineMaxWidth - lineWidth
    
    if   lineOffset == 0: # إزاحة من اليمين لليسار
        command = command.replace('(px)', str(freeSpace), 1)
        line = line + command
    elif lineOffset == 1: # إزاحة من اليسار لليمين
        command = command.replace('(px)', str(freeSpace), 1)
        line = command + line
    elif lineOffset == 2: # إزاحة من اليمين للوسط
        command = command.replace('(px)', str(freeSpace // 2), 1)
        line = command + line
    elif lineOffset == 3: # إزاحة من اليسار للوسط
        line = command.replace('(px)', str(freeSpace // 2), 1) + line + command.replace('(px)', str(freeSpace // 2 + 1), 1)
    
    return line