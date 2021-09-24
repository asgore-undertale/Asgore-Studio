from PyQt5.QtWidgets import QApplication
from Parts.Scripts.UsefulLittleFunctions import saveFile, tryTakeNum, checkForCommand
from time import time
from sys import argv
from PIL import Image
import keyboard, pygame, random

app = QApplication(argv)
pygame.init()

class Commands:
    def __init__(self):
        super(Commands, self).__init__()
        
    def checkCommands(self, text, index):
        try:
            if checkForCommand('[^]', text, index):
                self.waitconfirm()
            elif checkForCommand('[!]', text, index):
                self.shack()
            elif checkForCommand(r'[\t#]', text, index):
                self.resetTextColor()
            elif checkForCommand(r'[\b#]', text, index):
                self.resetBoxColor()
            elif checkForCommand(r'[\@]', text, index):
                self.resetCurrentSleepTime()
            elif checkForCommand(r'[\$]', text, index):
                self.resetTextSize()
            elif checkForCommand('[@', text, index) and text[index+8] == ']':
                self.setCurrentSleepTime(text, index)
            elif checkForCommand('[$', text, index) and text[index+5] == ']':
                self.setTextSize(text, index)
            elif checkForCommand('[t#', text, index) and text[index+9] == ']':
                self.setTextColor(text, index)
            elif checkForCommand('[b#', text, index) and text[index+9] == ']':
                self.setBoxColor(text, index)
        except: pass
        self.update()
    
    def waitconfirm(self):
        self.waitForPress()
        self.passTimes = 3
        self.waitForRelease()
    
    def shack(self):
        d = self.textzone.copy()
        e = self.background.copy()
        for i in range(self.shakeTimes):
            a = random.randint(0, self.shakeRange) - (self.shakeRange / 2)
            b = random.randint(0, self.shakeRange) - (self.shakeRange / 2)
            self.textzone.blit(d, (a, b))
            self.background.blit(e, (a, b))
            self.update()
            self.pygameWait(1/40)
            self.open()
        self.textzone.blit(d, (0, 0))
        self.background.blit(e, (0, 0))
        self.passTimes = 3
    
    def setTextColor(self, text, index):
        self.textColor = (int(text[index+3], 16) * int(text[index+4], 16),
            int(text[index+5], 16) * int(text[index+6], 16),
            int(text[index+7], 16) * int(text[index+8], 16)
            )
        self.passTimes = 10
    
    def resetTextColor(self):
        self.textColor = (255, 255, 255)
        self.passTimes = 5
    
    def setBoxColor(self, text, index):
        self.boxColor[0] = (
            int(text[index+3], 16) * int(text[index+4], 16),
            int(text[index+5], 16) * int(text[index+6], 16),
            int(text[index+7], 16) * int(text[index+8], 16)
            )
        self.passTimes = 10
    
    def resetBoxColor(self):
        self.boxColor[0] = 0
        self.passTimes = 5
    
    def setCurrentSleepTime(self, text, index):
        self.currentSleepTime = tryTakeNum(text[index+2:index+8], 0, False)
        self.passTimes = 9
    
    def resetCurrentSleepTime(self):
        self.currentSleepTime = 0
        self.passTimes = 4
    
    def setTextSize(self, text, index):
        fontSize = tryTakeNum(text[index+2:index+5], 0)
        if not fontSize: return
        self.setPer(fontSize)
        self.passTimes = 6
    
    def resetTextSize(self):
        self.setPer(self.fontS)
        self.passTimes = 4

class PyGame:
    def __init__(self):
        super(PyGame, self).__init__()
    
    def Checks(self):
        display = self.textzone
        for event in pygame.event.get():
            if event.type is pygame.QUIT: pygame.display.set_mode((1, 1), flags = pygame.HIDDEN)
            self.winShot(event.type)
        if keyboard.is_pressed(self.confirmInput):
            if self.skip: self.currentSleepTime = 0
            return True
    
    def winShot(self, eventType):
        if eventType == pygame.KEYDOWN:
            all_keys = pygame.key.get_pressed()
            if not all_keys[pygame.K_LCTRL] or not all_keys[pygame.K_s]: return
            
            savePath = saveFile(['png'], None, 'صورة')
            if savePath: pygame.image.save(self.textzone, savePath)
    
    def waitForPress(self):
        self.skip = False
        self.waitForRelease()
        while True:
            if self.Checks():
                break
        self.waitForRelease()
        self.skip = True
    
    def waitForRelease(self):
        while keyboard.is_pressed(self.confirmInput):
            self.Checks()
    
    def pygameWait(self, waitTime = 0):
        if waitTime: start = time()
        while waitTime:
            if self.Checks():
                break
            if waitTime and time() - start > waitTime:
                break

