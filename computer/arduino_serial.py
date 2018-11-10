from __future__ import print_function, division, absolute_import

import time

from robust_serial import write_order, Order, write_i8, write_i16, read_i8, read_order, decode_order
from robust_serial.utils import open_serial_port

if __name__ == '__main__':
    try:
        serial_file=open_serial_port(baudrate=115200, timeout=None)
    except Exception as e:
        raise e

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

    # Equivalent to write_i8(serial_file, Order.MOTOR.value)
    for i in range(4):
        write_order(serial_file, Order.LED)
        write_i8(serial_file, 1)
        time.sleep(1)
        order = read_order(serial_file)
        decode_order(serial_file, order, debug=True)

        write_order(serial_file, Order.LED)
        write_i8(serial_file, 0)
        time.sleep(1)
        order = read_order(serial_file)
        decode_order(serial_file, order, debug=True)

    # for _ in range(10):
    #     order = read_order(serial_file)
    #     print("Ordered received: {:?}", order)

