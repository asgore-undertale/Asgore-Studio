from Parts.Scripts.fixTables import *
import re

def XmlToAft(tableContent):
    chars_list = re.findall('<char id="(.*?)"', tableContent)
    x_list = re.findall('x="(.*?)"', tableContent)
    y_list = re.findall('y="(.*?)"', tableContent)
    width_list = re.findall('width="(.*?)"', tableContent)
    height_list = re.findall('height="(.*?)"', tableContent)
    xoffset_list = re.findall('xoffset="(.*?)"', tableContent)
    yoffset_list = re.findall('yoffset="(.*?)"', tableContent)
    xadvance_list = re.findall('xadvance="(.*?)"', tableContent)
    
    table = '\nVERSION="1.0"\nSEPARATOR="█"\n#####################\nChar█X█Y█Width█Height█Xoffset█Yoffset█Xadvance'
    for c, x, y, w, h, xoff, yoff, xad in zip(chars_list, x_list, y_list, width_list, height_list, xoffset_list, yoffset_list, xadvance_list):
        table += f'\n{chr(int(c))}█{x}█{y}█{w}█{h}█{xoff}█{yoff}█{xad}'
    
    return table

def charmapToZTS(charmap):
    line1, line2 = '', ''
    charmap = sameItemsLengh(charmap, 1)
    for k, v in fixCharmap(charmap).items():
        line1 += v
        line2 += k
    return f'{line1}\n{line2}'

def charmapToACT(charmap):
    table = '\nVERSION="1.0"\nSEPARATOR="█"\n#####################\nالحرف█أول█وسط█آخر█منفصل'
    for k, v in fixCharmap(charmap).items():
        table += f'\n{k}████{v}'
    return fixACT(table)