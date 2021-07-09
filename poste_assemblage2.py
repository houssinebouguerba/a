import pyautogui
size_a=(pyautogui.size())
import sys

Width_champ= size_a[0]
Height_champ=size_a[1]-60
#Width_champ=810
#Height_champ=415

import random


max1=100
max2=200
nom="Med_Amin"
code="EM20"
quantite_of=800# quantité
cadence=80 #100 pieces/h
tab_courbe=[cadence*0,cadence*1,cadence*2,cadence*3,cadence*4,cadence*5,cadence*6,cadence*7,cadence*0,cadence*1,cadence*2,cadence*3,cadence*4
            ,cadence*5,cadence*6,cadence*7,cadence*0,cadence*1,cadence*2,cadence*3,cadence*4,cadence*5,cadence*6,cadence*7]#courbe théorique 
heur_travail=8
print(((3600/cadence)*quantite_of)/((heur_travail*3600)-(0)))
cadence_val=70
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication,QWidget
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
import pyqtgraph as pg
from pyqtgraph import PlotWidget ,plot

from ui_TestWidget import Ui_TestWidget
from time import strftime
var = False
import smbus
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from trs_roud_progress import  QRoundProgressBar_TRS
from qroundprogressbar import QRoundProgressBar
from PyQt5.QtGui import QBrush, QColor, QPalette
import board
import neopixel
pixels=neopixel.NeoPixel(board.D18,20)#led adressable adresse=GPIO 20

import RPi.GPIO as GPIO  # import GPIO
import numpy as np
b1=22 #capteur 1
b2=17
b3=27
bfc=23 #capteur bac conforme
bfnc=10 #capteur bac conforme
debit_operateur=9 #switch 
m4=11



GPIO.setmode(GPIO.BCM)
GPIO.setup(b1,GPIO.IN)
GPIO.setup(b2,GPIO.IN)
GPIO.setup(b3,GPIO.IN)
GPIO.setup(bfc,GPIO.IN)
GPIO.setup(bfnc,GPIO.IN)
GPIO.setup(debit_operateur,GPIO.IN)
GPIO.setup(m4,GPIO.IN)

import serial
import configparser
import os
import time
time_intrval=['00:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00','07:00:00','08:00:00','09:00:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:00:00',
              '16:00:00','17:00:00','18:00:00','19:00:00','20:00:00','21:00:00','22:00:00','23:00:00']
from PyQt5 import QtCore, QtWidgets, uic

        
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)

from dateutil import parser
import sys

from functools import partial

# Import QApplication and the required widgets from PyQt5.QtWidgets
from os import listdir
from os.path import isfile, join
import pygame
t1=8 #temps poste1 heur
t1_m=0#temps poste1 minutes
t2=16#temps poste2
t2_m=0
t3=23#temps poste3
t3_m=0
interval1=time_intrval[t1:t1+8]
interval2=time_intrval[t2:t2+8]
interval3=time_intrval[0:8]
time_intrval2=interval1+interval2+interval3
now=datetime.datetime.now()
date_demain=datetime.datetime.now()
date_demain += datetime.timedelta(days=1)

t1_s=now.replace(hour=t1, minute=t1_m, second=00, microsecond=0)#debit  poste1
t1_f=now.replace(hour=t2, minute=t2_m, second=00, microsecond=0)#fin poste1
t2_s=now.replace(hour=t2, minute=t2_m, second=00, microsecond=0)
t2_f=now.replace(hour=t3, minute=t3_m, second=00, microsecond=0)
t3_s=now.replace(hour=t3, minute=t3_m, second=00, microsecond=0)
t3_f=date_demain.replace(hour=t1, minute=t1_m, second=00, microsecond=0)

print(date_demain)

def update_postes(valeurs,post_1):
    try:
        
        selrq="select * from postes where poste ='"+str(post_1)+"'"
        #selrq2="INSERT INTO valeurs (val,marche_arret,m1,m2,m3) VALUES (20,1,0,1,0)"
        val=cursor.execute(selrq)
        len_=len(cursor.fetchall())
        if len_==0:
            selrq2="INSERT INTO postes (debit_time,fin_time,poste) VALUES (%s,%s,%s)"
            cursor.execute(selrq2,valeurs)
            connection.commit()

        else:
            sql = "UPDATE postes  SET debit_time = %s ,fin_time =%s  where poste= %s"
            cursor.execute(sql,valeurs)
            connection.commit()                  
    except Exception as e:
        print(e)



try:#connection serveur
    connection = mysql.connector.connect(host='localhost',
                                         database='poste_assemblage',
                                         user='root',
                                         password='admin')


    """connection = mysql.connector.connect(host='10.90.0.23',
                                         database='poste_assemblage',
                                         user='root',
                                         password='azerty123')"""


    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS "+str(code)+"_pieces (etat INT, temp_exec INT, temp_date_asm Datetime DEFAULT current_timestamp,poste TEXT,date Date DEFAULT current_timestamp)")
    cursor.execute("CREATE TABLE IF NOT EXISTS "+str(code)+"_satr_time (satart_time Datetime,end_time Datetime)")
    cursor.execute("CREATE TABLE IF NOT EXISTS "+str(code)+"_arret (type Text, temp_Arret Text,date_arret Datetime DEFAULT current_timestamp,poste Text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS postes (poste Text,debit_time Datetime,fin_time Datetime)")
    cursor.execute("CREATE TABLE IF NOT EXISTS of (num Text,descrip Text ,date Datetime,quantite INT,article Text,lot Text)")
    req="SELECT count(*) FROM "+str(code)+"_pieces WHERE temp_date_asm BETWEEN '2020-09-24 08:00:00' and '2020-10-24 09:00:00'"
    
    cursor.execute(req)
    res=cursor.fetchone()[0]
    print(res)
    #INSERT INTO `of`(`num`, `descrip`, `date`, `quantite`, `article`, `lot`) VALUES ('of_12_local','of_fin_prod','2020-10-10 10:10:10',8000,'aricle_of123','lot_123')
    
    update_postes((t1_s,t1_f,'POSTE 1'),'POSTE 1') #mise a jour  temps debit/fin poste 
    update_postes((t2_s,t2_f,'POSTE 2'),'POSTE 2')
    update_postes((t3_s,t3_f,'POSTE 3'),'POSTE 3')    
    
    req2="SELECT debit_time from postes "
    cursor.execute(req2)
    p2=cursor.fetchall()       
    post1_=str(p2[0][0]).split(" ")[1]
    post2_=str(p2[1][0]).split(" ")[1]
    post3_=str(p2[2][0]).split(" ")[1]
    print(str(post1_).split(":")[0])
    connection.commit()
    
    req4="SELECT num from of "
    cursor.execute(req4)
    num_of=cursor.fetchone()[0]
    print(num_of)
    req4="SELECT descrip from of "
    cursor.execute(req4)
    descrip_of=cursor.fetchone()[0]

    req4="SELECT quantite from of "
    cursor.execute(req4)
    quantite_of=cursor.fetchone()[0]
    
    req4="SELECT article from of "
    cursor.execute(req4)
    article_of=cursor.fetchone()[0]

    req4="SELECT lot from of "
    cursor.execute(req4)
    lot_of=cursor.fetchone()[0]

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))





