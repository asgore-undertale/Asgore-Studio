import re

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
        elif '          ' in line:
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
