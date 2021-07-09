from PIL import Image, ImageDraw, ImageFont
from Parts.Scripts.TakeFromTable import TakeFromTable

def drawFontTable(aftPath, chars, cellWidth, cellHeight, imgSize, ttfName, ttfSize, rightOffset, fontmode, savepath):
    charsTable = TakeFromTable(aftPath)
    font = ImageFont.truetype(ttfName, ttfSize, encoding="utf-8")
    canvas = Image.new('RGBA', imgSize)

    for char in chars:
        x = charsTable[char][0]
        y = charsTable[char][1]
        
        for i in range(cellWidth):
            for j in range(cellHeight):
                canvas.putpixel((x + i, y + j), 0)
        
        if rightOffset: x += cellWidth - font.getsize(char)[0]
        
        draw = ImageDraw.Draw(canvas)
        draw.fontmode = str(fontmode)
        draw.text((x, y), char, 'black', font)

    canvas.save(savepath, "PNG")