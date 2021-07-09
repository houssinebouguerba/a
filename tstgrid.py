from PyQt5 import QtCore, QtGui, QtWidgets 
import cv2

class Thread(QtCore.QThread):
   changePixmap = QtCore.pyqtSignal(QtGui.QImage)
   def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QtGui.QImage.Format_RGB888)
                p = convertToQtFormat.scaled(700, 1000, QtCore.Qt.KeepAspectRatio)
                self.changePixmap.emit(p)


class PlayStreaming(QtWidgets.QWidget):
    def __init__(self):
        super(PlayStreaming,self).__init__()
        self.initUI()

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def initUI(self):
        self.setWindowTitle("Image")
        # create a label
        self.label = QtWidgets.QLabel(self)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)


class UIWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIWidget, self).__init__(parent)
        # Initialize tab screen
        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()   
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1,"Face")
        self.tabs.addTab(self.tab2,"Human")
        self.tabs.addTab(self.tab3,"Vehicle")

        # Create first tab
        self.createGridLayout()
        self.tab1.layout = QtWidgets.QVBoxLayout()
        #self.display = PlayStreaming()
        #self.tab1.layout.addWidget(self.display, stretch=1)
        self.tab1.layout.addWidget(self.horizontalGroupBox)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tabs)

    def createGridLayout(self):
        self.horizontalGroupBox = QtWidgets.QGroupBox()
        layout = QtWidgets.QGridLayout()
        layout.addWidget(QtWidgets.QPushButton('Test'),0,0) 
        layout.addWidget(QtWidgets.QPushButton('Run'),0,1) 
        layout.addWidget(QtWidgets.QPushButton('Set Faces'),0,2) 
        layout.addWidget(QtWidgets.QPushButton('Recognize'),1,0) 
        layout.addWidget(QtWidgets.QPushButton('Rescale'),1,1) 
        layout.addWidget(QtWidgets.QPushButton('FacePose'),1,2)
        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = UIWidget()
    w.show()
    sys.exit(app.exec_())
