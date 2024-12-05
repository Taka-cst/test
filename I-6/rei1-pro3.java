import processing.serial.*;
Serial port;

void setup(){
    port=new Serial(this,"COM4",9600);
}
void draw(){

}
void mousePressed(){
    port.write('H');
}
void mouseReleased(){
    port.write('L');
}