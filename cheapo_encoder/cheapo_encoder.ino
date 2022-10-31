const int left_motor_tick = 8;
const int right_motor_tick = 9;


int left_speed = 0;
int right_speed = 0;
int left_tick_prev = 0;
int right_tick_prev = 0;

void setup()
{
  pinMode(left_motor_tick, INPUT);
  pinMode(right_motor_tick, INPUT);
  Serial.begin(115200);
}

void loop()
{

  if (left_tick_prev != digitalRead(left_motor_tick))
  {
    left_speed++;
    left_tick_prev = digitalRead(left_motor_tick);
  }
  if (right_tick_prev != digitalRead(right_motor_tick))
  {
    right_speed++;
    right_tick_prev = digitalRead(right_motor_tick);
  }
  delay(1);
}
