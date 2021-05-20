import re
from os import path

def CreateCharmap(fnt_directory):
    if not path.exists(fnt_directory): return
    with open(fnt_directory, 'r', encoding='utf-8') as f: font_content = f.read()
    
    chars_list, x_list, y_list, width_list, height_list, xoffset_list, yoffset_list, xadvance_list = [], [], [], [], [], [], [], []
    rows = font_content.split('\n')
    
    VERSION = float(rows[1][9:-1])
    SEPARATOR = rows[2][11:-1]
    
    for row in range(5, len(rows)):
        cols = rows[row].split('\n')
        for col in range(len(cols)):
            info = cols[col].split(SEPARATOR)
            chars_list.append(info[0])
            x_list.append(info[1])
            y_list.append(info[2])
            width_list.append(info[3])
            height_list.append(info[4])
            xoffset_list.append(info[5])
            yoffset_list.append(info[6])
            xadvance_list.append(info[7])
    
    charmap, highest = {}, 0
    for c, x, y, w, h, xoff, yoff, xad in zip(chars_list, x_list, y_list, width_list, height_list, xoffset_list, yoffset_list, xadvance_list):
        c, x, y, w, h, xoff, yoff, xad = c, int(x), int(y), int(w), int(h), int(xoff), int(yoff), int(xad)
        if h > highest: highest = h
        charmap[c] = (x, y, w, h, xoff, yoff, xad)
    charmap['height'] = highest
    
    return charmap
