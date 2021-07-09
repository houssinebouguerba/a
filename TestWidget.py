

import sys
from win32api import GetSystemMetrics
Width_champ= GetSystemMetrics(0)
Height_champ=GetSystemMetrics(1)-70
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

from PyQt5 import QtCore, QtGui, QtWidgets
from QLed import QLed
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='bas1',
                                         user='root',
                                         password='azerty123')

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

mySql_insert_query = """SELECT* FROM  nb_machines """

cursor = connection.cursor()
cursor.execute(mySql_insert_query)
val=cursor.fetchone()[0]
#cursor.execute("CREATE TABLE IF NOT EXISTS machine5 (val_bobines INTEGER, nombre INTEGER, start_time DATETIME,end_time DATETIME ,etat boolean)")

connection.commit()
print(val)


def update_timeText(machine,round_bar,state,timer2,pattern,label):

        if (state):
            # Every time this function is called,
            #self.timeText.setStyleSheet('color: rgb(255, 255, 0);font: 15pt Helvetica MS;background-color: rgb(51, 153, 255); ;')

            # we will increment 1 centisecond (1/100 of a second)
            #if timer2[2]<=6 and timer2[2]<=6 and timer2[2]<=6 or state==False :
                #self.timeText.setStyleSheet('color: rgb(255, 255, 0);font: 15pt Helvetica MS;background-color: rgb(255, 50, 50);')
               # print("hh")

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


            timeString = pattern.format(timer2[0], timer2[1], timer2[2])

            # Update the timeText Label box with the current time

            label.setText(str(timeString))



def start(state):

        state = True


    # To pause the kitchen timer

def pause(state):
        print("ici pause")

        state = False

    # To reset the timer to 00:00:00

def reset(timer2,listlabel):

        timer2 = [0, 0, 0]
        listlabel.setText("00:00:00")

