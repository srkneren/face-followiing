#include <Servo.h>


Servo motorx;
int derece ;
int val ;
void setup(){
  
Serial.begin(115200);
Serial.setTimeout(100);
motorx.attach(9);

motorx.write(0);
}

void loop(){
  if(Serial.available()){
    
    derece = Serial.read();
    
    Serial.print(derece);
    motorx.write(derece);
  }
}
