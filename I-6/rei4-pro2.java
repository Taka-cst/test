import processing.serial.*;

Serial myPort;
int currentCommand = 1;

void setup() {
  size(200, 200);
  myPort = new Serial(this, "COM3", 9600);
}

void draw() {
  background(255);
  fill(0);
  textSize(32);
}

void mousePressed() {
  myPort.write(str(currentCommand));
  currentCommand++;
  if (currentCommand > 6) {
    currentCommand = 1;
  }
}