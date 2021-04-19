harakat = 'َﹰﹱﹲﹴﹶﹷﹸﹹﹺﹻﹼﹽﹾﹿ'
def handle_harakat(text, new_text = ''):
    text = ' ' + text
    for _ in range(1, len(text)):
        if not text[_] in harakat or not text[_ - 1] in harakat: new_text += text[_]
    return new_text