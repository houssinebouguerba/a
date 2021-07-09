import pyautogui
size_a=(pyautogui.size())
import sys
Width_champ= size_a[0]
Height_champ=size_a[1]-60
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget

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

i2c_ADDRESS=[0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x20,0x21,0x22,0x23,0x24,0x25]

nbr_machine=["Machine1","Machine2","Machine3","Machine4","Machine5"]
nbmachine=nbr_machine[0]
pannes=['Manque matière','Réglage machine', 'Panne','Autres']
lastval = 0
value = 0



try:
        
        bus=smbus.SMBus(1)
        print("bus ok")
except:
        print("bus erreur")

        
try:
    connection = mysql.connector.connect(host='10.90.0.14',
                                         database='bas1',
                                         user='root',
                                         password='azerty123')



    mySql_insert_query = """SELECT* FROM  nb_machines """

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Pannes_Tab (Machine TEXT, Cause TEXT, Date_debit Datetime,Date_Fin Datetime)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Arret_Tab (Machine TEXT, Cause TEXT, Date_Arret Datetime)")

    cursor.execute(mySql_insert_query)
    val=cursor.fetchone()[0]
    connection.commit()
    print(val)
except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

def get_poids(offset,poids,O_val):
    try:
        GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
        hx = HX711(dout_pin=21, pd_sck_pin=20)
        ratio = offset / poids  # calculate the ratio for channel A and gain 128
        hx.set_scale_ratio(ratio)
        x=hx.get_weight_mean(1)-O_val# set ratio for current channel
        print(x, 'g')

    except :
        print('Bye :)')

def get_machine():
        cursor.execute("select nom from machines")
        nb=cursor.fetchall()
        del nbr_machine[:]
        for m in nb:
                nbr_machine.append(m[0])
        return nbr_machine
print("len",len(get_machine()))                
def postes(time):
        
        now = datetime.datetime.now()
        t1=now.replace(hour=8, minute=0, second=0, microsecond=0)
        t2=now.replace(hour=15, minute=0, second=0, microsecond=0)
        t3=now.replace(hour=23, minute=0, second=0, microsecond=0)

        
        if t3<time or time<t1:
                poste='poste3'
        if t1<=time<=t2:
                poste='poste1'
        if t2<time<=t3:
                poste='poste2'

        
        return poste

#################################
def rendement_jour_poste_machine(date,poste,machine):
    try:
        cursor.execute("SELECT "+str(poste)+"_réel,"+str(poste)+"_estimée FROM rendement_jour_poste_machine WHERE date='"+str(date)+"' and machine='"+str(machine)+"'")
        r=cursor.fetchone()
        p=(int(r[0])*100)/int(r[1])
    except:
            p=0
            
    return p

#######################################################
def rendement_jour_poste(jour,poste):
    try:

        cursor.execute("SELECT "+str(poste)+"_réel,"+str(poste)+"_estimée FROM rendement_jour_poste WHERE jour='"+str(jour)+"'")
        r=cursor.fetchone()
        p=(int(r[0])*100)/int(r[1])
    except:
            
            p=0
            
    return p
def rendement_jour(jour):
    try:
        cursor.execute("SELECT valeur_réel,valeur_estimée FROM rendement_jour WHERE jour='"+str(jour)+"'")
        r=cursor.fetchone()
        
        p=(int(r[0])*100)/int(r[1])
    except:
            
            p=0
            
    return p

def rendement_jour_machine(jour,machine):
    try:
        cursor.execute("SELECT valeur_réel,valeur_estimée FROM nb_pièces_machine WHERE machine='"+str(machine)+"' and date='"+str(jour)+"'")
        r=cursor.fetchone()
        
        p=(int(r[0])*100)/int(r[1])
    except:
            
            p=0
            
    return p


        
def select_date_debit_bobine(machine,bobine):
    try:
        cursor.execute("SELECT MAX(Date_debit) FROM debit_bobine WHERE machine='"+str(machine)+"' and bobine='"+str(bobine)+"'")
        date=cursor.fetchall()
        date=date[0][0]
        date=date.strftime('%Y-%d-%m %H:%M:%S')
    except:
            
            date="0000-00-00 00:00:00"
    return date.split()[0],date.split()[1]
        

def compteur_bobine(machine,bobine):
    try:
        cursor.execute("SELECT COUNT(*) FROM debit_bobine WHERE machine='"+str(machine)+"' and bobine='"+str(bobine)+"'")
        num=cursor.fetchall()
        num=num[0][0]
    except:
            
            num=0
    return num
        
    
#print(compteur_bobine(nbmachine,9))

#enregistrement date de l'arret

def save_debit_bobine(machine,bobine,Date_debit):
    try:
        cursor.execute("insert into  debit_bobine (machine, bobine, Date_debit) Value('"+str(machine)+"','"+str(bobine)+"','"+str(Date_debit)+"')")
        connection.commit()
    except:
        print("err2")
def save_Arret_bobine(machine,bobine,Date_Arret):
    try:
        cursor.execute("insert into  arret_bobine (machine, bobine, Date_Arret) Value('"+str(machine)+"','"+str(bobine)+"','"+str(Date_Arret)+"')")
        connection.commit()
    except:
        print("err3")

