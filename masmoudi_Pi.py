
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
from trs_roud_progress import  QRoundProgressBar_TRS

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
plongeur=17
antigout=3
pompe=10
arret_urgence=27
start=22
GPIO.setmode(GPIO.BCM)
GPIO.setup(plongeur,GPIO.OUT)
GPIO.setup(antigout,GPIO.OUT)
GPIO.setup(pompe,GPIO.OUT)
GPIO.setup(arret_urgence,GPIO.IN)
GPIO.setup(start,GPIO.IN)
############Gpio Raspberry##############################

cal=5#nombre des échantillons (rapidité et précision )

from csv import writer


import csv
def get_num_prod(filename,OF,machine,employe,date):
    fields = []
    rows = []
    num=0
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = (csvreader)
        for row in csvreader:
            rows.append(row)
    for row in rows:
        if row[0]== OF and row[1]==machine and row[2]==employe and row[3].split(" ")[0]==date:
            num=num+1
    return num

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        
def save_config(file,parametre,value_save):# enregistrer les données dans un fichier json

                    with open(file, "r") as jsonFile:
                        data = json.load(jsonFile)                    
                    data[parametre] = str(value_save)

                    with open(file, "w") as jsonFile:
                        json.dump(data, jsonFile)
                    jsonFile.close()
                   



try:#connection serveur
    connection = mysql.connector.connect(host='localhost',
                                         database='control_poids',
                                         user='root',
                                         password='admin')


    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tp_control_poids (id INT PRIMARY KEY, ratio TEXT, set_ int,preset int,num_prod int,poids TEXT)")
    req="SELECT * FROM tp_control_poids"
   
    cursor.execute(req)
    res=cursor.fetchall()
    if len(res)==0:
       
        req="insert into tp_control_poids (id,ratio,set_,preset,num_prod,poids) values (1,'0',0,0,0,'0')"
   
        cursor.execute(req)
        connection.commit()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

def select_data():
    req="SELECT * FROM tp_control_poids"
    cursor.execute(req)
    res=cursor.fetchall()
    connection.reset_session()
    return res

#select_data()

def update_data(champ,data):
    req="UPDATE tp_control_poids set "+str(champ)+"='"+str(data)+"'"
    cursor.execute(req)
    connection.commit()
    connection.reset_session()


try:
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    # Create an object hx which represents your real hx711 chip
    # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
    hx = HX711(dout_pin=21, pd_sck_pin=20)
    err = hx.zero()
    # measure tare and save the value as offset for current channel
    # and gain selected. That means channel A and gain 128
    """with open("configPoids.json", "r") as jsonFile:
        data = json.load(jsonFile)
    Ratio=data['Ratio']
    set_val=int(data['set'])
    pre_set_val=int(data['preset'])"""
   
    v=select_data()
   
    Ratio=(v[0][1])
    set_val=int(v[0][2])
    pre_set_val=int(v[0][3])
    print(set_val,pre_set_val)
    hx.set_scale_ratio(float(Ratio))  # set ratio for current channel

   
   
   
