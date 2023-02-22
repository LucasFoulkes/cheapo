const int motor_left[] = {10, 11};
const int motor_right[] = {6, 7};

void setup()
{
  pinMode(motor_left[0], OUTPUT);
  pinMode(motor_left[1], OUTPUT);
  pinMode(motor_right[0], OUTPUT);
  pinMode(motor_right[1], OUTPUT);
  Serial.begin(115200);
}

void forward()
{
  stop();
  digitalWrite(motor_left[0], HIGH);
  digitalWrite(motor_left[1], LOW);
  digitalWrite(motor_right[0], HIGH);
  digitalWrite(motor_right[1], LOW);
}

void backward()
{
  stop();
  digitalWrite(motor_left[0], LOW);
  digitalWrite(motor_left[1], HIGH);
  digitalWrite(motor_right[0], LOW);
  digitalWrite(motor_right[1], HIGH);
}

void left()
{
  stop();
  digitalWrite(motor_left[0], LOW);
  digitalWrite(motor_left[1], HIGH);
  digitalWrite(motor_right[0], HIGH);
  digitalWrite(motor_right[1], LOW);
}

void right()
{
  stop();
  digitalWrite(motor_left[0], HIGH);
  digitalWrite(motor_left[1], LOW);
  digitalWrite(motor_right[0], LOW);
  digitalWrite(motor_right[1], HIGH);
}

void stop()
{
  digitalWrite(motor_left[0], LOW);
  digitalWrite(motor_left[1], LOW);
  digitalWrite(motor_right[0], LOW);
  digitalWrite(motor_right[1], LOW);
}

void loop()
{
  if (Serial.available())
  {
    char command = Serial.read();
    switch (command)
    {
    case 'f':
      forward();
      Serial.println("forward");
      break;
    case 'b':
      backward();
      Serial.println("backward");
      break;
    case 'l':
      left();
      Serial.println("left");
      break;
    case 'r':
      right();
      Serial.println("right");
      break;
    case 's':
      stop();
      Serial.println("stop");
      break;
    }
  }
}
