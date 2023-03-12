const byte encoderPinA = 2;
const int threshold = 5;
volatile unsigned long lastInterruptTime = 0;
volatile int counter = 0;
const int rightMotorPin1 = 10;
const int rightMotorPin2 = 9;
int rightSpeed = 0;
unsigned long previousMillis = 0;
const long interval = 100,
{
    unsigned long interruptTime = millis();
    if (interruptTime - lastInterruptTime > threshold)
    {
        counter++;
        lastInterruptTime = interruptTime;
    }
}

void setup()
{
    pinMode(rightMotorPin1, OUTPUT);
    pinMode(rightMotorPin2, OUTPUT);
    attachInterrupt(digitalPinToInterrupt(encoderPinA), isrEncoder, CHANGE);
    Serial.begin(9600);
}

void loop()
{
    if (Serial.available() > 0)
    {
        String inputString = Serial.readStringUntil('\n');
        rightSpeed = inputString.toInt();

        int rightValue = map(rightSpeed, -100, 100, -255, 255);

        if (rightSpeed > 0)
        {
            digitalWrite(rightMotorPin1, LOW);
            analogWrite(rightMotorPin2, abs(rightValue));
        }
        else if (rightSpeed < 0)
        {
            analogWrite(rightMotorPin1, abs(rightValue));
            digitalWrite(rightMotorPin2, LOW);
        }
        else
        {
            digitalWrite(rightMotorPin1, LOW);
            digitalWrite(rightMotorPin2, LOW);
        }
    }
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval)
    {
        previousMillis = currentMillis;
        Serial.println(counter);
        counter = 0;
    }
}
