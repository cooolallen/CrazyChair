
from Arduino.robust_serial import Order, write_i8, write_i16, read_i8, read_i16
from Arduino.robust_serial import write_order, read_order, decode_order, send_command
from Arduino.robust_serial import get_pressure, vibrate
from Arduino.robust_serial.utils import open_serial_port

import time
import serial

class Arduino(object):
	def __init__(self):
		self.is_connected = False
		self.serial = None
		self.initialize()

	def initialize(self):
		try:
			# self.serial=open_serial_port(baudrate=115200, timeout=None)
			self.serial = serial.Serial(port='/dev/cu.usbmodem1421',baudrate=115200, timeout=None)
		except Exception as e:
			raise e

		print(self.serial)
		# Initialize communication with Arduino
		while not self.is_connected:
			print("Waiting for arduino...")
			write_order(self.serial, Order.HELLO)
			bytes_array=bytearray(self.serial.read(1))
			if not bytes_array:
				time.sleep(2)
				continue
			byte=bytes_array[0]
			#if byte in [Order.HELLO.value, Order.ALREADY_CONNECTED.value]:
			if byte is Order.ALREADY_CONNECTED.value:
				self.is_connected=True


		print("Connected to Arduino")
		self.serial.flush()


	def get_pressure(self):
		return get_pressure(self.serial)

	def vibrate(self):
		return vibrate(self.serial)


if __name__ == '__main__':
	test = Arduino()
	print(test.get_pressure())