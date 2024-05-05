# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chaercher_period.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from suiviTemps import SuiviTemps
from employer import Employe

class Ui_Dialog_periode(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1153, 634)
        Dialog.setStyleSheet("background-color:#CDBEFF;")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(940, 220, 111, 31))
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
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(840, 50, 301, 211))
        self.label_6.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(850, 120, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:16px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(880, 150, 231, 41))
        self.dateTimeEdit.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(970, 60, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:50px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 801, 551))
        self.tableWidget.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#FFFFFF;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(157)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.label_6.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.dateTimeEdit.raise_()
        self.label_5.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def chercher_periode(self):
        date=self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        print(date)
        Periods=SuiviTemps.chercherParDate(date)
        print(Periods)
        row=0
        self.tableWidget.setRowCount(len(Periods))
        for periode in Periods:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(f'{periode[0]}'))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(periode[1]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(periode[2]))
            employe=Employe.read(periode[3])
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(employe[1]))
            self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(employe[2]))
            row=row+1    
        
        
           

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", ""))
        self.label_4.setText(_translate("Dialog", "Temps :"))
        self.label_5.setText(_translate("Dialog", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Date Arrivée"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Date Départ"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Prenom"))
        
        self.pushButton.clicked.connect(self.chercher_periode)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_periode()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
