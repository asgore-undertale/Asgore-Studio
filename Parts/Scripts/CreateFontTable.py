from Parts.Vars import _ACT_VERSION_, _A_SEPARATOR_
from Parts.Scripts.TakeFromTable import TakeFromTable

def CreateAftFontTable(firstX, firstY, BetweenCharsX, BetweenCharsY, unifiedWidth, unifiedHeight, charsPerRow, Chars, fontPath, fontSize):
    charsTable = TakeFromTable(fontPath, Chars, fontSize)
    table = f'\nVERSION="{_ACT_VERSION_}"\nSEPARATOR="{_A_SEPARATOR_}"\n#####################\nChar{_A_SEPARATOR_}X{_A_SEPARATOR_}Y{_A_SEPARATOR_}Width{_A_SEPARATOR_}Height{_A_SEPARATOR_}Xoffset{_A_SEPARATOR_}Yoffset{_A_SEPARATOR_}Xadvance'
    for c in range(len(Chars)):
        if Chars[c] not in charsTable: continue
        X = firstX + (c %  charsPerRow * unifiedWidth ) + (c %  charsPerRow * BetweenCharsX)
        Y = firstY + (c // charsPerRow * unifiedHeight) + (c // charsPerRow * BetweenCharsY)
        table += f'\n{Chars[c]}{_A_SEPARATOR_}{X}{_A_SEPARATOR_}{Y}{_A_SEPARATOR_}{unifiedWidth}{_A_SEPARATOR_}{unifiedHeight}{_A_SEPARATOR_}{charsTable[Chars[c]][4]}{_A_SEPARATOR_}{charsTable[Chars[c]][5]}{_A_SEPARATOR_}{charsTable[Chars[c]][6]}'
    return table