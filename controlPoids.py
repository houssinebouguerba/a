
from PyQt5.QtWidgets import QLineEdit,QDialogButtonBox,QFormLayout,QDialog,QMessageBox
from PyQt5 import QtWidgets,QtChart
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from pyqt_led import Led
from QLed import QLed
import sys
from subprocess import call
from time import sleep
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets                     # uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QCalendarWidget, QPushButton, QWidget,
                             QLabel, QVBoxLayout,QMessageBox)              # +++
import time
from functools import partial
import datetime
from PyQt5.QtCore import QDir, Qt, QUrl
#from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
#from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon
#from pyqtgraph import PlotWidget, plot
import numpy as np
from time import strftime

import matplotlib

from matplotlib import pyplot as plt
from datetime import date, timedelta
import calendar
from PyQt5.QtCore import QDateTime, Qt            # +++

       
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import RPi.GPIO as GPIO  # import GPIO
import statistics as stat
from hx711 import HX711
import json
########import bib######################################
vane1=3
vane2=17
arret_urgence=27
start=22
GPIO.setmode(GPIO.BCM) 
GPIO.setup(vane1,GPIO.OUT)
GPIO.setup(vane2,GPIO.OUT)
GPIO.setup(arret_urgence,GPIO.IN)
GPIO.setup(start,GPIO.IN)
############Gpio Raspberry##############################

cal=5 #nombre des échantillons (rapidité et précision )
def save_config(file,parametre,value_save):# enregistrer les données dans un fichier json

                    with open(file, "r") as jsonFile:
                        data = json.load(jsonFile)                    
                    data[parametre] = str(value_save)

                    with open(file, "w") as jsonFile:
                        json.dump(data, jsonFile)
                    jsonFile.close()
                    
                    
try:
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    # Create an object hx which represents your real hx711 chip
    # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
    hx = HX711(dout_pin=21, pd_sck_pin=20)
    err = hx.zero()
    # measure tare and save the value as offset for current channel
    # and gain selected. That means channel A and gain 128
    with open("configPoids.json", "r") as jsonFile:
        data = json.load(jsonFile)
    Ratio=data['Ratio']
    set_val=int(data['set'])
    pre_set_val=int(data['preset'])
    print(set_val,pre_set_val)
    hx.set_scale_ratio(float(Ratio))  # set ratio for current channel

    
    
    
except Exception as k :
    print(k)





