import time

from robust_serial import Order, write_i8, write_i16, read_i8, read_i16
from robust_serial import write_order, read_order, decode_order, send_command
from robust_serial import get_pressure, vibrate
from robust_serial.utils import open_serial_port

if __name__ == '__main__':
    try:
        serial_file=open_serial_port(baudrate=115200, timeout=None)
    except Exception as e:
        raise e

    print(serial_file)
    is_connected=False
    # Initialize communication with Arduino
    while not is_connected:
        print("Waiting for arduino...")
        write_order(serial_file, Order.HELLO)
        bytes_array=bytearray(serial_file.read(1))
        if not bytes_array:
            time.sleep(2)
            continue
        byte=bytes_array[0]
        #if byte in [Order.HELLO.value, Order.ALREADY_CONNECTED.value]:
        if byte is Order.ALREADY_CONNECTED.value:
            is_connected=True

    print("Connected to Arduino")
    serial_file.flush()

    while True:
        # r=get_pressure(serial_file)
        # print(r)
        vibrate(serial_file)
        
        time.sleep(3)

        # order, value = [int(x) for x in raw_input("Enter two numbers here: ").split()]
        # send_command(serial_file, order, value)

