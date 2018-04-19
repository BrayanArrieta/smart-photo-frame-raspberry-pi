import sys, traceback, os
import ctypes
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel
from PyQt5.QtGui import QIcon,QPixmap
from google.cloud import storage

from oauth2client.client import GoogleCredentials
GOOGLE_APPLICATION_CREDENTIALS = 'credentials.json'
# credentials = GoogleCredentials.get_application_default()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=GOOGLE_APPLICATION_CREDENTIALS
client = storage.Client(GOOGLE_APPLICATION_CREDENTIALS)
bucket = client.get_bucket('smart-photo-frame-raspberry-pi.appspot.com')
class App(QWidget):
    def __init__(self,resolution):
        super().__init__()
        # constants
        self.title = 'Window'
        self.left = 0
        self.top = 26
        self.width = resolution.width()
        self.height = resolution.height()
        # methods
        self.config()
        self.initUI()
    def config(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
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
    def uploadEvent(self):
        blob = bucket.get_blob('image.png')
        with open('images/image.png', 'wb') as file_obj:
            blob.download_to_file(file_obj)
        self.label.setPixmap(QPixmap('images/image.png'))
        # print(blob._get_download_url())
        # print(blob.download_as_string().decode())
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
    ex = App(app.desktop().screenGeometry())
    sys.exit(app.exec_())

# try:
#
#     blob = bucket.get_blob('image.png')
#     with open('images/image.png', 'wb') as file_obj:
#         blob.download_to_file(file_obj)
# except Exception :
#     print ("Exception in user code:")
#     print ('-' * 60)
#     traceback.print_exc(file=sys.stdout)
