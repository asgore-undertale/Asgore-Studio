from Parts.Scripts.ReshapeHarakat import Reshape

harakat = 'َﹰﹱﹲﹴﹶﹷﹸﹹﹺﹻﹼﹽﹾﹿًٌٍَُِّْ'

def keepLast(text):
    new_text = ''
    text = ' ' + text
    for _ in range(1, len(text)):
        if not text[_] in harakat or not text[_ - 1] in harakat: new_text += text[_]
    return new_text

def delete(text):
    for haraka in harakat:
        text = text.replace(haraka, '')
    return text

def getBack(text):
    new_text = ''
    text = text + ' '
    for i in range(len(text)-1):
        if text[i+1] in harakat: new_text += text[i+1]
        if text[i] not in harakat: new_text += text[i]
    return new_text

def getForward(text):
    new_text = ''
    text = ' ' + text
    for i in range(len(text)-1):
        if text[i+1] not in harakat: new_text += text[i+1]
        if text[i] in harakat: new_text += text[i]
    return new_text

def handle_harakat(text, index):
    if index == 1: return delete(text)
    if index == 2: return keepLast(text)
    if index == 3: return getBack(text)
    if index == 4: return getForward(text)
    if index == 5: return Reshape(text)