def save_arret_date(machine,cause,Date_debit):
    try:
        cursor.execute("insert into  Arret_Tab (Machine , Cause , Date_Arret  ) Value('"+str(machine)+"','"+str(cause)+"','"+str(Date_debit)+"')")
        connection.commit()
    except:
        print("err4")
#enregistremet date arret et retoude de fonctionnement et machine     
def save(machine,cause,Date_debit,Date_Fin):
    try:    
        cursor.execute("insert into  Pannes_Tab (Machine , Cause , Date_debit,Date_Fin  ) Value('"+str(machine)+"','"+str(cause)+"','"+str(Date_debit)+"','"+str(Date_Fin)+"')")
        connection.commit()

    except:
        print("err5")
def save_poids_machine(machine,bobine,poids):
    try:        
        cursor.execute("UPDATE   "+str(machine)+" set val_bobines="+str(poids)+" WHERE id="+str(bobine))
        connection.commit()

    except:
        print("err6")
        
       
"""def update_timeText(machine,round_bar,state,timer2,pattern,label):

        if (state):
            # Every time this function is called,
            #self.timeText.setStyleSheet('color: rgb(255, 255, 0);font: 10pt Helvetica MS;background-color: rgb(51, 153, 255); ;')

            # we will increment 1 centisecond (1/100 of a second)

            timer2[2]+= 1
            # Every 100 centisecond is equal to 1 second
            if (timer2[2] >= 60):

                timer2[2] = 0

                timer2[1] += 1
            # Every 60 seconds is equal to 1 min
            if (timer2[1] >= 60):

                timer2[0] += 1

                timer2[1] = 0                



            # Call the update_timeText() function after 1 centisecond


            timeString = pattern.format(timer2[0], timer2[1])

            # Update the timeText Label box with the current time

            label.setText(str(timeString))

"""

def start(state):

        state = True


    # To pause the kitchen timer

def pause(state):
        state = False

    # To reset the timer to 00:00:00

def reset(timer2,listlabel):

        timer2 = [0, 0, 0]
        listlabel.setText("00:00:00")










class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

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
        self.lastval=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
        

        """timer1 = QtCore.QTimer(self)
        timer2 = QtCore.QTimer(self)
        timer3 = QtCore.QTimer(self)
        timer4 = QtCore.QTimer(self)
        timer5 = QtCore.QTimer(self)
        timer6 = QtCore.QTimer(self)
        timer7 = QtCore.QTimer(self)
        timer8 = QtCore.QTimer(self)
        timer9 = QtCore.QTimer(self)
        timer10 = QtCore.QTimer(self)
        timer11 = QtCore.QTimer(self)
        timer12 = QtCore.QTimer(self)
        timer13 = QtCore.QTimer(self)
        timer14 = QtCore.QTimer(self)
        timer15 = QtCore.QTimer(self)
        timer16 = QtCore.QTimer(self)
        timer1.timeout.connect(lambda:update_timeText(1,1,self.state1,self.timer1,self.pattern,self.listlabel[0]))
        timer2.timeout.connect(lambda:update_timeText(1,1,self.state2,self.timer2,self.pattern,self.listlabel[1]))
        timer3.timeout.connect(lambda:update_timeText(1,1,self.state3,self.timer3,self.pattern,self.listlabel[2]))
        timer4.timeout.connect(lambda:update_timeText(1,1,self.state4,self.timer4,self.pattern,self.listlabel[3]))
        timer5.timeout.connect(lambda:update_timeText(1,1,self.state5,self.timer5,self.pattern,self.listlabel[4]))
        timer6.timeout.connect(lambda:update_timeText(1,1,self.state6,self.timer6,self.pattern,self.listlabel[5]))
        timer7.timeout.connect(lambda:update_timeText(1,1,self.state7,self.timer7,self.pattern,self.listlabel[6]))
        timer8.timeout.connect(lambda:update_timeText(1,1,self.state8,self.timer8,self.pattern,self.listlabel[7]))
        timer9.timeout.connect(lambda:update_timeText(1,1,self.state9,self.timer9,self.pattern,self.listlabel[8]))
        timer10.timeout.connect(lambda:update_timeText(1,1,self.state10,self.timer10,self.pattern,self.listlabel[9]))
        timer11.timeout.connect(lambda:update_timeText(1,1,self.state11,self.timer11,self.pattern,self.listlabel[10]))
        timer12.timeout.connect(lambda:update_timeText(1,1,self.state12,self.timer12,self.pattern,self.listlabel[11]))
        timer13.timeout.connect(lambda:update_timeText(1,1,self.state13,self.timer13,self.pattern,self.listlabel[12]))
        timer14.timeout.connect(lambda:update_timeText(1,1,self.state14,self.timer14,self.pattern,self.listlabel[13]))
        timer15.timeout.connect(lambda:update_timeText(1,1,self.state15,self.timer15,self.pattern,self.listlabel[14]))
        timer16.timeout.connect(lambda:update_timeText(1,1,self.state16,self.timer16,self.pattern,self.listlabel[15]))


#Reduced update time to fasten the change from w/ secs to w/o secs
        timer1.start(1000)
        timer2.start(1000)
        timer3.start(1000)
        timer4.start(1000)
        timer5.start(1000)
        timer6.start(1000)
        timer7.start(1000)
        timer8.start(1000)
        timer9.start(1000)
        timer10.start(1000)
        timer11.start(1000)
        timer12.start(1000)
        timer13.start(1000)
        timer14.start(1000)
        timer15.start(1000)
        timer16.start(1000)

        for i in range(16):
            self.start(i)"""
        






    def initUI(self):
        self.num=1
        self.val=0
        self.pos=0
        self.intrface=1
        self.RoundBar_list=[]
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
        timer.start(10)
 

