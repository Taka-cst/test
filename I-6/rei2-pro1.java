int SWITCHPIN = 7;
void setup(){
    Serial.begin(9600);
    pinMode(SWITCHPIN, INPUT);
}
void loop(){
    int push;
    push=digitalRead(SWITCHPIN);
    if(push==1){
        Serial.write("Test OK!!!\r");
        delay(100);
    }
}