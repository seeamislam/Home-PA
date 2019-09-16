void setup() {
  Serial.begin(9600); // use the same baud-rate as the python side
  pinMode(13,INPUT);
}
void loop() {
  int state = digitalRead(13);
  if (state == 1){
  Serial.println("open"); // Door is detected as open
  delay(1000);}


  if (state == 0){
    Serial.println("closed"); // Door detected as closed
    delay(1000);}
}
