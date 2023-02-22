const int leftMotorPin1 = 3;
const int leftMotorPin2 = 5;
const int rightMotorPin1 = 10;
const int rightMotorPin2 = 9;

const int MAX_SPEED = 255;

int leftSpeed = 0;
int rightSpeed = 0;

void setup()
{
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);

  Serial.begin(9600);
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

    Serial.print(leftValue);
    Serial.print(",");
    Serial.print(rightValue);
    Serial.print("\n");

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
}
