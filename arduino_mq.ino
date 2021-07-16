
int mq_sensor=A0;

void setup() {
  // From which pin, you want to read 14 Digital, 6 Analog
  pinMode(mq_sensor,INPUT); // read permission

  // Serial Communication
  Serial.begin(9600); // 9600bps
}

void loop() {
  // Data Read, let m be 1023 
  int m=analogRead(mq_sensor); // ADC - 10bit (0 to 5V to 0 to 1023)

  Serial.print("#"); // # - SOF
  Serial.print(","); // , - Seperator
  Serial.print(m); // m - Data
  Serial.print(","); // , - Seperator
  Serial.println("~"); // ~ - EOF
  delay(1000); // 1 second  
}
