"""
import pyglet
song = pyglet.media.load('alrme.mp3')
song.play()
pyglet.app.run()

"""
"""
from playsound import playsound
playsound("alarm.wav")

"""

"""import pygame
pygame.mixer.init()
pygame.mixer.music.load("a.wav")
pygame.mixer.music.play()
a=0
while pygame.mixer.music.get_busy() == True:
    a=a+1
    print(a)
    if a==500:
        pygame.mixer.music.stop()
        break
    continue
"""
"""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("/home/pi/Downloads") if isfile(join("/home/pi/Downloads", f) )]
print(onlyfiles)
for file in onlyfiles:
    if str(file).split(".")[1]=="wav":
        print(file)
"""

"""from PyQt5 import QtCore, QtWidgets
import string

class Thired(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Thired, self).__init__(parent)

        self.line_edit = QtWidgets.QLineEdit()
        self.list_widget = QtWidgets.QListWidget()
        options = list(string.ascii_letters)
        print(options)
        self.list_widget.addItems(options)
        self.list_widget.itemClicked.connect(self.on_itemClicked)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.line_edit)
        lay.addWidget(self.list_widget)
        self.resize(640, 480)

    @QtCore.pyqtSlot(QtWidgets.QListWidgetItem)
    def on_itemClicked(self, item):
        self.line_edit.setText(item.text())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = Thired()
    gui.show()
    sys.exit(app.exec_())
"""


"""import pygame
pygame.mixer.init()
pygame.mixer.music.load("a.wav")
pygame.mixer.music.play()
a=0
while pygame.mixer.music.get_busy() == True:
    a=a+1
    print(a)
    if a==500:
        pygame.mixer.music.stop()
        break
    continue


"""
"""
import pygame
playlist = list()
playlist.append ( "alarm/Alarm.wav" )
playlist.append ( "alarm/Alarm.wav" )

import pygame
pygame.mixer.init()
pygame.mixer.music.load("alarm/Alarm.wav")
pygame.mixer.music.play(2) # repeat 5 times

while pygame.mixer.music.get_busy():
    print(5)
    
"""
import pygame
pygame.mixer.init()
pygame.mixer.music.load("Nouveau1/analog-watch-alarm_daniel-simion.wav")
pygame.mixer.music.play()
a=0
while pygame.mixer.music.get_busy() == True:
                            a=a+1
                            print(a)
                            if a==10:
                                pygame.mixer.music.stop()


