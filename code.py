# Chapter 3 cpx lab-1
#Boolean inputs
from adafruit_circuitplayground import cp
import time

while True:

    if cp.switch:
     cp.red_led=True
    else:
     cp.red_led=False

    if cp.button_a:
        cp.play_file("drum_cowbell.wav")
    if cp.button_b:
        cp.play_file("cash_register_x.wav")
    if cp.touch_A1:
        cp.pixels[0] = (255, 0, 0) #Red
    else:
        cp.pixels[0] = (0, 0, 0) #Off
