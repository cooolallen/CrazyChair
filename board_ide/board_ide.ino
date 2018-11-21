#include <Arduino.h>

#include "order.h"
#include "slave.h"
#include "parameters.h"

bool is_connected=false; ///< True if the connection with the master is available
int8_t led_on=0;

// RESISTOR USE variable
int16_t sum1 = 0, sum2 = 0, sum3 = 0, sum4 = 0, sum5 = 0, sum6 = 0;
int sample_count = 0;
int16_t v1=0, v2=0, v3=0, v4=0, v5=0, v6=0;

void setup()
{
	// Init Serial
	Serial.begin(SERIAL_BAUD);

	// Init PINs
	pinMode(BROADLED_PIN, OUTPUT);
	pinMode(VIBRATOR_PIN, OUTPUT);
	pinMode(RESISTOR_PIN, OUTPUT);
    digitalWrite(BROADLED_PIN, LOW); // set led to off

	// visual check if broad is good
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

    // tell computer the number of samples
    //delay(2000);
    //write_i16((int16_t)124);
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
                if(led_on==1)digitalWrite(BROADLED_PIN, HIGH);
                else	     digitalWrite(BROADLED_PIN,  LOW);
                break;
            }
            case RESISTOR:
            {
                //get voltage
                //take a number of analog samples and add them up
                //sample_count=0;
                sum1=sum2=sum3=sum4=sum5=sum6=sample_count=0;
                while(sample_count<NUM_SAMPLES)
                {
                    sum1+=analogRead(A0);
                    sum2+=analogRead(A1);
                    sum3+=analogRead(A2);
                    sum4+=analogRead(A3);
                    sum5+=analogRead(A4);
                    sum6+=analogRead(A5);
                    sample_count++;
                    delay(10);
                }
                 
                // calculate the voltage
                // use 5.0 for a 5.0V ADC reference voltage
                // 5.015V is the calibrated reference voltage
                v1=(int)(((float)sum1/(float)NUM_SAMPLES*VDD)/1024.0);
                v2=(int)(((float)sum2/(float)NUM_SAMPLES*VDD)/1024.0);
                v3=(int)(((float)sum3/(float)NUM_SAMPLES*VDD)/1024.0);
                v4=(int)(((float)sum4/(float)NUM_SAMPLES*VDD)/1024.0);
                v5=(int)(((float)sum5/(float)NUM_SAMPLES*VDD)/1024.0);
                v6=(int)(((float)sum6/(float)NUM_SAMPLES*VDD)/1024.0);
                // assume voltage is a.bc, then we send abc
                write_i16(v1);
                write_i16(v2);
                write_i16(v3);
                write_i16(v4);
                write_i16(v5);
                write_i16(v6);

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
