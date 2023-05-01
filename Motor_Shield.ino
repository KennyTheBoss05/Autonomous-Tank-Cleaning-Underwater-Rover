#include <AFMotor.h>

AF_DCMotor motor(4); //left wheel
AF_DCMotor motor2(3); //right wheel

char cmd = ' ';

void setup() 
{
  //Set initial speed of the motor & stop
  motor.setSpeed(200);
  motor.run(RELEASE);
  motor2.setSpeed(200);
  motor2.run(RELEASE);

  Serial.begin(9600);
}

void loop() 
{
  uint8_t i;
  uint8_t j;
  cmd = ' ';
  // check for incoming serial data:

 if (Serial.available())   
    {
      uint8_t j = 0;  
  cmd = Serial.read();
  if(cmd == 'w')
  {
    Serial.println("W");
   

  // Turn on motor
  motor.run(FORWARD);
  motor2.run(FORWARD);
  
  // Accelerate from zero to maximum speed
  for (i=0; i<255; i++) 
  {
    motor.setSpeed(i);
    motor2.setSpeed(i);  
    delay(10);
  }
  
  // Decelerate from maximum speed to zero
  for (i=255; i!=0; i--) 
  {
    motor.setSpeed(i);
    motor2.setSpeed(i);   
    delay(10);
  }
  }

  if(cmd == 's')
  {
    Serial.println("S");

  // Now change motor direction
  motor.run(BACKWARD);
  motor2.run(BACKWARD);
  
  // Accelerate from zero to maximum speed
  for (i=0; i<255; i++) 
  {
    motor.setSpeed(i);
    motor2.setSpeed(i);   
    delay(10);
  }

  // Decelerate from maximum speed to zero
  for (i=255; i!=0; i--) 
  {
    motor.setSpeed(i);
    motor2.setSpeed(i);   
    delay(10);
  }
  }

  if(cmd == 'a')
  {
    Serial.println("A");
   

  // Turn on motor
  motor2.run(FORWARD);
  
  // Accelerate from zero to maximum speed
  for (i=0; i<255; i++) 
  {
    motor2.setSpeed(i);  
    delay(10);
  }
  
  // Decelerate from maximum speed to zero
  for (i=255; i!=0; i--) 
  {
    motor2.setSpeed(i);   
    delay(10);
  }
  }

  if(cmd == 'd')
  {
    Serial.println("D");

  // Now change motor direction
  motor.run(FORWARD);
  
  // Accelerate from zero to maximum speed
  for (i=0; i<255; i++) 
  {
    motor.setSpeed(i);   
    delay(10);
  }

  // Decelerate from maximum speed to zero
  for (i=255; i!=0; i--) 
  {
    motor.setSpeed(i);  
    delay(10);
  }
  }

  // Now turn off motor
  motor.run(RELEASE);
  motor2.run(RELEASE);
  delay(100);
}
}
