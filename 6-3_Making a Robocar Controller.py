from pyatcrobo2.parts import DCMotor, IRPhotoReflector, ColorSensor
import time

dcm_l = DCMotor('M1')
dcm_r = DCMotor('M2')
irp = IRPhotoReflector('P0')
cs = ColorSensor('I2C')
threshold = 500

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

def get_signals():
    val_irp = irp.get_value()
    if val_irp > threshold_irp:
        signal_l = "on"
    else:
        signal_l = "off"

    color = cs.get_colorcode()
    if color == cs.COLOR_RED:
        signal_r = "r"
    elif color == cs.COLOR_GREEN:
        signal_r = "g"
    elif color == cs.COLOR_BLUE:
        signal_r = "b"
    elif color == cs.COLOR_YELLOW:
        signal_r = "y"
    else:
        signal_r = "none"
            
    return (signal_l, signal_r)

def start():
    while True:
        signals = get_signals()
        if signals[0] == "off":
            brake()
        else:
            if signals[1] == "b":
                move_forward()
            elif signals[1] == "r":
                spin_right()
            elif signals[1] == "g":
                spin_left()
            elif signals[1] == "y":
                move_backward()
            else:
                stop()

start()
