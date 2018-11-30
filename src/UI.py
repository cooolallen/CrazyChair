# ui generated by 
# pyuic5 MainWindow.ui -o ui_MainWindow.py
# pyuic5 RecordData.ui -o ui_RecordData.py
# pyuic5 Warning.ui -o ui_Warning.py

from PyQt5.QtWidgets import QMainWindow, QDialog, QShortcut, QMessageBox

from UIs.ui_MainWindow import Ui_MainWindow
from UIs.ui_RecordData import Ui_DataRecorder
from UIs.ui_Warning import Ui_Warning

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QKeySequence, QGuiApplication

from ArduinoTest import ArduinoTest
from SVM import Judge
from Alarm import Alarm
from Arduino.Arduino import Arduino
import Constants

import serial
import struct
import datetime
from enum import Enum
from collections import defaultdict
from matplotlib import pyplot as plt
from os.path import join
import os

''' The enum class for the postures '''
class Posture(Enum):
	empty = 0
	normal = 1
	normalBack = 2
	lay = 3
	legOnLeft = 4
	legOnRight = 5

	def __str__(self):
		if self.value == 0:
			return 'empty'
		elif self.value == 1:
			return 'normal'
		elif self.value == 2:
			return 'normalBack'
		elif self.value == 3:
			return 'lay'
		elif self.value == 4:
			return 'legOnLeft'
		else:
			return 'legOnRight'
       
''' The class to handle the mainwindow and logic. '''
class MainWindow(QMainWindow):
	def __init__(self, test=Constants.test, parent=None):
		# UI init
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.voltageTimer = QTimer()
		self.voltageTimer.start(Constants.updateRate)		# update every 0.15 second
		self.guiTimer = QTimer()
		self.guiTimer.start(0)
		self.cm = plt.get_cmap('cool')
		self.alarm = Alarm(self)
		self.judge = Judge(Constants.DATA_DIR)
		self.warning = Warning()
		self.recorder = None
		self.time = None
		self.measure = None
		self.predict = {'predict':1, 'cnt':0, 'curr_predict':None}


		# check it is test mode or not (arduino don't need to connect)
		if test:
			self.arduino = ArduinoTest()
		else:
			self.arduino = Arduino()

		# Connection
		self.voltageTimer.timeout.connect(self.voltageUpdate)
		self.ui.actionRecord_Data.triggered.connect(self.recordData)
		self.guiTimer.timeout.connect(self.guiUpdate)

		# ShortCut
		self.ui.actionRecord_Data.setShortcut("Ctrl+D")

		# Check is there are the data valid or not
		self.judgeStatusCheck()

		# Show the main window
		self.show()

	def voltageUpdate(self):
		data = self.arduino.get_pressure()
		if data:
			self.time = str(datetime.datetime.now())
			self.measure = data
			self.updatePosture()

			# record the data is data recorder is open
			if self.recorder is not None and self.recorder.recording:
				posture_id = self.recorder.ui.ComboClass.currentIndex()
				self.recorder.measure[posture_id].append((self.time, self.measure))

	def updatePosture(self):
		curr_predict = self.judge.predict(self.measure)
		if curr_predict == self.predict['curr_predict']:
			self.predict['cnt'] += 1
		else:
			self.predict['curr_predict'] = curr_predict
			self.predict['cnt'] = 1

		# update the predict only when it is greater than consecutive factor
		# to prevent the prediction change in a very short time
		if self.predict['cnt'] >= Constants.consecutiveFactor:
			self.predict['predict'] = self.predict['curr_predict']

		# update the alarm status
		if self.predict['predict'] not in Constants.goodPosture:
			self.alarm.tick()
		else:
			self.alarm.reset()


	def recordData(self):
		self.recorder = DataRecorder(self)
		self.recorder.finished.connect(self.recordDataClose)

	def judgeStatusCheck(self):
		# Check the data is available or not only when it is not in testing mode
		# Show the data recorder window if there are no data
		if not Constants.test and self.judge.clf is None:
			QMessageBox.warning(self, 'warning', 'Please record some data to initialize the service')
			self.recordData()

	def recordDataClose(self, val):
		if val == 1:
			self.dumpStoringData()
		self.recorder = None
		self.judge.initialize()
		self.judgeStatusCheck()

	def dumpStoringData(self):
		# dump the recording data when data recorder is done. (press ok)
		for class_id, data in self.recorder.measure.items():
			filename = join(Constants.DATA_DIR, 'class' + str(class_id) + '.txt')
			with open(filename, 'w+') as file:
				for time, measure in data:
					txt = list(map(str, measure))
					row = '\t'.join([time] + txt)
					file.write(row + '\n')

	def guiUpdate(self):
		# convert a list of float to 0 ~ 255 in stylesheet format
		def getFormatColor(raw_color):
			res = 'rgb('
			res += ', '.join([str(int(i * 255)) for i in raw_color])
			res += ')'
			return res
		
		# convert volt into color
		def getColorMap(volts, cm):
			res = []
			for v in volts:
				color = cm(int(v / 5.15 * 255))
				res.append(getFormatColor(color))

			return res

		# update the pressure heatmap
		if self.measure is not None:
			colors = getColorMap(self.measure, self.cm)
			self.ui.bottomLeft.setStyleSheet('QWidget { background: %s }' % colors[0])
			self.ui.bottomBack.setStyleSheet('QWidget { background: %s }' % colors[1])
			self.ui.bottomRight.setStyleSheet('QWidget { background: %s }' % colors[2])
			self.ui.backLeft.setStyleSheet('QWidget { background: %s }' % colors[3])
			self.ui.backRight.setStyleSheet('QWidget { background: %s }' % colors[4])
			self.ui.backDown.setStyleSheet('QWidget { background: %s }' % colors[5])

		# update the posture image
		filename = str(Posture(self.predict['predict'])) + '.png'
		self.ui.imageHolder.setPixmap(QPixmap(join(Constants.IMG_DIR, filename)))
		self.ui.imageHolder.show()

