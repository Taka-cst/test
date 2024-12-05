import processing.serial.*;
Serial port;
void setup(){
    port=new Serial(this,"COM4",9600);
}
void draw(){
    int inReadData=port.read();
    println(inReadData);
    delay(100);
}