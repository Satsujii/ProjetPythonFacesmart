# Form implementation generated from reading ui file 'c:\Users\Hp\Desktop\projet-pfa-2\chercher_tache.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1155, 530)
        Dialog.setStyleSheet("background-color:#CDBEFF;")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(910, 230, 111, 31))
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
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(930, 80, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:60px;\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(800, 70, 341, 211))
        self.label_6.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(880, 170, 241, 31))
        self.lineEdit_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(810, 170, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:16px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 751, 431))
        self.tableWidget.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#FFFFFF;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(242)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(800, 290, 341, 211))
        self.label_7.setStyleSheet("\n"
"border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(820, 390, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:16px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setGeometry(QtCore.QRect(940, 300, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:60px;\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=Dialog)
        self.label_10.setGeometry(QtCore.QRect(820, 310, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:16px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=Dialog)
        self.label_11.setGeometry(QtCore.QRect(820, 420, 301, 41))
        self.label_11.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=Dialog)
        self.label_12.setGeometry(QtCore.QRect(820, 340, 301, 41))
        self.label_12.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_6.raise_()
        self.label_4.raise_()
        self.lineEdit_4.raise_()
        self.pushButton.raise_()
        self.label_8.raise_()
        self.tableWidget.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", ""))
        self.label_8.setText(_translate("Dialog", ""))
        self.label_4.setText(_translate("Dialog", "Tache :"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Prenom"))
        self.label_5.setText(_translate("Dialog", "Status :"))
        self.label_9.setText(_translate("Dialog", ""))
        self.label_10.setText(_translate("Dialog", "ID Tache :"))
