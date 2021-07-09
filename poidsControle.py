import sys
Width_champ= 500
Height_champ=600
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

from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode




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

import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711 

                                       
class calibration(QWidget):
    signal3=pyqtSignal(str)
    mode=0



                       
    def __init__(self):
        super().__init__()
        self.etas=0
        self.val_yb_sy=20
        self.xlab=20
        serifFont = QFont("Times", 10, QFont.Bold)
       

       

        self.Reset= QPushButton(self)        
        self.Reset.setText("Reset")
        self.Reset.setFixedWidth(100)
        self.Reset.setFixedHeight(40)
        self.Reset.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.Reset.move(350,20)
        self.Reset.clicked.connect(self.reset_fn)

        self.button_sy= QPushButton()                
        self.button_sy.setFixedWidth(100)
        self.button_sy.setFixedHeight(40)
        self.button_sy.move(self.xlab,self.val_yb_sy)
        self.button_sy.setText("Adresse:")
        
        
        

        self.nom = QLabel(self)
        self.nom.setText("Mettre la tare")
        self.nom.move(self.xlab,self.val_yb_sy+200)
        self.nom_ = QtWidgets.QLineEdit(self)
        self.nom_.move(100,20)
        self.nom_.setFixedWidth(100)
        self.nom_.setFixedHeight(30)


        self.button_sy.clicked.connect(lambda:self.fun(0))


       
       
        #self.button_sy.setStyleSheet('color: rgb(204, 204, 0);background-color: rgb(0, 0, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      

       

        self.show()
        self.initUI()      
    def fun(self,i):
        print("ok")

    def reset_fn(self):


        try:
            GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
            # Create an object hx which represents your real hx711 chip
            # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
            hx = HX711(dout_pin=21, pd_sck_pin=20)
            # measure tare and save the value as offset for current channel
            # and gain selected. That means channel A and gain 128
            err = hx.zero()
            # check if successful
            if err:
                raise ValueError('Tare is unsuccessful.')

            reading = hx.get_raw_data_mean()
            if reading:  # always check if you get correct value or only False
                # now the value is close to 0
                print('Data subtracted by offset but still not converted to units:',
                      reading)
            else:
                print('invalid data', reading)

            # In order to calculate the conversion ratio to some units, in my case I want grams,
            # you must have known weight.

            self.nom2 = QLabel(self)
            self.nom2.setText("Mettre la tare2")
            self.nom2.move(self.xlab,self.val_yb_sy+100)
            self.nom2.setText("mettre le poids connu sur la balance,puis appuyez sur entrée")
            self.nom2.show()

            
            input('Put known weight on the scale and then press Enter')
   
            reading = hx.get_data_mean()
            if reading:
                print('Mean value from HX711 subtracted by offset:', reading)
                self.nom.setText("écrivez combien de grammes et appuyez sur entrée")

            
                known_weight_grams = input(
                    'Write how many grams it was and press Enter: ')
                self.nom.setText("écrivez combien de grammes et appuyez sur ")

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
            else:
                raise ValueError('Cannot calculate mean value. Try debug mode. Variable reading:', reading)

            # Read data several times and return mean value
            # subtracted by offset and converted by scale ratio to
            # desired units. In my case in grams.
            print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
            input('Press Enter to begin reading')
            print('Current weight on the scale in grams is: ')
           
            print(hx.get_weight_mean(20), 'g')

        except Exception as e:
            print(e)

        finally:
            GPIO.cleanup()


 
    def initUI(self):    
       
        self.setGeometry(320, 140, 470, 320)  



       
        self.setWindowTitle('Configurations Adresse')    


class Widget(QWidget):
   

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Vous voulez vraiment quitter l'application ?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
           
   
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.resize(703, 350)
        self.initUI()
        #self.draw_layout()

       
       

    def initUI(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
        timer.start(500)
        self.setGeometry(0,45,810,415)
        self.setWindowTitle("Seringue")
       
       
        self.reeltimeText=QtWidgets.QLabel(self)
        #self.reeltimeText.move(int(Width_champ/2),10)
        self.reeltimeText.move(400,5)
        self.reeltimeText.resize(100,45)
        self.reeltimeText.setStyleSheet('color: rgb(0, 0, 0);font: 15pt Helvetica MS;')

        self.combo_port = QtWidgets.QComboBox(self)
        self.combo_port.addItem("p1")
        self.combo_port.addItem("p2")
        self.combo_port.addItem("p3")
        self.combo_port.move(15,100)

        self.max_personnes= QtWidgets.QSpinBox(self)        
        self.max_personnes.setValue(1)
        self.max_personnes.setMinimum(1)
        self.max_personnes.setMaximum(1000000000)
        self.max_personnes.move(150,100)



       

        self.button_valid= QPushButton(self)        
        self.button_valid.setText("Valider")
        self.button_valid.setFixedWidth(100)
        self.button_valid.setFixedHeight(40)
        self.button_valid.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.button_valid.move(300,270)
        self.button_valid.clicked.connect(self.calibration)


        #self.combo_poste.activated[str].connect(self.combo_poste_return)
       
    def calibration(self):
        conf=calibration()
        conf.move(0,0)
        conf.show()            

    def Time(self):
            self.reeltimeText.setText(strftime("%H"+":"+"%M"+":"+"%S"))
                             
           
           
    def delaysecond(self):
            if self.togle==1:
                 self.togle=0
            else:
                self.togle=1
       
       



if __name__ == "__main__":
    import sys  
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = Widget()
    w.show()
    sys.exit(app.exec_())



