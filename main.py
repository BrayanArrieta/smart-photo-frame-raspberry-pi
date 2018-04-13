import sys
import ctypes
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel
from PyQt5.QtGui import QIcon,QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Window'
        self.left = 0
        self.top = 26
        self.width = 0
        self.height = 0
        self.setWindowSize()
        self.initUI()

    def initUI(self):
        button_upload = QPushButton( self)
        # button.setToolTip('This is an example button')
        button_upload.setIcon(QtGui.QIcon('app_images/upload-button.svg'))
        button_upload.setIconSize(QtCore.QSize(60, 60))
        button_upload.resize((self.width/4)/2,self.height / 8)
        button_upload.move(0, self.height-button_upload.height())

        button_previous = QPushButton( self)
        # button1.setToolTip('This is an example button')
        button_previous.setIcon(QtGui.QIcon('app_images/left-arrow.svg'))
        button_previous.setIconSize(QtCore.QSize(60, 60))
        button_previous.resize((self.width / 4)+(self.width / 4/2),self.height / 8)
        button_previous.move(((self.width/4)*2)-button_previous.width(), self.height-button_previous.height())

        button_next = QPushButton( self)
        # button2.setToolTip('This is an example button')
        button_next.setIcon(QtGui.QIcon('app_images/forward-right-arrow-button'))
        button_next.setIconSize(QtCore.QSize(60, 60))
        button_next.resize(self.width / 4+(self.width / 4/2), self.height / 8)
        button_next.move(((self.width/4)*3)-button_next.width()+button_next.width()/3, self.height-button_next.height())

        button_download = QPushButton( self)
        # button3.setToolTip('This is an example button')
        button_download.setIcon(QtGui.QIcon('app_images/download-button.svg'))
        button_download.setIconSize(QtCore.QSize(60, 60))
        button_download.resize(self.width / 4/2, self.height / 8)
        button_download.move(((self.width/4)*4)-button_download.width(),self.height-button_download.height())

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel(self)


        pixmap = QPixmap('images/img1.jpg')
        label.setPixmap(pixmap)
        label.move(self.width/2-pixmap.width()/2,self.height/2-pixmap.height()/2)
        self.show()

    def closeEvent(self, event):
        self.deleteLater()
        event.accept()

    def setWindowSize(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.width = screensize[0]
        self.height = screensize[1]-self.top


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
