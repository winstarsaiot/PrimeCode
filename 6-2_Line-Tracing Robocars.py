from pystubit.board import button_a, button_b, display
from pyatcrobo2.parts import DCMotor, IRPhotoReflector
import time

threshold = 0

dcm_l = DCMotor('M1')
dcm_r = DCMotor('M2')
irp = IRPhotoReflector('P0') 

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

def set_threshold():
    global threshold
    display.show("W", delay=0)
    while not button_a.is_pressed():
        pass    
    val_white = irp.get_value()
    display.clear()    
    while button_a.is_pressed():
        pass
    time.sleep_ms(500)
    display.show("B", delay=0)
    while not button_a.is_pressed():
        pass
    val_black = irp.get_value()
    display.clear()    
    while button_a.is_pressed():
        pass
    threshold = int((val_white + val_black) / 2)

def linetrace():
    while button_b.is_pressed():
        pass
    while not button_b.is_pressed(): 
        val = irp.get_value()
        if val > threshold:
            turn_right()
        else:
            turn_left()
        brake()

def start():
    set_threshold()
    while True:
        if button_b.is_pressed():
            linetrace()

start()
