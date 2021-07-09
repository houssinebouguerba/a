import pyautogui
size_a=(pyautogui.size())
import sys
Width_champ= size_a[0]
Height_champ=size_a[1]-60
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
from qroundprogressbar import QRoundProgressBar
from qroundprogressbar2 import QRoundProgressBar_total
from ui_TestWidget import Ui_TestWidget
from time import strftime
var = False
import smbus
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

import serial
import configparser
import os
import time

from PyQt5 import QtCore, QtWidgets, uic

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)

from dateutil import parser
time_save=20
time_click=7
import sys

from functools import partial

# Import QApplication and the required widgets from PyQt5.QtWidgets
from os import listdir
from os.path import isfile, join
import pygame
pygame.mixer.init()
pygame.mixer.music.load("Nouveau1/old-fashioned-door-bell-daniel_simon.wav")

__version__ = "0.1"
__author__ = "Leodanis Pozo Ramos"

ERROR_MSG = "ERROR"


# 




try:# Enter your COM port in the below line
    ard = serial.Serial('/dev/ttyACM0', 9600)  # open serial port that Arduino is using
    sleep(2)
except:
    ard=0





value = 0
def evaluateExpression(expression):
    """Evaluate an expression."""
    return expression







def March_alarm(x):

    try:
                data_tout_alarme=[0,0,0,0,0,0]
                with open("data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                initial_sound_alarme=data['list_alarm']
                a=initial_sound_alarme.split('[')[1]
                b=a.split(']')[0]
                c=b.split("'")
                initial_sound_alarme=[c[1],c[3],c[5],c[7],c[9],c[11]]
                
                silencieux_data=data['alarme'].split('[')        
                initial_alarme=silencieux_data[1].split(']')
                data_initial_alarme=initial_alarme[0].split(', ')
                print(data_initial_alarme)
                for i in range (6):
                            
                        if data_initial_alarme[i]=='True':
                            data_tout_alarme[i]=True
                            
                        if data_initial_alarme[i]=='False':
                            data_tout_alarme[i]=False           
                 
    except:
            print("err16")
            data_tout_alarme=[True,False,False,False,False,False]


    
    if data_tout_alarme[4]==True:
        pygame.mixer.init()
        pygame.mixer.music.load("Nouveau1/"+initial_sound_alarme[3])
        pygame.mixer.music.play()
        a=0
        while pygame.mixer.music.get_busy() == True:
                                    a=a+1
                                    print(a)
                                    if a==x:
                                        pygame.mixer.music.stop()







def touch_clavier(x):

    try:
                data_tout_alarme=[0,0,0,0,0,0]
                with open("data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                silencieux_data=data['alarme'].split('[')        
                initial_alarme=silencieux_data[1].split(']')
                data_initial_alarme=initial_alarme[0].split(', ')
                print(data_initial_alarme)
                for i in range (6):
                            
                        if data_initial_alarme[i]=='True':
                            data_tout_alarme[i]=True
                            
                        if data_initial_alarme[i]=='False':
                            data_tout_alarme[i]=False           
                 
    except:
            print("err16")
            data_tout_alarme=[True,False,False,False,False,False]


    
    if data_tout_alarme[5]==True:
        pygame.mixer.init()
        pygame.mixer.music.load("Nouveau1/analog-watch-alarm_daniel-simion.wav")
        pygame.mixer.music.play()
        a=0
        while pygame.mixer.music.get_busy() == True:
                                    a=a+1
                                    print(a)
                                    if a==x:
                                        pygame.mixer.music.stop()
                                

def up(x,lab):
        touch_clavier(time_click)
        if int(x)<=8:
                x= int(x)+1
        else:
                x=0
        lab.setText(str(x))
def down(x,lab):
        touch_clavier(time_click)
        if int(x)>=1:
                x= int(x)-1
        else:
                x=9
        lab.setText(str(x))

def save_config(file,parametre,value_save):

                    with open(file, "r") as jsonFile:
                        data = json.load(jsonFile)                    
                    data[parametre] = str(value_save)

                    with open(file, "w") as jsonFile:
                        json.dump(data, jsonFile)
                    jsonFile.close()


                                        
touch_clavier(20)
class Thired(QtWidgets.QDialog):
    signal_alarm=pyqtSignal(str)
    def __init__(self, parent=None):
        super(Thired, self).__init__(parent)
        self.list_sound=[]

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit2 = QtWidgets.QLineEdit()
        self.list_widget = QtWidgets.QListWidget()

        onlyfiles = [f for f in listdir("/home/pi/Desktop/QRoundProgressBar-master/Nouveau1") if isfile(join("/home/pi/Desktop/QRoundProgressBar-master/Nouveau1", f) )]
        for file in onlyfiles:
            try:
                if str(file).split(".")[1]=="wav":
                    self.list_sound.append(file)
            except:
                print("err1")
                
        
        options = self.list_sound
        
        
        self.list_widget.addItems(options)
        self.list_widget.itemClicked.connect(self.on_itemClicked)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.line_edit)
        lay.addWidget(self.list_widget)
        self.resize(300, 200)
        self.move(500, 200)

    @QtCore.pyqtSlot(QtWidgets.QListWidgetItem)
        
    def on_itemClicked(self, item):
        self.line_edit.setText(item.text())
        self.main=conf_Alarm() 
        try:
            self.signal_alarm.connect(self.main.get_sound_alarm)
            self.signal_alarm.emit(str(item.text()))
        except:
            print('err5')
        




class PyCalav (QMainWindow):
    """PyCalc's View (GUI)."""
    signalv=pyqtSignal(str)

    
    def closeEvent(self, event):
        self.destroy()
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle("Clav")
        self.setFixedSize(235, 250)
        self.move(500,150)


        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.le = QLabel()
        self.le.move(30,20)
        self.le.resize(400,22)
        self.le.setText("mL/s :")

        self.inite = QLabel()
        self.inite.move(30,20)
        self.inite.resize(400,22)
        
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.inite)       
        # Add the display to the general layout
        self.generalLayout.addWidget(self.le)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "C": (0, 3),
            
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            ":": (1, 3),
            
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            
            
            "0": (3, 0),
            "-": (3, 1),
            "Esp": (3, 2),
            "Entrée": (2, 3),
           
            
        }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        touch_clavier(time_click)
        self.display.setText(text)

        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        

        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")
    def ESp_Display(self,val):
        self.display.setText(str(val)+" ")
        self.display.setFocus()       
    def en_valeur(self,vol):
        touch_clavier(time_click)
        self.main=conf_volume() 
        try:
            self.signalv.connect(self.main.get_volume)

            self.signalv.emit(str(int(vol)))
            self.destroy()
        except Exception as e:
            print(e)
       

class PyCalavCtrl:
    """PyCalc's Controller."""
    signalv="lmm"

    def closeEvent(self, event):
        self.destroy()

    def __init__(self, model, view):
        self.signalv=pyqtSignal(str)
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        

        self.main_v=conf_volume() 
        result = self._evaluate(expression=self._view.displayText())
        self._view.inite.setText(str(result)+" ml")
        self._view.en_valeur(result)
        return result

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
       
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"Entrée", "C"}:
                if btnText in{"Esp"}:
                    btn.clicked.connect(partial(self._buildExpression, " "))
                else:

                    btn.clicked.connect(partial(self._buildExpression, btnText))
                

        self._view.buttons["Entrée"].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)



# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""
    def closeEvent(self, event):
        self.destroy()

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle("Clav")
        self.setFixedSize(235, 250)
        self.move(500,150)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.le = QLabel()
        self.le.move(30,20)
        self.le.resize(400,22)
        self.le.setText("yyyy-m-d H:M:S :")
        
        self.date_time = QLabel()
        self.date_time.move(30,20)
        self.date_time.resize(400,22)
        self.date_time.setText(str(datetime.datetime.now()).split('.')[0])        
        
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.date_time)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.le)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "C": (0, 3),
            
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            ":": (1, 3),
            
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            
            
            "0": (3, 0),
            "-": (3, 1),
            "Esp": (3, 2),
            "Entrée": (2, 3),
           
            
        }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        touch_clavier(time_click)
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        
        self.setDisplayText("")
    def ESp_Display(self,val):
        touch_clavier(time_click)
        self.display.setText(str(val)+" ")
        self.display.setFocus()

class PyCalcCtrl:
    """PyCalc's Controller."""
    def closeEvent(self, event):
        self.destroy()

    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        touch_clavier(time_click)
        try:
                datee=[]
                datf=[]
                
                result = self._evaluate(expression=self._view.displayText())
                result=str(result)
                
                for result in (result.split(" ")):
                                    datee.append(result)
                
                for dt in (datee[0].split("-")):
                                    datf.append(int(dt))
                for hr in (datee[1].split(":")):
                                    datf.append(int(hr))
                a=(str(datf).split("[")[1])
                b=a.split("]")[0]
                
                da=datetime.datetime(datf[0],datf[1],datf[2],datf[3],datf[4],datf[5])
                
                os.popen('sudo date -s "'+str(da)+'"')
        except:
                result=str(datetime.datetime.now()).split('.')[0]
                os.popen('sudo date -s "'+str(result)+'"')
                
        #self.date_time.setText(str("kkkkkkkk"))2020-10-10 10:10:10      


        return result

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"Entrée", "C"}:
                if btnText in{"Esp"}:
                    btn.clicked.connect(partial(self._buildExpression, " "))
                else:

                    btn.clicked.connect(partial(self._buildExpression, btnText))
                

        self._view.buttons["Entrée"].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)
        
        
    def showDialog(self):
        temps, ok = QInputDialog.getText(self, 'date/heur', 'yyyy-m-d H:M:S :')
        
        if ok:
            print("oki")
            date = parser.parse(temps)
            self.le.setText(str(date))

            os.popen('sudo date -s "'+str(date)+'"')

        else:
                self.le.setText(str(datetime.datetime.now()).split('.')[0])    

