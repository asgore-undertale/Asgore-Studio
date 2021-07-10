from Parts.Scripts.UsefulLittleFunctions import getRegexPattern
import re

EnglishLetters = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def minimax(text):
    if mini and len(text) < mini: return
    if maxi and len(text) > maxi: return
    return text
    
def inEnglish(text):
    for char in text:
        if char not in EnglishLetters:
            return
    return text

def Extract(text, before, after, addBeforeAfter = False, mini = False, maxi = False, onlyEnglish = False):
    if not before or not after: return
    try: mini = int(mini)
    except: mini = False
    try: maxi = int(maxi)
    except: maxi = False
    if mini > maxi: return
    
    _UnusedChar = (u'\uffff' * 4)
    _EnterChar  = '\n'
    
    if isinstance(before, bytes): _UnusedChar, _EnterChar = _UnusedChar.encode(), _EnterChar.encode()
    
    text = text.replace(_EnterChar, _UnusedChar)
    before = before.replace(_EnterChar, _UnusedChar)
    after = after.replace(_EnterChar, _UnusedChar)
    
    if before == after:
        extracted_list = text.split(before)
        if len(extracted_list) > 2:
            del extracted_list[0]
            del extracted_list[-1]
    else:
        extracted_list = re.findall(getRegexPattern(before, after), text)
    
    if addBeforeAfter:
        extracted_list = [(before+x+after).replace(_UnusedChar, _EnterChar) for x in extracted_list]
    else:
        extracted_list = [x.replace(_UnusedChar, _EnterChar) for x in extracted_list]
    
    if onlyEnglish:
        extracted_list = list(map(inEnglish, extracted_list))
        extracted_list = list(filter(lambda a: a, extracted_list))
    
    if mini or maxi:
        extracted_list = list(map(minimax, extracted_list))
        extracted_list = list(filter(lambda a: a, extracted_list))
    
    return extracted_list