class DialogBox(Commands, PyGame):
    def __init__(self, win, x=0, y=0, boxW=0, boxH=0, perline=0, boxC=[0, (255, 255, 255)], borderS=0, confirmInput = 'enter', sleepT=0,
            textC=(255, 255, 255), fontP='', fontS=0, ImgP='', charmap={}, RTL=False, showBoxes = False
        ):
        super(DialogBox, self).__init__()
        
        self.win = win
        self.x = x
        self.y = y
        self.boxWidth = boxW + (borderS * 2)
        self.boxHeight = boxH + (borderS * 2)
        self.textzoneWidth = boxW
        self.textzoneHeight = boxH
        self.boxColor = boxC
        self.textColor = textC
        self.borderS = borderS
        self.sleepTime = sleepT
        self.perline = perline
        self.fontS = fontS
        self.fontP = fontP
        self.ImgP = ImgP
        self.textzone = pygame.Surface((self.boxWidth, self.boxHeight), pygame.SRCALPHA)
        self.background = pygame.Surface((self.boxWidth, self.boxHeight))
        self.RTL = RTL
        self.showBoxes = showBoxes
        self.confirmInput = confirmInput
        self.shakeRange = fontS
        
        self.charmap = charmap
        self.passTimes = 0
        self.currentSleepTime = 0
        self.shakeTimes = 7
        self.skip = True
        
        self.setPer(self.fontS)
		
        if self.fontP.endswith('.ttf'):
            self.font = pygame.font.Font(self.fontP, self.fontS)
    
    def update(self):
        self.win.blit(self.background, (self.x, self.y))
        self.win.blit(self.textzone, (self.x, self.y))
        pygame.display.update()
    
    def open(self):
        self.textzone.set_alpha(255)
        self.background.set_alpha(255)
        self.textzone = pygame.Surface((self.boxWidth, self.boxHeight), pygame.SRCALPHA)
        self.draw()
        self.update()
    
    def close(self):
        self.textzone.set_alpha(0)
        self.background.set_alpha(0)
        self.update()
    
    def draw(self):
        pygame.draw.rect(self.background, self.boxColor[0], (self.x, self.y, self.boxWidth, self.boxHeight))
        pygame.draw.rect(self.textzone, self.boxColor[1], (self.x, self.y, self.boxWidth, self.boxHeight), self.borderS)
    
    def getLinesNum(self):
        return (self.boxHeight + self.perline) // (self.fontS + self.perline)
    
    def setPer(self, fontSize):
        self.per = fontSize / self.charmap['tallest']

    def multiCharDatabyPer(self, data):
        return list(data[:2]) + list(map(lambda x: int(x * self.per), data[2:7])) + list(data[7:])
    
    def write(self, pages):
        _x, _y = (self.borderS * (not self.RTL)) + ((self.boxWidth - self.borderS) * self.RTL), self.borderS
        x, y = _x, _y
        self.setPer(self.fontS)
        self.currentSleepTime = self.sleepTime
        
        for page in pages:
            self.open()
            if self.showBoxes:
                pygame.draw.rect(self.textzone, (255, 0, 0), (self.borderS, self.borderS, self.textzoneWidth, self.textzoneHeight), 1) # textzonebox
                self.update()
            for line in page:
                x, y = self.writeLine(line, x, y)
                x = _x
                y += self.fontS + self.perline
            y = _y
            self.waitForPress()
        
        self.close()
        while True: self.Checks()
    
    def writeLine(self, text, x, y):
        self.checkCommands(text, 0)
        for c in range(len(text)):
            if self.passTimes:
                self.passTimes -= 1
                continue
            
            self.draw()
            char = text[c]
            
            if self.fontP.endswith('.ttf'):
                charimg = self.font.render(char, True, self.textColor)
                charW, charH = charimg.get_size()
                charXadvance = 0
                
                if self.RTL: x -= charW
                xPos, yPos = x, y
                self.textzone.blit(charimg, (xPos, yPos))
                
            elif self.fontP.endswith('.aft') or self.fontP.endswith('.fnt'):
                if char not in self.charmap: continue
                charinfo = self.multiCharDatabyPer(self.charmap[char])
                if charinfo[2] > self.boxWidth: continue
                
                charX, charY, charW, charH = charinfo[0], charinfo[1], charinfo[2], charinfo[3]
                charXoffset, charYoffset, charXadvance = charinfo[4], charinfo[5], charinfo[6]
                
                img = Image.open(self.ImgP)
                cropedImg = img.crop((charX, charY, charX+self.charmap[char][2], charY+self.charmap[char][3]))
                charimg = pygame.image.fromstring(cropedImg.tobytes(), cropedImg.size, cropedImg.mode)
                charimg.fill(self.textColor, special_flags=pygame.BLEND_MULT) ###
                charimg = pygame.transform.scale(charimg, (charW, charH))
                
                if self.RTL: x -= charW
                xPos = x + (-charXoffset * self.RTL) + (charXoffset * (not self.RTL))
                yPos = y + charYoffset
                self.textzone.blit(charimg, (xPos, yPos))
                
            elif self.fontP.endswith('.aff'):
                if char not in self.charmap: continue
                charinfo = self.multiCharDatabyPer(self.charmap[char])
                if charinfo[2] > self.boxWidth: continue
                
                charX, charY, charW, charH = charinfo[0], charinfo[1], charinfo[2], charinfo[3]
                charXoffset, charYoffset, charXadvance = charinfo[4], charinfo[5], charinfo[6]
                charDrawdata = charinfo[7]
                pxWidth = charH / len(charDrawdata)
                
                if self.RTL: x -= charW
                xPos = x + (-charXoffset * self.RTL) + (charXoffset * (not self.RTL))
                yPos = y + charYoffset
                
                for r in range(len(charDrawdata)):
                    for p in range(len(charDrawdata[r])):
                        if charDrawdata[r][p] != self.charmap['filler']: continue
                        pygame.draw.rect(
                            self.textzone, self.textColor, (xPos + (pxWidth * p), yPos + (pxWidth * r), pxWidth, pxWidth)
                            )
            
            if self.showBoxes:
                pygame.draw.rect(self.textzone, (0, 0, 255), (x, y, charW, charH), 1) # charbox
            if self.RTL: x -= charXadvance
            if not self.RTL: x += charW + charXadvance
            
            self.checkCommands(text, c+1)
            self.update()
            self.pygameWait(self.currentSleepTime)
        
        if self.showBoxes:
            pygame.draw.rect(self.textzone, (0, 225, 0), (self.borderS, y, self.textzoneWidth, self.fontS), 1) # linebox
            self.update()
        
        return x, y