except Exception as k :
    print("errrr1:"+str(k))





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
        self.setStyleSheet(" background-color: rgb(255, 255, 255); ")        
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
        self.set_line_calibration.setMaxLength(6)
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
        self.put_button.setFixedSize(100, 50)
        self.put_button.clicked.connect(self.affiche_champ)# 1 er etape de calibration
        self.put_button.move(600, 50)


        self.retour_button = QtWidgets.QPushButton("Retour",self)
        self.retour_button.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.retour_button.clicked.connect(self.retour)
        self.retour_button.setFixedSize(100, 50)
        self.retour_button.move(50, 350)

        self.ok_button = QtWidgets.QPushButton("Calibrer",self)
        self.ok_button.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.ok_button.setFixedSize(100, 50)
        self.ok_button.clicked.connect(self.reading_calibration)# appel fonction calibration
        self.ok_button.move(600, 120)
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
        print(self.set_line_calibration.text())
        try:
            if self.reading and self.set_line_calibration.text()!="":                
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
                #save_config("configPoids.json","Ratio",str(ratio))
                update_data("ratio",ratio)

             
               
            else:
                print('Cannot calculate mean value. Try debug mode. Variable reading:')

            # Read data several times and return mean value
            # subtracted by offset and converted by scale ratio to
            # desired units. In my case in grams.
            print('Current weight on the scale in grams is: ')
            #print(hx.get_weight_mean(cal), 'g')
            try:
                self.calibration_termin.setText("calibration terminé: "+str(int(hx.get_weight_mean(cal)))+ " g" )
            except:
                self.calibration_termin.setText("Erreur")

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
        v=select_data()
        self.reglage_poids=int(v[0][5])
       
        self.initUI()
        self._connectSignals()

       
    def initUI(self):
       
       
        try:#lire le fichier json #parametre du capteur hx11
            """with open("configPoids.json", "r") as jsonFile:
                data = json.load(jsonFile)
            ""Ratio=data['Ratio']
            self.set_val=int(data['set'])
            self.pre_set_val=int(data['preset'])
            self.num_prod=int(data['num_prod'])"""
           
            v=select_data()
            self.Ratio=float(v[0][1])
            self.set_val=int(v[0][2])
            self.pre_set_val=int(v[0][3])
            self.num_prod=int(v[0][4])            
            self.temps_pos=int(v[0][6])          
        except Exception as e:
            print(e)
            self.Ratio=20
            self.set_val=0
            self.pre_set_val=0
            self.num_prod=0
            self.temps_pos=1        
       
        self.setStyleSheet(" background-color: rgb(255, 255, 255); ")
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
        self.set_line.setMaxLength(6)
        self.set_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.set_line.setFixedSize(85, 20)
        #self.set_line.setMaxLength(20)
        self.set_line.setText(str(self.set_val))
        self.set_line.mousePressEvent=self.getval



        self.time_set = QtWidgets.QLineEdit(self)
        self.time_set.setEchoMode(0)
        self.time_set.setMaxLength(6)
        self.time_set.mousePressEvent=self.getval_time
        self.time_set.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_set.setFixedSize(70, 35)
        self.time_set.setText(str(self.temps_pos))
        self.time_set.move(120, 220)
       
        self.time_lab=QtWidgets.QLabel("T-R(s):",self)
        self.time_lab.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.time_lab.move(20, 220)

        self.ok_button_set_time = QtWidgets.QPushButton("OK",self)
        self.ok_button_set_time.clicked.connect(self.save_val_time)
        self.ok_button_set_time.move(200, 220)
       
       
       



        self.pre_set = QtWidgets.QLineEdit()
        self.pre_set.setEchoMode(0)
        self.pre_set.setMaxLength(6)
        self.pre_set.mousePressEvent=self.getval_preset
        self.pre_set.setStyleSheet("background-color: rgb(255,255, 255);")
        self.pre_set.setText(str(self.pre_set_val))

       
        self.set=QtWidgets.QLabel("set (g)        :",self)
        self.set.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.Pre_set_label=QtWidgets.QLabel("Pre set (g)  :",self)
        self.Pre_set_label.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        #self.temps_posself.pre_set_val set_val          

        self.ok_button = QtWidgets.QPushButton("OK",self)
        self.ok_button.clicked.connect(self.save_val)
        self.ok_button.move(200, 150)
       
        self.Poids_label=QtWidgets.QLabel("Poids(kg): "+str(int(self.reglage_poids/1000)),self)
        self.Poids_label.setFixedSize(200, 40)
        self.Poids_label.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.Poids_label.move(20, 270)        

        self.Poids_button = QtWidgets.QPushButton("Reset",self)
        self.Poids_button.clicked.connect(self.reset_poids)
        self.Poids_button.move(200, 270)        
       

        self.laberreur=QtWidgets.QLabel(self)
        self.laberreur.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.laberreur.setFixedSize(100, 90)

        self.laberreur.move(50, 120)

        self.retour_button = QtWidgets.QPushButton("Retour",self)
        self.retour_button.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')
        self.retour_button.clicked.connect(self.retour)
        self.retour_button.setFixedSize(100, 50)

        self.retour_button.move(20, 330)
       

        self.formGroupBox = QGroupBox(self)
        self.layout = QFormLayout()
        self.formGroupBox.setFixedSize(300, 150)
           
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 50, 0,0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.addWidget(self.set, 0,0)
        self.gridLayout.addWidget(self.set_line, 0,1)
        self.gridLayout.addWidget(self.Pre_set_label, 1,0)
        self.gridLayout.addWidget(self.pre_set, 1,1)
        #self.gridLayout.addWidget(self.time_set, 2,1)
        #self.gridLayout.addWidget(self.pre_set, 1,1)
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
    def reset_poids(self):
            update_data("poids",0)
            v=select_data()
            poids=v[0][5]
            self.Poids_label.setText("Poids(kg): "+str(int(poids)/1000))
       
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
        self.formGroupBox_clavier.move(305, 100)
        self.formGroupBox_clavier.setVisible(True)
        self.laberreur.setText("")

    def getval_time(self,event):
        self.champs=3
        self.formGroupBox_clavier.move(305, 220)
        self.formGroupBox_clavier.setVisible(True)
        self.laberreur.setText("")

    def getval(self,event):
        self.champs=1
        self.laberreur.setText("")
        self.formGroupBox_clavier.move(305, 70)
        self.formGroupBox_clavier.setVisible(True)

    def save_val_time(self):
        try:
            if self.time_set.text()!="":
                update_data("temps_pos",(self.time_set.text()))
           
        except:
            print("err")
           
   
    def save_val(self):
        try:
            if int(self.set_line.text()) >= int(self.pre_set.text()):
                x=int(self.set_line.text())+int(self.pre_set.text())
                self.main=Main_Window()
                self.signal.connect(self.main.get_set_preset)
                self.signal.emit(int(self.set_line.text()),int(self.pre_set.text()))
                #save_config("configPoids.json","set",str(self.set_line.text()))
                #save_config("configPoids.json","preset",str(self.pre_set.text()))
                update_data("set_",(self.set_line.text()))
                update_data("preset",(self.pre_set.text()))
             
               
               
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

        if self.champs==3:
           
            self.time_set.setText(text)

            self.time_set.setFocus()              
           
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
        if self.champs==3:
            expression = self.displayText(self.time_set) + sub_exp
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
            """with open("configPoids.json", "r") as jsonFile:
                data = json.load(jsonFile)
            ""Ratio=data['Ratio']
            self.set_val=int(data['set'])
            self.pre_set_val=int(data['preset'])
            self.num_prod=int(data['num_prod'])"""
           
            v=select_data()
            self.Ratio=float(v[0][1])
            self.set_val=int(v[0][2])
            self.pre_set_val=int(v[0][3])
            self.num_prod=int(v[0][4])            
            self.temps_pos=int(v[0][6])            
        except Exception as e:
            print(e)
            self.Ratio=20
            self.set_val=0
            self.pre_set_val=0
            self.num_prod=55
            self.temps_pos=1
       
       
        self.poids=QtWidgets.QLabel(self)
        self.poids.move(420,100)
        self.poids.resize(400,150)
        self.poids.setStyleSheet('color: rgb(0, 0, 0);font: 70pt Helvetica MS;')
       
        self.getPoids= QtCore.QTimer(self)
        self.getPoids.timeout.connect(lambda:self.get_poids(self.poids))
        self.getPoids.start(500) #lire poids dans une période de 500 ms        

        self.affichage_= QtCore.QTimer(self)
        self.affichage_.timeout.connect(self.affichage)
        self.affichage_.start(1125) #lire poids dans une période de 500 ms        


        self.setStyleSheet(" background-color: rgb(0, 0, 255); ")
        self.etat=0#rien faire
        self.etat_remplissage=0
        self.pre=0 #fin de cycle de remplissage
        self.etat_preset=1
        self.x=0
        self.aux_save=0
        self.Max_val=0
        self.time_start=time.time()
       
       
        self.button_tarage = QPushButton('Tarage',self)
        self.button_tarage.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.button_tarage.resize(180,80)
       
        self.button_tarage.move(600,650)
        self.button_tarage.clicked.connect(self.tarage_fn)


        self.button_exit = QPushButton(self)
        self.button_exit.setFixedWidth(50)
        self.button_exit.setFixedHeight(50)
        self.button_exit.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.button_exit.setIcon(QtGui.QIcon('arret.png'))
        self.button_exit.setIconSize(QSize(70,70))
       
        self.button_exit.move(1100,10)
        self.button_exit.clicked.connect(self.exit_button)


        self.button_calibration = QPushButton('calibration',self)
        self.button_calibration.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.button_calibration.clicked.connect(self.calibration_fn)
        self.button_calibration.resize(180,80)
        self.button_calibration.move(260,650)


       
       

        image_TDS = QPushButton(self)
        image_TDS.setFixedWidth(150)
        image_TDS.setFixedHeight(150)
        image_TDS.setStyleSheet(" background-color : rgb(255,255,255); border : 3px; border-radius : 10px;")
        image_TDS.setIcon(QtGui.QIcon('TDS.png'))
        image_TDS.setIconSize(QSize(150,150))
        image_TDS.move(750,20)        
       

        self.numprod=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.numprod.move(250,50)
        self.numprod.resize(100,45)
        self.numprod.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
        self.numprod.setText(str(self.num_prod))

        self.quantite=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.quantite.move(20,50)
        self.quantite.resize(140,60)
        self.quantite.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.quantite.setText("Quantité:")
        
        self.machine=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.machine.move(20,100)
        self.machine.resize(200,60)
        self.machine.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.machine.setText("Machine N°:")
        
        self.machine_l=QtWidgets.QLabel(self)
        self.machine_l.move(250,100)
        self.machine_l.resize(140,60)
        self.machine_l.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.machine_l.setText("2")

        self.produit_type=QtWidgets.QLabel(self)
        self.produit_type.move(20,150)
        self.produit_type.resize(350,60)
        self.produit_type.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.produit_type.setText("Type de produit:")

        self.produit_type_l=QtWidgets.QLabel(self)
        self.produit_type_l.move(250,150)
        self.produit_type_l.resize(140,60)
        self.produit_type_l.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.produit_type_l.setText("Amandes")

        self.operateur=QtWidgets.QLabel(self)
        self.operateur.move(20,200)
        self.operateur.resize(300,60)
        self.operateur.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.operateur.setText("opérateur:")

        self.operateur_l=QtWidgets.QLabel(self)
        self.operateur_l.move(250,200)
        self.operateur_l.resize(140,60)
        self.operateur_l.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.operateur_l.setText("Ahmed")

        self.OF_=QtWidgets.QLabel(self)
        self.OF_.move(20,250)
        self.OF_.resize(300,60)
        self.OF_.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.OF_.setText("OF:")

        self.OF_l=QtWidgets.QLabel(self)
        self.OF_l.move(250,250)
        self.OF_l.resize(140,60)
        self.OF_l.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.OF_l.setText("OF1")

        self.button_Volume = QPushButton('Réglage',self)
        self.button_Volume.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.button_Volume.move(790,650)
        self.button_Volume.clicked.connect(self.volume_fn)
        self.button_Volume.resize(180,80)

        self.n_m_sac=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.n_m_sac.move(450,300)
        self.n_m_sac.resize(200,60)
        self.n_m_sac.setStyleSheet('color: rgb(0, 0, 0);font: 30pt Helvetica MS;')

        self.progress2= QRoundProgressBar_TRS(self)        
        gradientPoints5 = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        self.progress2.setDataColors(gradientPoints5)        
        self.progress2.setStyleSheet("background-color: rgb(255, 255, 255)")                   
        self.progress2.resize(200,200)
        self.progress2.setValue( (self.num_prod/300)*100)
        self.progress2.move(400,400)

        self.button_ext = QPushButton('Exit',self)
        self.button_ext.move(70,650)
        self.button_ext.setStyleSheet('color: rgb(0, 0, 0);font: 20pt Helvetica MS;')
        self.button_ext.clicked.connect(self.Remplissage_fn)#debit remplissage
        self.button_ext.resize(180,80)
             
       
        self.setWindowTitle('Balance')
        self.setStyleSheet(" background-color: rgb(255, 255, 255); ")        



  
 


 
         
    def exit_button(self): #arret du système
        call("sudo  shutdown -h now",shell=True)
       
       
    def reset_fn(self):#reset compteur de piéces
        self.num_prod=0
        #save_config("configPoids.json","num_prod",str(0))
        update_data("num_prod",0)
 


           
    def affichage(self):
        now = datetime.datetime.now()
        date_time__ = now.strftime("%d-%m-%Y")
        self.num_prod=get_num_prod("masmoudi.csv","OF","machine","employe",date_time__)
        self.numprod.setText(str(self.num_prod))
        self.n_m_sac.setText(str(self.num_prod)+"/"+str(300))
        self.progress2.setValue( (self.num_prod/300)*100)
        
        #self.n_m_sac.setText("%.2f" % ((self.num_prod/300)))
    def change_etat_Arret(self): #Arret remplissage
        if GPIO.input(arret_urgence)==1:
            self.pre=0
            self.etat_remplissage=0

    def change_etat_start(self):#debit remplissage
        self.numprod.setText(str(self.num_prod))
        if GPIO.input(start)==1 and self.x<=self.pre_set_val:#gpio debit remplissage ==1
            self.time_start=time.time()
            self.button_remplissage.setStyleSheet('background-color : lime;color: rgb(0, 255, 0);font: 20pt Helvetica MS;')
            self.etat_remplissage=1
            self.etat_preset=1
            self.pre=1
    def get_poids(self,t):#lire , affiche poids / allumer led/compter les pièces
        try:
            self.x=(hx.get_weight_mean(cal))#lire poids
            if self.x>=self.Max_val:
                self.Max_val=self.x
            t.setText(str((int(self.x)))+" g")
            if self.x>=1000 and self.aux_save==0:
                self.aux_save=1
            if self.x<=100 and self.aux_save==1:
                print("save")
                row_contents = ["OF",'machine','employe',time.strftime("%d-%m-%Y %H:%M:%s"),self.Max_val,'jjjjj','kkkkkk']
                append_list_as_row('masmoudi.csv', row_contents)
                self.Max_val=0
                self.aux_save=0
                
        except Exception as e:
            print(e)
                   
    def get_set_preset(self,a,b): # lire les valeurs  à partir de signale réglage
        print("a,b:",a,b)
        self.set_val=a
        self.pre_set_val=b
        self.reeltimeText.setText(str(self.pre_set_val)+" g")#affichage set et pre_set
        self.reeltimeText_set.setText(str(self.set_val)+" g")        
       
    def calib_set(self,a):#lire les valeurs  à partir de signale calibration
       
        self.getPoids.start(500)
        self.reeltimeText.setText(str(a))
    def Remplissage_fn(self):#debit remplissage
        self.close()



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
    main.setGeometry(0, -1, 1100, 760)

    main.show()
    sys.exit(app.exec_())






