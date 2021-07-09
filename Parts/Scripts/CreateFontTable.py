from Parts.Vars import _ATE_VERSION_, _ATE_SEPARATOR_

def CreateFontTable(firstX, firstY, BetweenCharsX, BetweenCharsY, unifiedWidth, unifiedHeight, charsPerRow, Chars):
    table = f'\nVERSION="{_ATE_VERSION_}"\nSEPARATOR="{_ATE_SEPARATOR_}"\n#####################\nChar{_ATE_SEPARATOR_}X{_ATE_SEPARATOR_}Y{_ATE_SEPARATOR_}Width{_ATE_SEPARATOR_}Height{_ATE_SEPARATOR_}Xoffset{_ATE_SEPARATOR_}Yoffset{_ATE_SEPARATOR_}Xadvance'
    for c in range(len(Chars)):
        X = firstX + (c %  charsPerRow * unifiedWidth ) + (c %  charsPerRow * BetweenCharsX)
        Y = firstY + (c // charsPerRow * unifiedHeight) + (c // charsPerRow * BetweenCharsY)
        table += f'\n{Chars[c]}{_ATE_SEPARATOR_}{X}{_ATE_SEPARATOR_}{Y}{_ATE_SEPARATOR_}{unifiedWidth}{_ATE_SEPARATOR_}{unifiedHeight}{_ATE_SEPARATOR_}{0}{_ATE_SEPARATOR_}{0}{_ATE_SEPARATOR_}{0}'
    return table