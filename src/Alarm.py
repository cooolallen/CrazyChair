''' The class to control all the alarm related function. '''

import Constants
from Email import PostOfficer
from PyQt5.QtWidgets import QMessageBox
import datetime

class Alarm(object):
	def __init__(self, defaultParams, parent=None):
		self.parent = parent
		self.initialState = defaultParams
		self.postOfficer = PostOfficer()
		self.updateParams = None
		self.reset()

	def reset(self):
		self.timer = self.initialState.copy()

	def updateInitialState(self):
		self.initialState = self.updateParams
		self.reset()

	def getInitialState(self):
		return self.initialState

	def tick(self):
		if self.updateParams is not None:
			self.updateInitialState()
			self.updateParams = None

		self.not_lst = []
		for k in self.timer.keys():
			self.timer[k] -= 1
			if self.timer[k] == 0:
				# timer timeout
				self.timer[k] = self.initialState[k]
				self.notify(k)

	def notify(self, notType):
		print(str(datetime.datetime.now()), notType, 'has been triggered')
		if notType == 'vibrate':
			self.parent.arduino.vibrate()
		elif notType == 'pop_up':
			self.showWarning()
		elif notType == 'phone':
			self.sending_phone_notification()
		else:
			print('warning: key %s not found for the notification type' % (notType))

	def showWarning(self):
		self.parent.warning.showWarning()

	def sending_phone_notification(self):
		# using email as our first step
		self.postOfficer.send(msg='posture not good')

