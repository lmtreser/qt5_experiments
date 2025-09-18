/*
  Arduino Connect - Firmware 
  Lucas Martín Treser
  Septiembre de 2025

  Utiliza la biblioteca DHT_sensor_library de Adafruit
*/

#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

DHT sensorHT(DHTPIN, DHTTYPE);

const int LED = 3;
const int DELAY = 5000;

bool estado_l = false;
bool estado_b = false;
unsigned long t_actual = 0;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
  sensorHT.begin();
}

void loop() {

  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim(); // quitar espacios y saltos de línea

    if (cmd.equalsIgnoreCase("LED")) {
      toggleLed();
    } 
    else if (cmd.equalsIgnoreCase("BUILTIN")) {
      toggleB();
    }
  }

  if (millis() > t_actual + DELAY) {
    
    t_actual = millis();
    float t_humedad = sensorHT.readHumidity();
    float t_temperatura = sensorHT.readTemperature();

    Serial.print(t_humedad);
    Serial.print(",");
    Serial.println(t_temperatura);
  }
}

// Funciones para alternar LEDs
void toggleLed() {
  estado_l = !estado_l;
  digitalWrite(LED, estado_l);
}

void toggleB() {
  estado_b = !estado_b;
  digitalWrite(LED_BUILTIN, estado_b);
}
