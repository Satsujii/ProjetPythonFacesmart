# Form implementation generated from reading ui file 'c:\Users\Hp\Desktop\projet-pfa-2\gestion_tache copy.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(971, 581)
        Dialog.setStyleSheet("background-color:#CDBEFF;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 351, 201))
        self.label.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(540, 30, 351, 201))
        self.label_2.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 351, 201))
        self.label_3.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(540, 270, 351, 201))
        self.label_4.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 80, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:90px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 70, 171, 121))
        self.pushButton.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:25px;\n"
"border:none;")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 320, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:90px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 310, 201, 121))
        self.pushButton_2.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:25px;\n"
"border:none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(570, 80, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:90px;\n"
"")
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 70, 201, 121))
        self.pushButton_3.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:25px;\n"
"border:none;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(570, 330, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:90px;\n"
"")
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 310, 201, 121))
        self.pushButton_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:25px;\n"
"border:none;")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Ajouter Tache"))
        self.label_6.setText(_translate("Dialog", ""))
        self.pushButton_2.setText(_translate("Dialog", "Supprimer Tache"))
        self.label_7.setText(_translate("Dialog", ""))
        self.pushButton_3.setText(_translate("Dialog", "Modifier Tache"))
        self.label_8.setText(_translate("Dialog", ""))
        self.pushButton_4.setText(_translate("Dialog", "Affecter Tache"))
