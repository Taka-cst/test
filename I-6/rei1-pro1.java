int LEDPIN =9;
void setup(){
    Serial.begin(9600);
    pinMode(LEDPIN, OUTPUT);
}

void loop(){
    char val;
    if(Serial.available()>0){
        val=Serial.read();
    }
    if(val=='H'){
        digitalWrite(LEDPIN, HIGH);
    }else{
        digitalWrite(LEDPIN, LOW);
    }
}