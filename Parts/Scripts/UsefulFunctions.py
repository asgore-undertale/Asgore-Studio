def intToHex(num):
    return str(hex(num)).replace("0x","")

def hexToString(hexstring):
    return bytearray.fromhex(hexstring).decode('cp437')

def stringToHex(string):
    return string.encode('utf-8').hex()