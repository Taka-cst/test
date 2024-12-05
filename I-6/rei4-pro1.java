// import processing.serial.*;
// void setup() {
//   for (int pin=8;pin<=13;pin++) {pinMode(pin, OUTPUT);}
// }
// void loop() {
//     m1();delay(500);resets();
//     m2();delay(500);resets();
//     m3();delay(500);resets();
//     m4();delay(500);resets();
//     m5();delay(500);resets();
// }
// void resets(){
//     for(int pin=8;pin<=10;pin++) {digitalWrite(pin, LOW);}
//     for (int pin=11;pin<=13;pin++) {digitalWrite(pin, LOW);}
// }
// void m1(){
//     int times=0;
//     while(1){
//         if(times>500){break;}
//         digitalWrite(8, LOW);
//         digitalWrite(11, HIGH);
//         digitalWrite(12, LOW);
//         digitalWrite(13, HIGH);
//         delay(1);
//         digitalWrite(8, HIGH);
//         digitalWrite(9, LOW);
//         digitalWrite(11, LOW); 
//         digitalWrite(12, HIGH);
//         digitalWrite(13, LOW);
//         delay(1);
//         digitalWrite(9, HIGH);
//         digitalWrite(10, LOW);
//         digitalWrite(11, HIGH);
//         digitalWrite(12, LOW);
//         digitalWrite(13, HIGH);
//         delay(1);
//         digitalWrite(10, HIGH);
//         times++;
//     }
// }
// void m2(){
//     int times=0;
//     while(1){if(times>=500){break;}
//     digitalWrite(8, LOW);
//     digitalWrite(11, HIGH);
//     digitalWrite(12, HIGH);
//     digitalWrite(13, HIGH);
//     delay(1);
//     digitalWrite(8, HIGH);
//     digitalWrite(9, LOW);
//     digitalWrite(11, HIGH);
//     digitalWrite(12, LOW);
//     digitalWrite(13, HIGH);
//     delay(1);
//     digitalWrite(9, HIGH);
//     digitalWrite(10, LOW);
//     digitalWrite(11, HIGH);
//     digitalWrite(12, HIGH);
//     digitalWrite(13, HIGH);
//     delay(1);
//     digitalWrite(10, HIGH);   
//     times++;
//     } 
// }

// void m3(){
//     int times=0;
//     while(1){
//         if(times>=500){break;}
//         digitalWrite(13,HIGH);
//         digitalWrite(10,LOW);
//         digitalWrite(9,LOW);
//         digitalWrite(8,LOW);
//         delay(3);
//         digitalWrite(13,HIGH);
//         times++;
//     }
// }
// void m4(){
//     int times=0;
//     while(1){
//         if(times>=500){break;}
//         digitalWrite(12,HIGH);
//         digitalWrite(10,LOW);
//         digitalWrite(9,LOW);
//         digitalWrite(8,LOW);
//         delay(3);
//         digitalWrite(12,HIGH);
//         times++;
//     }
// }
// void m5(){
//     int times=0;
//     while(1){
//         if(times>=500){break;}
//         digitalWrite(11,HIGH);
//         digitalWrite(10,LOW);
//         digitalWrite(9,LOW);
//         digitalWrite(8,LOW);
//         delay(3);
//         digitalWrite(11,HIGH);
//         times++;
//     }
// }