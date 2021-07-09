from Parts.Scripts.FixTables import *
from Parts.Vars import _ATE_SEPARATOR_

def charmapToTable(charmap : dict, type : str):
    if not charmap: return
    if type == 'act': return charmapToACT(charmap)
    if type == 'zts': return charmapToZTS(charmap)
    if type == 'aft': return charmapToAFT(charmap)

def charmapToAFT(charmap):
    table = f'\nVERSION="1.0"\nSEPARATOR="{_ATE_SEPARATOR_}"\n#####################\nChar{_ATE_SEPARATOR_}X{_ATE_SEPARATOR_}Y{_ATE_SEPARATOR_}Width{_ATE_SEPARATOR_}Height{_ATE_SEPARATOR_}Xoffset{_ATE_SEPARATOR_}Yoffset{_ATE_SEPARATOR_}Xadvance'
    for k, v in fixCharmap(charmap).items():
        if not isinstance(v, tuple): return
        v = list(map(str, v))
        table += f'\n{k}{_ATE_SEPARATOR_}' + _ATE_SEPARATOR_.join(v)
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
    table = f'\nVERSION="1.0"\nSEPARATOR="{_ATE_SEPARATOR_}"\n#####################\nالحرف{_ATE_SEPARATOR_}أول{_ATE_SEPARATOR_}وسط{_ATE_SEPARATOR_}آخر{_ATE_SEPARATOR_}منفصل'
    for k, v in fixCharmap(charmap).items():
        if isinstance(v, tuple): return
        table += f'\n{k}{_ATE_SEPARATOR_*4}{v}'
    return sortACT(table)