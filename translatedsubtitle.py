# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Shaurya Gupta\Desktop\Linguistic Magic\translatedsubtitle.ui'
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
speak = wincl.Dispatch("SAPI.SpVoice")
from translate import Translator

r=sr.Recognizer()
start_time=datetime.datetime(100,1,1,0,0,0)
max_time = datetime.datetime(100,1,1,0,0,25)
block_num=1
def process1():
    files = os.listdir("./")
    for f in files:
        if f.lower()[-3:] == "mp4":
            print ("processing", f)
            process(f)

def process(f):
    inFile = f
    outFile = f[:-3] + "wav"
    cmd = "ffmpeg -i {} -vn  -ac 2 -ar 44100 -ab 320k -f wav {}".format(inFile, outFile)
    os.popen(cmd)
def speech_to_srt(current_time,block,tolangu):
    if current_time>=max_time:
        return "Speech recognition complete."
    else:
        block +=1
        block_str = str(block)
        
        audio="output.wav"
        with sr.AudioFile(audio) as source:
            print("Now recording sentence:")
            audio = r.record(source)
            
            
            try:
                sentence = (r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Reecognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            if sentence == "speech recognition is over":
                return "Speech recognition has ended by user request."
            else:
                time_add = len(sentence.split())
                end_time = current_time + datetime.timedelta(0,time_add)
                str_current_time = str(current_time.time())
                str_end_time =  str(end_time.time())
                
                
                
                with open("graduate_project.srt","a") as f:
                    f.write(block_str)
                    f.write("\n")
                    f.write(str_current_time)
                    f.write("-->")
                    f.write(str_end_time)
                    f.write("\n")
                    translator= Translator(from_lang="english",to_lang=tolangu)
                    #sentence1=translator.translate(sentence)
                    #speak.Speak(gs.translate(sentence, 'de'))
                    #myobj = gTTS(text=sentence1, lang='en', slow=False)
                    #myobj.save("output.mp3")
                    #os.system("mpg321 output.mp3")
                    f.write(translator.translate(sentence))
                    f.write(".")
                    f.write("\n")
                    f.write("\n")
                    return speech_to_srt(end_time,block,tolangu)
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def helloworld(self):
        tolangu=self.lineEdit_3.text()
        process1()
        time.sleep(8)
        speech_to_srt(start_time,block_num,tolangu)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 331, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("3.PNG"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 711, 211))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(26)
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
        self.label_5.setGeometry(QtCore.QRect(10, 270, 691, 31))
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
        self.lineEdit.setGeometry(QtCore.QRect(720, 270, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 320, 171, 31))
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
        self.label_6.setGeometry(QtCore.QRect(10, 360, 691, 31))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(730, 360, 321, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 410, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 460, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(740, 460, 321, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 520, 611, 31))
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
        self.label_3.setGeometry(QtCore.QRect(70, 570, 971, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 620, 1041, 51))
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
        self.label.setText(_translate("MainWindow", "TRANSLATED SUBTITLE CREATOR"))
        self.label_5.setText(_translate("MainWindow", "ENTER THE NAME OF THE VIDEO WHOSE TRANSLATED SUBTITLE YOU WANT"))
        self.pushButton.setText(_translate("MainWindow", "OKAY"))
        self.label_6.setText(_translate("MainWindow", "ENTER THE PATH OF THE VIDEO WHOSE TRANSLATED SUBTITLE YOU WANT"))
        self.pushButton_2.setText(_translate("MainWindow", "OKAY"))
        self.label_7.setText(_translate("MainWindow", "ENTER THE NEW LANGUAGE  OF THE SUBTITLES"))
        self.pushButton_3.setText(_translate("MainWindow", "CREATE TRANSLATED SUBTITLE FILE"))
        self.label_3.setText(_translate("MainWindow", "YOUR CONVERSION STATUS IS SHOWED HERE IN THE PROGESS BAR. KEEP STARING AT IT."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

