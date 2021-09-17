from Parts.Scripts.FixTables import *
from Parts.Vars import _A_SEPARATOR_, _ACT_DESC_, _AFT_DESC_

def charmapToTable(charmap : dict, type : str):
    if not charmap: return
    if type == 'act': return charmapToACT(charmap)
    if type == 'zts': return charmapToZTS(charmap)
    if type == 'aft': return charmapToAFT(charmap)

def charmapToAFT(charmap):
    table = _AFT_DESC_.replace('[_SEPARATOR_]', _A_SEPARATOR_)
    for k, v in fixCharmap(charmap).items():
        if not isinstance(v, tuple): return
        v = list(map(str, v))
        table += f'\n{k}{_A_SEPARATOR_}' + _A_SEPARATOR_.join(v)
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
    table = ''
    for k, v in fixCharmap(charmap).items():
        if isinstance(v, tuple): return
        table += f'\n{k}{_A_SEPARATOR_*4}{v}'
    return _ACT_DESC_.replace('[_SEPARATOR_]', _A_SEPARATOR_) + sortACT(table, _A_SEPARATOR_)