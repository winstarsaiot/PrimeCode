from pystubit.board import button_a, buzzer
from pyatcrobo2.parts import DCMotor, UltrasonicSensor
import time

def alarm():
    for i in range(3):
        buzzer.on('C7',duration=50)
        time.sleep_ms(50)

us = UltrasonicSensor('P0')
dcm = DCMotor('M1')
dcm.power(100)

while True:
    if button_a.is_pressed():
        distance = us.get_distance()
        if distance > 0 and distance < 10:
            alarm()
        if distance < 5:
            dcm.brake()
        else:
            dcm.cw()
    else:  
        dcm.stop()

'''
# An Anti-Fall Robocar
from pyatcrobo2.parts import DCMotor, UltrasonicSensor

us = UltrasonicSensor('P0')
dcm = DCMotor('M1')
dcm.power(100)

while True:
    distance = us.get_distance()
'''
