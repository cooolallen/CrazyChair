int led = 9;
int brightness = 0;
int value = 0;


#define NUM_SAMPLES 10
int sum = 0;
int sample_count = 0;
float voltage = 0.0;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600); // user the same baud-rate as the python side
  Serial.println("Connection established...");
}

void loop() {
  // led control
  while (Serial.available()) {
    value = Serial.read();
  }
  
  if (value == '1')
    brightness = 255;
  else if (value == '0')
    brightness = 0;
    
  analogWrite(led, brightness);
  
  // get voltage
  // take a number of analog samples and add them up
    while (sample_count < NUM_SAMPLES) {
        sum += analogRead(A2);
        sample_count++;
        delay(10);
    }
    // calculate the voltage
    // use 5.0 for a 5.0V ADC reference voltage
    // 5.015V is the calibrated reference voltage
    voltage = ((float)sum / (float)NUM_SAMPLES * 5.015) / 1024.0;
    // send voltage for display on Serial Monitor
    Serial.print(voltage);
    Serial.println (" V");
    sample_count = 0;
    sum = 0;
  
}
