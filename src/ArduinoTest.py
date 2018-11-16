# Testing module for arduino
# we don't need arduino plug in to test the UI


import random

class ArduinoTest(object):
	def write(self, value):
		pass

	# mimic the behavior of arduino
	def readline(self):
		msg = "\t".join([str(random.randint(0, 501) / 100) for _ in range(6)]).encode('utf-8')

		return msg