import re, csv
from Parts.Scripts.ExtractFromText import Extract
from Parts.Windows import StudioWindow
from Parts.Vars import _CSV_DELIMITER_


filesTypes = [
    "(msyt) Zelda: Breath of the wild",
    "(txt) Extracted from kruptar tool",
    "(csv) Table",
    "(po) Yakuza Kiwami",
    "(kup) Extracted from kuriimu tool",
    "(yaml) Zelda: oracle of ages"
]

def fileType(index):
    if index == 0: return 'msyt'
    if index == 1: return 'txt'
    if index == 2: return 'csv'
    if index == 3: return 'po'
    if index == 4: return 'kup'
    if index == 5: return 'yaml'

def loadByIndex(index, filePath, columnIndex):
    fileContent, table = '', ''
    textList, transList, oldTransList = '', '', ''
    
    if index == 0:
        fileContent, textList = loadMsyt(filePath)
    if index == 1:
        fileContent, textList = loadKruptar(filePath)
    if index == 2:
        textList, table = loadCsvTable(filePath, columnIndex)
    if index == 3:
        fileContent, textList, transList = loadPo(filePath)
        oldTransList = list(transList)
    if index == 4:
        fileContent, textList, transList = loadKup(filePath)
        oldTransList = list(transList)
    if index == 5:
        fileContent, textList = loadYaml(filePath)
    
    return fileContent, table, textList, transList, oldTransList, len(textList)-1

def saveByIndex(index, filePath, fileContent, textList, transList, oldTransList):
    if index == 0: saveMsyt(filePath, fileContent, textList, transList)
    if index == 1: saveKruptar(filePath, fileContent, textList, transList)
    if index == 2: saveCsvTable(filePath, table, columnIndex, textList, transList)
    if index == 3: savePo(filePath, fileContent, textList, transList, oldTransList)
    if index == 4: saveKup(filePath, fileContent, textList, transList, oldTransList)
    if index == 5: saveYaml(filePath, fileContent, textList, transList)

# ------------------------------------->

def MsytToTxt(file_content):
    new_file_text, new_file_commands, new_file_dump = '', '', ''
    new_file_text_line, first_commands, last_commands = '', '', ''
    command_num = 0
    
    for line in file_content.split('\n'):
        if '- text:' in line:
            new_file_text_line += line.replace('      - text: ', '')
        elif '- control:' in line:
            new_file_text_line += '＜c' + str(command_num) + '＞'
            new_file_commands = new_file_commands.replace(']]', ']') + '[' + str(command_num) + ']]\n'
            command_num += 1
        elif ' ' * 10 in line:
            '''
            if 'animation' in line or 'sound' in line or 'sound2' in line or 'raw' in line:
                first_commands += '＜c' + str(command_num-1) + '＞'
                new_file_text_line = new_file_text_line.replace('＜c' + str(command_num-1) + '＞', '')
                elif 'auto_advance' in line or 'pause' in line or 'choice' in line or 'single_choice' in line:
                   last_commands += '＜c' + str(command_num-1) + '＞'
                  new_file_text_line = new_file_text_line.replace('＜c' + str(command_num-1) + '＞', '')
            '''
            new_file_commands = new_file_commands.replace(']]', ', ' + line.replace('          ', '') + ']]')
        else:
            if new_file_text_line:
                new_file_dump += '\t\t[-----------]\n'
                new_file_text += first_commands + new_file_text_line + last_commands + '\n'
                new_file_text_line, first_commands, last_commands = '', '', ''
            new_file_dump += line + '\n'
    
    newFileContent = '{\n'+new_file_text+'}\n\n' + '{\n'+new_file_commands+'}\n\n' + '{\n'+new_file_dump+'}'
    
    return newFileContent, new_file_commands

def TxtToMsyt(file_content):
    msyt_content_list = re.findall("\{\uffff(.*?)\uffff\}", file_content.replace('\n', '\uffff'))#for regex
    for i in range(len(msyt_content_list)): msyt_content_list[i] = msyt_content_list[i].replace('\uffff', '\n')
    if len(msyt_content_list) == 2: msyt_content_list.insert(1, '')
    
    TxtToMsyt.newFileContent = msyt_content_list[2]
    
    t = '\n' + msyt_content_list[0]
    text_list = t.split('\n')
    del text_list[0]
    
    def edit_line(line):
        if line[0] != '＜': line = '      - text: ' + line
        line = line.replace('\n', '\n      - text: ').replace('＞', '＞      - text: ')
        line = line.replace('＞      - text: ＜', '＞＜').replace('＞      - text: \n', '＞\n')
        line = line.replace('＞      - text: ', '＞\n      - text: ').replace('＜', '\n＜')
        line = line.replace('""', '')
        TxtToMsyt.newFileContent = TxtToMsyt.newFileContent.replace('\t\t[-----------]', line, 1)
    
    list(map(edit_line, text_list))
    
    commands_list = re.findall("\[(.*?)\]", msyt_content_list[1])
    for i in range(len(commands_list)):
        j = '\n      - control:' + commands_list[i].replace(str(i)+', ', ', ').replace(', ', '\n          ')
        TxtToMsyt.newFileContent = TxtToMsyt.newFileContent.replace('＜c' + str(i) + '＞', j)
    
    TxtToMsyt.newFileContent = TxtToMsyt.newFileContent.replace('\n      - text: \n', '\n').replace('\n\n\n      - control:', '\n      - control:')
    TxtToMsyt.newFileContent = TxtToMsyt.newFileContent.replace('\n\n      - control:\n', '\n      - control:\n').replace('}\n\n{\n', '')
    return TxtToMsyt.newFileContent

