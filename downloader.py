# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Shaurya Gupta\Desktop\Linguistic Magic\downloader.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import requests 
from bs4 import BeautifulSoup 
from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
class Ui_MainWindow(object):
    def hello_world(self):
        link=self.lineEdit_2.text()
        try:
            yt = YouTube(link)
        except:
            print("Connection Error")
        mp4files = yt.filter('mp4')
        yt.set_filename('SHAURYA_VIDEO')
        d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
        try:
            d_video.download()
        except: 
            print("Some Error!") 
        print('Task Completed!') 
        
    def helloworld(self):
        archive_url=self.lineEdit.text()
        video_links = get_video_links(archive_url) 
        download_video_series(video_links)
    def get_video_links(archive_url): 
        r = requests.get(archive_url) 
        soup = BeautifulSoup(r.content,'html5lib') 
        links = soup.findAll('a') 
        video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')] 
        return video_links 


    def download_video_series(video_links): 
        for link in video_links: 
            file_name = link.split('/')[-1] 
            print ("Downloading file:%s",file_name) 
            r = requests.get(link, stream = True) 
 
            with open(file_name, 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk) 
            print ("%s downloaded!\n",file_name) 

        print ("All videos downloaded!")
        return    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 370, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.hello_world)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 600, 1041, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 530, 971, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 421, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("3.PNG"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 220, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"background-color: rgb(85, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 270, 171, 31))
        self.pushButton.clicked.connect(self.helloworld)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 320, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 320, 311, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 10, 731, 191))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(42)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 0);")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(700, 220, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "DOWNLOAD"))
        self.label_3.setText(_translate("MainWindow", "YOUR CONVERSION STATUS IS SHOWED HERE IN THE PROGESS BAR. KEEP STARING AT IT."))
        self.label_5.setText(_translate("MainWindow", "ENTER THE URL OF THE SITE FROM WHICH YOU WANT TO BATCH DONWLOAD MOVIES"))
        self.pushButton.setText(_translate("MainWindow", "DOWNLOAD"))
        self.label_6.setText(_translate("MainWindow", "ENTER THE YOUTUBE URL FOR DOWNLOADING OF A VIDEO"))
        self.label.setText(_translate("MainWindow", "BEAST DOWNLOADER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