class calibration(QMainWindow):
    signal=pyqtSignal(int)

    def closeEvent(self, event):
        self.retour()
        event.accept()

    def __init__(self):
        super().__init__()        
       
        self.initUI()
        self._connectSignals()

       
    def initUI(self):
        self.setStyleSheet(" background-color: rgb(0, 128, 255); ")
        self.champs=0
        self.reading=1
        self.buttons = {}
        self.buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
           
            
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            
            "C": (3, 1),
            "0": (3, 0),
            "Esp": (3, 2),
            
        }       
       
        self.setGeometry(0, -1, 800, 480)# Geometry ,emplacement
        self.set_line_calibration = QtWidgets.QLineEdit()# champ de text calibration 
        self.set_line_calibration.setEchoMode(0)
        self.set_line_calibration.setMaxLength(4)
        #self.set_line_calibration.setFixedWidth(50)
        self.set_line_calibration.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.set_line.setFixedSize(85, 20)
        #self.set_line.setMaxLength(20)
        self.set_line_calibration.mousePressEvent=self.getval #appel clavier 

       
        self.set=QtWidgets.QLabel("Masse (g)  :",self)
        self.Pre_set_label=QtWidgets.QLabel("Mettre Un poids connu sur la balance \n et puis appuyez sur Entrée",self)
        self.Pre_set_label.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.Pre_set_label.setFixedSize(400, 50)
        self.Pre_set_label.move(10, 20)

        self.calibration_termin=QtWidgets.QLabel(self)
        self.calibration_termin.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.calibration_termin.move(20, 175)
        self.calibration_termin.setFixedSize(300, 50)




        self.put_button = QtWidgets.QPushButton("Entrée",self)
        self.put_button.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.put_button.clicked.connect(self.affiche_champ)# 1 er etape de calibration
        self.put_button.move(600, 50)


        self.retour_button = QtWidgets.QPushButton("Retour",self)
        self.retour_button.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.retour_button.clicked.connect(self.retour)
        self.retour_button.move(50, 350)

        self.ok_button = QtWidgets.QPushButton("Calibrer",self)
        self.ok_button.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.ok_button.clicked.connect(self.reading_calibration)# appel fonction calibration 
        self.ok_button.move(600, 100)
        self.ok_button.setVisible(False)

        self.formGroupBox = QGroupBox(self)
        self.layout = QFormLayout()
        self.formGroupBox.setFixedSize(250, 100)
        self.formGroupBox.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')   
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0,0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.addWidget(self.set, 0,0)
        self.gridLayout.addWidget(self.set_line_calibration, 0,1)
        self.formGroupBox.setLayout(self.gridLayout)
        self.formGroupBox.move(10, 70)
        self.formGroupBox.setVisible(False)
        
       

        self.formGroupBox_clavier = QGroupBox("clavier ",self)
        self.layout_clavier = QFormLayout()
        self.formGroupBox_clavier.setFixedSize(300, 250)
        self.formGroupBox_clavier.move(220, 20)
        self.gridLayout_clavier = QtWidgets.QGridLayout(self)
        self.gridLayout_clavier.setContentsMargins(0, 0, 0,0)
        self.gridLayout_clavier.setSpacing(0)
        self.formGroupBox_clavier.setStyleSheet("background-color: rgb(200, 200, 200);")

        for btnText, pos in self.buttons.items():#creation boutton clavier 
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(50, 50)
            self.gridLayout_clavier.addWidget(self.buttons[btnText], pos[0], pos[1])
        #self.gridLayout_clavier.addWidget(self.ok_button, 1, 1)        
        self.formGroupBox_clavier.setLayout(self.gridLayout_clavier)
        self.formGroupBox_clavier.setVisible(False)


       
        self.setWindowTitle('Calibration')    
        self.show()
    def retour(self): 
            self.main=Main_Window()            
            self.main.resize(800, 470)
            self.main.setGeometry(0, -1, 800, 480)
            self.main.show()
            self.destroy()

    def affiche_champ(self): #1 er etape de calibration
        try:
            self.reading = hx.get_data_mean()
        except:
            print("no reading")
        
        
        self.formGroupBox.setVisible(True)
        self.ok_button.setVisible(True)
        
    def mousePressEvent(self,event):
        self.formGroupBox_clavier.setVisible(False)



    def getval(self,event): # afficher clavier 
        print(self.champs)
        self.formGroupBox_clavier.move(240, 110)
        self.formGroupBox_clavier.setVisible(True)



    def reading_calibration(self): #calibration 
        try:
            if self.reading:                
                known_weight_grams = int(self.set_line_calibration.text())
                if int(known_weight_grams)==0:
                    known_weight_grams=1
                try:
                    value = float(known_weight_grams)
                except ValueError:
                    print('Expected integer or float and I have got:',known_weight_grams)

                # set scale ratio for particular channel and gain which is
                # used to calculate the conversion to units. Required argument is only
                # scale ratio. Without arguments 'channel' and 'gain_A' it sets
                # the ratio for current channel and gain.
                ratio = self.reading / value  # calculate the ratio for channel A and gain 128
                hx.set_scale_ratio(ratio)  # set ratio for current channel
                print('Ratio is set.',ratio)
                save_config("configPoids.json","Ratio",str(ratio))

                
                
            else:
                raise ValueError('Cannot calculate mean value. Try debug mode. Variable reading:', reading)

            # Read data several times and return mean value
            # subtracted by offset and converted by scale ratio to
            # desired units. In my case in grams.
            print('Current weight on the scale in grams is: ')
            print(hx.get_weight_mean(cal), 'g')
            self.calibration_termin.setText("calibration terminé: "+str(int(hx.get_weight_mean(cal)))+ " g" )

        except (KeyboardInterrupt, SystemExit):
            print('Bye :)')
                       





    def save_val(self): #enregistrer calibration 
            self.main=Main_Window()# retour main
            self.signal.connect(self.main.calib_set)# signale porteuse parametres 
            self.signal.emit(int(self.set_line_calibration.text()))
            
            self.destroy()
            self.main.resize(800, 470)
            self.main.setGeometry(0, -1, 800, 480)
            self.main.show()

    def setDisplayText(self, text):
        """Set display's text.""" 
        self.set_line_calibration.setText(text)
        self.set_line_calibration.setFocus()               

    def displayText(self,txt):
        """Get display's text."""
        return txt.text()
    def clearDisplay(self):
        self.setDisplayText("")
    def _buildExpression(self, sub_exp):
        """Build expression."""
        expression = self.displayText(self.set_line_calibration) + sub_exp
        self.setDisplayText(expression)

    def destroy_windo(self):
        self.destroy()

    def _connectSignals(self):
       
        """Connect signals and slots."""
        for btnText, btn in self.buttons.items():
            print(btnText, btn)
            if btnText not in {"Entrée", "C","Esp"}:

                    btn.clicked.connect(partial(self._buildExpression, btnText))
                

        self.buttons["C"].clicked.connect(self.clearDisplay)








