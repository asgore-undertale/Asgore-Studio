def OffsetLine(line, charmap, LineMaxWidth, lineOffset):
    if ' ' not in charmap:
        print('(Space) have no width.')
        return line
    
    lineWidth = 0
    for char in line:
        if char not in charmap: continue
        lineWidth += charmap[char][2] + charmap[char][6]
    
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