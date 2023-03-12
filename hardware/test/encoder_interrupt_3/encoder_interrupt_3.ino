#include <TimerOne.h>

const byte encoderPinA = 2;
const int threshold = 5;
volatile unsigned long lastInterruptTime = 0;
volatile int counter = 0;

void ISR_counter()
{
    unsigned long interruptTime = millis();
    // Only count the pulse if it is far enough apart from the previous pulse
    if (interruptTime - lastInterruptTime > threshold)
    {
        counter++;
        lastInterruptTime = interruptTime;
    }
}

void ISR_timerone()
{
    Timer1.detachInterrupt();
    Serial.println(counter);
    counter = 0;
    Timer1.attachInterrupt(ISR_timerone);
}

void setup()
{
    Serial.begin(9600);
    Timer1.initialize(100000);
    attachInterrupt(digitalPinToInterrupt(encoderPinA), ISR_counter, CHANGE);
    Timer1.attachInterrupt(ISR_timerone);
}

void loop()
{
}
