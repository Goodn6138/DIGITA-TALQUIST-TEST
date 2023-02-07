from machine import Pin, I2C
from PulseCounter import import PulseCounter
import ssd1306
#......................SCREEN SETUP.............................
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c, addr = 0x3c)
#......................TCL SENSOR
s3 = Pin(7 , Pin.OUT)
s2 = Pin(6 , Pin.OUT)
s1 = Pin(8 , Pin.OUT)
s0 = Pin(5 , Pin.OUT)
OUT = Pin(3 , Pin.IN)
LED = Pin(4 , Pin.IN)

s0.high()
s1.low()

while True:
    s2.low() #0 RED PIN
    s3.low()
    red = PulseCounter(0, OUT)
    red = red.get_pulse_count()
    display.text("RED: {}".format(red), 0, 0,1)
    
    s2.high() #1 G PIN
    s3.high() #1
    green = PulseCounter(0, OUT)
    green =green.get_pulse_count()
    display.text("GREEN: {}".format(green),0,10,1)
    
    s2.low() #0 B PIN
    s3.high() #1
    blue = PulseCounter(0, OUT)
    blue = blue.get_pulse_count()
    display.text("BLUE: {}".format(blue),0,20,1)
    
   # print("Blue {} GREEN {} RED {} ".format(blue , green,red))
    
    
