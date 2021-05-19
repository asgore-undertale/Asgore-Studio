from PIL import Image, ImageDraw, ImageFont
from Parts.Scripts.CharmapCreator import CreateCharmap

def drawFontTable(ateFontTable, chars, cellWidth, cellHeight, cellsPerLine, ttfName, ttfSize, rightOffset, savepath):
    charsTable = CreateCharmap(ateFontTable)
    font = ImageFont.truetype(ttfName, ttfSize, encoding="utf-8")

    imgWidth, imgHeight = cellWidth * cellsPerLine, cellHeight * (len(chars) // cellsPerLine)
    if len(chars) % cellsPerLine: imgHeight += cellHeight
    canvas = Image.new('RGBA', (imgWidth, imgHeight))

    for char in chars:
        x = charsTable[char][0]
        y = charsTable[char][1]
        if rightOffset: x += cellWidth - font.getsize(char)[0]
        draw = ImageDraw.Draw(canvas)
        draw.text((x, y), char, 'black', font)

    canvas.save(savepath, "PNG")