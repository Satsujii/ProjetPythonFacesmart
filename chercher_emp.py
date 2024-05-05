# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chercher_emp.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from employer import Employe
from suiviTemps import SuiviTemps
from tache import Tache
import time


class Ui_Dialog_emp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1191, 670)
        Dialog.setStyleSheet("background-color:#CDBEFF;")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(780, 40, 381, 611))
        self.label_5.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(920, 50, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:90px")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(790, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(790, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 751, 431))
        self.tableWidget.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#FFFFFF;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(182)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(110, 450, 341, 211))
        self.label_6.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 490, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:16px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 490, 261, 31))
        self.lineEdit_3.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 550, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:16px;\n"
"")
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 550, 241, 31))
        self.lineEdit_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 610, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 2px solid #FFFFFF;\n"
"border-radius: 10px;\n"
"background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(800, 190, 331, 41))
        self.label.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(800, 270, 331, 41))
        self.label_9.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(800, 320, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(800, 350, 331, 41))
        self.label_11.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(800, 400, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(800, 430, 331, 41))
        self.label_13.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(800, 480, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(800, 520, 331, 41))
        self.label_15.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.chercher_employe)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", "Nom :"))
        self.label_3.setText(_translate("Dialog", "Prenom :"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Date Arrivee"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Date Départ"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Periode"))
        self.label_4.setText(_translate("Dialog", "Nom :"))
        self.label_8.setText(_translate("Dialog", "Prenom :"))
        self.pushButton.setText(_translate("Dialog", ""))
        self.label_10.setText(_translate("Dialog", "Email :"))
        self.label_12.setText(_translate("Dialog", "Password :"))
        self.label_14.setText(_translate("Dialog", "Tache :"))
        
    def chercher_employe(self):
        nom=self.lineEdit_3.text()
        prenom=self.lineEdit_4.text()
        self.employe=Employe.ChercherParNom(nom,prenom)
        self.label.setText(self.employe[1])
        self.label_9.setText(self.employe[2])
        self.label_11.setText(self.employe[3])
        self.label_13.setText(self.employe[4])
        tache=Tache.chercherParID(self.employe[5])
        self.label_15.setText(tache[1])
        self.Afficher_period()
        
    def Afficher_period(self):
        periodes=SuiviTemps.chercherParId(self.employe[0])
        print(periodes)
        row=0
        self.tableWidget.setRowCount(len(periodes))
        for periode in periodes:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(f'{periode[0]}'))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(periode[1]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(periode[2]))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(periode[3]))
            periode_second=int(periode[4])
            convert = time.strftime("%H:%M:%S", time.gmtime(periode_second))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(convert))
            row=row+1    
        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_emp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
