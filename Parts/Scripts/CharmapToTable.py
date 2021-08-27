from Parts.Scripts.FixTables import *
from Parts.Vars import _ACT_SEPARATOR_

def charmapToTable(charmap : dict, type : str):
    if not charmap: return
    if type == 'act': return charmapToACT(charmap)
    if type == 'zts': return charmapToZTS(charmap)
    if type == 'aft': return charmapToAFT(charmap)

def charmapToAFT(charmap):
    table = f'\nVERSION="1.0"\nSEPARATOR="{_ACT_SEPARATOR_}"\n#####################\nChar{_ACT_SEPARATOR_}X{_ACT_SEPARATOR_}Y{_ACT_SEPARATOR_}Width{_ACT_SEPARATOR_}Height{_ACT_SEPARATOR_}Xoffset{_ACT_SEPARATOR_}Yoffset{_ACT_SEPARATOR_}Xadvance'
    for k, v in fixCharmap(charmap).items():
        if not isinstance(v, tuple): return
        v = list(map(str, v))
        table += f'\n{k}{_ACT_SEPARATOR_}' + _ACT_SEPARATOR_.join(v)
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
    table = f'\nVERSION="1.0"\nSEPARATOR="{_ACT_SEPARATOR_}"\n#####################\nالحرف{_ACT_SEPARATOR_}أول{_ACT_SEPARATOR_}وسط{_ACT_SEPARATOR_}آخر{_ACT_SEPARATOR_}منفصل'
    for k, v in fixCharmap(charmap).items():
        if isinstance(v, tuple): return
        table += f'\n{k}{_ACT_SEPARATOR_*4}{v}'
    return sortACT(table)