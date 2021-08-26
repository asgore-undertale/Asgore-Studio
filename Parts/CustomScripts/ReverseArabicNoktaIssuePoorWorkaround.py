from Parts.Vars import ArabicChars, FreezedArabicChars, neutralChars, Harakat, Returns

Name = 'حل مشكلة النقطة بعكس العربية'

fullStack = ArabicChars + FreezedArabicChars + neutralChars + Harakat + Returns
def Script(text):
    container = ''
    for char in text:
        if char not in fullStack:
            container += char
        else:
            container = ''
    
    if not container: return text
    
    if container[-1] == '.':
        fixedcontainer = '.' + container[0:-1]
    
    text = text.replace(container, fixedcontainer, 1)
    return text