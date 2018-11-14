# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecordData.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataRecorder(object):
    def setupUi(self, DataRecorder):
        DataRecorder.setObjectName("DataRecorder")
        DataRecorder.resize(448, 312)
        self.gridLayout_2 = QtWidgets.QGridLayout(DataRecorder)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ComboClass = QtWidgets.QComboBox(DataRecorder)
        self.ComboClass.setObjectName("ComboClass")
        self.ComboClass.addItem("")
        self.ComboClass.addItem("")
        self.ComboClass.addItem("")
        self.ComboClass.addItem("")
        self.ComboClass.addItem("")
        self.verticalLayout.addWidget(self.ComboClass)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.imageHolder = QtWidgets.QLabel(DataRecorder)
        self.imageHolder.setObjectName("imageHolder")
        self.horizontalLayout.addWidget(self.imageHolder)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DataRecorder)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(DataRecorder)
        self.buttonBox.accepted.connect(DataRecorder.accept)
        self.buttonBox.rejected.connect(DataRecorder.reject)
        QtCore.QMetaObject.connectSlotsByName(DataRecorder)

    def retranslateUi(self, DataRecorder):
        _translate = QtCore.QCoreApplication.translate
        DataRecorder.setWindowTitle(_translate("DataRecorder", "Data Recorder"))
        self.ComboClass.setItemText(0, _translate("DataRecorder", "Please select a posture"))
        self.ComboClass.setItemText(1, _translate("DataRecorder", "class0"))
        self.ComboClass.setItemText(2, _translate("DataRecorder", "class1"))
        self.ComboClass.setItemText(3, _translate("DataRecorder", "class2"))
        self.ComboClass.setItemText(4, _translate("DataRecorder", "class3"))
        self.imageHolder.setText(_translate("DataRecorder", "TextLabel"))

