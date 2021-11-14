from Parts.Scripts.FreezeArabic import Freeze
from Parts.Scripts.UsefulLittleFunctions import sortDictByKeyLengh, tryTakeNum, hexToString
from Parts.Vars import _A_SEPARATOR_, _CSV_DELIMITER_, checkVersion, _ZTA_SEPARATOR_, _ZTA_RANGE_
from Parts.Scripts.FixTables import *
from os import path
import pygame, re, csv

def TakeFromTable(filePath, chars = '', fontSize = 16, hexToStr = True):
    if not path.exists(filePath): return
    if filePath.endswith('.act'): return TakeFromACT(filePath)
    if filePath.endswith('.csv'): return TakeFromCSV(filePath)
    if filePath.endswith('.ttf'): return TakeFromTTF(filePath, chars, fontSize)
    if filePath.endswith('.aft'): return TakeFromAFT(filePath)
    if filePath.endswith('.fnt'): return TakeFromFNT(filePath)
    if filePath.endswith('.aff'): return TakeFromAFF(filePath)
    if filePath.endswith('.tbl'): return TakeFromTBL(filePath, hexToStr)
    if filePath.endswith('.zts'): return TakeFromZTS(filePath)
    if filePath.endswith('.zta'): return TakeFromZTA(filePath)

def TakeFromFNT(fntPath):
    with open(fntPath, 'r', encoding='utf-8', errors='replace') as f: fontContent = f.read()
    
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
        charmap[chr(tryTakeNum(c))] = tuple(map(tryTakeNum, (x, y, w, h, xoff, yoff, xad)))
        if tryTakeNum(h) > tallest: tallest = tryTakeNum(h)
    
    charmap['tallest'] = tallest
    return fixCharmap(charmap)

def TakeFromAFT(aftPath):
    with open(aftPath, 'r', encoding='utf-8', errors='replace') as f: fontContent = f.read()
    rows = fontContent.split('\n')
    
    VERSION = rows[1][9:-1]
    SEPARATOR = rows[2][11:-1]
    checkVersion(VERSION, 1)
    
    charmap = {}
    tallest = 0
    
    for r in range(5, len(rows)):
        if not rows[r]: continue
        cells = rows[r].split(SEPARATOR)
        
        height = tryTakeNum(cells[4])
        charmap[cells[0]] = (tryTakeNum(cells[1]), tryTakeNum(cells[2]), tryTakeNum(cells[3]), height, tryTakeNum(cells[5]), tryTakeNum(cells[6]), tryTakeNum(cells[7]))
        if height > tallest: tallest = height
    
    charmap['tallest'] = tallest
    return fixCharmap(charmap)

def TakeFromAFF(affPath):
    with open(affPath, 'r', encoding='utf-8', errors='replace') as f: fontContent = f.read()
    rows = fontContent.split('\n')
    
    VERSION = rows[1][9:-1]
    SEPARATOR = rows[2][11:-1]
    MIN_SEPARATOR = rows[3][15:-1]
    FILLER = rows[4][8:-1]
    checkVersion(VERSION, 2)
    
    charmap = {}
    tallest = 0
    
    for r in range(7, len(rows)):
        if not rows[r]: continue
        cells = rows[r].split(SEPARATOR)
        
        DrowData = cells[1].split(MIN_SEPARATOR)
        height = len(DrowData)
        
        width  = 0
        for row in DrowData:
            if len(row) > width: width = len(row)
        
        charmap[cells[0]] = (0, 0, width, height, tryTakeNum(cells[2]), tryTakeNum(cells[3]), tryTakeNum(cells[4]), DrowData)
        if height > tallest: tallest = height
    
    charmap['tallest'] = tallest
    charmap['filler'] = FILLER
    return fixCharmap(charmap)

def TakeFromTTF(ttfPath, chars, fontSize):
    charmap = {}
    tallest = 0
    dialogue_font = pygame.font.Font(ttfPath, fontSize)
    for char in Freeze(chars):
        try:
            dialogue = dialogue_font.render(char, True, (0,0,0))
            height = dialogue.get_size()[1]
            if height > tallest: tallest = height
            charmap[char] = (0, 0, dialogue.get_size()[0], height, 0, 0, 0)
        except: pass
    charmap['tallest'] = tallest
    return fixCharmap(charmap)

def TakeFromACT(actPath):
    actPath = open(actPath, 'r', encoding="utf-8", errors='replace').read()
    rows = actPath.split('\n')
    charmap = {}
    
    VERSION = rows[1][9:-1]
    SEPARATOR = rows[2][11:-1]
    checkVersion(VERSION, 0)
    
    for r in range(5, len(rows)):
        if not rows[r]: continue
        row = rows[r].split(SEPARATOR)
        for i in range(5 - len(row)): row.append('')
        charmap = takeFromArabic(charmap, row)
    
    return charmap

def TakeFromCSV(csvPath):
    charmap = {}
    
    with open(csvPath, newline='', encoding='utf8', errors='replace') as csvfile:
        rows = list(csv.reader(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"'))
    
    VERSION = rows[1][9:-1]
    SEPARATOR = rows[2][11:]
    checkVersion(VERSION, 0)
    
    for r in range(5, len(rows)):
        if not rows[r]: continue
        for i in range(5 - len(rows[r])): rows[r].append('')
        charmap = takeFromArabic(charmap, rows[r])
    
    return sortDictByKeyLengh(fixCharmap(charmap))

def TakeFromTBL(tblPath, hexToStr = True):
    # ---------- (tblToList) from (TablrsEditorsFonctions) because of circle import.
    tblPath = open(tblPath, 'r', encoding="utf-8", errors='replace').read()
    rows = tblPath.split('\n')
    charmap = {}
    List = []
    
    for row in rows:
        if not row: continue
        List.append(row.split('=', 1))
    # ----------
    
    for row in List:
        if hexToStr:
            value = hexToString(row[0])
        else:
            value = row[0]
        charmap[row[1]] = value
    
    return sortDictByKeyLengh(fixCharmap(charmap))

def TakeFromZTS(ztsPath):
    charmap = {}
    lines = open(ztsPath, 'r', encoding="utf-8", errors='replace').read().split('\n')
    for i, j in zip(lines[0], lines[1]): charmap[j] = i
    
    return fixCharmap(charmap)

def TakeFromZTA(ztaPath):
    charmap = {}
    text = open(ztaPath, 'r', encoding="utf-8", errors='replace').read()
    ranges = re.findall(_ZTA_RANGE_, text)
    
    for r in ranges:
        try:
            startPoint = int(r[0])
            steps = int(r[1])
            
            chars = []
            for j in range(startPoint, startPoint+steps):
                chars.append(chr(j))
            
            replacement = _ZTA_RANGE_.replace('(.*?)', r[0], 1).replace('(.*?)', r[1], 1).replace('\\', '')
            text = text.replace(replacement, _ZTA_SEPARATOR_.join(chars))
        except: pass
    
    lines = text.split('\n')
    for i, j in zip(lines[0].split(_ZTA_SEPARATOR_), lines[1].split(_ZTA_SEPARATOR_)): charmap[j] = i
    
    return fixCharmap(charmap)