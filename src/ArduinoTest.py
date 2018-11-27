# Testing module for arduino
# we don't need arduino plug in to test the UI
import random

class ArduinoTest(object):
	def write(self, value):
		pass

	# mimic the behavior of arduino
	def get_pressure(self):
		return [random.randint(0, 515) / 100 for _ in range(6)]

	def vibrate(self):
		print("vibration trigger")
		return