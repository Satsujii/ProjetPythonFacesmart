# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face-recog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import face_recognition
import numpy as np
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import time 
from suiviTemps import SuiviTemps
from employer import Employe
nom=""
prenom=""

class Ui_Dialog_face_recog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1258, 576)
        Dialog.setMinimumSize(QtCore.QSize(1258, 576))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setStyleSheet("background-color:#CDBEFF;")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.imgLabel = QtWidgets.QLabel(parent=Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(30, 60, 661, 451))
        self.imgLabel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.imgLabel.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"\n"
"\n"
"")
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(810, 40, 411, 371))
        self.label.setMinimumSize(QtCore.QSize(5, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("background-color:#332562;\n"
"border-radius:20px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.CheckInBtn = QtWidgets.QPushButton(parent=Dialog)
        self.CheckInBtn.setGeometry(QtCore.QRect(850, 280, 141, 41))
        self.CheckInBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.CheckInBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.CheckInBtn.setFont(font)
        self.CheckInBtn.setStyleSheet("QPushButton#CheckInBtn{\n"
"background-color:rgba(205, 190, 255, 255);\n"
"color:rgba(0, 0, 0, 200);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton#CheckInBtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(205, 190, 255, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}")
        self.CheckInBtn.setObjectName("CheckInBtn")
        self.CheckOutBtn = QtWidgets.QPushButton(parent=Dialog)
        self.CheckOutBtn.setGeometry(QtCore.QRect(1050, 280, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.CheckOutBtn.setFont(font)
        self.CheckOutBtn.setStyleSheet("QPushButton#CheckOutBtn{\n"
"background-color:rgba(205, 190, 255, 255);\n"
"color:rgba(0, 0, 0, 200);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton#CheckOutBtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(205, 190, 255, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"")
        self.CheckOutBtn.setObjectName("CheckOutBtn")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(930, 60, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setTabletTracking(False)
        self.label_5.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_5.setStyleSheet("background-color:#332562;\n"
"font-size:120px;\n"
"color:#FFFFFF")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 60, 51, 31))
        self.label_2.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius:5px;\n"
"font-size:30px;\n"
"")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.CheckOutBtn.clicked.connect(self.CheckOut_employer)
        self.CheckInBtn.clicked.connect(self.CheckIn_employer)
        
    def CheckIn_employer(self):
        self.Worker1.stop()
        cv2.destroyAllWindows()
        self.Worker1.Capture.release()
        self.Worker1.terminate()
        time.sleep(1)
        
        employe=Employe.ChercherParNom(nom,prenom)
        print(employe[0])
        temps=SuiviTemps(employe[0])
        temps.Ajouter_checkin()
        
        self.Worker1.start()
        print("start")
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        
        
        
        
      
    def CheckOut_employer(self):
        #self.Worker1 = Worker1()
        self.Worker1.stop()
        cv2.destroyAllWindows()
        self.Worker1.Capture.release()
        self.Worker1.terminate()
        time.sleep(1)
        
        employe=Employe.ChercherParNom(nom,prenom)
        print(employe[0])
        temps=SuiviTemps(employe[0])
        temps.Ajouter_checkout()
        
        self.Worker1.start()
        print("start")
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
          
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CheckInBtn.setText(_translate("Dialog", "C H E C K     I N"))
        self.CheckOutBtn.setText(_translate("Dialog", "C H E C K     O U T"))
        self.label_5.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", ""))
        
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        
        
        

    
    
    def ImageUpdateSlot(self, Image):
        self.imgLabel.setPixmap(QPixmap.fromImage(Image))

class Worker1(QThread):
 
    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):
        global nom
        global prenom
        known_face_names=[]
        known_face_encodings=[]
        for path in os.listdir("data"):
            image_name=str(path).split('.')[0]
            known_face_names.append(image_name)
            image = face_recognition.load_image_file(f"data/{path}")
            face_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(face_encoding)
            
        self.ThreadActive = True
        self.Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = self.Capture.read()
            if ret:
                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Find all the faces and face enqcodings in the frame of video
                face_locations = face_recognition.face_locations(Image)
                face_encodings = face_recognition.face_encodings(Image, face_locations)
                
                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                     # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        
                        Nomprenom=name.split('_')
                        nom=Nomprenom[0]
                        prenom=Nomprenom[1]
                        
                    
                    
                    # Draw a box around the face
                    cv2.rectangle(frame, (left-10, top+20), (right+10, bottom-15), (0, 255, 0), )
                    cv2.rectangle(frame, (left-10, bottom - 35), (right+10, bottom), (0, 255, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    #frame = cv2.flip(frame, 1)
                    cv2.putText(frame, name, (left + 6, bottom - 10), font, 0.6, (0, 0, 0), 1)
                    
                    print(name)
                                
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(670, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    
    def stop(self):
        self.ThreadActive = False
                 



    
    
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_face_recog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