class Volume_(QMainWindow): #réglage volume 
    signal=pyqtSignal(int,int)

    def closeEvent(self, event):
        self.retour()
        event.accept()

    def __init__(self):
        super().__init__()        
       
        self.initUI()
        self._connectSignals()

       
    def initUI(self):
        self.setStyleSheet(" background-color: rgb(0, 128, 255); ")
        self.champs=0
        self.buttons = {}
        self.buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
           
            
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            
            "C": (3, 1),
            "0": (3, 0),
            "Esp": (3, 2),
            
        }       
       
        self.setGeometry(0, -1, 800, 480)
        self.set_line = QtWidgets.QLineEdit()
        self.set_line.setEchoMode(0)
        self.set_line.setMaxLength(4)
        self.set_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.set_line.setFixedSize(85, 20)
        #self.set_line.setMaxLength(20)
        self.set_line.mousePressEvent=self.getval

        self.pre_set = QtWidgets.QLineEdit()
        self.pre_set.setEchoMode(0)
        self.pre_set.setMaxLength(4)
        self.pre_set.mousePressEvent=self.getval_preset
        self.pre_set.setStyleSheet("background-color: rgb(255, 255, 255);")

       
        self.set=QtWidgets.QLabel("set (g)        :",self)
        self.set.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.Pre_set_label=QtWidgets.QLabel("Pre set (g)  :",self)
        self.Pre_set_label.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')

        self.ok_button = QtWidgets.QPushButton("OK",self)
        self.ok_button.clicked.connect(self.save_val)
        self.ok_button.move(200, 100)

        self.laberreur=QtWidgets.QLabel(self)
        self.laberreur.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.laberreur.setFixedSize(200, 40)

        self.laberreur.move(50, 130)

        self.retour_button = QtWidgets.QPushButton("Retour",self)
        self.retour_button.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.retour_button.clicked.connect(self.retour)
        self.retour_button.move(50, 350)
        

        self.formGroupBox = QGroupBox(self)
        self.layout = QFormLayout()
        self.formGroupBox.setFixedSize(300, 100)
           
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0,0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.addWidget(self.set, 0,0)
        self.gridLayout.addWidget(self.set_line, 0,1)
        self.gridLayout.addWidget(self.Pre_set_label, 1,0)
        self.gridLayout.addWidget(self.pre_set, 1,1)
        self.formGroupBox.setLayout(self.gridLayout)
        self.formGroupBox.show()
       

