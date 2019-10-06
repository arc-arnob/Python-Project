# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(251, 514)
        Form.setStyleSheet("background-color:rgb(96, 178, 255)")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 310, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_l = QtWidgets.QPushButton(Form)
        self.pushButton_l.setGeometry(QtCore.QRect(90, 410, 81, 31))
        self.pushButton_l.setStyleSheet("background-color:rgb(184, 184, 184)")
        self.pushButton_l.setObjectName("pushButton_l")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 10, 191, 181))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 370, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Password"))
        self.pushButton_l.setText(_translate("Form", "Login"))
