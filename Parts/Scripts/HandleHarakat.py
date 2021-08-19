from Parts.Scripts.ReshapeHarakat import Reshape
from Parts.Vars import Harakat


def handleHarakat(text, index):
    if index == 1: return delete(text)
    if index == 2: return keepFirst(text)
    if index == 3: return getBack(text)
    if index == 4: return getForward(text)
    if index == 5: return Reshape(text)
    if index == 6: return merg(text)

def keepFirst(text):
    new_text = ''
    text = ' ' + text
    for _ in range(1, len(text)):
        if not text[_] in Harakat or not text[_ - 1] in Harakat: new_text += text[_]
    return new_text

def delete(text):
    for haraka in Harakat:
        text = text.replace(haraka, '')
    return text

def getBack(text):
    new_text = ''
    text = text + ' '
    for i in range(len(text)-1):
        if text[i+1] in Harakat: new_text += text[i+1]
        if text[i] not in Harakat: new_text += text[i]
    return new_text

def getForward(text):
    new_text = ''
    text = ' ' + text
    for i in range(len(text)-1):
        if text[i+1] not in Harakat: new_text += text[i+1]
        if text[i] in Harakat: new_text += text[i]
    return new_text

def merg(text):
    text = text.replace('ﹼﹶ', 'ﱠ').replace('ﹽﹶ', 'ﳲ').replace('ﹼﹷ', 'ﳲ').replace('ﹽﹷ', 'ﳲ').replace('َّ', 'ﱠ')
    text = text.replace('ﹼﹸ', 'ﱠ').replace('ﹽﹸ', 'ﳳ').replace('ﹼﹹ', 'ﳳ').replace('ﹽﹹ', 'ﳳ').replace('ُّ', 'ﱡ')
    text = text.replace('ﹼﹺ', 'ﱢ').replace('ﹽﹺ', 'ﳴ').replace('ﹼﹻ', 'ﳴ').replace('ﹽﹻ', 'ﳴ').replace('ِّ', 'ﱢ')
    
    text = text.replace('ﹼﹰ', 'ﹰ').replace('ﹽﹰ', 'ﹱ').replace('ﹼﹱ', 'ﹱ').replace('ﹽﹱ', 'ﹱ').replace('ًّ', 'ﹰ')
    text = text.replace('ﹼﹲ', 'ﱞ').replace('ﹽﹲ', 'ﱞ').replace('ٌّ', 'ﱞ')
    text = text.replace('ﹼﹴ', 'ﱟ').replace('ﹽﹴ', 'ﱟ').replace('ٍّ', 'ﱟ')
    return text