from Parts.Vars import _ACT_VERSION_, _A_SEPARATOR_
from Parts.Scripts.TakeFromTable import TakeFromTable

def CreateAftFontTable(firstX, firstY, BetweenCharsX, BetweenCharsY, cellWidth, cellHeight, charsPerRow, Chars, fontPath, fontSize, monoSized = False, fromRight = False):
    charsTable = TakeFromTable(fontPath, Chars, fontSize)
    char = list(charsTable)[0]
    charHeight = charsTable[char][3]
    per = (fontSize * charHeight / charsTable['tallest'] - charHeight) / charsTable['tallest']
    
    table = f'\nVERSION="{_ACT_VERSION_}"\nSEPARATOR="{_A_SEPARATOR_}"\n#####################\nChar{_A_SEPARATOR_}X{_A_SEPARATOR_}Y{_A_SEPARATOR_}Width{_A_SEPARATOR_}Height{_A_SEPARATOR_}Xoffset{_A_SEPARATOR_}Yoffset{_A_SEPARATOR_}Xadvance'
    for c in range(len(Chars)):
        if Chars[c] not in charsTable: continue
        Width = int((monoSized * cellWidth) + ((not monoSized) * charsTable[Chars[c]][2]) * (1 + per))
        Height = int((monoSized * cellHeight) + ((not monoSized) * charsTable[Chars[c]][3]) * (1 + per))
        X = int(firstX + (c %  charsPerRow * cellWidth ) + (c %  charsPerRow * BetweenCharsX) + ((not monoSized and fromRight) * (cellWidth - Width)))
        Y = int(firstY + (c // charsPerRow * cellHeight) + (c // charsPerRow * BetweenCharsY))
        Xoffset = int(charsTable[Chars[c]][4] * (1 + per))
        Yoffset = int(charsTable[Chars[c]][5] * (1 + per))
        Xadvance = int(charsTable[Chars[c]][6] * (1 + per))
        table += f'\n{Chars[c]}{_A_SEPARATOR_}{X}{_A_SEPARATOR_}{Y}{_A_SEPARATOR_}{Width}{_A_SEPARATOR_}{Height}{_A_SEPARATOR_}{Xoffset}{_A_SEPARATOR_}{Yoffset}{_A_SEPARATOR_}{Xadvance}'
    return table