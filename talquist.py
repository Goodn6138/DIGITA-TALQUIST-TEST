from machine import Pin
from PulseCounter import PulseCounter

s3 = Pin(7 , Pin.OUT)
s2 = Pin(6 , Pin.OUT)
s1 = Pin(8 , Pin.OUT)
s0 = Pin(5 , Pin.OUT)
OUT = Pin(3 , Pin.IN)
LED = Pin(4 , Pin.IN)

s0.high()
s1.high()
while True:
    s2.low() #0 RED PIN
    s3.low()
    red = PulseCounter(0, OUT)
    red = red.get_pulse_count()
    
    s2.high() #1 G PIN
    s3.high() #1
    green = PulseCounter(0, OUT)
    green =green.get_pulse_count()
    
    s2.low() #0 B PIN
    s3.high() #1
    blue = PulseCounter(0, OUT)
    blue = blue.get_pulse_count()
    print("Blue {} GREEN {} RED {} ".format(blue , green,red))
    

