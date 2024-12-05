import processing.serial.*;
Serial port;
void setup(){
    port=new Serial(this,"COM4",9600);
}

void draw(){
    String myString = port.readStringUntil('\r');
    println(myString);
    delay(100);
}