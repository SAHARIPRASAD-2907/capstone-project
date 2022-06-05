#include <SoftwareSerial.h>
#include <DHT.h>

#define DHTPIN 7
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

int chk;
float hum;  // Stores humidity value
float temp; // Stores temperature value

int soilMoistVal()
{
    int sensorValue = analogRead(A14);
    return sensorValue;
}

void phValue()
{
    float a, b, c, d;
    String strs = Serial.readString();
    int str_len = strs.length() + 1;
    char str[str_len];
    strs.toCharArray(str, str_len);
    for (int i = 0, j; str[i] != '\0'; ++i)
    {
        while (!(str[i] >= '0' && str[i] <= '9') && !(str[i] == '\0') && !(str[i] == ',') && !(str[i] == '.'))
        {
            for (j = i; str[j] != '\0'; ++j)
            {
                str[j] = str[j + 1];
            }
            str[j] = '\0';
        }
    }
    int k = 0;
    char *token = strtok(str, ",");
    a = atof(token);
    token = strtok(NULL, ",");
    b = atof(token);
    token = strtok(NULL, ",");
    c = atof(token);
    token = strtok(NULL, ",");
    d = atof(token);
    token = strtok(NULL, ",");
    Serial.print(a);
    Serial.print("\t");
    Serial.print(b);
    Serial.print("\t");
    Serial.print(c);
    Serial.print("\t");
    Serial.print(d);
    Serial.print("\t");
}

int waterLevel()
{
    const int sensorMin = 0;
    const int sensorMax = 1024;
    int sensorReading = analogRead(A0);
    return sensorReading;
}

void setup()
{
    Serial.begin(9600);
    dht.begin();
}

void loop()
{
    float *reqVal;
    hum = dht.readHumidity();
    temp = dht.readTemperature();
    int valSensorSoil = soilMoistVal();
    int valSensorWaterLevel = waterLevel();
    phValue();
    Serial.print(hum); // B
    Serial.print("\t");
    Serial.print(temp); // C
    Serial.print("\t");
    Serial.print(valSensorSoil); // D
    Serial.print("\t");
    Serial.print(valSensorWaterLevel); // E
    Serial.print("\t");
    Serial.println();
    // delay(2000); // 2 seconds
    delay(600000); // 10 minutes
}