#select value from database
        timerselect = QtCore.QTimer(self)
        timerselect.timeout.connect(self.timer_select)
        timerselect.start(3000)
#save  value from database
        timersave = QtCore.QTimer(self)
        timersave.timeout.connect(self.timer_save_poids)
        timersave.start(2000)

        
#change poste bar       
        timerbar = QtCore.QTimer(self)
        timerbar.timeout.connect(self.bar_value)
        timerbar.start(5000)
#change machine        
        chage_interface = QtCore.QTimer(self)
        chage_interface.timeout.connect(self.chage_interface_fn)
        chage_interface.start(10000)

        chage_numbobine = QtCore.QTimer(self)
        chage_numbobine.timeout.connect(self.num_bobine)
        chage_numbobine.start(20000)
        
        
        
        """timerselect = QtCore.QTimer(self)
        timerselect.timeout.connect(self.confirm)
#Reduced update time to fasten the change from w/ secs to w/o secs
        timerselect.start(40000)"""
        
        """interface_globalf = QtCore.QTimer(self)
        interface_globalf.timeout.connect(self.interface_global)
        interface_globalf.start(2000)"""
#---------Window settings --------------------------------
 
# Expanded window height by 30px
 
        self.setGeometry(0,45,Width_champ,Height_champ)
        self.setWindowTitle("Poste2")
        self.setWindowIcon(QtGui.QIcon(""))
        self.state1 = False;self.state2 = False;self.state3 = False;self.state4 = False
        self.state5 = False;self.state6 = False;self.state7 = False;self.state8 = False
        self.state9 = False;self.state10 = False;self.state11 = False;self.state12 = False
        self.state13 = False;self.state14 = False;self.state15 = False;self.state16 = False

        self.timer1=[0,0,0]
        self.timer2=[0,0,0]
        self.timer3=[0,0,0]
        self.timer4=[0,0,0]
        self.timer5=[0,0,0]
        self.timer6=[0,0,0]
        self.timer7=[0,0,0]
        self.timer8=[0,0,0]
        self.timer9=[0,0,0]
        self.timer10=[0,0,0]
        self.timer11=[0,0,0]
        self.timer12=[0,0,0]
        self.timer13=[0,0,0]
        self.timer14=[0,0,0]
        self.timer15=[0,0,0]
        self.timer16=[0,0,0]
        
        self.pattern = '{0:02d}:{1:02d}'
        self.listlabel=[]
        self.timeText1=QtWidgets.QLabel(self);self.timeText2=QtWidgets.QLabel(self);self.timeText3=QtWidgets.QLabel(self);self.timeText4=QtWidgets.QLabel(self)
        self.timeText1.setText(str("11"));self.timeText2.setText(str("22"));self.timeText3.setText(str("33"));self.timeText4.setText(str("44"))
        self.timeText5=QtWidgets.QLabel(self);self.timeText6=QtWidgets.QLabel(self);self.timeText7=QtWidgets.QLabel(self);self.timeText8=QtWidgets.QLabel(self)
        self.timeText5.setText(str("11"));self.timeText6.setText(str("22"));self.timeText7.setText(str("33"));self.timeText8.setText(str("44"))
        self.timeText9=QtWidgets.QLabel(self);self.timeText10=QtWidgets.QLabel(self);self.timeText11=QtWidgets.QLabel(self);self.timeText12=QtWidgets.QLabel(self)
        self.timeText9.setText(str("11"));self.timeText10.setText(str("22"));self.timeText11.setText(str("33"));self.timeText12.setText(str("44"))
        self.timeText13=QtWidgets.QLabel(self);self.timeText14=QtWidgets.QLabel(self);self.timeText15=QtWidgets.QLabel(self);self.timeText16=QtWidgets.QLabel(self)
        self.timeText13.setText(str("11"));self.timeText14.setText(str("22"));self.timeText15.setText(str("33"));self.timeText16.setText(str("44"))
        
        self.listlabel.append(self.timeText1);self.listlabel.append(self.timeText2);self.listlabel.append(self.timeText3);self.listlabel.append(self.timeText4)
        self.listlabel.append(self.timeText5);self.listlabel.append(self.timeText6);self.listlabel.append(self.timeText7);self.listlabel.append(self.timeText8)
        self.listlabel.append(self.timeText9);self.listlabel.append(self.timeText10);self.listlabel.append(self.timeText11);self.listlabel.append(self.timeText12)
        self.listlabel.append(self.timeText13);self.listlabel.append(self.timeText14);self.listlabel.append(self.timeText15);self.listlabel.append(self.timeText16)
        #self.listlabel[6].move(700,100)
        #self.listlabel[6].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')

        """for i  in range(4):
            #self.timeText=QtWidgets.QLabel(self)
            self.listlabel[i].move(int(Width_champ/20)+60,(int((Height_champ)/7)+35)*(i+1))
            self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')"""
        for i  in range(16):
             if i<4:
                self.listlabel[i].move((int(Width_champ/20)+60),(int((Height_champ)/7)+35)*(i+1))
                self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
             if i>=4 and i<8:
                self.listlabel[i].move((int(Width_champ/20)+130)*2,(int((Height_champ)/7)+35)*(i-4+1))
                self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
             if i>=8 and i<12:
                self.listlabel[i].move((int(Width_champ/20)+150)*3,(int((Height_champ)/7)+35)*(i-8+1))
                self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
             if i>=12:
                self.listlabel[i].move((int(Width_champ/20)+160)*4,(int((Height_champ)/7)+35)*(i-12+1))
                self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
                
        self.num_label1=QtWidgets.QLabel(self);self.num_label2=QtWidgets.QLabel(self);self.num_label3=QtWidgets.QLabel(self);self.num_label4=QtWidgets.QLabel(self);
        self.num_label5=QtWidgets.QLabel(self);self.num_label6=QtWidgets.QLabel(self);self.num_label7=QtWidgets.QLabel(self);self.num_label8=QtWidgets.QLabel(self);
        self.num_label9=QtWidgets.QLabel(self);self.num_label10=QtWidgets.QLabel(self);self.num_label11=QtWidgets.QLabel(self);self.num_label12=QtWidgets.QLabel(self);
        self.num_label13=QtWidgets.QLabel(self);self.num_label14=QtWidgets.QLabel(self);self.num_label15=QtWidgets.QLabel(self);self.num_label16=QtWidgets.QLabel(self);
        self.num_label_list=[]
        self.num_label_list.append(self.num_label1);self.num_label_list.append(self.num_label2);self.num_label_list.append(self.num_label3);self.num_label_list.append(self.num_label4);
        self.num_label_list.append(self.num_label5);self.num_label_list.append(self.num_label6);self.num_label_list.append(self.num_label7);self.num_label_list.append(self.num_label8);
        self.num_label_list.append(self.num_label9);self.num_label_list.append(self.num_label10);self.num_label_list.append(self.num_label11);self.num_label_list.append(self.num_label12);
        self.num_label_list.append(self.num_label13);self.num_label_list.append(self.num_label14);self.num_label_list.append(self.num_label15);self.num_label_list.append(self.num_label16);
        for i  in range(16):
             if i<4:
                self.num_label_list[i].move((int(Width_champ/20)+60),(int((Height_champ)/7)+35)*(i+1)+30)
                self.num_label_list[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
                self.num_label_list[i].setText(str(self.num))

             if i>=4 and i<8:
                self.num_label_list[i].move((int(Width_champ/20)+130)*2,(int((Height_champ)/7)+35)*(i-4+1)+30)
                self.num_label_list[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
                self.num_label_list[i].setText(str(self.num))

             if i>=8 and i<12:
                self.num_label_list[i].move((int(Width_champ/20)+150)*3,(int((Height_champ)/7)+35)*(i-8+1)+30)
                self.num_label_list[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
                self.num_label_list[i].setText(str(self.num))

             if i>=12:
                self.num_label_list[i].move((int(Width_champ/20)+160)*4,(int((Height_champ)/7)+35)*(i-12+1)+30)
                self.num_label_list[i].setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
                self.num_label_list[i].setText(str(self.num))

        

        
        self.nb_machine=QtWidgets.QLabel(self)        
        self.nb_machine.move(int(Width_champ/2)-50,30)
        self.nb_machine.resize(210,45)
        self.nb_machine.setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
        self.nb_machine.setText("Machine 1")

 
        self.reeltimeText=QtWidgets.QLabel(self)
        self.reeltimeText.move(int(Width_champ/2)-250,30)
        self.reeltimeText.resize(190,45)
        self.reeltimeText.setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
        self.progressBar1 = QProgressBar()
        self.progressBar1.setMaximum(28800)
        self.progressBar2 = QProgressBar()
        self.progressBar2.setMaximum(28800)
        
        self.progressBar3 = QProgressBar()
        self.progressBar3.setMaximum(28800)



    def bar_value(self):


                    now = datetime.datetime.now()
                    t1=now.replace(hour=00, minute=0, second=0, microsecond=0)
                    t2=now.replace(hour=8, minute=0, second=0, microsecond=0)
                    t3=now.replace(hour=16, minute=0, second=0, microsecond=0)     
            
                    new_time3 = (now-t3).total_seconds()
                    if new_time3<0: 
                            self.progressBar3.setValue(0)
                    if new_time3>=28800: 
                            self.progressBar3.setValue(28800)
                    if 0<new_time3<=28800: 
                            self.progressBar3.setValue(int(new_time3))
                    new_time2 = (now-t2).total_seconds()
                    if new_time2<0: 
                            self.progressBar2.setValue(0)
                    if new_time2>=28800: 
                            self.progressBar2.setValue(28800)
                    if 0<new_time2<=28800:
                            self.progressBar2.setValue(int(new_time2))
                    new_time1 = (now-t1).total_seconds()
                    if new_time1<0:
                            self.progressBar1.setValue(0)
                    if new_time1>=28800:
                            self.progressBar1.setValue(28800)
                    
                            
                    if 0<new_time1<=28800:
                            self.progressBar1.setValue(int(new_time1))
                    
                
                    

        
            
    def chage_interface_fn(self):
        try:
                
            if self.intrface <= len(get_machine())-1:
                self.intrface +=1
            else:
                self.intrface=1
            self.nb_machine.setText("Machine "+ str(self.intrface))
        except:
            self.nb_machine.setText("Erreur")
    def interface_global(self):
        self.progressBar4 = QProgressBar(self)
        self.progressBar4.setGeometry(0, 20, 450, 25)
        self.progressBar4.setValue(0)
    def timer_save_poids(self):
        for val_bob in range(16):
                try:
                                            
                    self.value=bus.read_byte(i2c_ADDRESS[val_bob])
                    self.value=((self.value*10000)/255)
                    sleep(0.05) 


                        
                    #self.value=bus.read_byte(i2c_ADDRESS[9])
                    self.lastval[val_bob]=self.value
                except:
                    self.value=self.lastval[val_bob]
                
                save_poids_machine(nbmachine,val_bob+1,self.value)

    
    def timer_select(self):
        get_poids(-32700,150,-507)
        try:
            for nbr_bo in range(16):
                   time_bobine=select_date_debit_bobine(nbr_machine[self.intrface-1],nbr_bo)
                   self.listlabel[nbr_bo].setText(str(str(time_bobine[0])+"\n"+str(time_bobine[1])))
                   
                   cmp=compteur_bobine(nbr_machine[self.intrface-1],nbr_bo)
                   self.num_label_list[nbr_bo].setText(str(cmp))
        
            mySql_insert_query = """SELECT* FROM  """+str(get_machine()[self.intrface-1])
            

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            
            self.val=cursor.fetchall()
            
            connection.commit()
            poste=postes(datetime.datetime.now())
            rendements_jours_postes_machines=rendement_jour_poste_machine (datetime.date.today(),poste,nbr_machine[self.intrface-1])
            self.RoundBar_total_M.setValue(rendements_jours_postes_machines)
            rendements_jours=rendement_jour(datetime.date.today())
            self.RoundBar_total.setValue(rendements_jours)


            
            for k in range (len(self.val)):
                
                self.RoundBar_list[k].setValue(12)
                

                #self.num_label_list[k].setText(str(self.val[k][2]))
                if  self.val[k][1] <=15 and self.val[k][5]==0 :
                    self.pause(k)
                
                if self.val[k][1] >=15 and self.val[k][5]==1:               
                    #self.reset(k)            
                    self.start(k)

        except:
            print("erré")
            

    def Time(self):
            self.reeltimeText.setText(strftime("%H"+":"+"%M"+":"+"%S"))

    def start(self,i):
        if i==0:
            self.state1 = True
        if i==1:
            self.state2 = True
        if i==2:
            self.state3 = True
        if i==3:
            self.state4 = True
        if i==4:
            self.state5 = True
        if i==5:
            self.state6 = True
        if i==6:
            self.state7 = True
        if i==7:
            self.state8 = True
        if i==8:
            self.state9 = True
        if i==9:
            self.state10 = True
        if i==10:
            self.state11 = True
        if i==11:
            self.state12 = True
        if i==12:
            self.state13 = True
        if i==13:
            self.state14 = True
        if i==14:
            self.state15 = True
        if i==15:
            self.state16 = True



    def pause(self,i):
        if i==0:
            self.state1 = False
        if i==1:
            self.state2 = False
        if i==2:
            self.state3 = False
        if i==3:
            self.state4 = False
        if i==4:
            self.state5 = False
        if i==5:
            self.state6 = False
        if i==6:
            self.state7 = False
        if i==7:
            self.state8 = False
        if i==8:
            self.state9 = False
        if i==9:
            self.state10 = False
        if i==10:
            self.state11 = False
        if i==11:
            self.state12 = False
        if i==12:
            self.state13 = False
        if i==13:
            self.state14 = False
        if i==14:
            self.state15 = False
        if i==15:
            self.state16 = False



            
    # To reset the timer to 00:00:00

    def reset(self,i):
        if i==0:
            self.timer1 = [0, 0, 0]
            self.listlabel[0].setText("00:00:00")
        if i==1:
            self.timer2 = [0, 0, 0]
            self.listlabel[1].setText("00:00:00")
        if i==2:
            self.timer3 = [0, 0, 0]
            self.listlabel[2].setText("00:00:00")
        if i==3:
            self.timer4 = [0, 0, 0]
            self.listlabel[3].setText("00:00:00")
        if i==4:
            self.timer5 = [0, 0, 0]
            self.listlabel[4].setText("00:00:00")
        if i==5:
            self.timer6 = [0, 0, 0]
            self.listlabel[5].setText("00:00:00")

        if i==6:
            self.timer7 = [0, 0, 0]
            self.listlabel[6].setText("00:00:00")
        if i==7:
            self.timer8 = [0, 0, 0]
            self.listlabel[7].setText("00:00:00")
        if i==8:
            self.timer9 = [0, 0, 0]
            self.listlabel[8].setText("00:00:00")
        if i==9:
            self.timer10 = [0, 0, 0]
            self.listlabel[9].setText("00:00:00")
        if i==10:
            self.timer11 = [0, 0, 0]
            self.listlabel[10].setText("00:00:00")
        if i==11:
            self.timer12 = [0, 0, 0]
            self.listlabel[11].setText("00:00:00")
        if i==12:
            self.timer13 = [0, 0, 0]
            self.listlabel[12].setText("00:00:00")
        if i==13:
            self.timer14 = [0, 0, 0]
            self.listlabel[13].setText("00:00:00")
        if i==14:
            self.timer15 = [0, 0, 0]
            self.listlabel[14].setText("00:00:00")
        if i==15:
            self.timer16 = [0, 0, 0]
            self.listlabel[15].setText("00:00:00")
            

    # Simple status flag
    # False mean the timer is not running
    # True means the timer is running (counting)







    def RoundBar(self,RoundBar):
        #p2 = QPalette()
        #p2.setBrush(QPalette.AlternateBase, Qt.black)
        #p2.setColor(QPalette.Text, Qt.yellow)
        #RoundBar.setPalette(p2)
        
        RoundBar.setNullPosition(QRoundProgressBar.PositionLeft)
        RoundBar.setFormat('%v')

        RoundBar.setDecimals(0)
        gradientPoints5 = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        RoundBar.setDataColors(gradientPoints5)
        self.connectToSlider(RoundBar)
    def connectToSlider(self, bar: QRoundProgressBar):
        bar.setRange(self.Slider.minimum(), self.Slider.maximum())
        bar.setValue(self.val)

        self.Slider.valueChanged.connect(bar.setValue)
        
    def draw_layout(self):
        main_layout = QHBoxLayout(self) 
        #create frame of main tab 
        tab_layout = QHBoxLayout()
        









        self.horizontalLayout = QtWidgets.QHBoxLayout(self)

        self.setStyleSheet(" background-color: rgb(23, 32, 42); ")

        self.Slider = QtWidgets.QSlider(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider.sizePolicy().hasHeightForWidth())
        self.Slider.setSizePolicy(sizePolicy)
        self.Slider.setMaximum(999)
        self.Slider.setProperty("value", 150)

        #les boutons


        self.button1 = QPushButton(self)
        self.button1.setText('Manque matière')

        self.button1.setFixedWidth(int(Width_champ/2)-100)
        self.button1.setFixedHeight(int(Height_champ/2)-50)
        self.button1.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 255, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')       
        self.button1.clicked.connect(self.on_click_b1)

        self.button2 = QPushButton(self)
        self.button2.setText('Réglage machine')        
        self.button2.setFixedWidth(int(Width_champ/2)-100)
        self.button2.setFixedHeight(int(Height_champ/2)-50)
        self.button2.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 255, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')        
        self.button2.clicked.connect(self.on_click_b2)


        self.button3 = QPushButton( self)
        self.button3.setText('Panne')        
        self.button3.setFixedWidth(int(Width_champ/2)-100)
        self.button3.setFixedHeight(int(Height_champ/2)-50)
        self.button3.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 255, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')        
        self.button3.clicked.connect(self.on_click_b3)


        self.button4 = QPushButton( self)
        self.button4.setText('Autres')        
        self.button4.setFixedWidth(int(Width_champ/2)-100)
        self.button4.setFixedHeight(int(Height_champ/2)-50)        
        self.button4.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 255, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
        self.button4.clicked.connect(self.on_click_b4)        


        self.RoundBar1 = QRoundProgressBar()        
        self.RoundBar2 = QRoundProgressBar()
        self.RoundBar3 = QRoundProgressBar()        
        self.RoundBar4 = QRoundProgressBar()
        self.RoundBar5 = QRoundProgressBar()        
        self.RoundBar6 = QRoundProgressBar()
        self.RoundBar7 = QRoundProgressBar()        
        self.RoundBar8 = QRoundProgressBar()      
        self.RoundBar9 = QRoundProgressBar()
        self.RoundBar10 = QRoundProgressBar()
        self.RoundBar11 = QRoundProgressBar()
        self.RoundBar12 = QRoundProgressBar()
        self.RoundBar13 = QRoundProgressBar()
        self.RoundBar14 = QRoundProgressBar()
        self.RoundBar15 = QRoundProgressBar()
        self.RoundBar16 = QRoundProgressBar()
        self.RoundBar_total_M = QRoundProgressBar_total()
        self.RoundBar_total = QRoundProgressBar_total()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 71, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 68, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 44, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 71, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 68, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 44, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 71, 71))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 100, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.RoundBar_total.setPalette(palette)
    







        
        self.RoundBar_list.append(self.RoundBar1);self.RoundBar_list.append(self.RoundBar2);self.RoundBar_list.append(self.RoundBar3);self.RoundBar_list.append(self.RoundBar4);
        self.RoundBar_list.append(self.RoundBar5);self.RoundBar_list.append(self.RoundBar6);self.RoundBar_list.append(self.RoundBar7);self.RoundBar_list.append(self.RoundBar8);
        self.RoundBar_list.append(self.RoundBar9);self.RoundBar_list.append(self.RoundBar10);self.RoundBar_list.append(self.RoundBar11);self.RoundBar_list.append(self.RoundBar12);
        self.RoundBar_list.append(self.RoundBar13);self.RoundBar_list.append(self.RoundBar14);self.RoundBar_list.append(self.RoundBar15);self.RoundBar_list.append(self.RoundBar16);
        for i in range(16):            
            self.RoundBar(self.RoundBar_list[i])



        
        left_frame   = QFrame(self) 
        right_frame  = QFrame(self)
        right_frame2 = QFrame(self)
        right_frame_control = QFrame(self)
        
        for m in range(16):            
            self.HLayout[m] = QtWidgets.QHBoxLayout()
            self.VLayout[m] = QtWidgets.QVBoxLayout()
            self.VLayout[m].setSpacing(0)
            self.VLayout[m].setContentsMargins(0, 0, 0, 0)        
            
            self.VLayout[m].addWidget(self.listlabel[m],0)
            self.VLayout[m].addWidget(self.num_label_list[m],1)               
            self.HLayout[m].addWidget(self.RoundBar_list[m])
            self.HLayout[m].addLayout(self.VLayout[m])
            

        self.gridLayout_0 = QtWidgets.QGridLayout(right_frame_control)
        self.gridLayout_0.addWidget(self.button1,0,0)
        self.gridLayout_0.addWidget(self.button2,0,1)
        self.gridLayout_0.addWidget(self.button3,1,0)
        self.gridLayout_0.addWidget(self.button4,1,1)


        
        self.post1=QtWidgets.QLabel("post1")
        self.post1.setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
        self.post2=QtWidgets.QLabel("post2")
        self.post2.setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
        self.post3=QtWidgets.QLabel("post3")
        self.post3.setStyleSheet('color: rgb(255, 255, 255);font: 10pt Helvetica MS;')
        

        self.gridLayout_20 = QtWidgets.QVBoxLayout(self)
        self.gridLayout_20.setContentsMargins(int(Width_champ/3), 0, int(Width_champ/3), 0)
        self.gridLayout_20.setSpacing(0)
        
        self.gridLayout_21 = QtWidgets.QVBoxLayout(right_frame)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_22 = QtWidgets.QGridLayout(self)
        self.gridLayout_22.setContentsMargins(int(Width_champ/8), int(Height_champ/16), int(Width_champ/8), int(Height_champ/10))

        self.gridLayout_22.addWidget(self.post1, 0,0,1,1)                
        self.gridLayout_22.addWidget(self.post2, 1, 0,1,1)        
        self.gridLayout_22.addWidget(self.post3, 2, 0,1,1)
        
        self.gridLayout_22.addWidget(self.progressBar1, 0,1,1,1)                
        self.gridLayout_22.addWidget(self.progressBar2, 1, 1,1,1)        
        self.gridLayout_22.addWidget(self.progressBar3, 2, 1,1,1)        
        

        
        self.gridLayout_20.addWidget(self.RoundBar_total)
        self.gridLayout_21.addLayout( self.gridLayout_20)        
        self.gridLayout_21.addLayout( self.gridLayout_22)


        
        self.gridLayout_31 = QtWidgets.QVBoxLayout(right_frame2)
        self.gridLayout_31.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_31.setSpacing(0)
        
        self.gridLayout_32 = QtWidgets.QGridLayout(self)
        self.gridLayout_32.setContentsMargins(int(Width_champ/4), 10, int(Width_champ/4), 0)
        self.gridLayout_32.addWidget(self.reeltimeText, 0,1,2,2)                
        self.gridLayout_32.addWidget(self.nb_machine, 0, 2,2,2)


        
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.gridLayout_3.setContentsMargins(0, 25, 0, 0)
        self.gridLayout_3.setSpacing(0)     

        self.gridLayout_3.addLayout( self.HLayout[0],1,0,1,1)
        self.gridLayout_3.addLayout( self.HLayout[1],1,1,1,1)        
        self.gridLayout_3.addLayout( self.HLayout[2],1,2,1,1)        
        self.gridLayout_3.addLayout( self.HLayout[3],1,3,1,1)        

        self.gridLayout_3.addLayout( self.HLayout[4],2,0,1,1)
        self.gridLayout_3.addLayout( self.HLayout[5],2,1,1,1)        
        self.gridLayout_3.addLayout( self.HLayout[6],2,2,1,1)        
        self.gridLayout_3.addLayout( self.HLayout[7],2,3,1,1)

        self.gridLayout_3.addLayout( self.HLayout[8],3,0,1,1)
        self.gridLayout_3.addLayout( self.HLayout[9],3,1,1,1)        
        self.gridLayout_3.addLayout( self.HLayout[10],3,2,1,1)        
        self.gridLayout_3.addLayout( self.HLayout[11],3,3,1,1)            

        self.gridLayout_3.addLayout( self.HLayout[12],4,0,1,1)
        self.gridLayout_3.addLayout( self.HLayout[13],4,1,1,1)        
        self.gridLayout_3.addLayout( self.HLayout[14],4,2,1,1)        
        self.gridLayout_3.addLayout( self.HLayout[15],4,3,1,1)    
        self.gridLayout_3.addWidget(self.RoundBar_total_M, 2, 4, 2, 2)

        self.gridLayout_31.addLayout(self.gridLayout_32)
        self.gridLayout_31.addLayout( self.gridLayout_3)        
        
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(right_frame_control)
        self.Stack.addWidget(right_frame2)
        self.Stack.addWidget(right_frame)

        left_frame.setFrameShape(QFrame.StyledPanel)
        right_frame.setFrameShape(QFrame.StyledPanel)
        right_frame2.setFrameShape(QFrame.StyledPanel)

        self.right_frame = right_frame2

        # split left and right
        #splitter = QSplitter(SPLIT_H)  
        splitter = QSplitter(self)
        splitter.addWidget(left_frame)
        splitter.addWidget(self.Stack)       
        splitter.setStretchFactor(1, 10)

        # add to widget
        tab_layout.addWidget(splitter)
        main_layout.addLayout(tab_layout, 1)

        #draw left frame
        self.draw_left_frame(left_frame)
        self.setLayout(main_layout)
    def on_click_b1(self):
        if self.current_st1 == 0:
            self.button1.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 255, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
            self.current_st1 = 1
            save(nbmachine,pannes[0],self.arret_manq_time,datetime.datetime.now())


        else:
            self.button1.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(255, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
            self.current_st1 = 0
            self.arret_manq_time=datetime.datetime.now()
            save_arret_date(nbmachine,pannes[0],self.arret_manq_time)
    def on_click_b2(self):
        if self.current_st2 == 0:
            self.button2.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 255, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
            self.current_st2 = 1
            save(nbmachine,pannes[1],self.arret_reglage_time,datetime.datetime.now())


        else:
            self.button2.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(255, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
            self.current_st2 = 0
            self.arret_reglage_time=datetime.datetime.now()
            save_arret_date(nbmachine,pannes[1],self.arret_reglage_time)


    def on_click_b3(self):
        if self.current_st3 == 0:
            self.button3.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 255, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
            self.current_st3 = 1
            save(nbmachine,pannes[2],self.arret_panne_time,datetime.datetime.now())


        else:
            self.button3.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(255, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
            self.current_st3 = 0
            self.arret_panne_time=datetime.datetime.now()
            save_arret_date(nbmachine,pannes[2],self.arret_panne_time)
            
            
    def on_click_b4(self):
        if self.current_st4 == 0:
            self.button4.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 255, 0);font:10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
            self.current_st4= 1
            save(nbmachine,pannes[3],self.arret_autres_time,datetime.datetime.now())
            
            

        else:
            self.button4.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(255, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
            self.current_st4 = 0
            self.arret_autres_time=datetime.datetime.now()
            save_arret_date(nbmachine,pannes[3],self.arret_autres_time)

    def num_bobine(self):
        for val_b in range(16):
                try:


                    
                    self.value=bus.read_byte(i2c_ADDRESS[val_b])
                    self.value=((reada*10000)/255)

                    sleep(0.05) 

                    self.lastval[val_b]=self.value

                except:

                    self.value=self.lastval[val_b]
                
                self.list_val[val_b]=self.value
        
        
                if self.value >= 5 and self.tag_bobin[val_b]==1:
                    print("lllc")
                    self.tag_bobin[val_b]=0
                    #self.num_bobine_9 +=1
                    #print(self.num_bobine_9) 
                    save_debit_bobine(nbmachine,val_b,datetime.datetime.now())  
                    
                    
                    
                elif self.value <= 5 and self.tag_bobin[val_b]==0:
                    print("min")
                    self.tag_bobin[val_b]=1
                    save_Arret_bobine(nbmachine,val_b,datetime.datetime.now())



        
    def draw_left_frame(self, frame):
        main_layout = QVBoxLayout(frame)

        confirm_btn = QPushButton( self)        
        confirm_btn.setText('global')
        confirm_btn.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(23, 32, 42);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
        
        confirm_btn_control = QPushButton( self)
        confirm_btn_control.setText("controle")
        confirm_btn_control.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(23, 32, 42);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')
        
        confirm_btn.setFixedWidth(60)
        confirm_btn_control.setFixedWidth(60)
        confirm_btn_control.setFixedHeight(50)        
        confirm_btn.setFixedHeight(50)        

        
        main_layout.addWidget(confirm_btn, 0)
        main_layout.addWidget(confirm_btn_control, 1)

        confirm_btn.clicked.connect(self.confirm)
        confirm_btn_control.clicked.connect(self.confirm_control)

        #main_layout.setAlignment(ALIGN_TOP)


    @pyqtSlot()
    #def TAB_VIEW_quote_search_code(self, req_quote):
    def confirm(self): #, req_quote):
        if self.currentWidgetRightFrame == 0:
            self.Stack.setCurrentIndex(1)
            self.currentWidgetRightFrame = 1
        else:
            self.Stack.setCurrentIndex(0)
            self.currentWidgetRightFrame = 0
          
    def confirm_control(self): #, req_quote):
        if self.currentWidgetRightFrame == 0:
            self.Stack.setCurrentIndex(2)
            self.currentWidgetRightFrame = 1
        else:
            self.Stack.setCurrentIndex(0)
            self.currentWidgetRightFrame = 0

if __name__ == "__main__":
    import sys  
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = Widget()
    w.show()
    sys.exit(app.exec_())


    
