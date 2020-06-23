# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\password.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 213)
        self.lineEditPwd = QtWidgets.QLineEdit(Dialog)
        self.lineEditPwd.setGeometry(QtCore.QRect(42, 90, 331, 31))
        self.lineEditPwd.setObjectName("lineEditPwd")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(46, 60, 321, 20))
        self.label.setObjectName("label")
        self.pushButtonConf = QtWidgets.QPushButton(Dialog)
        self.pushButtonConf.setGeometry(QtCore.QRect(144, 150, 101, 31))
        self.pushButtonConf.setObjectName("pushButtonConf")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enter Your Password"))
        self.label.setText(_translate("Dialog", "Enter a password"))
        self.pushButtonConf.setText(_translate("Dialog", "OK"))
