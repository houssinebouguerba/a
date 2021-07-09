
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.Debit_b = QPushButton(self)
        self.Debit_b.setText('Debit') 
        self.Debit_b.resize(80,50)
        self.Debit_b.setStyleSheet("background-color:#ff0000;")        
        #self.Debit_b.setStyleSheet('color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')        
        self.Debit_b.move(0,100)
        


        
        self.lab_debit=QtWidgets.QLabel("kkkkkkkkk",self)
        self.lab_debit.resize(200,50)
        self.lab_debit.move(80,100)
        self.lab_debit.setStyleSheet('color: rgb(255, 255, 255);background-color: rgb(0, 0, 0);font: 10pt Helvetica MS; QRadioButton::indicator { width: 100px; height: 100px;};')        

        
        groupBox = QGroupBox("Configuration",self)        
        self.seringue_b= QPushButton("OK")
        self.seringue_b.resize(100,100)
   
        self.lab_seringue=QtWidgets.QLabel("mmmm",self)

        vbox = QGridLayout()
        #vbox.addWidget(self.Debit_b,0,0)
        #vbox.addWidget(self.lab_debit,0,1)
        vbox.addWidget(self.seringue_b,1,0)
        vbox.addWidget(self.lab_seringue,1,1)
        groupBox.setLayout(vbox)
        groupBox.resize(400,400)

        groupBox.move(400,400)
        self.setWindowTitle('Buttons')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
