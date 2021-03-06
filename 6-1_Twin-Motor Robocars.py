from pyatcrobo2.parts import DCMotor
import time

dcm_l = DCMotor('M1')
dcm_r = DCMotor('M2')

dcm_l.power(100)
dcm_r.power(100)

def move_forward():
    dcm_l.ccw()
    dcm_r.ccw()

def move_backward():
    dcm_l.cw()
    dcm_r.cw()

def spin_left():
    dcm_l.cw()
    dcm_r.ccw()

def spin_right():
    dcm_l.ccw()
    dcm_r.cw()

def turn_left():
    dcm_l.brake()
    dcm_r.ccw()

def turn_right():
    dcm_l.ccw()
    dcm_r.brake()

def stop():
    dcm_l.stop()
    dcm_r.stop()

def brake():
    dcm_l.brake()
    dcm_r.brake()

'''
# Making a Reverse S
turn_right()
time.sleep_ms(6000)
turn_left()
time.sleep_ms(6000)
brake()
'''
'''
# Making a Square
move_forward()
time.sleep_ms(2000)
for _ in range(3):
    spin_right()
    time.sleep_ms(1000)
    move_forward()
    time.sleep_ms(2000)
brake()
'''
