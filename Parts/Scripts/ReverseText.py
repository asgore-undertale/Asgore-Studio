import re
from Parts.Vars import ArabicChars, FreezedArabicChars, Space

def swapSpacesOnEdges(text):
    if len(text) < 2: return text
    beforeSpaces, afterSpaces = 0, 0
    
    while text[0] == ' ':
        beforeSpaces += 1
        text = text[1:len(text)]
    while text[-1] == ' ':
        afterSpaces += 1
        text = text[0:-1]
    
    return (beforeSpaces * ' ') + text + (afterSpaces * ' ')

def reverseArabic(text):
    container = ''
    for char in text:
        if char not in ArabicChars and char not in FreezedArabicChars and char not in Space:
            container += char
        else:
            if not container: continue
            text = text.replace(container, container[::-1], 1)
            container = ''
    text = text.replace(container, container[::-1], 1)
    
    return swapSpacesOnEdges(text[::-1])

def Reverse(text, case = True):
    if case: text = text[::-1]
    else: text = reverseArabic(text)
    
    return text