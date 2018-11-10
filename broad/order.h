#ifndef ORDER_H
#define ORDER_H

// Define the orders that can be sent and received
enum Order {
  HELLO 		   =0,
  ALREADY_CONNECTED=1,
  ERROR			   =2,
  RECEIVED 		   =3,
  STOP			   =4,
  LED			   =5,

  RESISTOR		   =6,
  VIBRATOR		   =7
};

typedef enum Order Order;

#endif
