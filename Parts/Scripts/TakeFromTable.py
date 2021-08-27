from Parts.Scripts.FreezeArabic import Freeze
from Parts.Scripts.UsefulLittleFunctions import sortDictByKeyLengh
from Parts.Vars import checkVersion
from Parts.Scripts.FixTables import *
from os import path
import pygame, re

def TakeFromTable(filePath, chars = '', fontSize = 16):
    if not path.exists(filePath): return
    if filePath.endswith('.act'): return TakeFromACT(filePath)
    if filePath.endswith('.zts'): return TakeFromZTS(filePath)
    if filePath.endswith('.ttf'): return TakeFromTTF(filePath, chars, fontSize)
    if filePath.endswith('.aft'): return TakeFromAFT(filePath)
    if filePath.endswith('.fnt'): return TakeFromFNT(filePath)
    if filePath.endswith('.aff'): return TakeFromAFF(filePath)

def TakeFromFNT(fntPath):
    with open(fntPath, 'r', encoding='utf-8') as f: fontContent = f.read()
    
    if '<?xml version="1.0"?>' in fontContent:
        find = ['<char id="(.*?)"', 'x="(.*?)"', 'y="(.*?)"', 'width="(.*?)"', 'height="(.*?)"', 'xoffset="(.*?)"',
            'yoffset="(.*?)"', 'xadvance="(.*?)"'
            ]
    else:
        find = ['\nchar id=(.*?) ', ' x=(.*?) ', ' y=(.*?) ', ' width=(.*?) ', ' height=(.*?) ', ' xoffset=(.*?) ',
            ' yoffset=(.*?) ', ' xadvance=(.*?) '
            ]
    
    chars_list = re.findall(find[0], fontContent)
    x_list = re.findall(find[1], fontContent)
    y_list = re.findall(find[2], fontContent)
    width_list = re.findall(find[3], fontContent)
    height_list = re.findall(find[4], fontContent)
    xoffset_list = re.findall(find[5], fontContent)
    yoffset_list = re.findall(find[6], fontContent)
    xadvance_list = re.findall(find[7], fontContent)
    
    charmap = {}
    tallest = 0
    for c, x, y, w, h, xoff, yoff, xad in zip(chars_list, x_list, y_list, width_list, height_list, xoffset_list, yoffset_list, xadvance_list):
        charmap[chr(int(c))] = tuple(map(int, (x, y, w, h, xoff, yoff, xad)))
        if int(h) > tallest: tallest = int(h)
    
    charmap['tallest'] = tallest
    return fixCharmap(charmap)

def TakeFromAFT(aftPath):
    with open(aftPath, 'r', encoding='utf-8') as f: fontContent = f.read()
    rows = fontContent.split('\n')
    
    VERSION = rows[1][9:-1]
    SEPARATOR = rows[2][11:-1]
    checkVersion(VERSION, 1)
    tallest = 0
    
    for r in range(5, len(rows)):
        if not rows[r]: continue
        cells = rows[r].split(SEPARATOR)
        
        height = int(cells[4])
        charmap[cells[0]] = (int(cells[1]), int(cells[2]), int(cells[3]), height, int(cells[5]), int(cells[6]), int(cells[7]))
        if height > tallest: tallest = height
    
    charmap['tallest'] = tallest
    return fixCharmap(charmap)

def TakeFromAFF(affPath):
    with open(affPath, 'r', encoding='utf-8') as f: fontContent = f.read()
    rows = fontContent.split('\n')
    
    VERSION = rows[1][9:-1]
    SEPARATOR = rows[2][11:-1]
    MIN_SEPARATOR = rows[3][15:-1]
    FILLER = rows[4][8:-1]
    checkVersion(VERSION, 2)
    tallest = 0
    
    for r in range(7, len(rows)):
        if not rows[r]: continue
        cells = rows[r].split(SEPARATOR)
        
        DrowData = cells[1].split(MIN_SEPARATOR)
        height = len(DrowData)
        
        width  = 0
        for row in DrowData:
            if len(row) > width: width = len(row)
        
        charmap[cells[0]] = (0, 0, width, height, int(cells[2]), int(cells[3]), int(cells[4]), DrowData)
        if height > tallest: tallest = height
    
    charmap['tallest'] = tallest
    charmap['filler'] = FILLER
    return fixCharmap(charmap)

def TakeFromTTF(ttfPath, chars, fontSize):
    dialogue_font = pygame.font.Font(ttfPath, fontSize)
    for char in Freeze(chars):
        try:
            dialogue = dialogue_font.render(char, True, (0,0,0))
            charmap[char] = (0, 0, dialogue.get_size()[0], dialogue.get_size()[1], 0, 0, 0)
        except: pass
    return fixCharmap(charmap)

