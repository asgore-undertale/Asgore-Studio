from Parts.Scripts.FixTables import *

def charmapToAFT(charmap):
    table = '\nVERSION="1.0"\nSEPARATOR="█"\n#####################\nChar█X█Y█Width█Height█Xoffset█Yoffset█Xadvance'
    for k, v in fixCharmap(charmap).items():
        if not isinstance(v, tuple): return
        table += f'\n{k}█' + '█'.join(v)
    return table

def charmapToZTS(charmap):
    line1, line2 = '', ''
    charmap = sameItemsLengh(charmap, 1)
    for k, v in fixCharmap(charmap).items():
        if isinstance(v, tuple): return
        line1 += v
        line2 += k
    return f'{line1}\n{line2}'

def charmapToACT(charmap):
    table = '\nVERSION="1.0"\nSEPARATOR="█"\n#####################\nالحرف█أول█وسط█آخر█منفصل'
    for k, v in fixCharmap(charmap).items():
        if isinstance(v, tuple): return
        table += f'\n{k}████{v}'
    return fixACT(table)