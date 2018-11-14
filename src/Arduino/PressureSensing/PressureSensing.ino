int led = 9;
int brightness = 0;
int value = 0;


#define NUM_SAMPLES 10
int sum1 = 0, sum2 = 0, sum3 = 0;
int sample_count = 0;
float v1 = 0.0, v2 = 0.0, v3 = 0.0;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600); // user the same baud-rate as the python side
  //Serial.println("Connection established...");
}

void loop() {
  // led control
  while (Serial.available()) {
    value = Serial.read();
  }
  brightness = value;
  
//  if (value == '1')
//    brightness = 255;
//  else if (value == '0')
//    brightness = 0;
 // Serial.print(brightness);
 // Serial.print("\t");
  analogWrite(led, brightness);
  
  // get voltage
  // take a number of analog samples and add them up
    while (sample_count < NUM_SAMPLES) {
        sum1 += analogRead(A0);
        sum2 += analogRead(A1);
        sum3 += analogRead(A2);
        sample_count++;
        delay(10);
    }
    // calculate the voltage
    // use 5.0 for a 5.0V ADC reference voltage
    // 5.015V is the calibrated reference voltage
    v1 = ((float)sum1 / (float)NUM_SAMPLES * 5.015) / 1024.0;
    v2 = ((float)sum2 / (float)NUM_SAMPLES * 5.015) / 1024.0;
    v3 = ((float)sum3 / (float)NUM_SAMPLES * 5.015) / 1024.0;
    // send voltage for display on Serial Monitor
    Serial.print(v1);
    Serial.print("\t");
    Serial.print(v2);
    Serial.print("\t");
    Serial.println(v3);
    sample_count = 0;
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
  
}