def loadMsyt(filePath):
    fileContent = open(filePath, 'r', encoding='utf-8', errors='replace').read()
    
    fileContent, reportContent = MsytToTxt(fileContent)
    msyt_content_list = Extract(fileContent, '{\n', '\n}')
    textList = msyt_content_list[0].split('\n')
    
    StudioWindow.Report('أوامر ملف .msyt', reportContent)
    
    return fileContent, textList

def saveMsyt(filePath, fileContent, textList, transList):
    for t in range(len(textList)):
        fileContent = fileContent.replace(f'\n{textList[t]}\n', f'\n{transList[t]}\n', 1)
    open(filePath, 'w', encoding='utf-8', errors='replace').write(TxtToMsyt(fileContent))

def loadKruptar(filePath):
    endcommand = FilesEditorWindow.endCommandCell.toPlainText()
    if not endcommand: return
    
    fileContent = open(filePath, 'r', encoding='utf-8', errors='replace').read()
    textList = fileContent.split(endcommand)
    del textList[-1]
    
    return fileContent, textList

def saveKruptar(filePath, fileContent, textList, transList):
    endCom = FilesEditorWindow.endCommandCell.toPlainText()
    for t in range(len(textList)):
        fileContent = fileContent.replace(textList[t] + endCom, transList[t] + endCom, 1)
    
    open(filePath, 'w', encoding='utf-8', errors='replace').write(fileContent)

def loadPo(filePath):
    fileContent = open(filePath, 'r', encoding='utf-8', errors='replace').read() + '\n\n'
    
    textList = Extract(fileContent, 'msgid "', '"\nmsgstr')
    transList = Extract(fileContent, 'msgstr "', '"\n\n')
    textList = list(map(lambda x: x.replace('\\n', '\n').replace('"\n"', ''), textList))
    transList = list(map(lambda x: x.replace('\\n', '\n').replace('"\n"', ''), transList))
    del textList[0], transList[0]
    
    return fileContent, textList, transList

def savePo(filePath, fileContent, textList, transList, oldTransList):
    for t in range(len(textList)):
        fileContent = fileContent.replace(f'msgstr "{oldTransList[t]}"\n\n', f'msgstr "{transList[t]}"\n\n', 1)
    open(filePath, 'w', encoding='utf-8', errors='replace').write(fileContent)

def loadKup(filePath):
    fileContent = open(filePath, 'r', encoding='utf-8', errors='replace').read()
    textList = Extract(fileContent, '<original>', '</original>')
    transList = Extract(fileContent, '<edited>', '</edited>')
    return fileContent, textList, transList

def saveKup(filePath, fileContent, textList, transList, oldTransList):
    for t in range(len(textList)):
        fileContent = fileContent.replace(f'<edited>{oldTransList[t]}</edited>', f'<edited>{transList[t]}</edited>', 1)
    open(filePath, 'w', encoding='utf-8', errors='replace').write(fileContent)

def loadCsvTable(filePath, columnIndex):
    if columnIndex < 0: return
    
    with open(filePath, newline='', encoding='utf8', errors='replace') as csvfile:
        table = list(csv.reader(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"'))
    
    textList = []
    for row in table:
        try: textList.append(row[columnIndex])
        except: pass
    
    return textList, table

def saveCsvTable(filePath, table, columnIndex, textList, transList):
    for t in range(len(textList)):
        try: table[t][columnIndex] = transList[t]
        except: pass
    with open(filePath, 'w', newline='', encoding="utf-8", errors='replace') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=_CSV_DELIMITER_, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in table:
            spamwriter.writerow(row)

def loadYaml(filePath):
    fileContent = open(filePath, 'r', encoding='utf-8', errors='replace').read() + '\n\n'
    
    textList = Extract(fileContent, '    text: |-\n', '\n\n')
    textList = list(map(lambda x: fixYamlExtractedText(x), textList))
    textList = list(filter(lambda x: x, textList))
    
    return fileContent, textList

def fixYamlExtractedText(text):
    lines = text.split('\n')
    for l in range(len(lines)):
        if ' ' * 6 in lines[l]:
            lines[l] = lines[l][6:len(lines[l])]
            continue
        lines[l] = ''
    return '\n'.join(lines)

def fixYamlEnteredText(text):
    text = ('\n'+text).replace('\n', '\n      ')
    return text[1:]

def saveYaml(filePath, fileContent, textList, transList):
    for t in range(len(textList)):
        textList[t] = fixYamlEnteredText(textList[t])
        transList[t] = fixYamlEnteredText(transList[t])
        fileContent = fileContent.replace(f'    text: |-\n{textList[t]}\n', f'    text: |-\n{transList[t]}\n', 1)
    open(filePath, 'w', encoding='utf-8', errors='replace').write(fileContent)
