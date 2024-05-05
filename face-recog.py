# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face-recog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1258, 576)
        Dialog.setMinimumSize(QtCore.QSize(1258, 576))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setStyleSheet("background-color:#CDBEFF;")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(30, 40, 691, 501))
        self.imgLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.imgLabel.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius:50px\n"
"\n"
"")
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(810, 40, 411, 481))
        self.label.setMinimumSize(QtCore.QSize(5, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("background-color:#332562;\n"
"border-radius:20px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_matricule = QtWidgets.QLabel(Dialog)
        self.label_matricule.setGeometry(QtCore.QRect(860, 200, 301, 41))
        self.label_matricule.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_matricule.setFont(font)
        self.label_matricule.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: 2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(255, 255, 255, 200);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom: 0px")
        self.label_matricule.setObjectName("label_matricule")
        self.CheckInBtn = QtWidgets.QPushButton(Dialog)
        self.CheckInBtn.setGeometry(QtCore.QRect(860, 440, 141, 41))
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
        self.CheckOutBtn = QtWidgets.QPushButton(Dialog)
        self.CheckOutBtn.setGeometry(QtCore.QRect(1030, 440, 141, 41))
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
        self.label_Nom = QtWidgets.QLabel(Dialog)
        self.label_Nom.setGeometry(QtCore.QRect(860, 270, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Nom.setFont(font)
        self.label_Nom.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: 2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(255, 255, 255, 200);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom: 0px")
        self.label_Nom.setObjectName("label_Nom")
        self.label_Prenom = QtWidgets.QLabel(Dialog)
        self.label_Prenom.setGeometry(QtCore.QRect(860, 340, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Prenom.setFont(font)
        self.label_Prenom.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border: 2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(255, 255, 255, 200);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom: 0px")
        self.label_Prenom.setObjectName("label_Prenom")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(950, 60, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setTabletTracking(False)
        self.label_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_5.setStyleSheet("background-color:#332562;\n"
"font-size:120px;\n"
"color:#FFFFFF")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 40, 51, 31))
        self.label_2.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius:5px;\n"
"font-size:30px;\n"
"")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_matricule.setText(_translate("Dialog", "Matricule"))
        self.CheckInBtn.setText(_translate("Dialog", "C H E C K     I N"))
        self.CheckOutBtn.setText(_translate("Dialog", "C H E C K     O U T"))
        self.label_Nom.setText(_translate("Dialog", "Nom"))
        self.label_Prenom.setText(_translate("Dialog", "Prenom"))
        self.label_5.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
