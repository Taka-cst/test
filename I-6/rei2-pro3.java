int SWITCHPIN1=7;
int SWITCHPIN2=8;

void setup(){
    Serial.begin(9600);
    pinMode(SWITCHPIN1,INPUT);
    pinMode(SWITCHPIN2,INPUT);
}

void loop(){
    int value1=digitalRead(SWITCHPIN1);
    int value2=digitalRead(SWITCHPIN2);
    Serial.write("Pushed1\n");
    Serial.write("Pushed2\n");
    delay(100);
}