def save_Arret(data,code):
    try:
        req="INSERT INTO "+str(code)+"_arret(type, temp_Arret,poste) VALUES (%s,%s,%s)"
        cursor.execute(req,data)
        connection.commit()
    except Exception as e :
        print(e)

def select_val_hour():#compteur piéces pour  chaque heurs
    t=((datetime.datetime.now()))
    x=[]
    for i in range (len(time_intrval)):
        if int(time_intrval[i].split(':')[0])<=int(t.hour):
            #print(time_intrval[i])
            
            if int(t.hour)==23:
                print('hour')
                req="SELECT count(*) FROM "+str(code)+"_pieces WHERE temp_date_asm BETWEEN '"+str(t.date())+" "+str(time_intrval[i])+"' and '"+str(t.date())+" 23:59:59'"
            else:
                
                req="SELECT count(*) FROM "+str(code)+"_pieces WHERE temp_date_asm BETWEEN '"+str(t.date())+" "+str(time_intrval[i])+"' and '"+str(t.date())+" "+str(time_intrval[i+1])+"'"
            
            cursor.execute(req)
            res=cursor.fetchone()[0]
            x.append(res)
    return x            
            
print(select_val_hour())
print(select_val_hour()[0:8])
print(select_val_hour()[8:16])
print(select_val_hour()[16:24])
def select_Arret(poste):
    t=((datetime.datetime.now()))
    x=[]
    for i in range (len(time_intrval)):
        if int(time_intrval[i].split(':')[0])<=int(t.hour):
            #print(time_intrval[i])
            req="SELECT temp_Arret FROM "+str(code)+"_arret WHERE date_arret BETWEEN '"+str(t.date())+" "+str(time_intrval[i])+"' and '"+str(t.date())+" "+str(time_intrval[i+1])+"' and poste = %s"
            cursor.execute(req,poste)
            res=cursor.fetchall()
            x.append(res)
    return x
def somme_arret(y):
    h=[]
    for i in y:
        if len(i)>0:
            for j in i:
                h.append(int(j[0]))
    return sum(h)
def select_count(etat,code):
        req="SELECT  count(*) from  "+str(code)+"_pieces WHERE etat= %s and date= %s and poste= %s"
        cursor.execute(req,etat)
        c=cursor.fetchone()[0]
        return c
def select_time_poste(poste):
        req="SELECT  debit_time,fin_time from postes WHERE poste= %s "
        cursor.execute(req,poste)
        c1=cursor.fetchall()[0]
        

        #c1=str(c1).split(" ")[1]
        
        #c2=cursor.fetchone()[1]
        #c2=str(c2).split(" ")[1]        
        return c1

#print("###########################",select_time_poste((("POSTE 1"),)))

def save_data(data,code):
    try:
        req="INSERT INTO  "+str(code)+"_pieces (etat, temp_exec,poste) VALUES (%s,%s,%s)"
        cursor.execute(req,data)
        connection.commit()
    except Exception as e :
        print(e)


def postes(time,post1_,post2_,post3_):#returne poste
        
        now = datetime.datetime.now()
        t1=now.replace(hour=int(str(post1_).split(":")[0]), minute=int(str(post1_).split(":")[1]), second=int(str(post1_).split(":")[2]), microsecond=0)
        t2=now.replace(hour=int(str(post2_).split(":")[0]), minute=int(str(post2_).split(":")[1]), second=int(str(post2_).split(":")[2]), microsecond=0)
        t3=now.replace(hour=int(str(post3_).split(":")[0]), minute=int(str(post3_).split(":")[1]), second=int(str(post3_).split(":")[2]), microsecond=0)

        
        if t3<time or time<t1:
                poste='POSTE 3'
        if t1<=time<=t2:
                poste='POSTE 1'
        if t2<time<=t3:
                poste='POSTE 2'

        
        return poste

def update_postes(valeurs,post_1):
    try:
        
        selrq="select * from postes where poste ='"+str(post_1)+"'"
        #selrq2="INSERT INTO valeurs (val,marche_arret,m1,m2,m3) VALUES (20,1,0,1,0)"
        val=cursor.execute(selrq)
        len_=len(cursor.fetchall())
        if len_==0:
            selrq2="INSERT INTO postes (debit_time,fin_time,poste) VALUES (%s,%s,%s)"
            cursor.execute(selrq2,valeurs)
            connection.commit()

        else:
            sql = "UPDATE postes  SET debit_time = %s ,fin_time =%s  where poste= %s"
            cursor.execute(sql,valeurs)
            connection.commit()                  
    except Exception as e:
        print(e)
update_postes((t1_s,t1_f,'POSTE 1'),'POSTE 1')
update_postes((t2_s,t2_f,'POSTE 2'),'POSTE 2')
update_postes((t3_s,t3_f,'POSTE 3'),'POSTE 3')
def update_value(valeurs):
    try:
        
        selrq="select * from "+str(code)+"_satr_time"
        #selrq2="INSERT INTO valeurs (val,marche_arret,m1,m2,m3) VALUES (20,1,0,1,0)"
        val=cursor.execute(selrq)
        len_=len(cursor.fetchall())
        if len_==0:
            selrq2="INSERT INTO "+str(code)+"_satr_time (satart_time,end_time) VALUES (%s,%s)"
            cursor.execute(selrq2,valeurs)
            connection.commit()
            
        else:
            sql = "UPDATE "+str(code)+"_satr_time  SET satart_time = %s ,end_time=%s"
            cursor.execute(sql,valeurs)
            connection.commit()
    except Exception as e:
        print(e)


