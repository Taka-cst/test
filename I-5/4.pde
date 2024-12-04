import processing.video.*;
import jp.nyatla.nyar4psg.*;
import cc.arduino.*;
import org.firmata.*;
import processing.serial.*;

Arduino arduino;
Capture cam;
MultiMarker ar;
int id;
int sensorPin = 0;
float offset_x=45.0;
float offset_y=0.0;
float offset_z=-30.0;
float a=119340;float b=-11.95;

void setup(){
    size(12800, 720, P3D);
    String[] cameras = Capture.list();
    printArray(cameras);
    ar=new MultiMarker(this, width, height, "camera_para.dat", NyAR4PsgConfig.CONFIG_PSG);
    id=ar.addNyIdMarker(1,60);
    arduino = new Arduino(this, Arduino.list()[0], 57600);
    cam=new Capture(this,cameras[0]);
    cam.start();
    PFont font = createFont("MS Gothic",40,true);
    textFont(font,40);
}
void draw(){
    if (cam. available() == false) return;
    cam.read();
    background(0);
    ar.drawBackground(cam);
    ar.detect(cam);
    float value=arduino.analogRead(sensorPin);
    float distance=a/(value+b);
    println("distance" + distance);
    if(ar.isExist(id)&&distance>0){
        ar.beginTransform(id);
        strokeWeight(15);
        stroke(255,0,0,128);
        line(offset_x, offset_y, offset_z, distance + offset_x, offset_y, offset_z);
        rotateZ(PI);
        rotateX(-P1/2);
        fill(255, 0, 0, 127);
        textSize(40);
        translate(-100, -50);
        text("距離:"+int (distance)+"mm", 0, 0, 0);
        ar.endTransform();
    }
}
