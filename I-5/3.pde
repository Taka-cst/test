import org.firmata.*;
import cc.arduino.*;
import processing.serial.*;

Arduino arduino;
int sensorPin = 0;
int d1=80;int d2=600;
float a=0;float b=0;
float value=0; float v1=0; float v2=0;
float[] buf=null;
int N=10;int k=0;

void setup(){
    arduino=new Arduino(this,Arduino.list()[0],57600);
    buf=new float[N];
}

void draw(){
    value=arduino.analogRead(sensorPin);
    k=(k+1)%N;
    float sum=0;
    for(int i=0;i<N;i++){
        sum+=buf[i];
    }
    value=sum/N;

    float distance=a/(value+b);
    println("a="+a);
    println("b="+b);
    println("distance="+distance);
}

void keyPressed(){
    if(key=='1'){v1=value;}
    else if(key=='2'){v2=value;}
    b=-(d1*v1 -d2*v2)/(d1-d2);
    a=b1*(v1+b);
}