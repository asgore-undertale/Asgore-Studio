import re
from Parts.Scripts.Un_Freeze_Arabic import Un_Freeze

def increase_y(y : int):
    if y == fit.lines_num - 1:
        fit.newtext += fit.newpage
        return 0
    else:
        fit.newtext += fit.newline
        return y + 1

def handle_xy(x : int, y : int, char : str):
    if x + fit.charmap[char][2] > fit.textzone_width:
        x = fit.charmap[char][2]
        y = increase_y(y)
    else: x += fit.charmap[char][2]
    return x, y

def check(char : str):
    if char not in fit.charmap:
        print(f'{char} not in charmap.')
        return True
    if fit.charmap[char][2] > fit.textzone_width:
        print(f'{char} is wider than Textzone.')
        return True

def width(text : str, width = 0):
    for char in text:
        if check(char): continue
        width += fit.charmap[char][2]
    return width

def split_handling(text : str, before_command : str, after_command : str, case : bool):
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

def fit(text : str, charmap : dict, textzone_width : int, lines_num : int, newline : str, newpage : str, before_command : str, after_command : str):
    sentence = split_handling(text, before_command, after_command, True)
    x, y, fit.newtext = 0, 0, ''
    fit.textzone_width, fit.lines_num, fit.newline, fit.newpage = textzone_width, lines_num, newline, newpage
    fit.charmap = charmap
    
    for part in range(len(sentence)):
        if not sentence[part]: continue
        if part % 2:
            sentence[part] = before_command + sentence[part] + after_command
            if sentence[part] == newpage:
                x, y = 0, 0
                fit.newtext += sentence[part]
            elif sentence[part] == newline: x, y = 0, increase_y(y)
            continue
        
        sentence[part] = Un_Freeze(sentence[part])
        words_list = split_handling(sentence[part], before_command, after_command, False)

        for word in words_list:
            word_width = width(word)
            if x + word_width > fit.textzone_width and not word_width > fit.textzone_width:
                x, y = word_width, increase_y(y)
                fit.newtext += word
            elif x + word_width > fit.textzone_width:
                for char in word:
                    if check(char): continue
                    x, y = handle_xy(x, y, char)
                    fit.newtext += char
            else:
                x += word_width
                fit.newtext += word
    return fit.newtext