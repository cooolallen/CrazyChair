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
        DataRecorder.resize(473, 312)
        self.gridLayout = QtWidgets.QGridLayout(DataRecorder)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ComboClass = QtWidgets.QComboBox(DataRecorder)
        self.ComboClass.setObjectName("ComboClass")
        self.verticalLayout.addWidget(self.ComboClass)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.imageHolder = QtWidgets.QLabel(DataRecorder)
        self.imageHolder.setText("")
        self.imageHolder.setObjectName("imageHolder")
        self.verticalLayout_2.addWidget(self.imageHolder)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RecordingButton = QtWidgets.QPushButton(DataRecorder)
        self.RecordingButton.setObjectName("RecordingButton")
        self.horizontalLayout.addWidget(self.RecordingButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DataRecorder)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(DataRecorder)
        self.buttonBox.accepted.connect(DataRecorder.accept)
        self.buttonBox.rejected.connect(DataRecorder.reject)
        QtCore.QMetaObject.connectSlotsByName(DataRecorder)

    def retranslateUi(self, DataRecorder):
        _translate = QtCore.QCoreApplication.translate
        DataRecorder.setWindowTitle(_translate("DataRecorder", "Data Recorder"))
        self.RecordingButton.setText(_translate("DataRecorder", "Start Recording"))

