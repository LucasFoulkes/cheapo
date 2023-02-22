const byte buttonPin1 = 12;
const byte buttonPin2 = 2;
volatile int counter1 = 0;
volatile int counter2 = 0;
const int leftMotorPin1 = 3;
const int leftMotorPin2 = 5;
const int rightMotorPin1 = 6;
const int rightMotorPin2 = 9;
int leftSpeed = 0;
int rightSpeed = 0;

void setup()
{
    PCICR |= B00000001;
    PCMSK0 |= B00010000;
    PCICR |= B00000100;
    PCMSK2 |= B00000100;

    pinMode(leftMotorPin1, OUTPUT);
    pinMode(leftMotorPin2, OUTPUT);
    pinMode(rightMotorPin1, OUTPUT);
    pinMode(rightMotorPin2, OUTPUT);

    Serial.begin(9600); // initialize serial communication at 9600 baud
}

void loop()
{
    if (Serial.available() > 0)
    {
        String inputString = Serial.readStringUntil('\n');
        leftSpeed = inputString.substring(0, inputString.indexOf(',')).toInt();
        rightSpeed = inputString.substring(inputString.indexOf(',') + 1).toInt();
        int leftValue = map(leftSpeed, -100, 100, -255, 255);
        int rightValue = map(rightSpeed, -100, 100, -255, 255);

        if (leftSpeed > 0)
        {
            digitalWrite(leftMotorPin1, LOW);
            analogWrite(leftMotorPin2, leftValue);
        }
        else if (leftSpeed < 0)
        {
            analogWrite(leftMotorPin1, abs(leftValue));
            digitalWrite(leftMotorPin2, LOW);
        }
        else
        {
            digitalWrite(leftMotorPin1, LOW);
            digitalWrite(leftMotorPin2, LOW);
        }
        if (rightSpeed > 0)
        {
            digitalWrite(rightMotorPin1, LOW);
            analogWrite(rightMotorPin2, rightValue);
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

    Serial.print(-50);
    Serial.print(',');
    Serial.print((counter1 + counter2) / 2);
    Serial.print(", ");
    Serial.print((counter1 - counter2) / 2);
    Serial.print(',');
    Serial.println(50);
    counter1 = 0;
    counter2 = 0;
    delay(100);
}

ISR(PCINT0_vect)
{
    counter1++; // increment counter1
}

ISR(PCINT2_vect)
{
    counter2++; // increment counter2
}
