from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QImage, QPixmap
from sys import argv
import pygame

def embed(window, label, surface, x, y):
    w = surface.get_width()
    h = surface.get_height()
    data = surface.get_buffer().raw
    image = QImage(data, w, h, QImage.Format_RGB32)
    pixmap = QPixmap(image)
    
    label.setPixmap(pixmap)
    label.move(x, y)
    label.resize(w, h)
    window.repaint()

# if __name__ == '__main__':
    # app = QApplication(argv)
    # pygame.init()

    # Xoffset, Yoffset = 5, 5

    # surface = pygame.Surface((110, 110))

    # window = QMainWindow()
    # window.setFixedSize(120, 120) #sizing the window will cause some curroption so this will help a little
    # label = QLabel(window)
    # window.show()

    # while True:
        # for i in range(25):
            # surface.fill((64, 225, i*8))
            # embed(window, label, surface, Xoffset, Yoffset)
            # input()