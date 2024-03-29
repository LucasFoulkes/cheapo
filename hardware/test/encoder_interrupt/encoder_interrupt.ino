#include <TimerOne.h>

const byte encoderPinA = 2;

volatile int counter = 0;
volatile int oldCount = 0;

void ISR_counter()
{
    counter++;
}

void ISR_timerone()
{
    Timer1.detachInterrupt();
    Serial.println(counter - oldCount);
    // Serial.println(counter);
    oldCount = counter;
    Timer1.attachInterrupt(ISR_timerone);
}

void setup()
{
    Serial.begin(9600);
    // pinMode(encoderPinA, INPUT_PULLUP);
    Timer1.initialize(100000);
    attachInterrupt(digitalPinToInterrupt(encoderPinA), ISR_counter, CHANGE);
    Timer1.attachInterrupt(ISR_timerone);
}

void loop()
{
}