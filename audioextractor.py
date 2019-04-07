# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Shaurya Gupta\Desktop\Linguistic Magic\audioextractor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
from gtts import gTTS 
import datetime
import time
import pyaudio
import speech_recognition as sr
import win32com.client as wincl

from translate import Translator

def process1(formatofvideo):
    files = os.listdir("./")
    for f in files:
        if f.lower()[-3:] == "mp4":
            print ("processing", f)
            process(f,formatofvideo)

def process(f,formatofvideo):
    if formatofvideo =="wav":
        inFile = f
        outFile = f[:-3] + "wav"
        cmd = "ffmpeg -i {} -vn  -ac 2 -ar 44100 -ab 320k -f wav {}".format(inFile, outFile)
        os.popen(cmd)
    else:
        inFile = f
        outFile = f[:-3] + "mp3"
        cmd = "ffmpeg -i {} -vn  -ac 2 -ar 44100 -ab 320k -f mp3 {}".format(inFile, outFile)
        os.popen(cmd)
        

           

        
        
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def helloworld(self):
        formatofvideo=self.lineEdit_3.text()
        process1(formatofvideo)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 841)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 321, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("3.PNG"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 30, 841, 171))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(34)
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"background-color: rgb(85, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(680, 250, 471, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 300, 171, 31))
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
        self.label_6.setGeometry(QtCore.QRect(20, 340, 641, 31))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(690, 340, 461, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 390, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 430, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(720, 430, 461, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 480, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.helloworld)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 530, 971, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(80, 600, 1041, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Audio and Movie Extractor"))
        self.label_5.setText(_translate("MainWindow", "ENTER THE NAME OF THE VIDEO YOU WANT TO EXTRACT AUDIO FROM"))
        self.pushButton.setText(_translate("MainWindow", "OKAY"))
        self.label_6.setText(_translate("MainWindow", "ENTER THE PATH OF THE VIDEO YOU WANT TO EXTRACT AUDIO FROM"))
        self.pushButton_2.setText(_translate("MainWindow", "OKAY"))
        self.label_7.setText(_translate("MainWindow", "ENTER THE FORMAT IN WHICH YOU WANT YOUR AUDIO FILE(mp3 or wav) "))
        self.pushButton_3.setText(_translate("MainWindow", "EXTRACT!!"))
        self.label_3.setText(_translate("MainWindow", "YOUR EXTRACTION STATUS IS SHOWED HERE IN THE PROGESS BAR. KEEP STARING AT IT."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

