import re
from Parts.Scripts.sortConvertingTables import sortCharsConvertingTable

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
#xoffset_list = '0' * len(chars_list)
#yoffset_list = '0' * len(chars_list)
#xadvance_list = '0' * len(chars_list)
################

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


def ZtsToAct(tableContent):
    lines = tableContent.split('\n')
    string1, string2 = lines[0], lines[1]
    table = '\nVERSION="1.0"\nSEPARATOR="█"\n#####################\nالحرف█أول█وسط█آخر█منفصل'

    for i, j in zip(string1, string2): table += f'\n{i}████{j}'
    return sortCharsConvertingTable(table)