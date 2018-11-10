#include <Arduino.h>

#include "order.h"
#include "slave.h"
#include "parameters.h"

bool is_connected=false; ///< True if the connection with the master is available
int8_t led_on=0;

void setup()
{
	// Init Serial
	Serial.begin(SERIAL_BAUD);

	// Init PINs
	pinMode(BROADLED_PIN, OUTPUT);
	digitalWrite(BROADLED_PIN, LOW);
	pinMode(VIBRATOR_PIN, OUTPUT);
	pinMode(RESISTOR_PIN, OUTPUT);

	// check if broad is good
	digitalWrite(BROADLED_PIN, HIGH);   // sets the LED on
	delay(1000);                  // waits for a second
	digitalWrite(BROADLED_PIN, LOW);    // sets the LED off
	delay(1000);                  // waits for a second
	digitalWrite(BROADLED_PIN, HIGH);   // sets the LED on
	delay(1000);                  // waits for a second
	digitalWrite(BROADLED_PIN, LOW);    // sets the LED off
	delay(1000);                  // waits for a second
	digitalWrite(BROADLED_PIN, HIGH);   // sets the LED on
	

	// Wait until the arduino is connected to master
	while(!is_connected)
	{
		write_order(HELLO);
		wait_for_bytes(1, 1000);
		get_messages_from_serial();
	}
  	digitalWrite(BROADLED_PIN, LOW);    // sets the LED off
}

void loop()
{
	get_messages_from_serial();
}

void get_messages_from_serial()
{
    if(Serial.available()>0)
    {
        // The first byte received is the instruction
        Order order_received=read_order();
        switch(order_received)
        {
            case HELLO:
            {
                // If the cards haven't say hello, check the connection
                if(!is_connected)
                {
                    is_connected=true;
                    write_order(HELLO);
                }
                else
                {
                    // If we are already connected do not send "hello" to avoid infinite loop
                    write_order(ALREADY_CONNECTED);
                }
                return;
            }
            case ALREADY_CONNECTED:
            {
                is_connected=true;
                break;
            }
            case LED:
            {
                led_on=read_i8();
                if(led_on)digitalWrite(BROADLED_PIN, HIGH);
                else	  digitalWrite(BROADLED_PIN, LOW);
                break;
            }
            default:
            {
				write_order(ERROR);
				write_i16(404);
				return;
            }
        }
        write_order(RECEIVED); // Confirm the reception
    }
	return;
}