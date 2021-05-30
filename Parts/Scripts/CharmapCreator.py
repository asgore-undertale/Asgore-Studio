import re, pygame
from os import path
from Parts.Scripts.Un_Freeze_Arabic import Un_Freeze

pygame.init()

def CreateCharmap(fnt_directory, text = '', fontSize = 0, type = 'aft'):
    charmap, highest = {}, 0
    
    if type == 'ttf':
        dialogue_font = pygame.font.Font(fnt_directory, fontSize)
        for char in Un_Freeze(text):
            try:
                dialogue = dialogue_font.render(char, True, (0,0,0))
                charmap[char] = (0, 0, dialogue.get_size()[0], dialogue.get_size()[1], 0, 0, 0)
            except: pass
    
    elif type == 'aft':
        if not path.exists(fnt_directory): return
        with open(fnt_directory, 'r', encoding='utf-8') as f: font_content = f.read()
        
        chars_list, x_list, y_list, width_list, height_list, xoffset_list, yoffset_list, xadvance_list = [], [], [], [], [], [], [], []
        rows = font_content.split('\n')
        
        VERSION = float(rows[1][9:-1])
        SEPARATOR = rows[2][11:-1]
        
        for r in range(5, len(rows)):
            row = rows[r]
            if not row or '|#|' in row: continue
            cols = row.split(SEPARATOR)
            charmap[cols[0]] = (int(cols[1]), int(cols[2]), int(cols[3]), int(cols[4]), int(cols[5]), int(cols[6]), int(cols[7]))
    
    for k in charmap:
        h = charmap[k][3]
        if h > highest: highest = h
    charmap['height'] = highest
    
    return charmap
