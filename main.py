from machine import Pin, ADC
from time import sleep
from math import log

led = Pin(25, Pin.OUT)
adc = ADC(26)

while True:
  
  Vin = 3.3
  B = 3950
  lect = adc.read_u16()
  print("El valor del ADC es: {}".format(lect))
  tension = (Vin / 65535) * lect
  print("El valor de Tension es: {}".format(tension))
  resistencia2 = (10000 * tension) / (Vin - tension)
  print("El valor de resistencia 2 es: {}".format(resistencia2))
  Temperatura = B / ((log(resistencia2 / 10000)) + (B / 298)) - 273.15
  print("El valor de la Temperatura es: {}".format(Temperatura))