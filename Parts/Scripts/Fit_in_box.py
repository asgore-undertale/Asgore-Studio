import re
from Parts.Scripts.Un_Freeze_Arabic import Un_Freeze

def increase_y(y : int, text : str):
    if y == fit.lines_num - 1: return 0, text + fit.newpage
    else: return y + 1, text + fit.newline

def handle_xy(x : int, y : int, textWidth : int, newtext : str):
    if x + textWidth > fit.boxWidth:
        x += textWidth
        y, newtext = increase_y(y, newtext)
    else: x += textWidth
    return x, y, newtext

def checkChar(char : str):
    if char not in fit.charmap:
        print(f'{char} not in charmap.')
        return True
    if fit.charmap[char][2] + fit.charmap[char][6] > fit.boxWidth:
        print(f'{char} is wider than Textzone.')
        return True

def checkWord(word : str, x : int, y : int, case : bool, newword = ''):
    if case:
        for char in word:
            if checkChar(char): continue
            x, y, newword = handle_xy(x, y, fit.charmap[char][2] + fit.charmap[char][6], newword)
            newword += char
    else:
        for char in word:
            if checkChar(char): continue
            newword += char
        x = word_width
        y, newword = increase_y(y, newword)
    return newword, x, y

def width(text : str, width = 0):
    for char in text:
        if checkChar(char): continue
        width += fit.charmap[char][2] + fit.charmap[char][6]
    return width

def split_handling(text : str, case : bool, before_command = '', after_command = ''):
    if case:
        if before_command and after_command:
            commands_chars = '.[]{}*+?()^'
            for char in commands_chars:
                before_command = before_command.replace(char, '\\'+char)
                after_command = after_command.replace(char, '\\'+char)
            text_list = re.split(before_command + "(.*?)" + after_command, text)
        else: text_list = [text]
    else:
        text_list = text.split(' ')
        for i in range(len(text_list) - 1): text_list.insert(i * 2 + 1, ' ')
    return text_list

def fit(text : str, charmap : dict, boxWidth : int, lines_num : int, newline : str, newpage : str, before_command : str, after_command : str):
    if not lines_num: return ''
    x, y, fit.newtext = 0, 0, ''
    fit.boxWidth, fit.lines_num, fit.newline, fit.newpage = boxWidth, lines_num, newline, newpage
    fit.charmap = charmap
    
    if newpage: pages = text.split(newpage)
    else: pages = [text]
    if newline: textList = [page.split(newline) for page in pages]
    else: textList = [pages]
    
    for p in range(len(textList)):
        for l in range(len(textList[p])):
            sentence = split_handling(textList[p][l], True, before_command, after_command)
            for part in range(len(sentence)):
                if not sentence[part]: continue
                if part % 2:
                    sentence[part] = before_command + sentence[part] + after_command
                    fit.newtext += sentence[part]
                    if sentence[part] == newpage: x, y = 0, 0
                    elif sentence[part] == newline: x, y = 0, increase_y(y)
                    continue
                
                sentence[part] = Un_Freeze(sentence[part])
                words_list = split_handling(sentence[part], False)
                
                for word in words_list:
                    if not word: continue
                    wordWidth = width(word)
                    if x + wordWidth > boxWidth and wordWidth < boxWidth:
                        word, x, y = checkWord(word, x, y, False)
                    elif x + wordWidth > boxWidth:
                        word, x, y = checkWord(word, x, y, True)
                    else:
                        word, x, y = checkWord(word, x, y, True)
                    fit.newtext += word
            
            if l < len(textList[p]) - 1: fit.newtext += newline
            x = 0
        if p < len(textList) - 1: fit.newtext += newpage
        y = 0
    
    return fit.newtext