// Define the pins used for the encoders
const int encoderPin1 = 12;
const int encoderPin2 = 13;

// Keep track of the number of ticks for each motor
volatile long tickCount1 = 0;
volatile long tickCount2 = 0;

// Keep track of the previous encoder state
int previousState1 = LOW;
int previousState2 = LOW;

// Define variables for timing the loop
unsigned long previousTime = 0;
const unsigned long interval = 1000000 / 120; // 120 times per second

void setup()
{
  // Set the encoder pins as inputs
  pinMode(encoderPin1, INPUT);
  pinMode(encoderPin2, INPUT);

  // Start the serial communication
  Serial.begin(9600);
}

void loop()
{
  // Read the encoder pins
  int state1 = digitalRead(encoderPin1);
  int state2 = digitalRead(encoderPin2);

  // Check if the encoder output changed from high to low
  if (state1 == LOW && previousState1 == HIGH)
  {
    tickCount1++;
  }
  if (state2 == LOW && previousState2 == HIGH)
  {
    tickCount2++;
  }

  // Update the previous encoder state
  previousState1 = state1;
  previousState2 = state2;

  // Check if it's time to print the tick counts to the serial monitor
  unsigned long currentTime = micros();
  if (currentTime - previousTime >= interval)
  {
    // Print the tick counts to the serial monitor
    Serial.print(tickCount1);
    Serial.print("_");
    Serial.println(tickCount2);

    // Reset the timer
    previousTime = currentTime;
  }
}
