from pyatcrobo2.parts import Servomotor, DCMotor
import time

arm = Servomotor('P13')
claw = Servomotor('P14')
body = DCMotor('M1')
irp = IRPhotoReflector('P0')

position = 1
threshold_high = 900
threshold_low = 650

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

def moveto(num):
    global position
    diff = num - position
    if abs(diff) > 3:
        diff = diff - 6 if diff > 0 else diff + 6
    direction = "cw" if diff > 0 else "ccw"
    rotate(direction = direction)
    for _ in range (abs(diff)):
        while not irp.get_value() > threshold_high:
            pass
        while not irp.get_value() < threshold_low:
            pass
    stop()
    position = num

armrobot.pick()
armrobot.move_to(4)
armrobot.place()

armrobot.move_to(2)
armrobot.pick()
armrobot.move_to(3)
armrobot.place()

armrobot.move_to(6)
armrobot.pick()
armrobot.move_to(5)
armrobot.place()

armrobot.move_to(1)
