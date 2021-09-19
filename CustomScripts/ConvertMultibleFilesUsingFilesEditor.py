from Parts.Scripts.UsefulLittleFunctions import dirList
from Parts.Tools.AsgoreFilesEditor import loadFile, ConvertAll, save_file
from Parts.Scripts.UsefulLittleFunctions import selectFolder

def Script():
    folder = selectFolder()
    if not folder: return
    
    files = dirList(folder)
    for file in files:
        loadFile(file)
        ConvertAll()
        save_file(file)