class TestWidget(QWidget,Ui_TestWidget):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)

        super(TestWidget, self).__init__(parent)
        self.initUI()

        self.setupUi(self)
        
        timer1 = QtCore.QTimer(self)
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
            self.start(i)
        



        

        """self.RoundBar1.setFormat('%v')
        self.RoundBar1.setDecimals(0)
        self.connectToSlider(self.RoundBar1)

        self.RoundBar2.setNullPosition(QRoundProgressBar.PositionRight)
        self.RoundBar2.setBarStyle(QRoundProgressBar.BarStyle.PIE)
        self.connectToSlider(self.RoundBar2)

        self.RoundBar3.setFormat('%m')
        self.RoundBar3.setBarStyle(QRoundProgressBar.BarStyle.LINE)
        self.connectToSlider(self.RoundBar3)"""
        
        left_frame   = QFrame(self)
        lbLeft = QLabel(" left_frame   ", left_frame) 

        self.gridLayout_55 = QtWidgets.QGridLayout(left_frame)
        self.gridLayout_55.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_55.setSpacing(50)

        

        
        self.gridLayout_3 = QFrame(self)
        self.gridLayout_3.setContentsMargins(11, 200, 11, 11)
        #self.gridLayout_3.setSpacing(200)
        self.gridLayout_3.setObjectName("gridLayout_3")
        #right_frame2.setFixedWidth(1000)



        
        """p1 = QPalette()
        p1.setBrush(QPalette.AlternateBase, Qt.black)
        p1.setColor(QPalette.Text, Qt.yellow)
        self.RoundBar1.setPalette(p1)
        self.RoundBar1.setNullPosition(QRoundProgressBar.PositionLeft)
        self.RoundBar1.setDecimals(0)
        gradientPoints = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        self.RoundBar1.setDataColors(gradientPoints)
        self.connectToSlider(self.RoundBar1)


        p2 = QPalette()
        p2.setBrush(QPalette.AlternateBase, Qt.black)
        p2.setColor(QPalette.Text, Qt.yellow)
        self.RoundBar2.setPalette(p2)
        self.RoundBar2.setNullPosition(QRoundProgressBar.PositionLeft)
        self.RoundBar2.setDecimals(0)
        gradientPoints5 = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        self.RoundBar2.setDataColors(gradientPoints5)
        self.connectToSlider(self.RoundBar2)

        p2 = QPalette()
        p2.setBrush(QPalette.AlternateBase, Qt.black)
        p2.setColor(QPalette.Text, Qt.yellow)
        self.RoundBar3.setPalette(p2)
        self.RoundBar3.setNullPosition(QRoundProgressBar.PositionLeft)
        self.RoundBar3.setDecimals(0)
        gradientPoints5 = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        self.RoundBar3.setDataColors(gradientPoints5)
        self.connectToSlider(self.RoundBar3)


        p1 = QPalette()
        p1.setBrush(QPalette.AlternateBase, Qt.black)
        p1.setColor(QPalette.Text, Qt.yellow)
        self.RoundBar4.setPalette(p1)
        self.RoundBar4.setNullPosition(QRoundProgressBar.PositionLeft)
        self.RoundBar4.setDecimals(0)
        gradientPoints = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        self.RoundBar4.setDataColors(gradientPoints)
        self.connectToSlider(self.RoundBar4)


        p2 = QPalette()
        p2.setBrush(QPalette.AlternateBase, Qt.black)
        p2.setColor(QPalette.Text, Qt.yellow)
        self.RoundBar5.setPalette(p2)
        self.RoundBar5.setNullPosition(QRoundProgressBar.PositionLeft)
        self.RoundBar5.setDecimals(0)
        gradientPoints5 = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        self.RoundBar5.setDataColors(gradientPoints5)
        self.connectToSlider(self.RoundBar5)

        p2 = QPalette()
        p2.setBrush(QPalette.AlternateBase, Qt.black)
        p2.setColor(QPalette.Text, Qt.yellow)
        self.RoundBar6.setPalette(p2)
        self.RoundBar6.setNullPosition(QRoundProgressBar.PositionLeft)
        self.RoundBar6.setDecimals(0)
        gradientPoints5 = [(1, Qt.green), (0.5, Qt.yellow), (0, Qt.red)]
        self.RoundBar6.setDataColors(gradientPoints5)
        self.connectToSlider(self.RoundBar6)"""



        """self.RoundBar2222 = QRoundProgressBar(self.right_frame2)
        self.RoundBar2222.setObjectName("RoundBar12")
        self.gridLayout_tot = QtWidgets.QGridLayout(self.right_frame2)        
        self.gridLayout_tot.addWidget(self.RoundBar2222, 4, 2, 1, 1)

        self.RoundBar2223 = QRoundProgressBar(self.right_frame2)
        self.RoundBar2223.setObjectName("RoundBar12")
        self.gridLayout_tot.addWidget(self.RoundBar2223, 4, 3, 1, 1)
"""
        
        
        self.RoundBar_list=[]
        self.RoundBar_list.append(self.RoundBar1);self.RoundBar_list.append(self.RoundBar2);self.RoundBar_list.append(self.RoundBar3);self.RoundBar_list.append(self.RoundBar4);
        self.RoundBar_list.append(self.RoundBar5);self.RoundBar_list.append(self.RoundBar6);self.RoundBar_list.append(self.RoundBar7);self.RoundBar_list.append(self.RoundBar8);
        self.RoundBar_list.append(self.RoundBar9);self.RoundBar_list.append(self.RoundBar10);self.RoundBar_list.append(self.RoundBar11);self.RoundBar_list.append(self.RoundBar12);
        self.RoundBar_list.append(self.RoundBar13);self.RoundBar_list.append(self.RoundBar14);self.RoundBar_list.append(self.RoundBar15);self.RoundBar_list.append(self.RoundBar16);
        for i in range(16):            
            self.RoundBar(self.RoundBar_list[i])