def TakeFromZTS(ztsPath):
    lines = open(ztsPath, 'r', encoding="utf-8").read().split('\n')
    string1, string2 = lines[0], lines[1]
    charmap = {}
    
    for i, j in zip(string1, string2): charmap[j] = i
    return fixCharmap(charmap)

def TakeFromACT(actPath):
    charmap = {}
    rows = open(actPath, 'r', encoding="utf-8").read().split('\n')
    
    VERSION = rows[1][9:-1]
    SEPARATOR = rows[2][11:-1]
    checkVersion(VERSION, 0)
    
    for r in range(5, len(rows)):
        if not rows[r]: continue
        for i in range(4 - rows[r].count(SEPARATOR)): rows[r] += SEPARATOR
        cols = rows[r].split(SEPARATOR)
        
        if   cols[0] == 'ً':
            charmap['ﹰ'] = cols[4]
        elif cols[0] == 'َ':
            charmap['ﹶ'] = cols[4]
        elif cols[0] == 'ٌ':
            charmap['ﹲ'] = cols[4]
        elif cols[0] == 'ُ':
            charmap['ﹸ'] = cols[4]
        elif cols[0] == 'ٍ':
            charmap['ﹴ'] = cols[4]
        elif cols[0] == 'ِ':
            charmap['ﹺ'] = cols[4]
        elif cols[0] == 'ّ':
            charmap['ﹼ'] = cols[4]
        elif cols[0] == 'ْ':
            charmap['ﹾ'] = cols[4]
        elif cols[0] == 'ء':
            charmap['ﺀ'] = cols[4]
        elif cols[0] == 'آ':
            charmap['ﺁ'] = cols[4]
            charmap['ﺂ'] = cols[3]
        elif cols[0] == 'أ':
            charmap['ﺃ'] = cols[4]
            charmap['ﺄ'] = cols[3]
        elif cols[0] == 'ؤ':
            charmap['ﺅ'] = cols[4]
            charmap['ﺆ'] = cols[3]
        elif cols[0] == 'إ':
            charmap['ﺇ'] = cols[4]
            charmap['ﺈ'] = cols[3]
        elif cols[0] == 'ئ':
            charmap['ﺉ'] = cols[4]
            charmap['ﺊ'] = cols[3]
            charmap['ﺌ'] = cols[2]
            charmap['ﺋ'] = cols[1]
        elif cols[0] == 'ا':
            charmap['ﺍ'] = cols[4]
            charmap['ﺎ'] = cols[3]
        elif cols[0] == 'ب':
            charmap['ﺏ'] = cols[4]
            charmap['ﺐ'] = cols[3]
            charmap['ﺒ'] = cols[2]
            charmap['ﺑ'] = cols[1]
        elif cols[0] == 'ة':
            charmap['ﺓ'] = cols[4]
            charmap['ﺔ'] = cols[3]
        elif cols[0] == 'ت':
            charmap['ﺕ'] = cols[4]
            charmap['ﺖ'] = cols[3]
            charmap['ﺘ'] = cols[2]
            charmap['ﺗ'] = cols[1]
        elif cols[0] == 'ث':
            charmap['ﺙ'] = cols[4]
            charmap['ﺚ'] = cols[3]
            charmap['ﺜ'] = cols[2]
            charmap['ﺛ'] = cols[1]
        elif cols[0] == 'ج':
            charmap['ﺝ'] = cols[4]
            charmap['ﺞ'] = cols[3]
            charmap['ﺠ'] = cols[2]
            charmap['ﺟ'] = cols[1]
        elif cols[0] == 'ح':
            charmap['ﺡ'] = cols[4]
            charmap['ﺢ'] = cols[3]
            charmap['ﺤ'] = cols[2]
            charmap['ﺣ'] = cols[1]
        elif cols[0] == 'خ':
            charmap['ﺥ'] = cols[4]
            charmap['ﺦ'] = cols[3]
            charmap['ﺨ'] = cols[2]
            charmap['ﺧ'] = cols[1]
        elif cols[0] == 'د':
            charmap['ﺩ'] = cols[4]
            charmap['ﺪ'] = cols[3]
        elif cols[0] == 'ذ':
            charmap['ﺫ'] = cols[4]
            charmap['ﺬ'] = cols[3]
        elif cols[0] == 'ر':
            charmap['ﺭ'] = cols[4]
            charmap['ﺮ'] = cols[3]
        elif cols[0] == 'ز':
            charmap['ﺯ'] = cols[4]
            charmap['ﺰ'] = cols[3]
        elif cols[0] == 'س':
            charmap['ﺱ'] = cols[4]
            charmap['ﺲ'] = cols[3]
            charmap['ﺴ'] = cols[2]
            charmap['ﺳ'] = cols[1]
        elif cols[0] == 'ش':
            charmap['ﺵ'] = cols[4]
            charmap['ﺶ'] = cols[3]
            charmap['ﺸ'] = cols[2]
            charmap['ﺷ'] = cols[1]
        elif cols[0] == 'ص':
            charmap['ﺹ'] = cols[4]
            charmap['ﺺ'] = cols[3]
            charmap['ﺼ'] = cols[2]
            charmap['ﺻ'] = cols[1]
        elif cols[0] == 'ض':
            charmap['ﺽ'] = cols[4]
            charmap['ﺾ'] = cols[3]
            charmap['ﻀ'] = cols[2]
            charmap['ﺿ'] = cols[1]
        elif cols[0] == 'ط':
            charmap['ﻁ'] = cols[4]
            charmap['ﻂ'] = cols[3]
            charmap['ﻄ'] = cols[2]
            charmap['ﻃ'] = cols[1]
        elif cols[0] == 'ظ':
            charmap['ﻅ'] = cols[4]
            charmap['ﻆ'] = cols[3]
            charmap['ﻈ'] = cols[2]
            charmap['ﻇ'] = cols[1]
        elif cols[0] == 'ع':
            charmap['ﻉ'] = cols[4]
            charmap['ﻊ'] = cols[3]
            charmap['ﻋ'] = cols[2]
            charmap['ﻌ'] = cols[1]
        elif cols[0] == 'غ':
            charmap['ﻍ'] = cols[4]
            charmap['ﻎ'] = cols[3]
            charmap['ﻐ'] = cols[2]
            charmap['ﻏ'] = cols[1]
        elif cols[0] == 'ف':
            charmap['ﻑ'] = cols[4]
            charmap['ﻒ'] = cols[3]
            charmap['ﻔ'] = cols[2]
            charmap['ﻓ'] = cols[1]
        elif cols[0] == 'ق':
            charmap['ﻕ'] = cols[4]
            charmap['ﻖ'] = cols[3]
            charmap['ﻘ'] = cols[2]
            charmap['ﻗ'] = cols[1]
        elif cols[0] == 'ك':
            charmap['ﻙ'] = cols[4]
            charmap['ﻚ'] = cols[3]
            charmap['ﻜ'] = cols[2]
            charmap['ﻛ'] = cols[1]
        elif cols[0] == 'ل':
            charmap['ﻝ'] = cols[4]
            charmap['ﻞ'] = cols[3]
            charmap['ﻠ'] = cols[2]
            charmap['ﻟ'] = cols[1]
        elif cols[0] == 'م':
            charmap['ﻡ'] = cols[4]
            charmap['ﻢ'] = cols[3]
            charmap['ﻤ'] = cols[2]
            charmap['ﻣ'] = cols[1]
        elif cols[0] == 'ن':
            charmap['ﻥ'] = cols[4]
            charmap['ﻦ'] = cols[3]
            charmap['ﻨ'] = cols[2]
            charmap['ﻧ'] = cols[1]
        elif cols[0] == 'ه':
            charmap['ﻩ'] = cols[4]
            charmap['ﻪ'] = cols[3]
            charmap['ﻬ'] = cols[2]
            charmap['ﻫ'] = cols[1]
        elif cols[0] == 'و':
            charmap['ﻭ'] = cols[4]
            charmap['ﻮ'] = cols[3]
        elif cols[0] == 'ى':
            charmap['ﻯ'] = cols[4]
            charmap['ﻰ'] = cols[3]
        elif cols[0] == 'ي':
            charmap['ﻱ'] = cols[4]
            charmap['ﻲ'] = cols[3]
            charmap['ﻴ'] = cols[2]
            charmap['ﻳ'] = cols[1]
        elif cols[0] == 'لآ':
            charmap['ﻵ'] = cols[4]
            charmap['ﻶ'] = cols[3]
        elif cols[0] == 'لأ':
            charmap['ﻷ'] = cols[4]
            charmap['ﻸ'] = cols[3]
        elif cols[0] == 'لإ':
            charmap['ﻹ'] = cols[4]
            charmap['ﻺ'] = cols[3]
        elif cols[0] == 'لا':
            charmap['ﻻ'] = cols[4]
            charmap['ﻼ'] = cols[3]
        elif cols[0] == 'پ':
            charmap['ﭖ'] = cols[4]
            charmap['ﭗ'] = cols[3]
            charmap['ﭙ'] = cols[2]
            charmap['ﭘ'] = cols[1]
        elif cols[0] == 'چ':
            charmap['ﭺ'] = cols[4]
            charmap['ﭻ'] = cols[3]
            charmap['ﭽ'] = cols[2]
            charmap['ﭼ'] = cols[1]
        elif cols[0] == 'ڤ':
            charmap['ﭪ'] = cols[4]
            charmap['ﭫ'] = cols[3]
            charmap['ﭭ'] = cols[2]
            charmap['ﭬ'] = cols[1]
        else:
            charmap[cols[0]] = cols[4]
    
    return sortDictByKeyLengh(fixCharmap(charmap))