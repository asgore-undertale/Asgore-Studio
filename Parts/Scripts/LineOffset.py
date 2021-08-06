def Width(text : str, charmap : dict):
    textWidth = 0
    for char in text:
        if char not in charmap: continue
        textWidth += charmap[char][2] + charmap[char][6]
    return textWidth

def OffsetTextWithSpaces(text : str, charsNum : int, textOffset : int, spacesNum = 0):
    if not spacesNum: spacesNum = charsNum - len(text)
    if spacesNum <= 0: return text
    
    if   textOffset == 0: # first
        return text + ' ' * spacesNum
    elif textOffset == 1: # last
        return ' ' * spacesNum + text
    elif textOffset == 2: # middle
        halfSpaces = spacesNum // 2
        return (' ' * halfSpaces) + text
    elif textOffset == 3: # middle filled
        halfSpaces = spacesNum // 2
        return (' ' * halfSpaces) + text + ' ' * (spacesNum - halfSpaces)

def OffsetLineWithSpaces(line : str, charmap : dict, LineMaxWidth : int, lineOffset : int, spacesNum = 0):
    if ' ' not in charmap:
        print('(Space) have no width.')
        return line
    
    if not spacesNum:
        lineWidth = Width(line, charmap)
        spacesNum = int((LineMaxWidth - lineWidth) / (charmap[' '][2] + charmap[' '][6]))
    if spacesNum <= 0: return text
    
    if   lineOffset == 0: # first
        return line + (' ' * spacesNum)
    elif lineOffset == 1: # last
        return (' ' * spacesNum) + line
    elif lineOffset == 2: # middle
        return (' ' * (spacesNum // 2)) + line
    elif lineOffset == 3: # middle filled
        return (' ' * (spacesNum // 2)) + line + (' ' * (spacesNum - (spacesNum // 2)))

#  : (px) should be in command
def OffsetLineWithCommands(line : str, charmap : dict, LineMaxWidth : int, lineOffset : int, command : str, freeSpace = 0):
    if not freeSpace:
        lineWidth = Width(line, charmap)
        freeSpace = LineMaxWidth - lineWidth
    if freeSpace <= 0: return text
    
    if   lineOffset == 0: # first
        command = command.replace('(px)', str(freeSpace), 1)
        return line + command
    elif lineOffset == 1: # last
        command = command.replace('(px)', str(freeSpace), 1)
        return command + line
    elif lineOffset == 2: # middle
        command = command.replace('(px)', str(freeSpace // 2), 1)
        return command + line
    elif lineOffset == 3: # middle filled
        return command.replace('(px)', str(freeSpace // 2), 1) + line + command.replace('(px)', str(freeSpace // 2 + 1), 1)