#############################
        self.currentWidgetRightFrame = 0

        

        self.Stack = QStackedWidget(self)
        #self.Stack.addWidget(left_frame)
        #self.Stack.addWidget(self.gridLayout_3)       

        left_frame.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_3.setFrameShape(QFrame.StyledPanel)

        timerselect = QtCore.QTimer(self)
        timerselect.timeout.connect(self.confirm)
        timerselect.start(10000)
        
    def confirm(self): #, req_quote):
        if self.currentWidgetRightFrame == 0:
            self.Stack.setCurrentIndex(1)
            self.currentWidgetRightFrame = 1
            print("one")
        else:
            self.Stack.setCurrentIndex(0)
            self.currentWidgetRightFrame = 0
            print("tow")
####################################        

        """p2 = QPalette(p1)
        p2.setBrush(QPalette.Base, Qt.lightGray)
        p2.setColor(QPalette.Text, Qt.magenta)
        p2.setColor(QPalette.Shadow, Qt.green)
        self.RoundBar5.setPalette(p2)
        self.RoundBar5.setNullPosition(QRoundProgressBar.PositionRight)
        self.RoundBar5.setBarStyle(QRoundProgressBar.BarStyle.PIE)
        self.RoundBar5.setDataColors(gradientPoints)
        self.connectToSlider(self.RoundBar5)

        self.RoundBar6.setDecimals(2)
        self.RoundBar6.setBarStyle(QRoundProgressBar.BarStyle.LINE)
        self.RoundBar6.setOutlinePenWidth(18)
        self.RoundBar6.setDataPenWidth(10)
        self.connectToSlider(self.RoundBar6)

        self.connectToSlider(self.RoundBar7)"""
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


    def initUI(self):
        self.num=1
        self.val=0
        self.pos=0
        self.intrface=1
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
#Reduced update time to fasten the change from w/ secs to w/o secs
        timer.start(10)
 


        timerselect = QtCore.QTimer(self)
        timerselect.timeout.connect(self.timer_select)
#Reduced update time to fasten the change from w/ secs to w/o secs
        timerselect.start(5000)
        
        timerbar = QtCore.QTimer(self)
        timerbar.timeout.connect(self.bar_value)
#Reduced update time to fasten the change from w/ secs to w/o secs
        timerbar.start(5000)
        
        chage_interface = QtCore.QTimer(self)
        chage_interface.timeout.connect(self.chage_interface_fn)
#Reduced update time to fasten the change from w/ secs to w/o secs
        chage_interface.start(20000)

        interface_globalf = QtCore.QTimer(self)
        interface_globalf.timeout.connect(self.interface_global)
#Reduced update time to fasten the change from w/ secs to w/o secs
        interface_globalf.start(5000)
#---------Window settings --------------------------------
 