class Widget(QWidget):
    print("enit")
  
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
        #pic = QLabel(self)
        #pic.setGeometry(350, 30, 400, 100)
        #pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/seringue.png"))
        self.resize(703, 350)
        
        self.plt = pg.PlotWidget(title="m1")
        self.plt.setBackground("w")
        self.plt.setTitle(str("production"))            
        self.data=[]
        self.data2_fin=[]
        self.data1_fin=[]
        self.data2 = []
        self.curve = self.plt.plot(pen={'color':'r','width':3},label="c1")
        self.curve2 = self.plt.plot(pen={'color':'b','width':3})

        v=self.plt.getViewBox()        
        v.setBackgroundColor((255,255,255))
        self.line = self.plt.addLine(x=0)
        
        
        
        self.initUI()
        self.draw_layout()
       

    def initUI(self):
        self.a=0     
        
        self.start_etat=0
        self.time_satat=0
        self.up=0 #indicateur de debit/fin  cycle 
        self.debit_op=time.time()#rien faire
        self.aux=0 #indicateur switch
        self.etat_m1=0 #etat de marche 1      
        self.etat_m2=0     
        self.etat_m3=0       
        self.etat_m4=0      
        self.etat_m5=0
        self.nb_conforme=0 #nombre  conforme
        self.nb_non_conforme=0
        self.etat_compteur_conform=0 #indicateur d'enregistrement conforme
        self.etat_compteur_non_conform=0 #indicateur d'enregistrement non conforme
        self.val_bar=0 # temps d'execution de tache 
        
        self.arret_1_etat=0  #etats des arret      
        self.arret_2_etat=0        
        self.arret_3_etat=0        
        self.arret_4_etat=0        
        self.marche_etat=1        
 
        self.arret_1_time=0# debit temps d'arret 1        
        self.arret_2_time=0        
        self.arret_3_time=0        
        self.arret_4_time=0
        self.compteur_prod=0
        
        
        self.arret1_time=0# temps d'arret 1          
        self.arret2_time=0        
        self.arret3_time=0        


        self.arret_1_click_time=0 #rien faire       
        self.arret_2_click_time=0        
        self.arret_3_click_time=0        
        self.arret_4_click_time=0
        self.i=0
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
        timer.start(30000)#temps réel

        arret_time_fn = QtCore.QTimer(self)
        arret_time_fn.timeout.connect(self.arret_time)
        arret_time_fn.start(1000) #temps d'arret 

        progress_ = QtCore.QTimer(self)
        progress_.timeout.connect(self.progress_val)
        progress_.start(1000)#temps d'execution du tache

        etats_ = QtCore.QTimer(self)
        etats_.timeout.connect(self.etats)
        etats_.start(5) #lire capteurs 

        update_graph_ = QtCore.QTimer(self)
        update_graph_.timeout.connect(self.update_graph)
        update_graph_.start(1200)# mise a jour courbe de production 

        performance_ = QtCore.QTimer(self)
        performance_.timeout.connect(self.performance)
        performance_.start(10000) #mise a jour bar performance
       
        self.setGeometry(0,45,Width_champ, Height_champ)
        #self.setGeometry(0,45,810,415)
        self.setWindowTitle("Poste d'assemblage")
        self.setWindowIcon(QtGui.QIcon(""))
       
        self.pattern = '{0:02d}:{1:02d}'





        self.muni_bar=QtWidgets.QLabel(self)
        self.muni_bar.move(0,0)
        self.muni_bar.resize(int(Width_champ),60)
        self.muni_bar.setStyleSheet('color: rgb(0, 255, 0);background-color: rgb(60, 60, 60);font: 20pt Helvetica MS;')
        #self.muni_bar.setText(postes(datetime.datetime.now()))
        
        self.num_OF_lb=QtWidgets.QLabel(self)
        self.num_OF_lb.move(20,5)
        self.num_OF_lb.setStyleSheet('color: rgb(200, 200, 200);background-color: rgb(60, 60, 60);font: 10pt Helvetica MS;')
        self.num_OF_lb.setText("NUMERO OF")
        
        self.num_OF=QtWidgets.QLabel(self)
        self.num_OF.move(20,35)
        self.num_OF.resize(150,20)                
        self.num_OF.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(60, 60, 60);font: 13pt Helvetica MS;')
        self.num_OF.setText(str(num_of))
        


        
        self.description_lb=QtWidgets.QLabel(self)
        self.description_lb.move(200,5)
        self.description_lb.setStyleSheet('color: rgb(200, 200, 200);background-color: rgb(60, 60, 60);font: 10pt Helvetica MS;')
        self.description_lb.setText("DESCRIPTION ")
        
        self.description=QtWidgets.QLabel(self)
        self.description.move(200,35)
        self.description.resize(150,20)                
        self.description.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(60, 60, 60);font: 13pt Helvetica MS;')
        self.description.setText(str(descrip_of))



        
        self.QUANTITE_lb=QtWidgets.QLabel(self)
        self.QUANTITE_lb.move(500,5)
        self.QUANTITE_lb.setStyleSheet('color: rgb(200, 200, 200);background-color: rgb(60, 60, 60);font: 10pt Helvetica MS;')
        self.QUANTITE_lb.setText("QUANTITE ")
        
        self.QUANTITE=QtWidgets.QLabel(self)
        self.QUANTITE.move(500,35)
        self.QUANTITE.resize(150,20)                
        self.QUANTITE.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(60, 60, 60);font: 13pt Helvetica MS;')
        self.QUANTITE.setText(str(quantite_of))
        

        self.ARTICLE_lb=QtWidgets.QLabel(self)
        self.ARTICLE_lb.move(700,5)
        self.ARTICLE_lb.setStyleSheet('color: rgb(200, 200, 200);background-color: rgb(60, 60, 60);font: 10pt Helvetica MS;')
        self.ARTICLE_lb.setText("ARTICLE ")
        
        self.ARTICLE=QtWidgets.QLabel(self)
        self.ARTICLE.move(700,35)
        self.ARTICLE.resize(150,20)                
        self.ARTICLE.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(60, 60, 60);font: 13pt Helvetica MS;')
        self.ARTICLE.setText(str(article_of))


        self.lot_lb=QtWidgets.QLabel(self)
        self.lot_lb.move(880,5)
        self.lot_lb.setStyleSheet('color: rgb(200, 200, 200);background-color: rgb(60, 60, 60);font: 10pt Helvetica MS;')
        self.lot_lb.setText("LOT ")
        
        self.lot=QtWidgets.QLabel(self)
        self.lot.move(880,35)
        self.lot.resize(150,20)                
        self.lot.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(60, 60, 60);font: 13pt Helvetica MS;')
        self.lot.setText(str(lot_of))
        
        
        self.operateur_lb=QtWidgets.QLabel(self)
        self.operateur_lb.move(int(Width_champ-400),5)
        self.operateur_lb.setStyleSheet('color: rgb(200, 200, 200);background-color: rgb(60, 60, 60);font: 10pt Helvetica MS;')
        self.operateur_lb.setText("OPERATEUR ")
        
        self.operateur=QtWidgets.QLabel(self)
        self.operateur.move(int(Width_champ-400),35)
        self.operateur.resize(150,20)                
        self.operateur.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(60, 60, 60);font: 13pt Helvetica MS;')
        self.operateur.setText("MED_AMIN-32lk")        


        self.reeltimeText=QtWidgets.QLabel(self)
        self.reeltimeText.move(int(Width_champ)-200,5)
        self.reeltimeText.resize(150,20)
        self.reeltimeText.setStyleSheet('color: rgb(200, 200, 200);background-color: rgb(60, 60, 60);font: 13pt Helvetica MS;')
        self.reeltimeText.setText(strftime("%H"+":"+"%M"))
        
        self.lab_indicateurs1=QtWidgets.QLabel(self)
        self.lab_indicateurs1.setFixedWidth(700)
        self.lab_indicateurs1.setFixedHeight(50)
        self.lab_indicateurs1.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(153, 153, 220);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs1.setText("                             INDICATEURS")        
        self.lab_indicateurs1.move(20,70)

        self.lab_indicateurs2=QtWidgets.QLabel(self)
        self.lab_indicateurs2.setFixedWidth(345)
        self.lab_indicateurs2.setFixedHeight(260)
        self.lab_indicateurs2.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs2.move(20,130)

        self.lab_indicateurs3=QtWidgets.QLabel(self)
        self.lab_indicateurs3.setFixedWidth(345)
        self.lab_indicateurs3.setFixedHeight(260)
        self.lab_indicateurs3.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs3.move(375,130)

        self.lab_quantite_bon=QtWidgets.QLabel(self)
        self.lab_quantite_bon.setFixedWidth(230)
        self.lab_quantite_bon.setFixedHeight(30)
        self.lab_quantite_bon.setText("     QUANTITE BONNE")
        self.lab_quantite_bon.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_quantite_bon.move(490,130)

        self.conforme=QtWidgets.QLabel(self)
        self.conforme.setText(""+str(self.nb_conforme))
        self.conforme.setFixedWidth(150)
        self.conforme.setFixedHeight(50)
        self.conforme.setStyleSheet('color: rgb(50, 205, 50);background-color: rgb(255, 255, 255);font: 25pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.conforme.move(570,160)


        self.lab_quantite_rebut=QtWidgets.QLabel(self)
        self.lab_quantite_rebut.setFixedWidth(230)
        self.lab_quantite_rebut.setFixedHeight(30)
        self.lab_quantite_rebut.setText("     QUANTITE REBUT")
        self.lab_quantite_rebut.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_quantite_rebut.move(490,220)



        self.non_conforme=QtWidgets.QLabel(self)
        self.non_conforme.setText("      "+str(self.nb_non_conforme))
        self.non_conforme.setFixedWidth(150)
        self.non_conforme.setFixedHeight(50)
        self.non_conforme.setStyleSheet('color: rgb(255, 30, 30);background-color: rgb(255, 255, 255);font: 25pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.non_conforme.move(570,250)

        self.CADENCE_LB=QtWidgets.QLabel(self)
        self.CADENCE_LB.setFixedWidth(230)
        self.CADENCE_LB.setFixedHeight(30)
        self.CADENCE_LB.setText("           CADENCE")
        self.CADENCE_LB.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.CADENCE_LB.move(490,310)        


        self.CADENCE=QtWidgets.QLabel(self)
        self.CADENCE.setFixedWidth(150)
        self.CADENCE.setFixedHeight(50)
        self.CADENCE.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 25pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.CADENCE.move(570,340)
        

        self.progress= QRoundProgressBar_TRS(self)
        

        gradientPoints5 = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        self.progress.setDataColors(gradientPoints5)        
        #self.progress.setValue(2000.5)
        self.progress.setStyleSheet("background-color: rgb(255, 255, 255)")           
        
        self.progress.resize(180,180)
        self.progress.move(100,150)


        self.TRS=QtWidgets.QLabel(self)
        self.TRS.setText("TRS")
        self.TRS.setFixedWidth(100)
        self.TRS.setFixedHeight(50)
        self.TRS.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.TRS.move(160,340)
        

        self.lab_indicateurs5=QtWidgets.QLabel(self)
        self.lab_indicateurs5.setFixedWidth(700)
        self.lab_indicateurs5.setFixedHeight(160)
        self.lab_indicateurs5.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs5.move(20,400)
        


        self.lab_indicateurs6=QtWidgets.QLabel(self)
        self.lab_indicateurs6.setFixedWidth(700)
        self.lab_indicateurs6.setFixedHeight(540)
        self.lab_indicateurs6.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs6.move(800,130)
        
        
        self.lab_indicateurs7=QtWidgets.QLabel(self)
        self.lab_indicateurs7.setFixedWidth(700)
        self.lab_indicateurs7.setFixedHeight(50)
        self.lab_indicateurs7.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(153, 153, 220);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs7.setText("                             TEMPS")        
        self.lab_indicateurs7.move(800,70)




        self.lab_bar_0=QtWidgets.QLabel(self)
        self.lab_bar_0.resize(150,30)
        self.lab_bar_0.move(820,130)
        self.lab_bar_0.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 10pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.lab_bar_0.setText(" Temps (s)")
        
        self.bar= QProgressBar(self) 
        self.bar.setGeometry(820, 160, 650, 30)
        self.bar.setValue(self.val_bar)
        self.bar.setMaximum(max1)
        self.bar.setAlignment(Qt.AlignCenter) 
        self.bar.setFormat(str(self.val_bar)+" s")
        self.bar.setMaximum(max1)
        self.bar.setStyleSheet("QProgressBar""{""background-color : rgb(100, 100, 100);""border  : 0px solid black""}""QProgressBar::chunk""{""background : rgb("+str(10)+", "+str(200)+","+str(0)+");""}") 


        self.lab_bar_err=QtWidgets.QLabel(self)
        self.lab_bar_err.resize(100,30)
        self.lab_bar_err.move(1400,130)
        self.lab_bar_err.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 12pt Helvetica MS;border : 3px; border-radius : 10px; ')           


        self.round1=QtWidgets.QLabel(self)
        self.round1.resize(80,45)
        self.round1.move(820,200)
        self.round1.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.round1.setText(" E1")
        
        self.round2=QtWidgets.QLabel(self)
        self.round2.resize(80,45)
        self.round2.move(960,200)
        self.round2.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.round2.setText(" E2")


        self.round3=QtWidgets.QLabel(self)
        self.round3.resize(80,45)
        self.round3.move(1100,200)
        self.round3.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.round3.setText(" E3")
        
        self.round4=QtWidgets.QLabel(self)
        self.round4.resize(80,45)
        self.round4.move(1240,200)
        self.round4.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.round4.setText(" PFC")        
        

        self.round5=QtWidgets.QLabel(self)
        self.round5.resize(80,45)
        self.round5.move(1380,200)
        self.round5.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.round5.setText(" PFNC")   


        
        self.lab_indicateurs10=QtWidgets.QLabel(self)
        self.lab_indicateurs10.setFixedWidth(700)
        self.lab_indicateurs10.setFixedHeight(50)
        self.lab_indicateurs10.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(153, 153, 220);font: 20pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs10.setText("             DECLARATIONS DES ARRETS")        
        self.lab_indicateurs10.move(800,680)

        self.lab_indicateurs11=QtWidgets.QLabel(self)
        self.lab_indicateurs11.setFixedWidth(700)
        self.lab_indicateurs11.setFixedHeight(250)
        self.lab_indicateurs11.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs11.move(800,740)


        self.Arret1 = QPushButton("MMP",self)                
        self.Arret1.setFixedWidth(120)
        self.Arret1.setFixedHeight(70)
        self.Arret1.move(820,750)
        self.Arret1.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(240, 248, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.Arret1.setIconSize(QSize(100,100))
        self.Arret1.clicked.connect(self.arret_1)

        self.Arret2 = QPushButton("Pause",self)                
        self.Arret2.setFixedWidth(120)
        self.Arret2.setFixedHeight(70)
        self.Arret2.move(1000,750)
        self.Arret2.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(240, 248, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.Arret2.setIconSize(QSize(100,100))
        self.Arret2.clicked.connect(self.arret_2)

        self.Arret3 = QPushButton("Autre",self)                
        self.Arret3.setFixedWidth(120)
        self.Arret3.setFixedHeight(70)
        self.Arret3.move(1200,750)
        self.Arret3.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(240, 248, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.Arret3.setIconSize(QSize(100,100))
        self.Arret3.clicked.connect(self.arret_3)


        self.Marche = QPushButton("Marche",self)                
        self.Marche.setFixedWidth(120)
        self.Marche.setFixedHeight(70)
        self.Marche.move(1370,750)
        self.Marche.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(240, 248, 255);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.Marche.setIconSize(QSize(100,100))
        self.Marche.clicked.connect(self.Marche_fn)



        self.arret_1_label=QtWidgets.QLabel(self)
        self.arret_1_label.setText("Arret1_time")
        self.arret_1_label.setFixedWidth(100)
        self.arret_1_label.setFixedHeight(50)        
        self.arret_1_label.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')              
        self.arret_1_label.move(850,820)

        self.arret_2_label=QtWidgets.QLabel(self)
        self.arret_2_label.setText("Arret1_time")
        self.arret_2_label.setFixedWidth(100)
        self.arret_2_label.setFixedHeight(50)        
        self.arret_2_label.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')              
        self.arret_2_label.move(1030,820)

        self.arret_3_label=QtWidgets.QLabel(self)
        self.arret_3_label.setText("Arret1_time")
        self.arret_3_label.setFixedWidth(100)
        self.arret_3_label.setFixedHeight(50)        
        self.arret_3_label.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')              
        self.arret_3_label.move(1220,820)

        self.marche_label=QtWidgets.QLabel(self)
        self.marche_label.setText("marche")
        self.marche_label.setFixedWidth(80)
        self.marche_label.setFixedHeight(50)        
        self.marche_label.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')              
        self.marche_label.move(1410,820)

        self.arret_label=QtWidgets.QLabel(self)
        self.arret_label.setText("Marche")
        self.arret_label.setFixedWidth(220)
        self.arret_label.setFixedHeight(50)        
        self.arret_label.setStyleSheet('color: rgb(0, 255, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')              
        self.arret_label.move(1100,860)


        



        self.lab_bar1=QtWidgets.QLabel(self)
        self.lab_bar1.resize(150,30)
        self.lab_bar1.move(30,400)
        self.lab_bar1.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 10pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.lab_bar1.setText(" Quantité (%)")


        self.lab_bar1_val=QtWidgets.QLabel(self)
        self.lab_bar1_val.resize(100,30)
        self.lab_bar1_val.move(600,400)
        self.lab_bar1_val.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 15pt Helvetica MS;border : 3px; border-radius : 10px; ')           
         
        
        self.bar1 = QProgressBar(self) 
        self.bar1.setGeometry(30, 430, 650, 15)
        self.bar1.setValue(90)
        self.bar1.setMaximum(100)
        self.bar1.setAlignment(Qt.AlignCenter) 
        self.bar1.setStyleSheet("QProgressBar""{""background-color : rgb(100, 100, 100);""border  : 0px solid black""}""QProgressBar::chunk""{""background : rgb("+str(10)+", "+str(200)+","+str(0)+");""}") 
        self.bar1.setTextVisible(False)


        self.lab_bar2=QtWidgets.QLabel(self)
        self.lab_bar2.resize(150,30)
        self.lab_bar2.move(30,450)
        self.lab_bar2.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 10pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.lab_bar2.setText(" Performance (%)")

        self.lab_bar2_val=QtWidgets.QLabel(self)
        self.lab_bar2_val.resize(100,30)
        self.lab_bar2_val.move(600,450)
        self.lab_bar2_val.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 15pt Helvetica MS;border : 3px; border-radius : 10px; ')           
 
        self.bar2= QProgressBar(self) 
        self.bar2.setGeometry(30, 480, 650, 15)
        self.bar2.setAlignment(Qt.AlignCenter) 
        self.bar2.setStyleSheet("QProgressBar""{""background-color : rgb(100, 100, 100);""border  : 0px solid black""}""QProgressBar::chunk""{""background : rgb("+str(10)+", "+str(200)+","+str(0)+");""}") 
        self.bar2.setMaximum(100)
        self.bar2.setTextVisible(False)


        self.lab_bar3=QtWidgets.QLabel(self)
        self.lab_bar3.resize(150,30)
        self.lab_bar3.move(30,500)
        self.lab_bar3.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 10pt Helvetica MS;border : 3px; border-radius : 10px; ')           
        self.lab_bar3.setText(" Disponibilité (%)")



        self.lab_bar3_val=QtWidgets.QLabel(self)
        self.lab_bar3_val.resize(100,30)
        self.lab_bar3_val.move(600,500)
        self.lab_bar3_val.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 15pt Helvetica MS;border : 3px; border-radius : 10px; ')           
 
        self.bar3= QProgressBar(self) 
        self.bar3.setGeometry(30, 530, 650, 15)
        self.bar3.setAlignment(Qt.AlignCenter) 
        self.bar3.setStyleSheet("QProgressBar""{""background-color : rgb(100, 100, 100);""border  : 0px solid black""}""QProgressBar::chunk""{""background : rgb("+str(10)+", "+str(200)+","+str(0)+");""}") 
        self.bar3.setTextVisible(False)



        self.labl_image=QtWidgets.QLabel(self)
        self.labl_image.setFixedWidth(650)
        self.labl_image.setFixedHeight(400)
        self.labl_image.setPixmap(QtGui.QPixmap('images/image1.jpg'))
        self.labl_image.move(820,250)
        
        self.lab_indicateurs12=QtWidgets.QLabel(self)
        self.lab_indicateurs12.setFixedWidth(700)
        self.lab_indicateurs12.setFixedHeight(420)
        self.lab_indicateurs12.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.lab_indicateurs12.move(20,570)
        
        """self.groupBox=QGroupBox(self)
        self.groupBox.setFixedSize(650,400)
        self.groupBox.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.gridlyout=QtWidgets.QGridLayout(self)
        
        self.win=pg.GraphicsWindow(title="l")
        self.win.setBackground("w")
        self.win.setFixedSize(600,340)
        
        self.gridlyout.addWidget(self.win,0,0)
        self.groupBox.setLayout(self.gridlyout)
        self.groupBox.move(40,580)
        self.p6=self.win.addPlot(20,40)
        
        
        
        
        
        
        self.p6.getAxis("bottom").setStyle(tickTextOffset=10)
        vb=self.p6.getViewBox()
        vb.setBackgroundColor((255,255,255))
        self.curve=self.p6.plot(pen={'color':'r','width':3},label="c1")
        self.curve2=self.p6.plot(pen={'color':'b','width':3})"""
        

        #pllot = QtCore.QTimer(self)
        #pllot.timeout.connect(self.update_graph)
        #pllot.start(1000)
        self.formGroupBox = QGroupBox(self)
        self.formGroupBox.setFixedSize(650, 400)                      
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.formGroupBox.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.gridLayout.setContentsMargins(0, 0, 0,0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.addWidget(self.plt, 0, 0)        
        self.formGroupBox.setLayout(self.gridLayout)
        self.formGroupBox.move(40,580)
        self.formGroupBox.show()


        self.poste=QtWidgets.QLabel(self)
        self.poste.move(int(Width_champ-200),35)
        self.poste.resize(150,20)
        self.poste.setStyleSheet('color: rgb(255,255, 255);background-color: rgb(60, 60, 60);font: 13pt Helvetica MS;')
        self.poste.setText(postes(datetime.datetime.now(),post1_,post2_,post3_))        
        
        
    def update_graph(self):
        poste_=postes(datetime.datetime.now(),post1_,post2_,post3_)
        val_c=select_count((1,datetime.date.today(),poste_),str(code))
        
        data=select_val_hour()        
        data_th=tab_courbe
        try:
            data1=data[8:16]
        except:
            data1=[0]
        try:
            data2=data[16:24]
        except:
            data2=[0]
            
        try:
            data3=data[0:8]
        except:
            data3=[0]            
            
        data1_fin=[]    
        data2_fin=[]    
        data3_fin=[]    
        if poste_=="POSTE 1":
            for i in range (1,len(data1)+1):data1_fin.append(sum(data1[:i]))              
            
            self.curve.setData(data1_fin)
            self.curve2.setData(data_th[:8])
        if poste_=="POSTE 2":
            for i in range (1,len(data2)+1):data2_fin.append(sum(data2[:i]))
            self.curve.setData(data2_fin)
            self.curve2.setData(data_th[:8])    
        if poste_=="POSTE 3":
            data3_fin=[]
            for i in range (1,len(data3)+1):data3_fin.append(sum(data3[:i]))               
            
            self.curve.setData(data3_fin)
            self.curve2.setData(data_th[:8]) 
          
       
    def etats(self):
            if GPIO.input(debit_operateur)==1 and self.aux==0:
                self.debit_op=time.time()
                self.aux=1
                
                if self.compteur_prod<=28 and time.time()-self.time_satat>=3:
                    self.compteur_prod=self.compteur_prod+1
                    save_data((1,self.val_bar,postes(datetime.datetime.now(),post1_,post2_,post3_)),code)
                    self.start_etat=1
                    self.time_satat=time.time()


                else:
                    self.compteur_prod=0
                print(self.compteur_prod)
                self.labl_image.setPixmap(QtGui.QPixmap('images/image'+str(self.compteur_prod)+'.jpeg'))
                


            if GPIO.input(debit_operateur)==0 :
                self.debit_op=time.time()
                self.aux=0
                
            if GPIO.input(b1)==0 and self.marche_etat==1 and self.up==0:
                self.up=1
                self.start_etat=1
                self.time_satat=time.time()
                self.etat_m1=1
                self.etat_m2=0
                self.etat_m3=0
                self.etat_m4=0
                self.etat_m5=0
                self.etat_compteur_conform=1
                self.etat_compteur_non_conform=1
                self.round1.setStyleSheet('color: rgb(255, 255, 255);background-color: lime;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round2.setStyleSheet('color: rgb(255, 255, 255);background-color: orange;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round3.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round4.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round5.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.labl_image.setPixmap(QtGui.QPixmap('images/image1.jpeg'))
                
#                 pixels[0]=(255,0,0)#allumer les leds
#                 pixels[2]=(255,255,0)
#                 pixels[4]=(0,0,0)
#                 pixels[6]=(0,0,0)
#                 pixels[8]=(0,0,0)

            
            if GPIO.input(b2)==0 and self.marche_etat==1:
                self.etat_m1=0
                self.etat_m2=1
                self.etat_m3=0
                self.etat_m4=0
                self.etat_m5=0
                self.round1.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round2.setStyleSheet('color: rgb(255, 255, 255);background-color: lime;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round3.setStyleSheet('color: rgb(255, 255, 255);background-color: orange;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round4.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round5.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.labl_image.setPixmap(QtGui.QPixmap('images/image2.jpeg'))

#                 pixels[0]=(0,0,0)#allumer les leds
#                 pixels[2]=(255,0,0)
#                 pixels[4]=(255,255,0)
#                 pixels[6]=(0,0,0)
#                 pixels[8]=(0,0,0)
                
            if GPIO.input(b3)==0 and self.marche_etat==1:
                self.etat_m1=0
                self.etat_m2=0
                self.etat_m3=1
                self.etat_m4=0
                self.etat_m5=0
                self.round1.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round2.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round3.setStyleSheet('color: rgb(255, 255, 255);background-color: lime;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round4.setStyleSheet('color: rgb(255, 255, 255);background-color: orange;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round5.setStyleSheet('color: rgb(255, 255, 255);background-color: orange;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.labl_image.setPixmap(QtGui.QPixmap('images/image3.jpeg'))
# 
#                 pixels[0]=(0,0,0)#allumer les leds
#                 pixels[2]=(0,0,0)
#                 pixels[4]=(255,0,0)
#                 pixels[6]=(255,255,0)
#                 pixels[8]=(255,255,0)

            if GPIO.input(bfc)==0 and self.marche_etat==1:
                self.up=0
                self.start_etat=0                
                self.etat_m1=0
                self.etat_m2=0
                self.etat_m3=0
                self.etat_m4=1
                self.etat_m5=0
                if self.etat_compteur_conform==1:
                    save_data((1,self.val_bar,postes(datetime.datetime.now(),post1_,post2_,post3_)),code)
                    #self.nb_conforme = self.nb_conforme + 1
                    self.etat_compteur_conform=0
                    self.val_bar=0
                self.round1.setStyleSheet('color: rgb(255, 255, 255);background-color: orange;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round2.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round3.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round4.setStyleSheet('color: rgb(255, 255, 255);background-color: lime;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round5.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.labl_image.setPixmap(QtGui.QPixmap('images/image4.jpeg'))
                """pixels[0]=(255,255,0)
                pixels[2]=(0,0,0)
                pixels[4]=(0,0,0)
                pixels[6]=(255,0,0)
                pixels[8]=(0,0,0)"""




            if GPIO.input(bfnc)==0 and self.marche_etat==1:
                self.up=0
                self.start_etat=0               
                self.etat_m1=0
                self.etat_m2=0
                self.etat_m3=0
                self.etat_m4=0
                self.etat_m5=1
                if self.etat_compteur_non_conform==1:
                    save_data((0,self.val_bar,postes(datetime.datetime.now(),post1_,post2_,post3_)),code)
                    #self.nb_non_conforme = self.nb_non_conforme + 1
                    self.etat_compteur_non_conform=0
                    self.val_bar=0

                
                
                self.round1.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round2.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round3.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round4.setStyleSheet('color: rgb(255, 255, 255);background-color: red;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.round5.setStyleSheet('color: rgb(255, 255, 255);background-color: lime;font: 20pt Helvetica MS;border : 3px; border-radius : 10px; ')
                self.labl_image.setPixmap(QtGui.QPixmap('images/image4.jpg'))                

#                 pixels[0]=(255,255,0)
#                 pixels[2]=(0,0,0)
#                 pixels[4]=(0,0,0)
#                 pixels[6]=(0,0,0)
#                 pixels[8]=(255,0,0)


    def Time(self):
            self.poste.setText(postes(datetime.datetime.now(),post1_,post2_,post3_))
            self.reeltimeText.setText(strftime("%H"+":"+"%M"))
            now=datetime.datetime.now()
            t1_s=now.replace(hour=t1, minute=t1_m, second=00, microsecond=0)#debit  poste1
            t1_f=now.replace(hour=t2, minute=t2_m, second=00, microsecond=0)#fin poste1
            t2_s=now.replace(hour=t2, minute=t2_m, second=00, microsecond=0)
            t2_f=now.replace(hour=t3, minute=t3_m, second=00, microsecond=0)
            t3_s=now.replace(hour=t3, minute=t3_m, second=00, microsecond=0)
            t3_f=date_demain.replace(hour=t1, minute=t1_m, second=00, microsecond=0)
            update_postes((t1_s,t1_f,'POSTE 1'),'POSTE 1') #mise a jour  temps debit/fin poste 
            update_postes((t2_s,t2_f,'POSTE 2'),'POSTE 2')
            update_postes((t3_s,t3_f,'POSTE 3'),'POSTE 3')    


    def performance(self):
                now1 = datetime.datetime.now()
                poste1=postes(datetime.datetime.now(),post1_,post2_,post3_)#poste

                t_p1_=select_time_poste(((str(poste1)),))
                print(t_p1_)
                t_p1=now1.replace(hour=int((t_p1_)[0].hour), minute=int((t_p1_)[0].minute), second=int((t_p1_)[0].second))#temps debit poste 

                #t_p1=now1.replace(hour=int(str(t_p1_).split(":")[0]), minute=int(str(t_p1_).split(":")[1]), second=int(str(t_p1_).split(":")[2]))#temps debit poste 

                som_arret=somme_arret(select_Arret((postes(datetime.datetime.now(),post1_,post2_,post3_),)))#somme des arretes
                val_c=select_count((1,datetime.date.today(),postes(datetime.datetime.now(),post1_,post2_,post3_)),str(code)) #valeur conforme
                self.lab_bar2_val.setText(str("%.2f" %(((60/cadence)*val_c)/((int(time.time()-t_p1.timestamp())/60)-((som_arret+self.arret_1_time +
                                                                                                            self.arret_2_time +self.arret_3_time )/60))*100))+" %")
                #self.lab_bar2_val.setText(str(int(((60/cadence)*val_c)/((int(time.time()-self.debit_op)/60)-(somme_arret(select_Arret())/60)))*100)+" %")
                if int((((60/cadence)*val_c)/((int(time.time()-t_p1.timestamp())/60)-((som_arret+self.arret_1_time + self.arret_2_time +self.arret_3_time )/60))*100))>=100:
                        self.bar2.setValue(100)
                else:
                        self.bar2.setValue(int((((60/cadence)*val_c)/((int(time.time()-t_p1.timestamp())/60)-((som_arret+self.arret_1_time +
                                                                                                            self.arret_2_time +self.arret_3_time )/60))*100)))
                self.bar3.setValue(int(100*((int(time.time()-t_p1.timestamp())-(som_arret+self.arret_1_time + self.arret_2_time +self.arret_3_time ))
                                        /int(time.time()-t_p1.timestamp()))))
                self.lab_bar3_val.setText(str("%.2f" %(100*((int(time.time()-t_p1.timestamp())-(som_arret+self.arret_1_time + self.arret_2_time
                                                                                    +self.arret_3_time ))/int(time.time()-t_p1.timestamp()))))+" %")
    def arret_time(self):
        now = datetime.datetime.now()
        poste=postes(datetime.datetime.now(),post1_,post2_,post3_)#poste
        val_c=select_count((1,datetime.date.today(),poste),str(code))#valeur conforme
        val_nc=select_count((0,datetime.date.today(),poste),str(code))#valeur non conforme
        self.non_conforme.setText(" "+str(val_nc))
        self.conforme.setText(" "+str(val_c))
        self.bar1.setValue((val_c*100)/quantite_of)#quantite (%)
        self.lab_bar1_val.setText(str("%.2f" %((val_c*100)/quantite_of))+" %")#bar quantite (%)
        #self.marche_label.setText(str(datetime.timedelta(seconds=int(time.time()-select_time_poste((("poste1"),))))))
        t_p_=select_time_poste(((str(poste)),))
        t_p_s=str(t_p_[0]).split(" ")[1]        
        t_p_f=str(t_p_[1]).split(" ")[1]
        t_p=now.replace(hour=int(str(t_p_s).split(":")[0]), minute=int(str(t_p_s).split(":")[1]), second=int(str(t_p_s).split(":")[2]))#temps debit poste 
        tr=str(datetime.datetime.now()-t_p).split(".")[0] #temps passeé par poste 
        hr=int(tr.split(':')[0])+int(tr.split(':')[1])/60+int(tr.split(':')[2])/3600 #temps passeé par poste en heures
        hs=int(tr.split(':')[0])*3600+int(tr.split(':')[1])*60+int(tr.split(':')[2])#temps passeé par poste en secondes
        self.marche_label.setText(tr)
        self.progress.setValue(100*((val_c*3600/cadence)/hs))#TRS
        self.CADENCE.setText(str(int((3600*val_c)/hs))+"/"+str(cadence))#CADENCE

        
        if self.arret_1_etat==1: 
                self.arret_1_time = int(time.time()-self.arret1_time)#compteur de temps en secondes
                self.arret_1_label.setText(str(datetime.timedelta(seconds=self.arret_1_time)))#affichage temps d'arret 
                
        if self.arret_2_etat==1:
                self.arret_2_time = int(time.time()-self.arret2_time)
                self.arret_2_label.setText(str(datetime.timedelta(seconds=self.arret_2_time)))
                
        if self.arret_3_etat==1:
                self.arret_3_time = int(time.time()-self.arret3_time)
                self.arret_3_label.setText(str(datetime.timedelta(seconds=self.arret_3_time)))
                
        if self.arret_4_etat==1:
                self.arret_4_time = self.arret_4_time + 1
                self.arret_4_label.setText(str(datetime.timedelta(seconds=self.arret_4_time)))
                
                
        if self.marche_etat==1:
                self.arret_1_time =0
                self.arret_2_time =0
                self.arret_3_time =0
                self.arret_4_time =0
                self.arret_1_label.setText(str(datetime.timedelta(seconds=self.arret_1_time)))                
                self.arret_2_label.setText(str(datetime.timedelta(seconds=self.arret_2_time)))                
                self.arret_3_label.setText(str(datetime.timedelta(seconds=self.arret_3_time)))                



    def progress_val(self):#temps d'execution 
        if self.start_etat==1:
                

                self.val_bar=int(time.time()-self.time_satat)   
                if self.val_bar<=max1/2:#couleur vet
                        self.bar.setValue(self.val_bar)
                        self.bar.setFormat(str(self.val_bar)+" s")
                        self.bar.setStyleSheet("QProgressBar""{""background-color : rgb(255, 255, 255);""border  : 2px solid black""}""QProgressBar::chunk""{""background : rgb("+str(10)+", "+str(200)+","+str(0)+");""}") 
                        self.lab_bar_err.setText("")
                        

    
                if self.val_bar<=(max1/4)*3  and self.val_bar>=(max1/2): #couleur jaunne 
                        self.bar.setValue(self.val_bar)
                        self.bar.setFormat(str(self.val_bar)+" s")
                        self.bar.setStyleSheet("QProgressBar""{""background-color : rgb(255, 255, 255);""border  : 2px solid black""}""QProgressBar::chunk""{""background : rgb("+str(255)+", "+str(255)+","+str(0)+");""}") 
                        self.lab_bar_err.setText("")

    
                if self.val_bar>=(max1/4)*3 and  self.val_bar<=max1: #couleur rouge
                        self.bar.setValue(self.val_bar)
                        self.bar.setFormat(str(self.val_bar)+" s")
                        self.bar.setStyleSheet("QProgressBar""{""background-color : rgb(255, 255, 255);""border  : 2px solid black""}""QProgressBar::chunk""{""background : rgb("+str(200)+", "+str(10)+","+str(0)+");""}") 
                        self.lab_bar_err.setText("")
                if self.val_bar>=max1:#temps dépasseeé 
                    self.lab_bar_err.setText(str(self.val_bar)+" s")
                        

    def arret_1(self):
                self.arret_label.setStyleSheet('color: rgb(255, 0, 0);background-color : rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
                self.arret_label.setText("MMP")
                self.arret_1_etat=1
                self.arret1_time=time.time()
                self.arret_2_etat=0        
                self.arret_3_etat=0        
                self.arret_4_etat=0        
                self.marche_etat=0
                self.arret_1_click_time=time.time()        

    def arret_2(self):
                self.arret_label.setStyleSheet('color: rgb(255, 0, 0);background-color : rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
                self.arret_label.setText("Pause")
                self.arret_1_etat=0       
                self.arret_2_etat=1
                self.arret2_time=time.time()
                
                self.arret_3_etat=0        
                self.arret_4_etat=0        
                self.marche_etat=0
                self.arret_2_click_time=time.time()        
                
                
    def arret_3(self):
                self.arret_label.setStyleSheet('color: rgb(255, 0, 0);background-color : rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
                self.arret_label.setText("Autre")
                self.arret_1_etat=0      
                self.arret_2_etat=0        
                self.arret_3_etat=1        
                self.arret_4_etat=0        
                self.marche_etat=0                     
                self.arret_3_click_time=time.time()        
                self.arret3_time=time.time()

       
                
                
    def Marche_fn(self):
                self.arret_label.setStyleSheet('color: rgb(0, 255, 0);background-color : rgb(255, 255, 255);font: 30pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
                self.arret_label.setText("Marche")
                
                self.arret_1_etat=0       
                self.arret_2_etat=0        
                self.arret_3_etat=0        
                self.arret_4_etat=0        
                self.marche_etat=1
                if self.arret_1_time !=0:
                    save_Arret(('MMP',self.arret_1_time,postes(datetime.datetime.now(),post1_,post2_,post3_)),code)#enregistrement d'arret MMP
                if self.arret_2_time !=0:
                    save_Arret(('Pause',self.arret_2_time,postes(datetime.datetime.now(),post1_,post2_,post3_)),code)
                if self.arret_3_time !=0:
                    save_Arret(('Autre',self.arret_3_time,postes(datetime.datetime.now(),post1_,post2_,post3_)),code)


        

    def draw_layout(self):
        main_layout = QHBoxLayout(self)
        #create frame of main tab
        tab_layout = QHBoxLayout()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)

        self.setStyleSheet(" background-color: rgb(230, 230, 250); ")

        """self.run = QPushButton(self)                
        self.run.setFixedWidth(65)
        self.run.setFixedHeight(60)
        self.run.move(720,350)
        self.run.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(0, 255, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.run.setIcon(QtGui.QIcon('marche.png'))
        self.run.setIconSize(QSize(100,100))


        self.configue = QPushButton(self)        
        self.configue.setFixedWidth(65)
        self.configue.setFixedHeight(60)
        self.configue.move(650,350)
        self.configue.setStyleSheet('color: rgb(0, 0, 0);background-color: rgb(204, 204, 0);font: 15pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')      
        self.configue.setIcon(QtGui.QIcon('configuration.png'))
        self.configue.setIconSize(QSize(65,60))
        self.configue.clicked.connect(self.config_f)"""
       



 

       
       
        main_layout.addLayout(tab_layout, 1)

        #draw left frame
        self.setLayout(main_layout)


 

if __name__ == "__main__":
    import sys  
    app = QApplication(sys.argv)
    app.setStyle("fusion")    
    
    w = Widget()
    w.show()
    sys.exit(app.exec_())


    #httpd = HTTPServer((IPAddr,8000), Serv)
    #httpd.serve_forever()


   



