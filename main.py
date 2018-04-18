import sys, traceback
import ctypes
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel
from PyQt5.QtGui import QIcon,QPixmap
# from google.cloud import storage

class App(QWidget):
    def __init__(self):
        super().__init__()
        # constants
        self.title = 'Window'
        self.left = 0
        self.top = 26
        self.width = 0
        self.height = 0
        # methods
        self.config()
        self.initUI()
    def config(self):
        self.setWindowSize()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.saludo="ndnd"
    def initUI(self):
        # upload
        button_upload = QPushButton( self)
        button_upload.setIcon(QtGui.QIcon('app_images/upload-button.svg'))
        button_upload.setIconSize(QtCore.QSize(60, 60))
        button_upload.resize((self.width/4)/2,self.height / 8)
        button_upload.move(0, self.height-button_upload.height())
        button_upload.clicked.connect(self.uploadEvent)
        # previous
        button_previous = QPushButton( self)
        button_previous.setIcon(QtGui.QIcon('app_images/left-arrow.svg'))
        button_previous.setIconSize(QtCore.QSize(60, 60))
        button_previous.resize((self.width / 4)+(self.width / 4/2),self.height / 8)
        button_previous.move(((self.width/4)*2)-button_previous.width(), self.height-button_previous.height())
        button_previous.clicked.connect(self.previousEvent)
        # next
        button_next = QPushButton( self)
        button_next.setIcon(QtGui.QIcon('app_images/forward-right-arrow-button'))
        button_next.setIconSize(QtCore.QSize(60, 60))
        button_next.resize(self.width / 4+(self.width / 4/2), self.height / 8)
        button_next.move(((self.width/4)*3)-button_next.width()+button_next.width()/3, self.height-button_next.height())
        button_next.clicked.connect(self.nextEvent)
        # download
        button_download = QPushButton( self)
        button_download.setIcon(QtGui.QIcon('app_images/download-button.svg'))
        button_download.setIconSize(QtCore.QSize(60, 60))
        button_download.resize(self.width / 4/2, self.height / 8)
        button_download.move(((self.width/4)*4)-button_download.width(),self.height-button_download.height())
        button_download.clicked.connect(self.downloadEvent)

        self.label = QLabel(self)


        pixmap = QPixmap('images/img1.jpg')
        self.label.resize(self.width-(self.width/12),self.height-(self.height/4))
        newPixmap = pixmap.scaled(QSize(self.label.width(), self.label.height()));
        self.label.setPixmap(newPixmap)
        self.label.move(self.width/2-self.label.width()/2,self.height/14)
        self.show()

    def closeEvent(self, event):
        self.deleteLater()
        event.accept()

    def setWindowSize(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.width = screensize[0]
        self.height = screensize[1]-self.top

    def uploadEvent(self):
        client = storage.Client()
        # https://console.cloud.google.com/storage/browser/[bucket-id]/  smart-photo-frame-raspberry-pi.appspot.com
        try:
            bucket = client.get_bucket('smart-photo-frame-raspberry-pi.appspot.com')
        except Exception :
            print ("Exception in user code:")
            print ('-' * 60)
            traceback.print_exc(file=sys.stdout)
        # # Then do other things...
        # blob = bucket.get_blob('remote/path/to/texto.txt')
        # print(blob.download_as_string())
    def downloadEvent(self):
        print ('clicked down')
    def previousEvent(self):
        pixmap = QPixmap('images/img1.jpg')
        newPixmap = pixmap.scaled(QSize(self.label.width(), self.label.height()));
        self.label.setPixmap(newPixmap)
        print ('clicked <-')
    def nextEvent(self):
        pixmap = QPixmap('images/img2.jpg')
        newPixmap = pixmap.scaled(QSize(self.label.width(), self.label.height()));
        self.label.setPixmap(newPixmap)
        print ('clicked ->')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

# client = storage.Client()
# # https://console.cloud.google.com/storage/browser/[bucket-id]/  smart-photo-frame-raspberry-pi.appspot.com
# try:
#     bucket = client.get_bucket('https://firebasestorage.googleapis.com/v0/b/smart-photo-frame-raspberry-pi.appspot.com/')
# except Exception :
#     print ("Exception in user code:")
#     print ('-' * 60)
#     traceback.print_exc(file=sys.stdout)