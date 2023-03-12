#define ENCA 2 // YELLOW
#define ENCB 3 // BLUE

void setup()
{
    Serial.begin(9600);
    pinMode(ENCA, INPUT_PULLUP);
    pinMode(ENCB, INPUT_PULLUP);
}

void loop()
{
    int a = digitalRead(ENCA);
    int b = digitalRead(ENCB);
    Serial.print(a);
    Serial.print(",");
    .Serial.print(b);
    Serial.println();
}