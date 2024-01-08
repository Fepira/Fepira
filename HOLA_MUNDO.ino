#include <Servo.h>
//Definicion de los servos
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

int eje1=90;
int eje2=90;
int eje3=90;
int eje4=90;


void setup(){  
  servo1.attach(7);
  servo2.attach(6);
  servo3.attach(8);
  servo4.attach(9);
  /*servo1.write(90);
  servo2.write(0);
  servo3.write(0);
  servo4.write(90);*/

  

}
void loop(){

  //SERVO 1
  if (analogRead(0)<200 && eje1<180){
    eje1++;
    servo1.write(eje1);
  }
  if (analogRead(0)>700 && eje1>0){
    eje1--;
    servo1.write(eje1);
  }
  //SERVO 2
  if (analogRead(1)<200 && eje2<180){
    eje2++;
    servo2.write(eje2);
  }
  if (analogRead(1)>700 && eje2>0){
    eje2--;
    servo2.write(eje2);
  }
  if (analogRead(2)<200 && eje3<180){
    eje3++;
    servo3.write(eje3);
  }
  if (analogRead(2)>700 && eje3>0){
    eje3--;
    servo3.write(eje3);
  }
  //SERVO 2
  if (analogRead(3)<200 && eje4<180){
    eje4++;
    servo4.write(eje4);
  }
  if (analogRead(3)>700 && eje4>0){
    eje4--;
    servo4.write(eje4);
  }
  delay(15);


}