class configue_f(QMainWindow):
    signal2=pyqtSignal(str)
    sringue=1
    try:
        with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile)

        force=data['force']
        alarme=data['alarme']
        vitesse=data['vitesse']
        adresse=data['adresse']
        mov=data['mov']
        list_alarm=data['list_alarm']
    except:
        print("fichier err4")
        force=0
        alarme=0
        vitesse=0
        adresse=0
        mov=0
        list_alarm=["","","","",""]
        

                        
    def __init__(self):
        super().__init__()
        self.button_sy=[0,0,0,0,0,0]
        self.val_yb_sy=20
        serifFont = QFont("Times", 10, QFont.Bold)
        for i in range(4):
                self.button_sy[i]= QPushButton(self)                
                self.button_sy[i].setFixedWidth(150)
                self.button_sy[i].setFixedHeight(50)
                self.button_sy[i].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.button_sy[i].move(20,self.val_yb_sy)
                self.val_yb_sy=self.val_yb_sy+60
                
        self.button_sy[0].setText("Date/Temps")
        self.button_sy[1].setText("Alarme")
        self.button_sy[2].setText("Force")
        self.button_sy[3].setText("Adresse")
        #self.button_sy[4].setText("Vitesse de\n Transmission")
        
        self.button_sy[0].clicked.connect(lambda:self.modif_date_time(0))
        
        self.button_sy[1].clicked.connect(lambda:self.modif_Alarm(1))
        self.button_sy[2].clicked.connect(lambda:self.modif_Force(2))
        self.button_sy[3].clicked.connect(lambda:self.modif_Adresse(3))
        #self.button_sy[4].clicked.connect(lambda:self.modif_Bode(4))
        

        """self.button_sy[0].clicked.connect(lambda:self.fun(0))
        self.button_sy[1].clicked.connect(lambda:self.fun(1))
        self.button_sy[2].clicked.connect(lambda:self.fun(2))
        self.button_sy[3].clicked.connect(lambda:self.fun(3))
        self.button_sy[4].clicked.connect(lambda:self.fun(4))"""
        self.button_sy[0].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.discrip=["discrrip1","discrrip2","discrrip3","discrrip4","discrrip5","discrrip6"]
                                          
        self.label_discrip=QtWidgets.QLabel(self)
        self.label_discrip.setFixedWidth(200)
        self.label_discrip.setFixedHeight(180)
        self.label_discrip.setText(str(self.discrip[0]))        
        self.label_discrip.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.label_discrip.move(220,80)

        self.lab_forc=QtWidgets.QLabel(self)
        self.lab_forc.setFixedWidth(40)
        self.lab_forc.setFixedHeight(40)
        self.lab_forc.setText(str(configue_f.force)+"%")        
        self.lab_forc.setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.lab_forc.move(130,145)

        self.lab_adresse=QtWidgets.QLabel(self)
        self.lab_adresse.setFixedWidth(40)
        self.lab_adresse.setFixedHeight(40)
        self.lab_adresse.setText(str(configue_f.adresse))  
        self.lab_adresse.setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.lab_adresse.move(140,205)   
        
        self.button_valid= QPushButton(self)
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(350,270)
        self.button_valid.clicked.connect(self.modif_boutton_seringue)


        
        self.initUI()
    def change_color(self,i):
    
                print("un ",i)
                for k in range(4):
                        self.button_sy[k].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                        self.seringue=i+1
                self.label_discrip.setText(str(self.discrip[i]))
                self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       


    def mouseMoveEvent(self, QMouseEvent):
        print("event")
        self.lab_forc.setText(str(configue_f.force)+"%")        
        self.lab_adresse.setText(str(configue_f.adresse))   
    def get_val_alarme(self,alarme,mov,list_alarm):
        configue_f.list_alarm=list_alarm
        configue_f.alarme=alarme
        configue_f.mov=mov
        alarme=alarme.split('[')
        alarme=str(alarme[1]).split(']')
        alarme=str(alarme[0]).split(', ')

        for i in range(6):
            if alarme[i]=='True':
                alarme[i]=1
            if alarme[i]=='False':
                alarme[i]=0                           
      
        
    def get_val_force(self,force):
        configue_f.force=force
    def get_val_bode(self,bode):

        configue_f.vitesse=bode

    def get_val_adresse(self,adresse):

        configue_f.adresse=adresse

    def modif_date_time(self,i):
                touch_clavier(time_click)
                self.change_color(i)

                view = PyCalcUi()
                view.show()
                model = evaluateExpression
                PyCalcCtrl(model=model, view=view)
                print("ok")
    def modif_Alarm(self,i):
                touch_clavier(time_click)
                self.change_color(i)

                view = conf_Alarm()
                view.show()
                
    def modif_Force(self,i):
                touch_clavier(time_click)
                self.change_color(i)

                view = conf_Force()
                view.show()
                
    def modif_Adresse(self,i):
                touch_clavier(time_click)
                self.change_color(i)

                view = conf_Adresse()
                view.show()
    def modif_Bode(self,i):
                self.change_color(i)

                view = conf_Bode()
                view.show()
        
    def fun(self,i):

        for k in range(4):
                self.button_sy[k].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.seringue=i+1
        self.label_discrip.setText(str(self.discrip[i]))
        self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

    def modif_boutton_seringue(self):
            touch_clavier(time_save)
            try:    
                    save_config("data.json","alarme",str(configue_f.alarme))
                    save_config("data.json","force",str(configue_f.force))
                    save_config("data.json","adresse",str(configue_f.adresse))
                    save_config("data.json","vitesse",str(configue_f.vitesse))
                    save_config("data.json","mov",str(configue_f.mov))
                    save_config("data.json","list_alarm",str(configue_f.list_alarm))
                    #self.main=Widget()
                    #self.signal2.connect(self.main.getval_seringue)
                    #self.signal2.emit(str(self.seringue*10))
                    
            except:
                print("o")
            self.destroy()
    def initUI(self):    
        
        self.setGeometry(320, 140, 470, 320)  


        
        self.setWindowTitle('Configurations totale')    













