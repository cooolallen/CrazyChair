int value = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600); // user the same baud-rate as the python side
  Serial.println("Connection established...");
}

void loop() {
  while (Serial.available()) {
    value = Serial.read();
  }
  
  if (value == '1')
    digitalWrite(LED_BUILTIN, HIGH);
   
  else if (value == '0')
    digitalWrite(LED_BUILTIN, LOW);
}
