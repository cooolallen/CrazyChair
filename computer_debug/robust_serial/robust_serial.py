from __future__ import print_function, division, unicode_literals, absolute_import

import struct
from enum import Enum


class Order(Enum):
    """
    Pre-defined orders
    """
    HELLO            =0
    ALREADY_CONNECTED=1
    ERROR            =2
    RECEIVED         =3
    STOP             =4
    LED              =5
    RESISTOR         =6
    VIBRATOR         =7

def read_i8(f):
    """
    :param f: file handler or serial file
    :return: (int8_t)
    """
    return struct.unpack('<b', bytearray(f.read(1)))[0]

def read_i16(f):
    """
    :param f: file handler or serial file
    :return: (int16_t)
    """
    return struct.unpack('<h', bytearray(f.read(2)))[0]

def read_i32(f):
    """
    :param f: file handler or serial file
    :return: (int32_t)
    """
    return struct.unpack('<l', bytearray(f.read(4)))[0]

def write_i8(f, value):
    """
    :param f: file handler or serial file
    :param value: (int8_t)
    """
    if -128 <= value <= 127:
        f.write(struct.pack('<b', value))
    else:
        print("Value error:{}".format(value))

def write_i16(f, value):
    """
    :param f: file handler or serial file
    :param value: (int16_t)
    """
    f.write(struct.pack('<h', value))

def write_i32(f, value):
    """
    :param f: file handler or serial file
    :param value: (int32_t)
    """
    f.write(struct.pack('<l', value))

def write_order(f, order):
    """
    :param f: file handler or serial file
    :param order: (Order Enum Object)
    """
    write_i8(f, order.value)

def read_order(f):
    """
    :param f: file handler or serial file
    :return: (Order Enum Object)
    """
    return Order(read_i8(f))

def decode_order(f, byte, debug=False):
    """
    :param f: file handler or serial file
    :param byte: (int8_t)
    :param debug: (bool) whether to print or not received messages
    """

    try:
        order=Order(byte)
        if order==Order.HELLO:
            msg="HELLO"
        elif order==Order.ALREADY_CONNECTED:
            msg="ALREADY_CONNECTED"
        elif order==Order.ERROR:
            error_code=read_i16(f)
            msg="Error {}".format(error_code)
        elif order==Order.RECEIVED:
            msg="RECEIVED"
        else:
            msg=""
            print("Unknown Order", byte)

        if debug:
            print("recieve:", msg)
    except Exception as e:
        print("Error decoding order {}: {}".format(byte, e))
        print('byte={0:08b}'.format(byte))

def send_command(f, order, value, debug=False):
    """
    :param f: file handler or serial file
    :param order: (Order Enum Object)
    :param value: (int8_t), (int16_t) or (int32_t)
    :param debug: (bool) whether to print or not received messages
    """
    write_i8(f, order)
    if order==Order.LED.value:
        write_i8(f, value)
    elif order==Order.RESISTOR.value:
        r_lst=[]
        for _ in range(6):
            r_lst.append(read_i16(f))
        print(r_lst)
    # elif order==Order.VIBRATOR:
        # do nothing
    # else:
        # do nothing


    if debug:
        print("send order", order, ", value:", value)

    # read acck from arduino
    r_order=read_order(f)
    decode_order(f, r_order, debug)

    return

def get_pressure(f, debug=False):
    write_order(f, Order.RESISTOR)
    r_lst=[]
    for _ in range(6):
        r_lst.append(read_i16(f))
    
    # ack from arduino
    r_order=read_order(f)
    decode_order(f, r_order, debug)

    return r_lst

def vibrate(f, debug=False):
    write_order(f, Order.VIBRATOR)
    # maybe add different vibration modes?
    #write_i8(mode)

    # ack from arduino
    r_order=read_order(f)
    decode_order(f, r_order, debug)

    return