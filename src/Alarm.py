''' The class to control all the alarm related function. '''

import Constants
from Email import PostOfficer
from PyQt5.QtWidgets import QMessageBox

class Alarm(object):
	def __init__(self, parent=None):
		self.parent = parent
		self.timer = Constants.alarmParams.copy()
		self.postOfficer = PostOfficer()

	def reset(self):
		self.timer = Constants.alarmParams.copy()

	def tick(self):
		self.not_lst = []
		for k in self.timer.keys():
			self.timer[k] -= 1
			if self.timer[k] == 0:
				# timer timeout
				self.timer[k] = Constants.alarmParams[k]
				self.notify(k)


	def notify(self, notType):
		print(notType, 'has been triggered')
		if notType == 'vibrate':
			self.parent.arduino.vibrate()
		elif notType == 'pop_out':
			self.showWarning()
		elif notType == 'phone':
			self.sending_phone_notification()
		else:
			print('warning: key %s not found for the notification type' % (notType))

	def showWarning(self):
		self.parent.warning.show()

	def sending_phone_notification(self):
		# using email as our first step
		self.postOfficer.send(msg='posture not good')

