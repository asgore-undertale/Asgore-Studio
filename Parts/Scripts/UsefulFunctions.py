def intToHex(num):
    return str(hex(num)).replace("0x","")

def hexToString(hexstring):
    return bytearray.fromhex(hexstring).decode('cp437')