''' The class for the data recorder dialog. '''
class DataRecorder(QDialog):
	def __init__(self, parent=None):
		# UI init
		super(QDialog, self).__init__(parent)
		self.ui = Ui_DataRecorder()
		self.ui.setupUi(self)
		self.updateComboBox()
		self.setPosturePicture(0)
		self.parent = parent
		self.recording = False
		self.measure = defaultdict(list)
		self.guiTimer = QTimer()
		self.guiTimer.start(0)

		# Connection
		self.ui.ComboClass.currentIndexChanged.connect(self.setPosturePicture)
		self.ui.RecordingButton.clicked.connect(self.recordingClicked)
		self.guiTimer.timeout.connect(self.guiUpdate)
		
		# show the window
		self.show()

	def updateComboBox(self):
		for i in range(len(Posture)):
			self.ui.ComboClass.addItem(str(Posture(i)))

	def setPosturePicture(self, value):
		filename = str(Posture(value)) + '.png'
		self.ui.imageHolder.setPixmap(QPixmap(join(Constants.IMG_DIR, filename)))
		self.ui.imageHolder.show()

	def recordingClicked(self):
		# # pop out a warning window if posture id is selected
		# if self.ui.ComboClass.currentIndex() == 0:
		# 	QMessageBox.warning(self, 'warning', 'You need to select a posture to record the data')
		# 	return

		self.recording = not self.recording
		# using guiUpdate to update the gui
		
	def guiUpdate(self):
		buttonMsg = 'Stop Recording' if self.recording else 'Start Recording'
		self.ui.ComboClass.setEnabled(not self.recording)
		self.ui.RecordingButton.setText(buttonMsg)

''' Posture Warning Class '''
class Warning(QDialog):
	def __init__(self, parent=None):
		# UI init
		super(QDialog, self).__init__(parent)
		self.ui = Ui_Warning()
		self.ui.setupUi(self)

		# connection
		self.ui.OKButton.clicked.connect(self.hide)
	
		self.show()



