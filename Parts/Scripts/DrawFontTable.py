from PIL import Image, ImageDraw, ImageFont
from Parts.Scripts.TakeFromTable import TakeFromTable

def drawFontTable(aftPath, chars, cellWidth, cellHeight, imgSize, fontPath, fontSize, fontmode, rightOffset, monoSized, savepath):
    charsTable = TakeFromTable(aftPath)
    canvas = Image.new('RGBA', imgSize)
    draw = ImageDraw.Draw(canvas)
    
    if fontPath.endswith('.ttf'):
        font = ImageFont.truetype(fontPath, fontSize, encoding="utf-8")
        
    elif fontPath.endswith('.aff'):
        affTable = TakeFromTable(fontPath)
        char = list(affTable)[0]
        charHeight = affTable[char][3]
        
        per = (fontSize * charHeight / affTable['tallest'] - charHeight) / affTable['tallest']
        charHeight += charHeight * per
        pxWidth = charHeight / len(affTable[char][-1])
    
    for char in chars:
        if char not in charsTable: continue
        
        x = charsTable[char][0]
        y = charsTable[char][1]
        
        for i in range(cellWidth):
            if x + i >= imgSize[0]: break
            for j in range(cellHeight):
                if y + j >= imgSize[1]: break
                canvas.putpixel((x + i, y + j), 0)
        
        if fontPath.endswith('.ttf'):
            x += (cellWidth - font.getsize(char)[0]) * (rightOffset and monoSized)
            draw.fontmode = str(fontmode)
            draw.text((x, y), char, 'white', font)
            
        elif fontPath.endswith('.aff'):
            charWidth = affTable[char][2] + (affTable[char][2] * per)
            x += (cellWidth - charWidth) * (rightOffset and monoSized)
            char_drawdata = affTable[char][7]
            
            for r in range(len(char_drawdata)):
                row = char_drawdata[r]
                for p in range(len(row)):
                    if row[p] != affTable['filler']: continue
                    
                    _x, _y =  x + (pxWidth * p), y + (pxWidth * r)
                    draw.rectangle((_x, _y, _x + pxWidth, _y + pxWidth), fill=(255, 255, 255))

    canvas.save(savepath, "PNG")