#############

        self.formGroupBox_clavier = QGroupBox("clavier ",self)
        self.layout_clavier = QFormLayout()
        self.formGroupBox_clavier.setFixedSize(300, 250)
        self.formGroupBox_clavier.move(220, 20)
        self.gridLayout_clavier = QtWidgets.QGridLayout(self)
        self.gridLayout_clavier.setContentsMargins(0, 0, 0,0)
        self.gridLayout_clavier.setSpacing(0)
        self.formGroupBox_clavier.setStyleSheet("background-color: rgb(200, 200, 200);")

        for btnText, pos in self.buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(50, 50)
            self.gridLayout_clavier.addWidget(self.buttons[btnText], pos[0], pos[1])
        #self.gridLayout_clavier.addWidget(self.ok_button, 1, 1)        
        self.formGroupBox_clavier.setLayout(self.gridLayout_clavier)
        self.formGroupBox_clavier.setVisible(False)


       
        self.setWindowTitle('Volume')    
        self.show()

    def retour(self): 
            self.main=Main_Window()            
            self.main.resize(800, 470)
            self.main.setGeometry(0, -1, 800, 480)
            self.main.show()
            self.destroy()

    def mousePressEvent(self,event):
        self.formGroupBox_clavier.setVisible(False)
    def getval_preset(self,event):
        self.champs=2
        self.formGroupBox_clavier.move(305, 50)
        self.formGroupBox_clavier.setVisible(True)
        self.laberreur.setText("")



    def getval(self,event):
        self.champs=1
        self.laberreur.setText("")
        self.formGroupBox_clavier.move(305, 20)
        self.formGroupBox_clavier.setVisible(True)
        
    def save_val(self):
        try:
            if int(self.set_line.text()) >= int(self.pre_set.text()):
                x=int(self.set_line.text())+int(self.pre_set.text())
                self.main=Main_Window()
                self.signal.connect(self.main.get_set_preset)
                self.signal.emit(int(self.set_line.text()),int(self.pre_set.text()))
                save_config("configPoids.json","set",str(self.set_line.text()))
                save_config("configPoids.json","preset",str(self.pre_set.text()))
                self.main.resize(800, 470)
                self.main.setGeometry(0, -1, 800, 480)
                self.main.show()
                self.destroy()
            else:
                self.laberreur.setText("valeurs n'existe pas")
        except:
            self.laberreur.setText("Erreur")

            

    def setDisplayText(self, text):
        """Set display's text."""

        if self.champs==1:
            
            self.set_line.setText(text)

            self.set_line.setFocus()               
            
        if self.champs==2:
            self.pre_set.setText(text)

            self.pre_set.setFocus()            
            

    def displayText(self,txt):
        """Get display's text."""
        return txt.text()
    def clearDisplay(self):
        self.setDisplayText("")
    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self.champs==1:
            expression = self.displayText(self.set_line) + sub_exp
            self.setDisplayText(expression)
        if self.champs==2:
            expression = self.displayText(self.pre_set) + sub_exp
            self.setDisplayText(expression)
    def destroy_windo(self):
        self.destroy()

    def _connectSignals(self):
       
        """Connect signals and slots."""
        for btnText, btn in self.buttons.items():
            print(btnText, btn)
            if btnText not in {"Entrée", "C","Esp"}:

                    btn.clicked.connect(partial(self._buildExpression, btnText))
                

        self.buttons["C"].clicked.connect(self.clearDisplay)






