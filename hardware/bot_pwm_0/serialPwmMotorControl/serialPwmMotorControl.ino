// Define constants and variables
const int leftMotorPin = 9;
const int rightMotorPin = 10;

int leftMotorSpeed = 0;
int rightMotorSpeed = 0;

// Setup function
void setup()
{

  // Set motor pins as outputs
  pinMode(leftMotorPin, OUTPUT);
  pinMode(rightMotorPin, OUTPUT);

  // Start serial communication
  Serial.begin(9600);
}

// Loop function
void loop()
{
  // Read motor commands from serial port
  if (Serial.available() > 0)
  {
    String motorCommand = Serial.readStringUntil('\n');
    int index = motorCommand.indexOf('_');
    if (index != -1)
    {
      leftMotorSpeed = constrain(motorCommand.substring(0, index).toInt(), 0, 100);
      rightMotorSpeed = constrain(motorCommand.substring(index + 1).toInt(), 0, 100);
    }
    delay(10); // Add a small delay to allow the Arduino to process the input
  }

  // Update the motor speeds
  analogWrite(leftMotorPin, leftMotorSpeed * 2.55);
  analogWrite(rightMotorPin, rightMotorSpeed * 2.55);
}
