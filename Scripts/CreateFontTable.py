def CreateFontTable(firstX, firstY, BetweenCharsX, BetweenCharsY, unifiedWidth, unifiedHeight, charsPerRow, Chars):
    table = '\nVERSION="1.0"\nSEPARATOR="█"\n#####################\nChar█X█Y█Width█Height█Xoffset█Yoffset█Xadvance'
    for c in range(len(Chars)):
        X = firstX + (c %  charsPerRow * unifiedWidth ) + ((c - 1) * BetweenCharsX)
        Y = firstY + (c // charsPerRow * unifiedHeight) + ((c - 1) * BetweenCharsY)
        table += f'\n{Chars[c]}█{X}█{Y}█{unifiedWidth}█{unifiedHeight}█{0}█{0}█{0}'
    return table