class Main_Window(QMainWindow):
    
    

    
    
    def __init__(self):
        super().__init__()
               
       
        self.initUI()        




    def initUI(self):
        
            
        try:#lire le fichier json #parametre du capteur hx11
            with open("configPoids.json", "r") as jsonFile:
                data = json.load(jsonFile)
            Ratio=data['Ratio']
            self.set_val=int(data['set'])
            self.pre_set_val=int(data['preset'])
            self.num_prod=int(data['num_prod'])
            print(self.num_prod)
            print("set:",self.set_val,self.pre_set_val)
            
        except:
            print("file Error")
            Ratio=20
            self.set_val=0
            self.pre_set_val=0
            self.num_prod=0          
        
        
        
        self.setGeometry(0, -1, 800, 480)
        self.poids=QtWidgets.QLabel(self)
        self.getPoids= QtCore.QTimer(self)
        self.getPoids.timeout.connect(lambda:self.get_poids(self.poids))
        self.getPoids.start(500) #lire poids dans une période de 500 ms         
        self.change_start= QtCore.QTimer(self)
        self.change_start.timeout.connect(self.change_etat_start)
        self.change_start.start(100) #lire boutton marche  dans une période de 500 ms 

        self.change_arret= QtCore.QTimer(self)
        self.change_arret.timeout.connect(self.change_etat_Arret)
        self.change_arret.start(100) #lire boutton Arret  dans une période de 500 ms 

        self.setStyleSheet(" background-color: rgb(204, 204, 255); ")
        self.etat=0#rien faire
        self.etat_remplissage=0
        self.pre=0 #fin de cycle de remplissage 
        self.button_tarage = QPushButton('Tarage',self)
        self.button_tarage.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.button_tarage.resize(180,80)
       
        self.button_tarage.move(400,350)
        self.button_tarage.clicked.connect(self.tarage_fn)


        self.button_exit = QPushButton(self)
        self.button_exit.setFixedWidth(50)
        self.button_exit.setFixedHeight(50)
        self.button_exit.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button_exit.setIcon(QtGui.QIcon('arret.png'))
        self.button_exit.setIconSize(QSize(70,70))
       
        self.button_exit.move(730,10)
        self.button_exit.clicked.connect(self.exit_button)


        self.button_calibration = QPushButton('calibration',self)
        self.button_calibration.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.button_calibration.clicked.connect(self.calibration_fn)
        self.button_calibration.resize(180,80)
        self.button_calibration.move(210,350)





        self.reeltimeText_set=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.reeltimeText_set.move(650,115)
        self.reeltimeText_set.resize(150,45)
        self.reeltimeText_set.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.reeltimeText_set.setText(str(self.set_val)+" g")


        self.reeltimeText=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.reeltimeText.move(650,70)
        self.reeltimeText.resize(150,45)
        self.reeltimeText.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.reeltimeText.setText(str(self.pre_set_val)+" g")


        self.numprod=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.numprod.move(120,50)
        self.numprod.resize(150,45)
        self.numprod.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.numprod.setText(str(self.num_prod))

        self.quantite=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.quantite.move(10,50)
        self.quantite.resize(100,45)
        self.quantite.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.quantite.setText("Quantité:")

        self.button_Volume = QPushButton('Réglage',self)
        self.button_Volume.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.button_Volume.move(590,350)
        self.button_Volume.clicked.connect(self.volume_fn)
        self.button_Volume.resize(180,80)


        self.reset_buton = QPushButton('Reset',self)
        self.reset_buton.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.reset_buton.move(10,100)
        self.reset_buton.clicked.connect(self.reset_fn)
        self.reset_buton.resize(90,50)


        self.button_remplissage = QPushButton('Remplissage',self)
        self.button_remplissage.setStyleSheet('background-color : red;color: rgb(255, 0, 0);font: 20pt Helvetica MS;')
        self.button_remplissage.move(20,350)
        self.button_remplissage.clicked.connect(self.Remplissage_fn)#debit remplissage
        self.button_remplissage.resize(180,80)
             
       
        self.setWindowTitle('Balance')
        self.setStyleSheet(" background-color: rgb(0, 128, 255); ")
        
        
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.poids.move(350,150)
        self.poids.resize(370,100)
        self.poids.setStyleSheet('color: rgb(0, 0, 0);font: 60pt Helvetica MS;')


        self.round=QtWidgets.QLabel(self)
        self.round.resize(45,45)
        self.round.setStyleSheet(" background-color : red; border : 3px; border-radius : 10px;")
        self.round.move(730,70)       

        self.round2=QtWidgets.QLabel(self)
        self.round2.resize(45,45)
        self.round2.setStyleSheet(" background-color : red; border : 3px; border-radius : 10px;")
        self.round2.move(730,120)        
            
         
    def exit_button(self): #arret du système
        call("sudo  shutdown -h now",shell=True)
        
        
    def reset_fn(self):#reset compteur de piéces 
        self.num_prod=0
        save_config("configPoids.json","num_prod",str(0))
        
    def change_etat_Arret(self): #Arret remplissage
        if GPIO.input(arret_urgence)==1:
            self.pre=0
            self.etat_remplissage=0

    def change_etat_start(self):#debit remplissage
        self.numprod.setText(str(self.num_prod))
        if GPIO.input(start)==1:#gpio debit remplissage ==1
            self.button_remplissage.setStyleSheet('background-color : lime;color: rgb(0, 255, 0);font: 20pt Helvetica MS;')
            self.etat_remplissage=1
            self.pre=1
    def get_poids(self,t):#lire , affiche poids / allumer led/compter les pièces 
            x=(hx.get_weight_mean(cal))#lire poids
            t.setText(str((int(x)))+" g")
            if x <= self.pre_set_val and (self.etat_remplissage==1) and GPIO.input(arret_urgence)==0:#if  poids<preset_valeur et etats remplissage =1 donc mise en marche les deux ponpes
                self.etat=0
                self.round.setStyleSheet(" background-color : lime; border : 3px; border-radius : 10px;")
                self.round2.setStyleSheet(" background-color : lime; border : 3px; border-radius : 10px;")
                GPIO.output(vane1,GPIO.HIGH)
                GPIO.output(vane2,GPIO.HIGH)

            if x >= self.pre_set_val and (self.etat_remplissage==1 ) and GPIO.input(arret_urgence)==0:#if  poids>preset_valeur et etats remplissage =1 donc mise en marche une seul ponpe
                self.etat=1
                self.round.setStyleSheet(" background-color : red; border : 3px; border-radius : 10px;")
                self.round2.setStyleSheet(" background-color : lime; border : 3px; border-radius : 10px;")
                GPIO.output(vane1,GPIO.LOW)
                GPIO.output(vane2,GPIO.HIGH)
                
            if (self.etat_remplissage==0)  or GPIO.input(arret_urgence)==1 or x >= self.set_val:
                self.round.setStyleSheet(" background-color : red; border : 3px; border-radius : 10px;")
                self.round2.setStyleSheet(" background-color : red; border : 3px; border-radius : 10px;")
                GPIO.output(vane1,GPIO.LOW)                
                GPIO.output(vane2,GPIO.LOW)
                self.etat_remplissage=0
                self.button_remplissage.setStyleSheet('background-color : red;color: rgb(255, 0, 0);font: 20pt Helvetica MS;')
                if self.pre==1 and GPIO.input(arret_urgence)==0:
                    self.num_prod +=1  #compteur des  pièces +1
                    self.pre=0
                    save_config("configPoids.json","num_prod",str(self.num_prod))#enregistrement dans le fichier 

                    
    def get_set_preset(self,a,b): # lire les valeurs  à partir de signale réglage
        print("a,b:",a,b)
        self.set_val=a
        self.pre_set_val=b
        self.reeltimeText.setText(str(self.pre_set_val)+" g")#affichage set et pre_set 
        self.reeltimeText_set.setText(str(self.set_val)+" g")        
        
    def calib_set(self,a):#lire les valeurs  à partir de signale calibration 
        print("a,b:",a)
        self.getPoids.start(500)
        self.reeltimeText.setText(str(a))
    def Remplissage_fn(self):#debit remplissage
        if self.etat_remplissage==0:
            self.button_remplissage.setStyleSheet('background-color : lime;color: rgb(0, 255, 0);font: 20pt Helvetica MS;')
            self.etat_remplissage=1
            self.pre=1
            
        else:
            self.button_remplissage.setStyleSheet('background-color : red;color: rgb(255, 0, 0);font: 20pt Helvetica MS;')
            self.etat_remplissage=0


    def volume_fn(self):
        self.getPoids.stop()  
        self.rmp = Volume_()
        self.rmp.show()
        self.destroy()


    def tarage_fn(self):
        try:

            err = hx.zero()
        except Exception as e:
            print(e)



    def calibration_fn(self):
        self.getPoids.stop()  
        self.rmp = calibration()
        self.rmp.show()
        self.destroy()
        
        """try:


            input('Put known weight on the scale and then press Enter')
            
            reading = hx.get_data_mean()
            if reading:
                print('Mean value from HX711 subtracted by offset:', reading)
                
                known_weight_grams = input('Write how many grams it was and press Enter: ')
                try:
                    value = float(known_weight_grams)
                    print(value, 'grams')
                except ValueError:
                    print('Expected integer or float and I have got:',
                          known_weight_grams)

                # set scale ratio for particular channel and gain which is
                # used to calculate the conversion to units. Required argument is only
                # scale ratio. Without arguments 'channel' and 'gain_A' it sets
                # the ratio for current channel and gain.
                ratio = reading / value  # calculate the ratio for channel A and gain 128
                hx.set_scale_ratio(ratio)  # set ratio for current channel
                print('Ratio is set.')
                save_config("configPoids.json","Ratio",str(ratio))

                
                
            else:
                raise ValueError('Cannot calculate mean value. Try debug mode. Variable reading:', reading)

            # Read data several times and return mean value
            # subtracted by offset and converted by scale ratio to
            # desired units. In my case in grams.
            print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
            input('Press Enter to begin reading')
            print('Current weight on the scale in grams is: ')
            print(hx.get_weight_mean(20), 'g')

        except (KeyboardInterrupt, SystemExit):
            print('Bye :)')"""
                

            
            
            
            



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    main = Main_Window()
    main.setGeometry(0, -1, 800, 480)

    main.show()
    sys.exit(app.exec_())

