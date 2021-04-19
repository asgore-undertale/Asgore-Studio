import re
from os import path

def CreateCharmap(fnt_directory):
    if not path.exists(fnt_directory): return
    with open(fnt_directory, 'r', encoding='utf-8') as f: font_content = f.read()
    chars_list, x_list, y_list, width_list, height_list, xoffset_list, yoffset_list, xadvance_list = 0, 0, 0, 0, 0, 0, 0, 0
    if '<?xml version="1.0"?>' in font_content:
        chars_list = re.findall('<char id="(.*?)"', font_content)
        x_list = re.findall('x="(.*?)"', font_content)
        y_list = re.findall('y="(.*?)"', font_content)
        width_list = re.findall('width="(.*?)"', font_content)
        height_list = re.findall('height="(.*?)"', font_content)
        xoffset_list = re.findall('xoffset="(.*?)"', font_content)
        yoffset_list = re.findall('yoffset="(.*?)"', font_content)
        xadvance_list = re.findall('xadvance="(.*?)"', font_content)
        
        chars_list = [chr(int(c)) for c in chars_list]
        '''
        elif 'info face="' in font_content:
        '''
    else: #return
        #Your special extractor here
        
        #The Legend of Zelda: A Link to the Past
        #width = '666666663666766666676777766666666635637666656667777664666666663764468666668887777488888884888888884'
        #chars_list, x_list, y_list, width_list, height_list = [], [], [], [], []
        #for line in font_content.split('\n'):
        #    if line:
        #        l = line.split('=')
        #        chars_list.append(l[1])
        #        num_in_line = l[0]
        #        x = (int(num_in_line, 16) % 16) * 8
        #        y = (int(num_in_line, 16) // 16) * 16
        #        x_list.append(x)
        #        y_list.append(y)
        #        width_list.append(width[int(num_in_line, 16)])
        #        height_list.append(16)
        ################
        
        #Normal
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
        ################
    
    if not x_list: x_list = '0' * len(chars_list)
    if not y_list: y_list = '0' * len(chars_list)
    if not width_list: width_list = '0' * len(chars_list)
    if not height_list: height_list = '0' * len(chars_list)
    if not xoffset_list: xoffset_list = '0' * len(chars_list)
    if not yoffset_list: yoffset_list = '0' * len(chars_list)
    if not xadvance_list: xadvance_list = '0' * len(chars_list)
    
    charmap, highest = {}, 0
    for c, x, y, w, h, xoff, yoff, xad in zip(chars_list, x_list, y_list, width_list, height_list, xoffset_list, yoffset_list, xadvance_list):
        c, x, y, w, h, xoff, yoff, xad = c, int(x), int(y), int(w), int(h), int(xoff), int(yoff), int(xad)
        if h > highest: highest = h
        charmap[c] = (x, y, w, h, xoff, yoff, xad)
    charmap['height'] = highest
    
    return charmap
