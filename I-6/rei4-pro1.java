void setup() {
    Serial.begin(9600);
    for (int pin=8;pin<=13;pin++) {pinMode(pin, OUTPUT);}
}
void loop() {
    if(Serial.available()>0){
        char data=Serial.read();
        if(data=='1'){m1();}
        if(data=='2'){m2();}
        if(data=='3'){m3();}
        if(data=='4'){m4();}
        if(data=='5'){m5();}
        if(data=='0'){resets();}
    }
}
void resets(){
    for(int pin=8;pin<=10;pin++) {digitalWrite(pin, LOW);}
    for (int pin=11;pin<=13;pin++) {digitalWrite(pin, LOW);}
}
void m1(){
    int times=0;
    while(1){
        if(times>500){break;}
        digitalWrite(8, LOW);
        digitalWrite(11, HIGH);
        digitalWrite(12, LOW);
        digitalWrite(13, HIGH);
        delay(1);
        digitalWrite(8, HIGH);
        digitalWrite(9, LOW);
        digitalWrite(11, LOW); 
        digitalWrite(12, HIGH);
        digitalWrite(13, LOW);
        delay(1);
        digitalWrite(9, HIGH);
        digitalWrite(10, LOW);
        digitalWrite(11, HIGH);
        digitalWrite(12, LOW);
        digitalWrite(13, HIGH);
        delay(1);
        digitalWrite(10, HIGH);
        times++;
    }
}
void m2(){
    int times=0;
    while(1){if(times>=500){break;}
    digitalWrite(8, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(13, HIGH);
    delay(1);
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(13, HIGH);
    delay(1);
    digitalWrite(9, HIGH);
    digitalWrite(10, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(13, HIGH);
    delay(1);
    digitalWrite(10, HIGH);   
    times++;
    } 
}

void m3(){
    int times=0;
    while(1){
        if(times>=500){break;}
        digitalWrite(13,HIGH);
        digitalWrite(10,LOW);
        digitalWrite(9,LOW);
        digitalWrite(8,LOW);
        delay(3);
        digitalWrite(13,HIGH);
        times++;
    }
}
void m4(){
    int times=0;
    while(1){
        if(times>=500){break;}
        digitalWrite(12,HIGH);
        digitalWrite(10,LOW);
        digitalWrite(9,LOW);
        digitalWrite(8,LOW);
        delay(3);
        digitalWrite(12,HIGH);
        times++;
    }
}
void m5(){
    int times=0;
    while(1){
        if(times>=500){break;}
        digitalWrite(11,HIGH);
        digitalWrite(10,LOW);
        digitalWrite(9,LOW);
        digitalWrite(8,LOW);
        delay(3);
        digitalWrite(11,HIGH);
        times++;
    }
}