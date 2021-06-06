#include <Servo.h>


Servo motory;
int derece ;
int val ;
void setup(){
  
Serial.begin(115200);
Serial.setTimeout(100);
motory.attach(3);

motory.write(0);
}

void loop(){
  if(Serial.available()){
    
    derece = Serial.read();
    
    Serial.print(derece);
    motory.write(derece);
  }
}
