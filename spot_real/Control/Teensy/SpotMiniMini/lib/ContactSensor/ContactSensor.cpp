#include "ContactSensor.hpp"
#include <Arduino.h>

void ContactSensor::Initialize(const int & in_sensor_pin, const int & in_led_pin) {
  sensor_pin = in_sensor_pin;
  led_pin = in_led_pin;

  pinMode(led_pin, OUTPUT);

  double av = 0;
  for(int i=0; i < numSamples; i++) {
    av += analogRead(sensor_pin);
    delay(5);
  }
  center = av / numSamples;
}

void ContactSensor::update_clk() {
  val = alpha * prev_val + (1 - alpha) * abs(analogRead(sensor_pin) - center);  // read the input pin
  if(val > thresh) {
    digitalWrite(led_pin, HIGH);
  } else {
    digitalWrite(led_pin, LOW);
  }
  prev_val = val;
}

bool ContactSensor::isTriggered() {
  // Serial.println(val);
  if(val > thresh) {
    return true;
  }
  return false;
}
