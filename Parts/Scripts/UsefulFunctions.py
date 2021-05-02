def intToHex(num):
    hexstring = str(hex(num)).replace("0x","")
    if num < 16: hexstring = '0' + hexstring
    return hexstring

def hexToString(hexstring):
    if hexstring % 2: return
    try:
        return bytearray.fromhex(hexstring).decode()
    except:
        newHexstring = ''
        for i in range(0, len(hexstring), 2):
            newHexstring += r'\x' + f'{hexstring[i]}{hexstring[i+1]}'
        return newHexstring

def stringToHex(string):
    return string.encode('utf-8').hex()