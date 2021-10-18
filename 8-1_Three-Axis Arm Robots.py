from pyatcrobo2.parts import Servomotor, DCMotor
import time

arm = Servomotor('P13')
claw = Servomotor('P14')
body = DCMotor('M1')

def pick():
    arm.set_angle(165)
    claw.set_angle(135)
    time.sleep_ms(1000)
    claw.set_angle(60)
    time.sleep_ms(1000)
    arm.set_angle(90)

def place():
    arm.set_angle(165)
    time.sleep_ms(1000)
    claw.set_angle(135)
    time.sleep_ms(1000)
    arm.set_angle(90)
    claw.set_angle(90)

def rotate(duration=-1, speed=50, direction="cw"):
    body.power(speed)
    if direction == "cw":
        body.cw()
    elif direction == "ccw":
        body.ccw()
    
    if duration != -1:
        time.sleep_ms(duration)
        body.brake()

def stop():
    body.brake()

pick() 
rotate(3400, direction="cw")
place()
rotate(2550, direction="ccw")
pick()
rotate(1700, direction="cw")
place()
rotate(1700, direction="cw")
pick()
rotate(1700, direction="cw")
place()
