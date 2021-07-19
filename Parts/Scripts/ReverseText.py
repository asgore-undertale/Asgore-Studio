from Parts.Vars import ArabicChars, FreezedArabicChars, Space, Harakat, Returns
from Parts.Scripts.UsefulLittleFunctions import swapCharsOnEdges
import re

fullStack = ArabicChars + FreezedArabicChars + Space + Harakat + Returns

def reverseArabic(text):
    container = ''
    for char in text:
        if char not in fullStack:
            container += char
        else:
            if not container: continue
            text = text.replace(container, container[::-1], 1)
            container = ''
    text = text.replace(container, container[::-1], 1)
    
    return swapCharsOnEdges(text[::-1], '')

def Reverse(text, case = True):
    if case: return text[::-1]
    else: return reverseArabic(text)