// https://www.youtube.com/watch?v=wIcC8-g9Lnw&t=1604s&ab_channel=DroneBotWorkshop
const byte buttonPin1 = 12; // pin 12
const byte buttonPin2 = 2;  // pin 2
volatile int counter1 = 0;
volatile int counter2 = 0;

void setup()
{
    Serial.begin(9600); // initialize serial communication at 9600 baud

    // ENABLE PCIE0 Bit0 = 1 (port B)
    PCICR |= B00000001;
    // SELECT PCINT4 Bit4 = 1 (pin 12)
    PCMSK0 |= B00010000;

    // ENABLE PCIE0 Bit2 = 1 (port D)
    PCICR |= B00000100;
    // SELECT PCINT18 Bit2 = 1 (pin 2)
    PCMSK2 |= B00000100;
}

void loop()
{
    // print all the values in a single line
    Serial.print("Counter1: ");
    Serial.print(counter1);
    Serial.print(" Counter2: ");
    Serial.println(counter2);

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
