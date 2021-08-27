from Parts.Vars import _ACT_VERSION_, _ACT_SEPARATOR_

def CreateFontTable(firstX, firstY, BetweenCharsX, BetweenCharsY, unifiedWidth, unifiedHeight, charsPerRow, Chars):
    table = f'\nVERSION="{_ACT_VERSION_}"\nSEPARATOR="{_ACT_SEPARATOR_}"\n#####################\nChar{_ACT_SEPARATOR_}X{_ACT_SEPARATOR_}Y{_ACT_SEPARATOR_}Width{_ACT_SEPARATOR_}Height{_ACT_SEPARATOR_}Xoffset{_ACT_SEPARATOR_}Yoffset{_ACT_SEPARATOR_}Xadvance'
    for c in range(len(Chars)):
        X = firstX + (c %  charsPerRow * unifiedWidth ) + (c %  charsPerRow * BetweenCharsX)
        Y = firstY + (c // charsPerRow * unifiedHeight) + (c // charsPerRow * BetweenCharsY)
        table += f'\n{Chars[c]}{_ACT_SEPARATOR_}{X}{_ACT_SEPARATOR_}{Y}{_ACT_SEPARATOR_}{unifiedWidth}{_ACT_SEPARATOR_}{unifiedHeight}{_ACT_SEPARATOR_}{0}{_ACT_SEPARATOR_}{0}{_ACT_SEPARATOR_}{0}'
    return table