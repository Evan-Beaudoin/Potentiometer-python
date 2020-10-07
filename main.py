# Created by: Evan
# Created on: Oct.2020
# This program reads the value of a potentiometer

from microbit import *

while True:
    potentiometer = pin1.read_analog()
    display.scroll(potentiometer)
    sleep(200)

