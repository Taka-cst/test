int PHOTOICPIN =1;
void setup(){
    Serial.begin(9600);
}
void loop(){
    int readData=analogRead(PHOTOICPIN);
    int value;
    value=map(readData,0,800,0,255);
    Serial.write(value);
    delay(100);
}

