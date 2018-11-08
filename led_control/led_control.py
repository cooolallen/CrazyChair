import serial

def main():
	Arduino_Serial = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=.1)
	print(Arduino_Serial.readline())					# somehow didn't get anything
	print("enter 1 to ON LED and 0 to OFF LED")

	while True:
		input_data = input().encode('utf-8')			# wait user's input
		print("you enter", input_data)					# for checking

		if (input_data == b'1'):
			Arduino_Serial.write(input_data)
			print('LED ON')
		elif (input_data == b'0'):
			Arduino_Serial.write(input_data)
			print('LED OFF')





if __name__ == '__main__':
	main()