#include <SoftwareSerial.h>
#include <Wire.h>
#include <Multiservo.h>
Multiservo myservo;
int pos = 90;
int posR = 90;
// motor driver CJNMCU
// схема подключение мотора
// https://www.xsimulator.net/community/attachments/motomonstersetup-jpg.27135/
const uint8_t EN = 8;
const uint8_t INA = 9;
const uint8_t INB = 10;
const uint8_t PWM = 11;
unsigned long timing = 0;
// скорость мотора
uint8_t motorSpeed = 55;
uint8_t motorSpeedBack = 60;
uint8_t motorStop = 0;
uint8_t motorSpeedHigh = 80;
uint8_t motorSpeedLow = 40;
uint8_t znakNumber = 0;
uint8_t znak = 0;
uint8_t NPr = 0;
uint8_t sc = 0;
uint8_t zp = 0;
uint8_t start = 0;

void setup() {
  Serial.begin(115200);
  pinMode(EN, OUTPUT);
  pinMode(INA, OUTPUT);
  pinMode(INB, OUTPUT);
  pinMode(PWM, OUTPUT);
  digitalWrite(EN, HIGH);
  Wire.begin();
  myservo.attach(11);
  myservo.write(pos);
  delay(6000);
}

void loop() {
  if (Serial.available() > 0)
  {
    znakNumber = Serial.parseInt();
    comeZnak();
    if (start == 0) {
      digitalWrite(INA, HIGH);
      digitalWrite(INB, HIGH);
      analogWrite(PWM, motorStop);
    }
    if (start == 1 || znakNumber == 5) {
      comeZnak();
    }
  }
}
/////////////////////////////////
void znakNerovno() {
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeedLow);
  myservo.write(85);
  delay(1000);
  while (millis() - timing > 2000) {
    timing = millis();
    digitalWrite(INA, HIGH);
    digitalWrite(INB, LOW);
    analogWrite(PWM, motorSpeedLow);
    znak = 2;
  }
}
//////////////////////////////////
void znakPriorit() {
  if (zp == 0) {
    digitalWrite(INA, HIGH);
    digitalWrite(INB, LOW);
    analogWrite(PWM, motorSpeedHigh);
    delay (1000);
    zp = 1;
  }
  if (zp == 1) {
    znak = 0;
  }
}
//////////////////////////////////
void forvard() {
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeed);
}
//////////////////////////////////

void stopCar() {
  digitalWrite(INA, HIGH);
  digitalWrite(INB, HIGH);
  analogWrite(PWM, motorStop);
  delay (2000);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeed);
  delay (700);
}
//////////////////////////////////

void back() {
  digitalWrite(INA, HIGH);
  digitalWrite(INB, HIGH);
  analogWrite(PWM, motorStop);
  delay (500);
  digitalWrite(INA, LOW);
  digitalWrite(INB, HIGH);
  analogWrite(PWM, motorSpeedBack);
  delay (500);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, HIGH);
  analogWrite(PWM, motorStop);
  delay (2000);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeed);
  delay (2000);
}
//////////////////////////////////
void parking() {
  myservo.write(pos);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeed);
  delay (500);
  myservo.write(102);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeed);
  delay (200);
  myservo.write(87);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeed);
  delay (500);
  myservo.write(77);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeed);
  delay (200);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, HIGH);
  analogWrite(PWM, motorStop);
  delay (5000);
  znakNumber = 0;
  myservo.write(48);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeedLow);
  delay (500);
  myservo.write(45);
  digitalWrite(INA, HIGH);
  digitalWrite(INB, LOW);
  analogWrite(PWM, motorSpeed);
  delay (1000);
}
//////////////////////////////////
void comeZnak() {
  if (Serial.available() > 0)
  {
    znakNumber = Serial.parseInt();
    if (znakNumber < 10) {
      switch (znakNumber) {
        case 0:
          znak = 0;
          forvard();
          flushSerial();
          break;
        case 1:
          znak = 1;
          stopCar();
          flushSerial();
          break;
        case 2:
          znak = 2;
          znakNerovno();
          flushSerial();
          break;
        case 3:
          znak = 3;
          back();
          flushSerial();
          break;
        case 4:
          znak = 4;
          parking();
          flushSerial();
          break;
        case 5:
          znak = 5;
          start = 1;
          forvard();
          flushSerial();
          break;
        case 6:
          znak = 6;
          digitalWrite(INA, HIGH);
          digitalWrite(INB, HIGH);
          analogWrite(PWM, motorStop);
          break;
          flushSerial();
        case 7:
          znak = 7;
          digitalWrite(INA, HIGH);
          digitalWrite(INB, HIGH);
          analogWrite(PWM, motorStop);
          break;
      }
    }
    if (znakNumber > 10) {
      posR = constrain(znakNumber, 65, 115); // можно изменить угол 22 82
      myservo.write(posR);
    }
  }
}

void flushSerial() {
  while (Serial.available()) {
    Serial.read();
  }
}
