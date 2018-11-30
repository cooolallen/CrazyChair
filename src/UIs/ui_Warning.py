# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Warning.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Warning(object):
    def setupUi(self, Warning):
        Warning.setObjectName("Warning")
        Warning.resize(390, 173)
        self.label = QtWidgets.QLabel(Warning)
        self.label.setGeometry(QtCore.QRect(70, 0, 351, 151))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.OKButton = QtWidgets.QPushButton(Warning)
        self.OKButton.setGeometry(QtCore.QRect(270, 130, 113, 32))
        self.OKButton.setObjectName("OKButton")

        self.retranslateUi(Warning)
        QtCore.QMetaObject.connectSlotsByName(Warning)

    def retranslateUi(self, Warning):
        _translate = QtCore.QCoreApplication.translate
        Warning.setWindowTitle(_translate("Warning", "Warning"))
        self.label.setText(_translate("Warning", "You didn\'t sit well :("))
        self.OKButton.setText(_translate("Warning", "OK"))

