import processing.video.*;
import jp.nyatla.nyar4psg.*;

Capture cam;
MultiMarker ar;
int id;

void setup(){
    size(1280,720,P3D);
    String[] cameras = Capture.list();
    printArray(cameras);
    ar=new MultiMarker(this,width,height, 
    "camera_para.dat", NyAR4PsgConfig.CONFIG_PSG);
    id=ar.addARMarker("patt.hiro",60);
    cam = new Capture(this, cameras[0]);
    cam.start();
}
void draw(){
    if(cam.available()==false){
        return;
    }
    cam.read();
    background(0);
    ar.drawBackground(cam);
    ar.detect(cam);
    if(ar.isExistMarker(id)){
        ar.beginTransform(id);
        fill(116,163,241,100);
        translate(0,0,15);
        box(30);
        ar.endTransform();
    }
}







