from Parts.Vars import _ACT_VERSION_, _A_SEPARATOR_

def CreateAftFontTable(firstX, firstY, BetweenCharsX, BetweenCharsY, unifiedWidth, unifiedHeight, charsPerRow, Chars):
    table = f'\nVERSION="{_ACT_VERSION_}"\nSEPARATOR="{_A_SEPARATOR_}"\n#####################\nChar{_A_SEPARATOR_}X{_A_SEPARATOR_}Y{_A_SEPARATOR_}Width{_A_SEPARATOR_}Height{_A_SEPARATOR_}Xoffset{_A_SEPARATOR_}Yoffset{_A_SEPARATOR_}Xadvance'
    for c in range(len(Chars)):
        X = firstX + (c %  charsPerRow * unifiedWidth ) + (c %  charsPerRow * BetweenCharsX)
        Y = firstY + (c // charsPerRow * unifiedHeight) + (c // charsPerRow * BetweenCharsY)
        table += f'\n{Chars[c]}{_A_SEPARATOR_}{X}{_A_SEPARATOR_}{Y}{_A_SEPARATOR_}{unifiedWidth}{_A_SEPARATOR_}{unifiedHeight}{_A_SEPARATOR_}{0}{_A_SEPARATOR_}{0}{_A_SEPARATOR_}{0}'
    return table