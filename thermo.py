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

import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(4, GPIO.IN) 



from pymongo import MongoClient
import pymongo,gridfs
import dns
import numpy as np
import cv2
client = MongoClient("mongodb://admin:admin@freecluster-shard-00-00-oqzix.mongodb.net:27017,freecluster-shard-00-01-oqzix.mongodb.net:27017,freecluster-shard-00-02-oqzix.mongodb.net:27017/test?ssl=true&replicaSet=FreeCluster-shard-0&authSource=admin&retryWrites=true&w=majority",serverSelectionTimeoutMS=2000)    
db = client.test
db=client['personnes_ther']

       
def save_image(image):
    try:
        fs = gridfs.GridFS( db )
        fileID = fs.put(open(image, 'rb') ,filename="image1")



        """file = fs.find_one({'filename': 'image1'})
        image = file.read()





        img = np.fromstring(image, dtype='uint8')
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (300, 300))
        img = np.multiply(img, 1 / 255.0)

        cv2.imshow('im',img)
        cv2.waitKey()
        cv2.destroyAllWindows()"""

        

    except Exception as e:
            print(e)
       
#save_image('im0.jpg')

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

        temperature = QtCore.QTimer(self)
        temperature.timeout.connect(self.read_temperature)
        temperature.start(1000)



        delaysecond_time = QtCore.QTimer(self)
        delaysecond_time.timeout.connect(self.delaysecond)
        delaysecond_time.start(1100)

        
        self.setGeometry(0,45,810,415)
        self.setWindowTitle("thermo")
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
        
        self.label1=QtWidgets.QLabel(self)
             

    def Time(self):
            self.reeltimeText.setText(strftime("%H"+":"+"%M"+":"+"%S"))
            
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


        self.run = QPushButton(self)                
        #self.run.clicked.connect(self.demarrer)
        self.run.setFixedWidth(65)
        self.run.setFixedHeight(60)
        self.run.move(650,360)
        self.run.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(0, 255, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.run.setIcon(QtGui.QIcon('marche.png'))
        self.run.setIconSize(QSize(100,100))

        self.image=QtWidgets.QLabel(self)
        self.image.setFixedWidth(400)
        self.image.setFixedHeight(360)
        self.image.setStyleSheet('color: rgb(255, 0, 0);background-color: rgb(255, 255, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.image.move(10,40)
        pixmap = QPixmap('marche.png')
        self.image.setPixmap(pixmap)


        self.temperature=QtWidgets.QLabel(self)
        self.temperature.setFixedWidth(100)
        self.temperature.setFixedHeight(40)
        self.temperature.setStyleSheet('color: rgb(255, 0, 0);backg++round-color: rgb(255, 255, 255);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.temperature.move(450,60)



        
        
        main_layout.addLayout(tab_layout, 1)

        #draw left frame
        self.setLayout(main_layout)
    def read_temperature(self):
        if GPIO.input(4)==1:
            self.temperature.setText("38.00")
            
        if GPIO.input(4)==0:
            self.temperature.setText("33.22")
    

if __name__ == "__main__":
    import sys  
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = Widget()
    w.show()
    sys.exit(app.exec_())



    