class conf_pression(QMainWindow):
    signal2=pyqtSignal(str,str)

                        
    def __init__(self):
        super().__init__()

        self.b_x=10
        self.y_b=190
        self.button_up=[0,0,0,0]
        self.button_down=[0,0,0,0]        
        self.label=[0,0,0,0]
        self.x_l=10

        self.button_up2=[0,0,0,0]
        self.button_down2=[0,0,0,0]        
        self.label2=[0,0,0,0]
        self.x_l2=210
        self.b_x2=210

        self.labelmax=QtWidgets.QLabel(self)
        self.labelmax.setFixedWidth(80)
        self.labelmax.setFixedHeight(40)
        self.labelmax.setText("MIN")
        self.labelmax.setStyleSheet('color: rgb(0, 0, 0);font: 25pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.labelmax.move(50,50)  


        self.labelmin=QtWidgets.QLabel(self)
        self.labelmin.setFixedWidth(80)
        self.labelmin.setFixedHeight(40)
        self.labelmin.setText("MAX")
        self.labelmin.setStyleSheet('color: rgb(0, 0, 0);font: 25pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.labelmin.move(250,50)  
        
        for i in range(4):
            
            
            self.label2[i]=QtWidgets.QLabel(self)
            self.label2[i].setFixedWidth(40)
            self.label2[i].setFixedHeight(20)
            self.label2[i].setText(str(i))

            self.label2[i].setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.label2[i].move(self.x_l2,100)
            self.x_l2=self.x_l2+40

  



        
        self.labelv2=QtWidgets.QLabel(self)
        self.labelv2.setFixedWidth(10)
        self.labelv2.setFixedHeight(20)
        self.labelv2.setText(".")
        self.labelv2.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.labelv2.move(320,100)
        

        for i in range(4):

            self.button_up2[i] = QPushButton(self)
            

            self.button_up2[i].setFixedWidth(30)
            self.button_up2[i].setFixedHeight(30)
            self.button_up2[i].setIcon(QtGui.QIcon('up.png'))
            self.button_up2[i].setIconSize(QSize(30,30))

            self.button_up2[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.button_up2[i].move(self.b_x2,130)
            self.b_x2=self.b_x2+40
        self.b_x2=210

        self.button_up2[0].clicked.connect(lambda:up(self.label2[0].text(),self.label2[0]))
        self.button_up2[1].clicked.connect(lambda:up(self.label2[1].text(),self.label2[1]))
        self.button_up2[2].clicked.connect(lambda:up(self.label2[2].text(),self.label2[2]))
        self.button_up2[3].clicked.connect(lambda:up(self.label2[3].text(),self.label2[3]))
       
        for j in range(4):

            self.button_down2[j] = QPushButton(self)

            self.button_down2[j].setFixedWidth(30)
            self.button_down2[j].setFixedHeight(30)
            self.button_down2[j].setIcon(QtGui.QIcon('down.png'))
            self.button_down2[j].setIconSize(QSize(30,30))
            self.button_down2[j].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.button_down2[j].move(self.b_x2,170)
            self.b_x2=self.b_x2+40

        self.button_down2[0].clicked.connect(lambda:down(self.label2[0].text(),self.label2[0]))
        self.button_down2[1].clicked.connect(lambda:down(self.label2[1].text(),self.label2[1]))
        self.button_down2[2].clicked.connect(lambda:down(self.label2[2].text(),self.label2[2]))
        self.button_down2[3].clicked.connect(lambda:down(self.label2[3].text(),self.label2[3]))
        
        for i in range(4):
            
            
            self.label[i]=QtWidgets.QLabel(self)
            self.label[i].setFixedWidth(40)
            self.label[i].setFixedHeight(20)
            self.label[i].setText(str(i))

            self.label[i].setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.label[i].move(self.x_l,100)
            self.x_l=self.x_l+40

  



        
        self.labelv=QtWidgets.QLabel(self)
        self.labelv.setFixedWidth(10)
        self.labelv.setFixedHeight(20)
        self.labelv.setText(".")
        self.labelv.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.labelv.move(120,100)  



        for i in range(4):

            self.button_up[i] = QPushButton(self)
            

            self.button_up[i].setFixedWidth(30)
            self.button_up[i].setFixedHeight(30)
            self.button_up[i].setIcon(QtGui.QIcon('up.png'))
            self.button_up[i].setIconSize(QSize(30,30))

            self.button_up[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.button_up[i].move(self.b_x,130)
            self.b_x=self.b_x+40
        self.b_x=10

        self.button_up[0].clicked.connect(lambda:up(self.label[0].text(),self.label[0]))
        self.button_up[1].clicked.connect(lambda:up(self.label[1].text(),self.label[1]))
        self.button_up[2].clicked.connect(lambda:up(self.label[2].text(),self.label[2]))
        self.button_up[3].clicked.connect(lambda:up(self.label[3].text(),self.label[3]))
       
        for j in range(4):

            self.button_down[j] = QPushButton(self)

            self.button_down[j].setFixedWidth(30)
            self.button_down[j].setFixedHeight(30)
            self.button_down[j].setIcon(QtGui.QIcon('down.png'))
            self.button_down[j].setIconSize(QSize(30,30))
            self.button_down[j].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.button_down[j].move(self.b_x,170)
            self.b_x=self.b_x+40
            
        self.button_down[0].clicked.connect(lambda:down(self.label[0].text(),self.label[0]))
        self.button_down[1].clicked.connect(lambda:down(self.label[1].text(),self.label[1]))
        self.button_down[2].clicked.connect(lambda:down(self.label[2].text(),self.label[2]))
        self.button_down[3].clicked.connect(lambda:down(self.label[3].text(),self.label[3]))
        self.button_valid= QPushButton(self)
        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(330,210)
        self.button_valid.clicked.connect(self.modif_boutton)
        self.initUI()        

    def modif_boutton(self):
            touch_clavier(time_save)

            if float(str(self.label[0].text()+self.label[1].text()+self.label[2].text()+"."+self.label[3].text())) < float(str(self.label2[0].text()+self.label2[1].text()+self.label2[2].text()+"."+self.label2[3].text())):
                    self.main=Widget()
                    self.signal2.connect(self.main.getval_presion)
                    self.signal2.emit(str(self.label[0].text()+self.label[1].text()+self.label[2].text()+"."+self.label[3].text()),str(self.label2[0].text()+self.label2[1].text()+self.label2[2].text()+"."+self.label2[3].text()))
                    save_config("data.json","pression",str(self.label[0].text()+self.label[1].text()+self.label[2].text()+"."+self.label[3].text())+","+str(self.label2[0].text()+self.label2[1].text()+self.label2[2].text()+"."+self.label2[3].text()))

                    self.destroy()
                    
            else:
                    print("err7")

        
    def initUI(self):    
        
        self.setGeometry(320, 180, 470, 270)  


        
        self.setWindowTitle('Configurations Pression')    


class conf_Alarm(QMainWindow):
    signal3=pyqtSignal(str,int,list)
    mode=0
    select=0
    pygame.mixer.init()
    sound_alarm_chang=[" "," "," "," "," "," "]
                        
    def __init__(self):
        super().__init__()

        
        self.button_sy=[0,0,0,0,0,0]
        self.lbel_sound=[0,0,0,0]
        self.button_start=[0,0,0,0,0,0]
        self.etat=[0,0,0,0,0,0]

        self.val_yb_sy=70
        serifFont = QFont("Times", 10, QFont.Bold)


        try:
                with open("data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                self.data_mov=data['mov']
                l_alarm=data['list_alarm']
                a=l_alarm.split('[')[1]
                b=a.split(']')[0]
                c=b.split("'")
                self.sound_alarm=[c[1],c[3],c[5],c[7],c[9],c[11]]
                conf_Alarm.sound_alarm_chang=self.sound_alarm

                data_alarme=data['alarme'].split('[')        
                data_alarme=data_alarme[1].split(']')
                self.data_alarme=data_alarme[0].split(', ')

                
                
        except:
                self.data_mov="0"
                self.sound_alarm=[" "," "," "," "," "," "]




        
        self.val_combo=self.data_mov+"%"
        self.matrix=[0,0,0,0,0,0]
        for i in range(4):
                self.button_start[i]= QPushButton(self)                
                self.button_start[i].setFixedWidth(30)
                self.button_start[i].setFixedHeight(30)
                self.button_start[i].setIcon(QtGui.QIcon('march.png'))
                self.button_start[i].move(350,self.val_yb_sy)
                self.val_yb_sy=self.val_yb_sy+50

        self.val_yb_sy=20

        for i in range(6):
                self.button_sy[i]= QCheckBox(self)                
                self.button_sy[i].setFixedWidth(155)
                self.button_sy[i].setFixedHeight(40)
                self.button_sy[i].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.button_sy[i].move(20,self.val_yb_sy)
                self.val_yb_sy=self.val_yb_sy+50
                
        self.val_yb_sy=70
        for i in range(4):

                self.lbel_sound[i]= QtWidgets.QLabel(self)               
                self.lbel_sound[i].setFixedWidth(150)
                self.lbel_sound[i].setFixedHeight(30)
                self.lbel_sound[i].setText(self.sound_alarm[i])
                self.lbel_sound[i].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.lbel_sound[i].move(185,self.val_yb_sy)
                self.val_yb_sy=self.val_yb_sy+50

                
        self.button_sy[0].setText("silencieux")
        self.button_sy[1].setText("Fin de course")
        self.button_sy[2].setText("Stalle")
        self.button_sy[3].setText("Rappel d'étalonnage")
        self.button_sy[4].setText("démarrage")
        self.button_sy[5].setText("clic de clavier")

        for i in range (6):
                
            if self.data_alarme[i]=='True':
                self.button_sy[i].setCheckState(True)
                self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            if self.data_alarme[i]=='False':
                self.button_sy[i].setCheckState(False)



        self.button_sy[0].clicked.connect(lambda:self.fun(0))
        self.button_sy[1].clicked.connect(lambda:self.fun(1))
        self.button_sy[2].clicked.connect(lambda:self.fun(2))
        self.button_sy[3].clicked.connect(lambda:self.fun(3))
        self.button_sy[4].clicked.connect(lambda:self.fun(4))
        self.button_sy[5].clicked.connect(lambda:self.fun(5))

        self.button_start[0].clicked.connect(lambda:self.start_pose_alarme(0))
        self.button_start[1].clicked.connect(lambda:self.start_pose_alarme(1))
        self.button_start[2].clicked.connect(lambda:self.start_pose_alarme(2))
        self.button_start[3].clicked.connect(lambda:self.start_pose_alarme(3))

        
        #self.button_sy[0].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.discrip=["discrrip1","discrrip2","discrrip3","discrrip4","discrrip5","discrrip6"]
                                          
        
        self.button_MOV= QPushButton(self)
        
        self.button_MOV.setText("MOV")
        self.button_MOV.setFixedWidth(150)
        self.button_MOV.setFixedHeight(40)
        self.button_MOV.setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_MOV.move(185,20)
        self.button_MOV.clicked.connect(self.start_pose_alarme)

        self.combo=QComboBox(self)
        self.combo.addItem(str(self.data_mov)+"%")
        self.combo.addItem("10%")
        self.combo.addItem("20%")
        self.combo.addItem("30%")
        self.combo.addItem("40%")
        self.combo.addItem("50%")
        self.combo.addItem("60%")
        self.combo.addItem("70%")
        self.combo.addItem("80%")
        self.combo.addItem("90%")
        self.combo.addItem("100%")
        self.combo.setFixedWidth(70)
        self.combo.setFixedHeight(40)
        self.combo.setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        
        self.combo.move(350,20)
        self.combo.activated[str].connect(self.combo_return)
        
       



        
        self.button_valid= QPushButton(self)
        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(60)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(400,270)
        self.button_valid.clicked.connect(self.modif_boutton_mode)
        self.initUI()


    def start_pose_alarme(self,i):         
                    self.button_start[i].setIcon(QtGui.QIcon('march.png'))
                    try:
                        pygame.mixer.init()
                        pygame.mixer.music.load("Nouveau1/"+conf_Alarm.sound_alarm_chang[i])
                        pygame.mixer.music.play(2)
                        a=0

                        while pygame.mixer.music.get_busy() == True:
                            a=a+1
                            print(a)
                            
                            if a==100:
                                pygame.mixer.music.stop()

                    except Exception as e:
                       print(e)



                    


    def mouseMoveEvent(self, QMouseEvent):
         for i in range(4):
            self.lbel_sound[i].setText(str(conf_Alarm.sound_alarm_chang[i]))
            print(self.lbel_sound[i].text())
         
        

    def combo_return(self,text):
        self.val_combo=str(text)
    def get_sound_alarm(self,sound):
        conf_Alarm.sound_alarm_chang[conf_Alarm.select-1]=str(sound)
                
        

    def fun(self,i):
        touch_clavier(time_click)
        conf_Alarm.select=i
        if i==0:
            for l in range(5):
                self.button_sy[l+1].setCheckState(False)
        for k in range(6):
                if self.button_sy[i].isChecked()==1 and i!=0 :
                    self.button_sy[0].setCheckState(False)



                self.button_sy[k].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.mode=i

        self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        if i!=0 and i!=5 and self.button_sy[i].isChecked()==1:
            self.config_lst_alarm=Thired()
            self.config_lst_alarm.show()
    def modif_boutton_mode(self):
            touch_clavier(time_save)
            try:
                    self.matrix=[0,0,0,0,0,0]
                    for m in range (6):
                        self.matrix[m]=self.button_sy[m].isChecked()

                                                         

                    self.conf_total=configue_f()
                    self.signal3.connect(self.conf_total.get_val_alarme)
                    self.signal3.emit(str(self.matrix),int(self.val_combo.split('%')[0]),conf_Alarm.sound_alarm_chang)
                    self.destroy()
            except:
                print("o")
            #self.destroy()
    def initUI(self):    
        
        self.setGeometry(320, 140, 470, 320)  


        
        self.setWindowTitle('Configurations Alarme')    


class conf_Adresse(QMainWindow):
    signal3=pyqtSignal(str)
    mode=0



                        
    def __init__(self):
        super().__init__()
        self.etas=0
        self.val_yb_sy=20
        self.xlab=20
        serifFont = QFont("Times", 10, QFont.Bold)
        
        self.sp = QSpinBox(self)
        self.sp.move(130,20)
        self.sp.setMaximum(100)
        self.sp.setValue(0)
        
        self.sp.setFixedWidth(100)
        self.sp.setFixedHeight(40)

        self.sp.show()
        

        self.button_sy= QPushButton(self)                 
        self.button_sy.setFixedWidth(100)
        self.button_sy.setFixedHeight(40)
        self.button_sy.setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_sy.move(self.xlab,self.val_yb_sy)

                

        self.button_sy.setText("Adresse:")



        try:
            with open("data.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data_adresse=data['adresse']
            self.sp.setValue(int(data_adresse))


        except:
            data_adresse=0
        

        self.button_sy.clicked.connect(lambda:self.fun(0))


        
        
        self.button_sy.setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

       
        self.button_valid= QPushButton(self)        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(350,270)
        self.button_valid.clicked.connect(self.modif_boutton_Force)
        self.show()
        self.initUI()      
    def fun(self,i):
        print("ok")

    def modif_boutton_Force(self):
            touch_clavier(time_save)
            try:
                   
                   
                    self.main_adr=configue_f()
                    self.signal3.connect(self.main_adr.get_val_adresse)

                    
                    self.signal3.emit(str(self.sp.value()))
                    self.destroy()
                    
            except:
                print("o")
            #self.destroy()
    def initUI(self):    
        
        self.setGeometry(320, 140, 470, 320)  



        
        self.setWindowTitle('Configurations Adresse')    




class conf_Bode(QMainWindow):
    signal3=pyqtSignal(str)
    mode=0




                        
    def __init__(self):
        super().__init__()
        self.etas=0
        self.val_yb_sy=20
        self.xlab=20
        serifFont = QFont("Times", 10, QFont.Bold)
        
        self.sp = QSpinBox(self)
        self.sp.move(150,20)
        self.sp.setMaximum(100000)
        self.sp.setValue(9600)
        
        self.sp.setFixedWidth(100)
        self.sp.setFixedHeight(40)

        self.sp.show()
        

        self.button_sy= QPushButton(self)                 
        self.button_sy.setFixedWidth(120)
        self.button_sy.setFixedHeight(40)
        self.button_sy.setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_sy.move(self.xlab,self.val_yb_sy)

                
        
        self.button_sy.setText("Vitesse b/s:")

        

        self.button_sy.clicked.connect(lambda:self.fun(0))


        
        
        self.button_sy.setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

        
        self.button_valid= QPushButton(self)        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(350,270)
        self.button_valid.clicked.connect(self.modif_boutton_Force)
        self.show()
        self.initUI()      
    def fun(self,i):
        print("ok")

    def modif_boutton_Force(self):
            touch_clavier(time_save)
            try:
                   
                    self.main_adr=configue_f()
                    self.signal3.connect(self.main_adr.get_val_bode)

                    
                    self.signal3.emit(str(self.sp.value()))
                    self.destroy()
                    
            except:
                print("o")
            #self.destroy()
    def initUI(self):    
        
        self.setGeometry(320, 140, 470, 320)  



        
        self.setWindowTitle('Configurations Vitesse de Transmission')    







class conf_Force(QMainWindow):
    signal3=pyqtSignal(str)
    mode=0


  
                        
    def __init__(self):
        super().__init__()
        self.button_sy=[0,0,0,0,0,0,0,0,0,0,0]
        self.etas=[0,0,0,0,0,0,0,0,0,0,0]
        self.val_yb_sy=20
        self.xlab=20
        serifFont = QFont("Times", 10, QFont.Bold)
        self.val_combo="0%"
        self.sp = QSpinBox(self)
        self.sp.move(310,230)
        self.sp.setFixedWidth(50)
        
        for i in range(11):
                
                self.button_sy[i]= QCheckBox(self)                
                self.button_sy[i].setFixedWidth(100)
                self.button_sy[i].setFixedHeight(40)
                self.button_sy[i].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.button_sy[i].move(self.xlab,self.val_yb_sy)
                self.val_yb_sy=self.val_yb_sy+50
                if i==5:
                    self.xlab=200
                    self.val_yb_sy=20
                
        
        self.button_sy[0].setText("0%")
        self.button_sy[1].setText("10%")
        self.button_sy[2].setText("20%")
        self.button_sy[3].setText("30%")
        self.button_sy[4].setText("40%")
        self.button_sy[5].setText("50%")
        self.button_sy[6].setText("60%")
        self.button_sy[7].setText("70%")
        self.button_sy[8].setText("80%")
        self.button_sy[9].setText("90%")
        self.button_sy[10].setText("Autre")
        


        try:
            with open("data.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data_force=data['force']

            

            if (data_force)=='1':
                    self.button_sy[0].setCheckState(True)
                    self.button_sy[0].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

            if (data_force)!='1' and int(data_force)/10-int(int(data_force)/10)==0:
                    self.button_sy[int(int(data_force)/10)].setCheckState(True)
                    self.button_sy[int(int(data_force)/10)].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

            elif(data_force)!='1':
                    self.button_sy[10].setCheckState(True)
                    self.button_sy[10].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    self.sp.setValue(int(data_force))
        except:
            data_force=0



        self.button_sy[0].clicked.connect(lambda:self.fun(0))
        self.button_sy[1].clicked.connect(lambda:self.fun(1))
        self.button_sy[2].clicked.connect(lambda:self.fun(2))
        self.button_sy[3].clicked.connect(lambda:self.fun(3))
        self.button_sy[4].clicked.connect(lambda:self.fun(4))
        self.button_sy[5].clicked.connect(lambda:self.fun(5))
        self.button_sy[6].clicked.connect(lambda:self.fun(6))
        self.button_sy[7].clicked.connect(lambda:self.fun(7))
        self.button_sy[8].clicked.connect(lambda:self.fun(8))
        self.button_sy[9].clicked.connect(lambda:self.fun(9))
        self.button_sy[10].clicked.connect(lambda:self.fun(10))

        
        self.discrip=["discrrip1","discrrip2","discrrip3","discrrip4","discrrip5","discrrip6"]
                                          



  
        self.button_valid= QPushButton(self)        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(350,270)
        self.button_valid.clicked.connect(self.modif_boutton_Force)
        self.initUI()      
    def fun(self,i):

        touch_clavier(time_click)
        for k in range(11):
            if self.button_sy[i].isChecked()==1 and k!=i :                    
                self.button_sy[k].setCheckState(False)
                self.button_sy[k].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')                      
        self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
    def modif_boutton_Force(self):
            touch_clavier(time_save)
            try:
                    self.etas=[0,0,0,0,0,0,0,0,0,0,0]
                    for m in range (11):
                        self.etas[m]=self.button_sy[m].isChecked()

                    c = [1,10,20,30,40,50,60,70,80,90,100]
                    somm=0

                    for i in range(len(c)):
                        somm = somm+c[i]*self.etas[i]
                    if somm==100:
                        somm=self.sp.value()

                    self.etas.insert(11,self.sp.value())
                    self.main_f=configue_f()
                    self.signal3.connect(self.main_f.get_val_force)
                    self.signal3.emit(str(somm))
                    self.destroy()

                    
            except:
                print("o")
            #self.destroy()
    def initUI(self):    
        
        self.setGeometry(320, 140, 470, 320)  


        
        self.setWindowTitle('Configurations Force')    






class conf_Mode(QMainWindow):
    signal3=pyqtSignal(str)
    mode=0
    try:
            with open("data.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data_Infusion=data['infusion']
    except:
            data_Infusion="Infusion Continue"

                        
    def __init__(self):
        super().__init__()
        self.button_sy=[0,0,0,0,0,0]
        self.val_yb_sy=20
        serifFont = QFont("Times", 10, QFont.Bold)
        self.mode_matrix=["Infusion Continue",".....",".....",".....",".....","....."]
        for i in range(6):
                self.button_sy[i]= QPushButton(self)                
                self.button_sy[i].setFixedWidth(250)
                self.button_sy[i].setFixedHeight(40)
                self.button_sy[i].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.button_sy[i].move(20,self.val_yb_sy)
                self.val_yb_sy=self.val_yb_sy+50
                
        self.button_sy[0].setText("Infusion Continue")
        self.button_sy[1].setText(".....")
        self.button_sy[2].setText(".....")
        self.button_sy[3].setText(".....")
        self.button_sy[4].setText(".....")
        self.button_sy[5].setText(".....")


        self.button_sy[0].clicked.connect(lambda:self.fun(0))
        self.button_sy[1].clicked.connect(lambda:self.fun(1))
        self.button_sy[2].clicked.connect(lambda:self.fun(2))
        self.button_sy[3].clicked.connect(lambda:self.fun(3))
        self.button_sy[4].clicked.connect(lambda:self.fun(4))
        self.button_sy[5].clicked.connect(lambda:self.fun(5))
        self.button_sy[0].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.discrip=["discrrip1","discrrip2","discrrip3","discrrip4","discrrip5","discrrip6"]
                                          
        self.label_discrip=QtWidgets.QLabel(self)
        self.label_discrip.setFixedWidth(200)
        self.label_discrip.setFixedHeight(180)
        self.label_discrip.setText(str(self.discrip[0]))        
        self.label_discrip.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.label_discrip.move(270,80)
        

        self.button_valid= QPushButton(self)
        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(350,270)
        self.button_valid.clicked.connect(self.modif_boutton_mode)
        self.initUI()
        
    def fun(self,i):
        touch_clavier(time_click)
        for k in range(6):
                self.button_sy[k].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.mode=i
        self.label_discrip.setText(str(self.discrip[i]))
        self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       



    def modif_boutton_mode(self):
            touch_clavier(time_save)
            try:
                    self.main=Widget()
                    self.signal3.connect(self.main.getval_mode)
                    save_config("data.json","mode",str(self.mode_matrix[self.mode]))
                    self.signal3.emit(str(self.mode_matrix[self.mode]))
                    
                    
            except:
                print("o")
            self.destroy()
    def initUI(self):    
        
        self.setGeometry(320, 140, 470, 320)  


        
        self.setWindowTitle('Configurations Mode')    



class conf_volume(QMainWindow):
    signal4=pyqtSignal(str)
    sringue=1
    val_label_volume=0
    target=0
    val_total_unitee="0 ml"

                        
    def __init__(self):
        super().__init__()
        self.button_sy=[0,0,0,0,0,0]
        self.val_yb_sy=20
        serifFont = QFont("Times", 10, QFont.Bold)
        self.statupdat=1
        for i in range(2):
                self.button_sy[i]= QPushButton(self)                
                self.button_sy[i].setFixedWidth(150)
                self.button_sy[i].setFixedHeight(40)
                self.button_sy[i].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.button_sy[i].move(20,self.val_yb_sy)
                self.val_yb_sy=self.val_yb_sy+50
                
        self.label_v=QtWidgets.QLabel(self)
        self.label_v.setFixedWidth(100)
        self.label_v.setFixedHeight(40)
        self.label_v.setText(str("0"))        

        self.label_v.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.label_v.move(300,20)                
                
        self.button_sy[0].setText("Volume")
        self.button_sy[1].setText("temps")
        
        """self.setstr_fn = QtCore.QTimer(self)
        self.setstr_fn.timeout.connect(self.setstr)
        self.setstr_fn.start(1200)"""
        


        self.button_sy[0].clicked.connect(lambda:self.modif_volume_button(0))
        self.button_sy[1].clicked.connect(lambda:self.modif_volume_button(1))
        self.button_sy[0].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.discrip=["discrrip1","discrrip2","discrrip3","discrrip4","discrrip5","discrrip6"]
        self.unitee=["ml","s"]
                                          
        self.label_discrip=QtWidgets.QLabel(self)
        self.label_discrip.setFixedWidth(200)
        self.label_discrip.setFixedHeight(180)
        self.label_discrip.setText(str(self.discrip[0]))        
        self.label_discrip.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.label_discrip.move(220,80)
        

        self.button_valid= QPushButton(self)
        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(350,270)
        self.button_valid.clicked.connect(self.modif_boutton_target)
        self.initUI()
        
    def fun(self,i):
        touch_clavier(time_click)

        for k in range(2):
                self.button_sy[k].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.seringue=i+1
        self.label_discrip.setText(str(self.discrip[i]))
        self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
    def mouseMoveEvent(self, QMouseEvent):  
                self.label_v.setFixedWidth(len(str(conf_volume.val_label_volume))+3*60)
                conf_volume.val_total_unitee=str(conf_volume.val_label_volume)+" "+str(self.unitee[conf_volume.target])
                self.label_v.setText(conf_volume.val_total_unitee)
                


        
    
    def get_volume(self,volume_):

        conf_volume.val_label_volume=volume_


    def modif_volume_button(self,i):
        touch_clavier(time_click)
        self.statupdat=1

        
        conf_volume.target=i
        for k in range(2):
                self.button_sy[k].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.seringue=i+1
        self.label_discrip.setText(str(self.discrip[i]))
        self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

        
        view = PyCalav()
        view.show()
                    # Create instances of the model and the controller
        model = evaluateExpression
        PyCalavCtrl(model=model, view=view)

        


    def modif_boutton_target(self):
            touch_clavier(time_save)          
            try:
                    self.main=Widget()
                    conf_volume.val_total_unitee=str(conf_volume.val_label_volume)+" "+str(self.unitee[conf_volume.target])
                    self.signal4.connect(self.main.getval_target)
                    self.signal4.emit(str(conf_volume.val_total_unitee))

                    save_config("data.json","objectif",str(conf_volume.val_total_unitee))
                    
            except:
                print("o")
            self.destroy()
    def initUI(self):    
        
        self.setGeometry(320, 140, 470, 320)  


        
        self.setWindowTitle('Configurations volume')    



class conf_seringue(QMainWindow):
    signal2=pyqtSignal(str)
    sringue=1

                        
    def __init__(self):
        super().__init__()
        self.button_sy=[0,0,0,0,0,0]
        self.val_yb_sy=20
        serifFont = QFont("Times", 10, QFont.Bold)
        for i in range(6):
                self.button_sy[i]= QPushButton(self)                
                self.button_sy[i].setFixedWidth(150)
                self.button_sy[i].setFixedHeight(40)
                self.button_sy[i].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.button_sy[i].move(20,self.val_yb_sy)
                self.val_yb_sy=self.val_yb_sy+50
                
        self.button_sy[0].setText("10 mL")
        self.button_sy[1].setText("20 mL")
        self.button_sy[2].setText("30 mL")
        self.button_sy[3].setText("40 mL")
        self.button_sy[4].setText("50 mL")
        self.button_sy[5].setText("60 mL")


        self.button_sy[0].clicked.connect(lambda:self.fun(0))
        self.button_sy[1].clicked.connect(lambda:self.fun(1))
        self.button_sy[2].clicked.connect(lambda:self.fun(2))
        self.button_sy[3].clicked.connect(lambda:self.fun(3))
        self.button_sy[4].clicked.connect(lambda:self.fun(4))
        self.button_sy[5].clicked.connect(lambda:self.fun(5))
        self.button_sy[0].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.discrip=["discrrip1","discrrip2","discrrip3","discrrip4","discrrip5","discrrip6"]
                                          
        self.label_discrip=QtWidgets.QLabel(self)
        self.label_discrip.setFixedWidth(200)
        self.label_discrip.setFixedHeight(180)
        self.label_discrip.setText(str(self.discrip[0]))        
        self.label_discrip.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.label_discrip.move(220,80)
        

        self.button_valid= QPushButton(self)
        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(350,270)
        self.button_valid.clicked.connect(self.modif_boutton_seringue)
        self.initUI()
        
    def fun(self,i):
        touch_clavier(time_click)
        for k in range(6):
                self.button_sy[k].setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                self.seringue=i+1
        self.label_discrip.setText(str(self.discrip[i]))
        self.button_sy[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(12, 190, 245);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       



    def modif_boutton_seringue(self):
            touch_clavier(time_save)
            try:
                    self.main=Widget()
                    self.signal2.connect(self.main.getval_seringue)
                    self.signal2.emit(str(self.seringue*10))
                    save_config("data.json","seringue",str(self.seringue*10))
                    
            except:
                print("o")
            self.destroy()
    def initUI(self):    
        
        self.setGeometry(320, 140, 470, 320)  


        
        self.setWindowTitle('Configurations Seringue')    



class conf_debit(QMainWindow):
    signal=pyqtSignal(str)

                        
    def __init__(self):
        super().__init__()
        self.combo_text_poste="Jour"
        self.combo_text_machine="Totale"
        self.button_up=[0,0,0,0]
        self.button_down=[0,0,0,0]
        self.b_x=100
        self.y_b=190
        self.label=[0,0,0,0]
        self.x_l=110
        for i in range(4):
            
            
            self.label[i]=QtWidgets.QLabel(self)
            self.label[i].setFixedWidth(50)
            self.label[i].setFixedHeight(30)
            self.label[i].setText(str(i))

            self.label[i].setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.label[i].move(self.x_l,100)
            self.x_l=self.x_l+50

  



        
        self.labelv=QtWidgets.QLabel(self)
        self.labelv.setFixedWidth(10)
        self.labelv.setFixedHeight(30)
        self.labelv.setText(".")
        self.labelv.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.labelv.move(250,100)  



        for i in range(4):

            self.button_up[i] = QPushButton(self)
            

            self.button_up[i].setFixedWidth(40)
            self.button_up[i].setFixedHeight(40)
            self.button_up[i].setIcon(QtGui.QIcon('up.png'))
            self.button_up[i].setIconSize(QSize(30,30))

            self.button_up[i].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.button_up[i].move(self.b_x,150)
            self.b_x=self.b_x+55
        self.b_x=100

        self.button_up[0].clicked.connect(lambda:up(self.label[0].text(),self.label[0]))
        self.button_up[1].clicked.connect(lambda:up(self.label[1].text(),self.label[1]))
        self.button_up[2].clicked.connect(lambda:up(self.label[2].text(),self.label[2]))
        self.button_up[3].clicked.connect(lambda:up(self.label[3].text(),self.label[3]))
       
        for j in range(4):

            self.button_down[j] = QPushButton(self)

            self.button_down[j].setFixedWidth(40)
            self.button_down[j].setFixedHeight(40)
            self.button_down[j].setIcon(QtGui.QIcon('down.png'))
            self.button_down[j].setIconSize(QSize(30,30))            
            self.button_down[j].setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.button_down[j].move(self.b_x,200)
            self.b_x=self.b_x+55
            
        self.button_down[0].clicked.connect(lambda:down(self.label[0].text(),self.label[0]))
        self.button_down[1].clicked.connect(lambda:down(self.label[1].text(),self.label[1]))
        self.button_down[2].clicked.connect(lambda:down(self.label[2].text(),self.label[2]))
        self.button_down[3].clicked.connect(lambda:down(self.label[3].text(),self.label[3]))
        self.button_valid= QPushButton(self)
        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_valid.move(330,190)
        self.button_valid.clicked.connect(self.modif_boutton)
        self.initUI()        


    def modif_boutton(self):
            touch_clavier(time_save)
            self.main=Widget()
            self.signal.connect(self.main.getval)
            self.signal.emit(str(self.label[0].text()+self.label[1].text()+self.label[2].text()+"."+self.label[3].text()))
            save_config("data.json","debit",str(self.label[0].text()+self.label[1].text()+self.label[2].text()+"."+self.label[3].text()))
            self.destroy()

        
    def initUI(self):    
        
        self.setGeometry(320, 180, 470, 270)  


        
        self.setWindowTitle('Configurations debit')    

class Widget(QWidget):
    
    x1=0
    y_batt=0
    use_bat=0
    p_seringue=0
    pression=0
    enregistrer_pression=0
    enregistrer_Debit=0
    enregistrer_seringue=0
    enregistrer_Mode=0
    enregistrer_objectif=0

    typ_seringue=20
    debit=20
    force_=0
    objectif="0 ml"
    alarm_etat=1
    flag_etat_alarm=1
    max_sering_force=[50,10,200,300,400,500,600]
    name_sering=[0,10,20,30,40,50,60]
    time_alarme="0"
    flag_alarm_force=0
    flag_alarm_sering=0
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Vous voulez vraiment quitter l'application ?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
    
    starttime=time.time()
    try:
            with open("data.json", "r") as jsonFile:
                data = json.load(jsonFile)
            val_mode=data['mode']
            val_label1=data['debit']
            val_label2=data['seringue']
            MIN_pression=float((data['pression'].split(','))[0])
            Max_pression=float((data['pression'].split(','))[1])
            label_volume=data['objectif']

            initial_alarme=data['alarme'].split('[')        
            initial_alarme=initial_alarme[1].split(']')
            data_initial_alarme=initial_alarme[0].split(', ')


            
            initial_sound_alarme=data['list_alarm']
            a=initial_sound_alarme.split('[')[1]
            b=a.split(']')[0]
            c=b.split("'")
            initial_sound_alarme=[c[1],c[3],c[5],c[7],c[9],c[11]]
            
    except:

        val_mode="Infusion Continue"
        val_label1=10
        val_label2=10
        Max_pression=100
        MIN_pression=0
        label_volume="Totale"

            
    
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        #pic = QLabel(self)
        #pic.setGeometry(350, 30, 400, 100)
        #pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/seringue.png"))




       
        self.currentWidgetRightFrame = 0
        self.current_st1=1
        self.current_st2=1
        self.current_st3=1
        self.current_st4=1
        self.arret_manq_time=0
        self.arret_reglage_time=0
        self.arret_panne_time=0
        self.arret_autres_time=0

        self.tag_bobin=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.num_bobine_num=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.value=0
        self.list_val=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


        self.resize(703, 350)
        self.initUI()
        self.num=1
        self.val=0
        self.pos=0
        self.intrface=1
        self.HLayout=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.VLayout=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.lb1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.lb2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]        
        self.draw_layout()
        self.togle=0
        self.etat=0
        
        

    def initUI(self):
        self.num=1
        self.val=0
        self.pos=0
        self.intrface=1
        self.RoundBar_list=[]
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
        timer.start(500)


        alarm_start = QtCore.QTimer(self)
        alarm_start.timeout.connect(self.alarmStart)
        alarm_start.start(5000)
        
        
        drow_rect = QtCore.QTimer(self)
        drow_rect.timeout.connect(lambda:self.up_rect(Widget.x1))
        drow_rect.start(1500)

        read_line_val = QtCore.QTimer(self)
        read_line_val.timeout.connect(self.read_line)
        read_line_val.start(1000)

        delaysecond_time = QtCore.QTimer(self)
        delaysecond_time.timeout.connect(self.delaysecond)
        delaysecond_time.start(1100)

        
        self.setGeometry(0,45,810,415)
        self.setWindowTitle("Seringue")
        self.setWindowIcon(QtGui.QIcon(""))
        self.state1 = False;self.state2 = False;self.state3 = False;self.state4 = False
        self.state5 = False;self.state6 = False;self.state7 = False;self.state8 = False
        self.state9 = False;self.state10 = False;self.state11 = False;self.state12 = False
        self.state13 = False;self.state14 = False;self.state15 = False;self.state16 = False


        
        self.pattern = '{0:02d}:{1:02d}'
        self.reeltimeText=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.reeltimeText.move(400,5)
        self.reeltimeText.resize(100,45)
        self.reeltimeText.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        
        self.pourcent=QtWidgets.QLabel(self)
        self.pourcent.move(570,82)
        self.pourcent.setStyleSheet('color: rgb(10, 150, 255);font: 10pt Helvetica MS;')
        self.pourcent.resize(45,18)
        
        self.pourcent_bat=QtWidgets.QLabel(self)
        self.pourcent_bat.move(650,45)
        self.pourcent_bat.setStyleSheet('color: rgb(10, 150, 255);font: 10pt Helvetica MS;')
        self.pourcent_bat.resize(45,18)
        
        self.lab_time_rest=QtWidgets.QLabel(self)
        self.lab_time_rest.move(230,310)
        self.lab_time_rest.setStyleSheet('color: rgb(10, 150, 255);font: 15pt Helvetica MS;')
        self.lab_time_rest.resize(200,20)
        
        self.lab_P=QtWidgets.QLabel(self)
        self.lab_P.move(410,120)
        self.lab_P.setStyleSheet('color: rgb(10, 150, 255);font: 35pt Helvetica MS;')
        self.lab_P.resize(30,40)
        self.lab_P.setText("P")

        self.lab_Pression=QtWidgets.QLabel(self)
        self.lab_Pression.move(450,130)
        self.lab_Pression.setStyleSheet('color: rgb(10, 150, 255);font: 15pt Helvetica MS;')
        self.lab_Pression.resize(60,40)

        self.temp_ecoule_champs=QtWidgets.QLabel(self)
        self.temp_ecoule_champs.setFixedWidth(250)
        self.temp_ecoule_champs.setFixedHeight(38)
        self.temp_ecoule_champs.setStyleSheet('color: rgb(10, 150, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.temp_ecoule_champs.move(230,270)
        self.temp_ecoule_champs.setText("00:00:00")




        self.lab_erreur_force=QtWidgets.QLabel(self)
        self.lab_erreur_force.setText("Force :                   ") 

        self.lab_erreur_force.setFixedWidth(240)
        self.lab_erreur_force.setFixedHeight(30)
        self.lab_erreur_force.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(102, 178, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.lab_erreur_force.move(400,200)
        
        self.lab_erreur_seringue=QtWidgets.QLabel(self)
        self.lab_erreur_seringue.setText("Seringue:                       ")
        self.lab_erreur_seringue.setFixedWidth(240)
        self.lab_erreur_seringue.setFixedHeight(30)
        self.lab_erreur_seringue.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(102, 178, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.lab_erreur_seringue.move(400,230)
        



        
        
        
        self.v_inf_champ=QtWidgets.QLabel(self)
        self.v_inf_champ.setFixedWidth(100)
        self.v_inf_champ.setFixedHeight(38)
        self.v_inf_champ.setText("2.67")
        self.v_inf_champ.setStyleSheet('color: rgb(10, 150, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.v_inf_champ.move(230,360)

        self.label1=QtWidgets.QLabel(self)
        

                 

    def paintEvent(self,e):
        painter = QPainter(self)
        if Widget.p_seringue==0:
                painter.setPen(QPen(QtGui.QColor(self.togle*255,0,0), 5, Qt.SolidLine))
        ##################################################
                painter.drawRect(450, 60, 100,30)
                painter.drawRect(550, 70, 20,10)         
                painter.drawRect(430-Widget.x1, 75, 120,1)
                
                painter.drawRect(430-Widget.x1, 60, 1,30)

                painter.setPen(QPen(QtGui.QColor(0,0,0), 2, Qt.SolidLine))

                if Widget.y_batt*3.3<=100 and Widget.use_bat==1:                
                        painter.drawRect(700, 40, 21,30)        
                        painter.drawRect(709, 38, 3,2)
                        
                painter.setPen(QPen(QtGui.QColor(self.togle*255,0,0), 2, Qt.SolidLine))                        
                painter.drawRect(570, 75, 40,1)
                painter.setPen(QPen(QtGui.QColor(self.togle*255,0,0), 2, Qt.SolidLine))         
                fill = QtGui.QBrush(QtGui.QColor(self.togle*255,0,0))
                painter.setBrush(fill)         
                painter.drawRect(550-Widget.x1, 60, (Widget.x1),30)
                painter.drawRect(570, 50, 25, 15)  
                
#############################################################################
        else:
                painter.setPen(QPen(QtGui.QColor(0,0,0), 5, Qt.SolidLine))
                painter.drawRect(450, 60, 100,30)
                painter.drawRect(550, 70, 20,10)

                
                painter.drawRect(430-Widget.x1, 75, 120,1)
                
                painter.drawRect(430-Widget.x1, 60, 1,30)

                painter.setPen(QPen(QtGui.QColor(0,0,0), 2, Qt.SolidLine))
                if Widget.y_batt*3.3<=100 and Widget.use_bat==1:                
                        painter.drawRect(700, 40, 21,30)        
                        painter.drawRect(709, 38, 3,2) 
                
                painter.drawRect(570, 75, 40,1)
                painter.setPen(QPen(QtGui.QColor(0,0,0), 2, Qt.SolidLine))
                
              
                if 10>(Widget.x1) and Widget.p_seringue==1 :
                        fill = QtGui.QBrush(QtGui.QColor(250*self.togle,0,0))
                        
                else:
                        fill = QtGui.QBrush((QtGui.QColor(0,225,0)))




                painter.setBrush(fill) 
                painter.drawRect(570, 50, 25, 15)    

                fill = QtGui.QBrush(QtGui.QColor((100-(Widget.x1))*2.55,(Widget.x1)*2.55,0))

                if 60>(Widget.x1)>30:
                        fill = QtGui.QBrush(QtGui.QColor(250,250,10))
                painter.setBrush(fill)         
                painter.drawRect(550-Widget.x1, 60, (Widget.x1),30)
                
                


                
#############################################################################
 
        fill = QtGui.QBrush(QtGui.QColor((100-Widget.y_batt*3.3)*2.5,Widget.y_batt*3.3*2.55,0))
        
        painter.setBrush(fill)  
      
        painter.setPen(QPen(QtGui.QColor(0,0,0), 2, Qt.SolidLine))
       
        if Widget.y_batt*3.3<=100 and Widget.use_bat==1:
                painter.drawRect(700, 70-Widget.y_batt, 21,Widget.y_batt)      

        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        
        if float(Widget.Max_pression)> float(Widget.pression) >float(Widget.MIN_pression) and Widget.enregistrer_pression==1 :
            

                painter.setBrush(QtGui.QBrush(QtGui.QColor(0,255,0)))
        else:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(255*self.togle,0,0)))

        painter.drawEllipse(550,120, 60,60)
        
        if Widget.use_bat==0:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(255,255,0)))
                painter.setPen(QPen(QtGui.QColor(0,0,0), 2, Qt.SolidLine))

                painter.drawRect(705, 25, 1,9)
                painter.drawRect(716, 25, 1,9)
                painter.drawRect(700, 34, 21,4)
                painter.drawRect(704, 38, 13,8)
                painter.drawRect(710, 46, 1,9)



    def Arret_alarm_f(self):
        touch_clavier(time_click)
        if Widget.alarm_etat==1:
            Widget.alarm_etat=0
            self.Arret_alarm.setIcon(QtGui.QIcon('silencieux.png'))
            self.Arret_alarm.setIconSize(QSize(100,100))
            print("1 #########")
            
        else:
            print("2 ##############")
            Widget.alarm_etat=1
            self.Arret_alarm.setIcon(QtGui.QIcon('alarme.png'))
            self.Arret_alarm.setIconSize(QSize(50,50))            
            
    def alarmStart(self):
        initial_alarme_state=[True,False,False,False,False,False]

        
        try:

            
                with open("data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                initial_alarme=data['alarme'].split('[')        
                initial_alarme=initial_alarme[1].split(']')
                data_initial_alarme=initial_alarme[0].split(', ')
                data_initial_debit=data['debit']

                initial_mov_alarme=data['mov']
                initial_force_alarme=data['force']
                
                initial_sound_alarme=data['list_alarm']
                a=initial_sound_alarme.split('[')[1]
                b=a.split(']')[0]
                c=b.split("'")
                initial_sound_alarme=[c[1],c[3],c[5],c[7],c[9],c[11]]
                for i in range (6):
                        
                    if data_initial_alarme[i]=='True':
                        initial_alarme_state[i]=True
                        
                    if data_initial_alarme[i]=='False':
                        initial_alarme_state[i]=False
                
        except:
            initial_force_alarme=0
            initial_mov_alarme=0
            initial_alarme_state=[True,False,False,False,False,False]
            initial_sound_alarme=['0035.wav', '0035.wav', 'School_Fire_Alarm-Cullen_Card-202875844.wav', '0035.wav', 'Tornado_Siren_II-Delilah-747233690.wav', ' ']

        try:
            max_sering= Widget.max_sering_force[Widget.name_sering.index(int(Widget.typ_seringue))]
        except:
            max_sering=1000
            print("err9")
        print("sering",Widget.force_ , max_sering + (int(initial_force_alarme)*max_sering)/100)
        if Widget.force_ >= max_sering + (int(initial_force_alarme)*max_sering)/100 and Widget.enregistrer_seringue:
            print("alarm")
            pygame.mixer.init()
            pygame.mixer.music.load("Nouveau1/analog-watch-alarm_daniel-simion.wav")
            pygame.mixer.music.play()
            self.lab_erreur_force.setText("Force : "+str(Widget.force_)+" Erreur ")
            self.lab_erreur_force.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(102, 178, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            Widget.flag_alarm_force  += 1
            if Widget.flag_alarm_force==1:
                save_config("datamarche_arret.json",str(datetime.datetime.now()),'erreur Force')
                
                Widget.val_label1=str(float(data_initial_debit)*int(initial_mov_alarme)/100)

                val="c"
                v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+","+str(Widget.label_volume)+","+val+','+str('*'))
                ard.write(v1.encode("utf-8"))

                


        if Widget.force_ <= max_sering + (int(initial_force_alarme)*max_sering)/100 and Widget.enregistrer_seringue:
            pygame.mixer.music.stop()
            Widget.flag_alarm_force=0
            self.lab_erreur_force.setText("Force : "+ str(Widget.force_))
            self.lab_erreur_force.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(102, 178, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       


        if (Widget.force_ <= max_sering + (int(initial_force_alarme)*max_sering)/100 and  Widget.x1 >= int(initial_mov_alarme)) and Widget.enregistrer_seringue:

            Widget.val_label1=str(data['debit'])
            val="c"
            v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+","+str(Widget.label_volume)+","+val+','+str('*'))
            ard.write(v1.encode("utf-8"))


            

        print("sering",Widget.x1)
        if Widget.x1<= int(initial_mov_alarme) and Widget.enregistrer_seringue:
            
            print("alarm_sering")
            if initial_alarme_state[1]==True:
                pygame.mixer.init()
                pygame.mixer.music.load("Nouveau1/"+initial_sound_alarme[0])
                pygame.mixer.music.play()
            self.lab_erreur_seringue.setText("Seringue: "+str(Widget.x1)+"% Erreur ")
            self.lab_erreur_seringue.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(102, 178, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            Widget.flag_alarm_sering  += 1
            if Widget.flag_alarm_sering==1:
                save_config("datamarche_arret.json",str(datetime.datetime.now()),'erreur Seringue')
                
                Widget.val_label1=str(float(data_initial_debit)*int(initial_mov_alarme)/100)

                val="c"
                v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+","+str(Widget.label_volume)+","+val+','+str('*'))
                ard.write(v1.encode("utf-8"))


        if Widget.x1 >= int(initial_mov_alarme) and Widget.enregistrer_seringue:
            pygame.mixer.music.stop()
            Widget.flag_alarm_sering=0
            self.lab_erreur_seringue.setText("Seringue: "+str(Widget.x1)+" % ")
            self.lab_erreur_seringue.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(102, 178, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

        if Widget.alarm_etat==0:
            pygame.mixer.music.stop()
        if initial_alarme_state[0]==True:
            pygame.mixer.music.stop()

        
    def up_rect(self,x):
        Widget.x1=x
        self.update()

    def read_line(self):
        try:    
                se_charg=ard.readline(ard.inWaiting())

                se_charg=str(se_charg).split("'")

                print(se_charg[1])
                se=se_charg[1].split(',')[0]
                charge=se_charg[1].split(',')[1]
                use_bat=se_charg[1].split(',')[2]
                p_sering=se_charg[1].split(',')[3]
                pression=se_charg[1].split(',')[4]

                typ_sering=se_charg[1].split(',')[5]
                debit=se_charg[1].split(',')[6]
                objectif=se_charg[1].split(',')[7]
                force=se_charg[1].split(',')[8]
                
                
                Widget.y_batt=float(charge)*30/100
                Widget.x1=float(se)
                Widget.use_bat=int(use_bat)
                Widget.p_seringue=int(p_sering)
                Widget.pression=float(pression)
                
                Widget.typ_seringue=int(typ_sering)
                Widget.debit=float(debit)
                Widget.objectif=str(objectif)
                Widget.force_=int(force)
                


        except:
                print("err6")
        


    def Time(self):
            self.reeltimeText.setText(strftime("%H"+":"+"%M"+":"+"%S"))
                              
            
            self.l_mode.setText(str(Widget.val_mode))
            if self.etat==1:
                    minttime=(time.time()-Widget.starttime)/60
                    temph_s_m = str(datetime.timedelta(minutes=minttime))
                    self.temp_ecoule_champs.setText(temph_s_m.split('.')[0])
            
            self.pourcent.setText(str((Widget.x1))+"%")
            
            try:

                    if str(Widget.label_volume).split(" ")[1]=="ml":
                        self.l_volume.setText("    "+str(Widget.label_volume))
                        
                    if str(Widget.label_volume).split(" ")[1]=="s":                                
                                temp=((float(str(Widget.label_volume).split(" ")[0]))/60)
                                result = str(datetime.timedelta(minutes=temp))
                                self.lab_time_rest.setText(result.split('.')[0])
                                self.l_volume.setText("    "+result.split('.')[0])

                                
                        
                
                    if Widget.y_batt*3.3<=100 and Widget.use_bat==1:
                            self.pourcent_bat.setText(str((Widget.y_batt*100/30))+"%")
                    else:
                             self.pourcent_bat.setText("        ")
                    if int(Widget.typ_seringue)==int(Widget.val_label2) and Widget.enregistrer_seringue:
                            self.label2.setStyleSheet('color: rgb(0, 255, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    if int(Widget.typ_seringue)!=int(Widget.val_label2) or not Widget.enregistrer_seringue:
                            self.label2.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    
                    if float(Widget.debit)==float(Widget.val_label1):
                            self.label1.setStyleSheet('color: rgb(0, 255, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    if float(Widget.debit)!=float(Widget.val_label1):
                            self.label1.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                

                    if (Widget.objectif)==(Widget.label_volume):
                            self.l_volume.setStyleSheet('color: rgb(0, 255, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    if (Widget.objectif)!=(Widget.label_volume):
                            self.l_volume.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

                            
                    
                    if  Widget.enregistrer_Debit and Widget.enregistrer_seringue and Widget.enregistrer_objectif:
                            obj=Widget.objectif.split(" ")[0]
                            if Widget.objectif.split(" ")[1]=="ml":                                
                                temp=((float(obj)/float(Widget.val_label1))*60)
                                temp_rest=(temp*float(Widget.x1))/100
                                result = str(datetime.timedelta(minutes=temp_rest))
                                self.lab_time_rest.setText(result.split('.')[0])
                                self.v_inf_champ.setText(str(float(obj)-(Widget.x1*float(obj))/100)+" ml")

                                
                            if Widget.objectif.split(" ")[1]=="s":                                
                                temp=((float(obj))/60)
                                result = str(datetime.timedelta(minutes=temp))
                                self.lab_time_rest.setText(result.split('.')[0])
                                self.v_inf_champ.setText(str(Widget.typ_seringue-(Widget.x1*Widget.typ_seringue)/100)+" ml")



                    self.label1.setText("    "+str(Widget.val_label1)+" mL/H")
                    self.label2.setText("    "+str(Widget.val_label2)+" mL")
                    self.labelmax_pression.setText("    "+str(Widget.MIN_pression)+"==>"+str(Widget.Max_pression))
                    self.lab_Pression.setText(str(Widget.pression))
                    

            except:
                        print("errtime")
            
    def delaysecond(self):
            if self.togle==1:
                 self.togle=0
            else:
                self.togle=1
        
        
    def draw_layout(self):
        main_layout = QHBoxLayout(self) 
        #create frame of main tab 
        tab_layout = QHBoxLayout()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)

        self.setStyleSheet(" background-color: rgb(204, 204, 255); ")

        #les boutons


        self.button3 = QPushButton(self)
        #self.button3.setText('Enregistrer')
        self.button3.setIcon(QtGui.QIcon('enregistrer.png'))
        self.button3.setIconSize(QSize(100,100))
        self.button3.setFixedWidth(60)
        self.button3.setFixedHeight(60)
        self.button3.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button3.clicked.connect(self.Enregistrer)
        self.button3.move(720,360)
        self.Arret_alarm = QPushButton(self)
        self.Arret_alarm.setIcon(QtGui.QIcon('alarme.png'))
        self.Arret_alarm.setIconSize(QSize(50,50))

        self.Arret_alarm.setFixedWidth(60)
        self.Arret_alarm.setFixedHeight(60)
        self.Arret_alarm.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.Arret_alarm.clicked.connect(self.Arret_alarm_f)
        self.Arret_alarm.move(720,280)        

        self.b_mode = QPushButton(self)
        self.b_mode.setText('Mode')

        self.b_mode.setFixedWidth(100)
        self.b_mode.setFixedHeight(40)
        self.b_mode.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.b_mode.clicked.connect(self.config_Mode)
        self.b_mode.move(10,20)        
        self.l_mode=QtWidgets.QLabel(self)
        self.l_mode.setFixedWidth(200)
        self.l_mode.setFixedHeight(38)
        self.l_mode.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.l_mode.move(110,21)
        self.l_mode.setText("Infusion Continue")




        self.button1 = QPushButton(self)
        self.button1.setText('Debit')
        self.button1.setFixedWidth(100)
        self.button1.setFixedHeight(40)
        self.button1.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button1.clicked.connect(self.config_debit)
        self.button1.move(10,70)        

        self.label1.setFixedWidth(200)
        self.label1.setFixedHeight(38)
        self.label1.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.label1.move(110,71)        



        self.button2 = QPushButton(self)
        self.button2.setText('Seringue')

        self.button2.setFixedWidth(100)
        self.button2.setFixedHeight(40)
        self.button2.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button2.clicked.connect(self.config_seringue)
        self.button2.move(10,120)        


        self.label2=QtWidgets.QLabel(self)
        self.label2.setFixedWidth(200)
        self.label2.setFixedHeight(38)
        self.label2.setText("              10")
        self.label2.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.label2.move(110,121)   

        self.volume = QPushButton(self)
        self.volume.setText('Objectif')

        self.volume.setFixedWidth(100)
        self.volume.setFixedHeight(40)
        self.volume.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.volume.clicked.connect(self.config_volume)
        self.volume.move(10,170)   

        self.l_volume=QtWidgets.QLabel(self)
        self.l_volume.setFixedWidth(200)
        self.l_volume.setFixedHeight(38)
        self.l_volume.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.l_volume.move(110,171)     

     




        self.button4 = QPushButton(self)
        self.button4.setText('Pression')

        self.button4.setFixedWidth(100)
        self.button4.setFixedHeight(40)
        self.button4.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button4.clicked.connect(self.config_pression)
        self.button4.move(10,220)
        
        self.labelmax_pression=QtWidgets.QLabel(self)
        self.labelmax_pression.setFixedWidth(200)
        self.labelmax_pression.setFixedHeight(38)
        self.labelmax_pression.setText(" 0 ")
        self.labelmax_pression.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.labelmax_pression.move(110,221)     

        self.run = QPushButton(self)                
        self.run.clicked.connect(self.demarrer)
        self.run.setFixedWidth(65)
        self.run.setFixedHeight(60)
        self.run.move(650,360)
        self.run.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(0, 255, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.run.setIcon(QtGui.QIcon('marche.png'))
        self.run.setIconSize(QSize(100,100))




        self.guche = QPushButton(self)        
        self.guche.clicked.connect(self.gauche_f)
        self.guche.setFixedWidth(60)
        self.guche.setFixedHeight(60)
        self.guche.move(400,350)
        self.guche.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.guche.setIcon(QtGui.QIcon('left.png'))
        self.guche.setIconSize(QSize(100,100))


        self.droite = QPushButton(self)        
        self.droite.clicked.connect(self.droite_f)
        self.droite.setFixedWidth(60)
        self.droite.setFixedHeight(60)
        self.droite.move(480,350)
        self.droite.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.droite.setIcon(QtGui.QIcon('right.png'))
        self.droite.setIconSize(QSize(100,100))

        self.configue = QPushButton(self)        
        self.configue.clicked.connect(self.configue_f)
        self.configue.setFixedWidth(60)
        self.configue.setFixedHeight(60)
        self.configue.move(650,280)
        self.configue.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.configue.setIcon(QtGui.QIcon('configuration.png'))
        self.configue.setIconSize(QSize(60,60))
        



        self.labeltem_passe=QtWidgets.QLabel(self)
        self.labeltem_passe.setFixedWidth(200)
        self.labeltem_passe.setFixedHeight(38)
        self.labeltem_passe.setText(" Temps écoulé: ")
        self.labeltem_passe.setStyleSheet('color: rgb(10, 150, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.labeltem_passe.move(10,270)
        
        self.labeltem_restant=QtWidgets.QLabel(self)
        self.labeltem_restant.setFixedWidth(160)
        self.labeltem_restant.setFixedHeight(38)
        self.labeltem_restant.setText(" Temps restant: ")
        self.labeltem_restant.setStyleSheet('color: rgb(10, 150, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.labeltem_restant.move(10,300) 

        self.etat=QtWidgets.QLabel(self)
        self.etat.setFixedWidth(200)
        self.etat.setFixedHeight(38)
        self.etat.setText(" Etat actuel: ")
        self.etat.setStyleSheet('color: rgb(10, 150, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.etat.move(10,330)
        
        self.volume_totale_infu=QtWidgets.QLabel(self)
        self.volume_totale_infu.setFixedWidth(200)
        self.volume_totale_infu.setFixedHeight(38)
        self.volume_totale_infu.setText(" Volume infusionné: ")
        self.volume_totale_infu.setStyleSheet('color: rgb(10, 150, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.volume_totale_infu.move(10,360) 



        self.eta_actuel=QtWidgets.QLabel(self)
        self.eta_actuel.setFixedWidth(100)
        self.eta_actuel.setFixedHeight(38)
        self.eta_actuel.setStyleSheet('color: rgb(255, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.eta_actuel.move(230,330)
        self.eta_actuel.setText("Arret")



        
        
        main_layout.addLayout(tab_layout, 1)

        #draw left frame
        self.setLayout(main_layout)


    def configue_f(self):
        touch_clavier(time_click)
        self.configue_ff=configue_f()
        self.configue_ff.show()
    def droite_f(self):
        touch_clavier(time_click)
        try:
                    val="A"
                    v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+","+str(Widget.label_volume)+","+val+','+str('+'))
                    ard.write(v1.encode("utf-8"))
        except:
            print("err15")
    def gauche_f(self):
        touch_clavier(time_click)
        try:
                    val="A"
                    v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+","+str(Widget.label_volume)+","+val+','+str('-'))
                    ard.write(v1.encode("utf-8"))    
        except:
            print("err16")
    def demarrer(self):
        
        try:
            print(self.etat)            
            if self.etat==0:
                    March_alarm(80)
                    val="M"
                    v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+","+str(Widget.label_volume)+","+val)
                    ard.write(v1.encode("utf-8"))
                    self.etat=1
                    self.run.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    self.run.setIcon(QtGui.QIcon('arret.png'))
                    self.run.setIconSize(QSize(100,100))
                    self.eta_actuel.setText('Marche')
                    self.eta_actuel.setStyleSheet('color: rgb(0, 255, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    Widget.starttime=time.time()
                    save_config("datamarche_arret.json",str(datetime.datetime.now()),'Marche')
                    
                    

            else:
                    val="A"
                    v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+","+str(Widget.label_volume)+","+val)
                    ard.write(v1.encode("utf-8"))
                    self.etat=0
                    self.run.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(0, 255, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    self.run.setIcon(QtGui.QIcon('marche.png'))
                    self.run.setIconSize(QSize(100,100))
                    self.eta_actuel.setText('Arret')
                    self.eta_actuel.setStyleSheet('color: rgb(255, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
                    save_config("datamarche_arret.json",str(datetime.datetime.now()),'Arret')

        except:
            print("err13")
                    
    def getval(self,val):
            Widget.val_label1=(str(float(val)))

    def getval_presion(self,MIN,MAX):
            
            Widget.Max_pression=((float(MAX)))
            Widget.MIN_pression=((float(MIN)))
            

            
    def getval_seringue(self,val):
            
            Widget.val_label2=(str((val)))

    def getval_target(self,val):
           
            Widget.label_volume=val

            
    def getval_mode(self,modeval):
            
            Widget.val_mode=(str((modeval)))

    def config_Mode(self):
        touch_clavier(time_click)
        self.config_Mode=conf_Mode()
        Widget.enregistrer_Mode=0
        self.config_Mode.show()
        self.l_mode.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       



            
    def config_seringue(self):
        touch_clavier(time_click)
        self.config_seringu=conf_seringue()
        Widget.enregistrer_seringue=0
        self.config_seringu.show()
        self.label2.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       


    def config_volume(self):
        touch_clavier(time_click)
        Widget.enregistrer_objectif=0
        self.config_volume=conf_volume()       
        self.config_volume.show()


    def config_pression(self):
        touch_clavier(time_click)
        self.conf_debit=conf_pression()
        Widget.enregistrer_pression=0
        self.labelmax_pression.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       

        self.conf_debit.show()
        
        
    def config_debit(self):
        touch_clavier(time_click)
        self.conf_debit=conf_debit()
        Widget.enregistrer_Debit=0
        self.label1.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.conf_debit.show()
        

    def Enregistrer(self):
        
        touch_clavier(time_save)
        try:
            if str(Widget.label_volume).split(" ")[1]=="ml":
                if int(str(Widget.label_volume).split(" ")[0])> int(Widget.val_label2):
                    
                    Widget.enregistrer_seringue=0
                    Widget.enregistrer_objectif=0
                else:
                    v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+','+str(Widget.label_volume))#debit,seringue, objectif(ml/s)            
                    ard.write(v1.encode("utf-8"))
                    Widget.enregistrer_pression=1
                    Widget.enregistrer_Debit=1
                    Widget.enregistrer_seringue=1
                    Widget.enregistrer_objectif=1
            else:
                    v1=str(str(Widget.val_label1)+","+str(Widget.val_label2)+','+str(Widget.label_volume))#debit,seringue, objectif(ml/s)            
                    ard.write(v1.encode("utf-8"))
                    Widget.enregistrer_pression=1
                    Widget.enregistrer_Debit=1
                    Widget.enregistrer_seringue=1
                    Widget.enregistrer_objectif=1                

            self.labelmax_pression.setStyleSheet('color: rgb(0, 255, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
            self.l_mode.setStyleSheet('color: rgb(0, 255, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        except:
            print("err12")


if __name__ == "__main__":
    import sys  
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = Widget()
    w.show()
    sys.exit(app.exec_())



    
