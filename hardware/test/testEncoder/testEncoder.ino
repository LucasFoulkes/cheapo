// Define motor pins
const int rightMotorPin1 = 10;
const int rightMotorPin2 = 9;
const int MAX_SPEED = 255;
int rightSpeed = 0;
const byte buttonPin1 = 12; // pin 12
volatile int counter1 = 0;
unsigned long previousMillis = 0;
const long interval = 250;

void setup()
{
    pinMode(rightMotorPin1, OUTPUT);
    pinMode(rightMotorPin2, OUTPUT);
    // ENABLE PCIE0 Bit0 = 1 (port B)
    PCICR |= B00000001;
    // SELECT PCINT4 Bit4 = 1 (pin 12)
    PCMSK0 |= B00010000;
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
        Serial.print("0,50,");
        Serial.println(counter1);
        counter1 = 0;
    }
}

ISR(PCINT0_vect)
{
    counter1++; // increment counter1
}