# Expanded window height by 30px
 
        self.setGeometry(0,0,Width_champ,Height_champ)
        self.setWindowTitle("Clock")
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
        
        self.pattern = '{0:02d}:{1:02d}:{2:02d}'
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
            self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')"""
        for i  in range(16):
             if i<4:
                self.listlabel[i].move((int(Width_champ/20)+60),(int((Height_champ)/7)+35)*(i+1))
                self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
             if i>=4 and i<8:
                self.listlabel[i].move((int(Width_champ/20)+130)*2,(int((Height_champ)/7)+35)*(i-4+1))
                self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
             if i>=8 and i<12:
                self.listlabel[i].move((int(Width_champ/20)+150)*3,(int((Height_champ)/7)+35)*(i-8+1))
                self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
             if i>=12:
                self.listlabel[i].move((int(Width_champ/20)+160)*4,(int((Height_champ)/7)+35)*(i-12+1))
                self.listlabel[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
                
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
                self.num_label_list[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
                self.num_label_list[i].setText(str(self.num))

             if i>=4 and i<8:
                self.num_label_list[i].move((int(Width_champ/20)+130)*2,(int((Height_champ)/7)+35)*(i-4+1)+30)
                self.num_label_list[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
                self.num_label_list[i].setText(str(self.num))

             if i>=8 and i<12:
                self.num_label_list[i].move((int(Width_champ/20)+150)*3,(int((Height_champ)/7)+35)*(i-8+1)+30)
                self.num_label_list[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
                self.num_label_list[i].setText(str(self.num))

             if i>=12:
                self.num_label_list[i].move((int(Width_champ/20)+160)*4,(int((Height_champ)/7)+35)*(i-12+1)+30)
                self.num_label_list[i].setStyleSheet('color: rgb(255, 255, 255);font: 15pt Helvetica MS;')
                self.num_label_list[i].setText(str(self.num))

        

        
        self.nb_machine=QtWidgets.QLabel(self)        
        self.nb_machine.move(int(Width_champ/2)-50,30)
        self.nb_machine.resize(210,45)
        self.nb_machine.setStyleSheet('color: rgb(255, 255, 255);font: 30pt Helvetica MS;')
        self.nb_machine.setText("Machine 1")

 
        self.reeltimeText=QtWidgets.QLabel(self)
        self.reeltimeText.move(int(Width_champ/2)-250,30)
        self.reeltimeText.resize(190,45)
        self.reeltimeText.setStyleSheet('color: rgb(255, 255, 255);font: 30pt Helvetica MS;')
        self.progressBar1 = QProgressBar(self)
        self.progressBar1.setGeometry(30, 770, 450, 25)
        self.progressBar1.setMaximum(480)
        self.progressBar2 = QProgressBar(self)
        self.progressBar2.setGeometry(445, 770, 450, 25)
        self.progressBar2.setValue(0)
        self.progressBar3 = QProgressBar(self)
        self.progressBar3.setGeometry(860, 770, 450, 25)
        self.progressBar3.setValue(0)
        

                
    def bar_value(self):
            old_time = datetime.datetime.now()
            new_time = old_time - datetime.timedelta(hours=8, minutes=00)
            self.progressBar1.setValue((new_time.hour*60)+new_time.minute)
    def chage_interface_fn(self):
            
        if self.intrface <= val-1:
            self.intrface +=1
        else:
            self.intrface=1
        self.nb_machine.setText("Machine "+ str(self.intrface))
    def interface_global(self):
        self.progressBar4 = QProgressBar(self)
        self.progressBar4.setGeometry(0, 20, 450, 25)
        self.progressBar4.setValue(0)

    def timer_select(self):
        mySql_insert_query = """SELECT* FROM  machine"""+str(self.intrface)
        if self.intrface==5:
            print("5k")

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        
        self.val=cursor.fetchall()
        connection.commit()

        for k in range (len(self.val)):
            self.RoundBar_list[k].setValue(self.val[k][0])
            
            self.num_label_list[k].setText(str(self.val[k][1]))
            if  self.val[k][0] <=15 and self.val[k][4]==0 :
                self.pause(k)
            
            if self.val[k][0] >=15 and self.val[k][4]==1:               
                #self.reset(k)            
                self.start(k)
        if self.intrface==val:
            print("mmmmmmm")
            

        
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


    # To pause the kitchen timer

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




    def lupdate_timeText(self):
        if (self.state):
            # Every time this function is called,
            #self.timeText.setStyleSheet('color: rgb(255, 255, 0);font: 15pt Helvetica MS;background-color: rgb(51, 153, 255); ;')

            # we will increment 1 centisecond (1/100 of a second)
            #if self.timer2[2]<=6 and self.timer2[2]<=6 and self.timer2[2]<=6 or self.state==False :
                #self.timeText.setStyleSheet('color: rgb(255, 255, 0);font: 15pt Helvetica MS;background-color: rgb(255, 50, 50);')
                #print("hh")

            self.timer2[2]+= 1
            # Every 100 centisecond is equal to 1 second
            if (self.timer2[2] >= 60):

                self.timer2[2] = 0

                self.timer2[1] += 1
            # Every 60 seconds is equal to 1 min
            if (self.timer2[1] >= 60):

                self.timer2[0] += 1

                self.timer2[1] = 0                



            # Call the update_timeText() function after 1 centisecond


            timeString = self.pattern.format(self.timer2[0], self.timer2[1], self.timer2[2])

            # Update the timeText Label box with the current time

            self.listlabel[0].setText(str(timeString))

            self.listlabel[1].setText(str(timeString))
            self.listlabel[9].setText(str(timeString))











if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = TestWidget()
    widget.show()
    sys.exit(app.exec_())
