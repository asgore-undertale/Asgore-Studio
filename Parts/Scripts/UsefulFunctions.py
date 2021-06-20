def intToHex(num):
    hexstring = str(hex(num)).replace("0x","")
    if len(hexstring) % 2: hexstring = '0' + hexstring
    return hexstring

def hexToString(hexstring):
    if len(hexstring) % 2: hexstring = '0' + hexstring
    try:
        return bytearray.fromhex(hexstring).decode()
    except:
        newHexstring = ''
        for i in range(0, len(hexstring), 2):
            newHexstring += r'\x' + f'{hexstring[i]}{hexstring[i+1]}'
        return newHexstring

def stringToHex(string):
    return string.encode('utf-8').hex()

def sortDictByKeyLengh(Dict):
    newDict = {}
    for k in sorted(Dict, key=len, reverse=True):
        newDict[k] = Dict[k]
    return newDict