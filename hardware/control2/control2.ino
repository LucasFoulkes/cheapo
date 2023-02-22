// Define motor pins
const int leftMotorPin1 = 3;
const int leftMotorPin2 = 5;
const int rightMotorPin1 = 10;
const int rightMotorPin2 = 9;

// Define maximum motor speed and wheel radius
const int MAX_SPEED = 255;

// Define variables for left and right motor speeds
int leftSpeed = 0;
int rightSpeed = 0;

void setup()
{
  // Set motor pins as outputs
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);

  // Initialize serial communication
  Serial.begin(9600);
}

void loop()
{
  // Check for incoming serial data
  if (Serial.available() > 0)
  {
    // Read incoming data
    String inputString = Serial.readStringUntil('\n');
    // Parse incoming data
    leftSpeed = inputString.substring(0, inputString.indexOf(',')).toInt();
    rightSpeed = inputString.substring(inputString.indexOf(',') + 1).toInt();

    // Map motor speeds to values between -255 and 255
    int leftValue = map(leftSpeed, -100, 100, -255, 255);
    int rightValue = map(rightSpeed, -100, 100, -255, 255);

    // Send mapped motor speeds back to Pygame program
    Serial.print(leftValue);
    Serial.print(",");
    Serial.print(rightValue);
    Serial.print("\n");

    // Set the motor directions and speeds based on the mapped values
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

    // Send odometry data back to Pygame program
    // TODO: Implement odometry data transmission
  }
}
