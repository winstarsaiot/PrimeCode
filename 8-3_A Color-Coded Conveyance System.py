from pyatcrobo2.parts import Servomotor, DCMotor, ColorSensor
import time

arm = Servomotor('P13')
claw = Servomotor('P14')
body = DCMotor('M1')
irp = IRPhotoReflector('P0')
cs = ColorSensor('I2C')

COLOR_POSITIONS = {
    "grey": 1,
    "red": 2,
    "green": 3,
    "undef": 4,
    "blue": 5,
    "yellow": 6,
}
position = 1
threshold_high = 900
threshold_low = 650

def pick():
    arm.set_angle(170)
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

def recognize_color():
    color = cs.get_colorcode()
    if color == cs.COLOR_RED:
        color_name = "red"
    elif color == cs.COLOR_GREEN:
        color_name = "green"
    elif color == cs.COLOR_BLUE:
        color_name = "blue"
    elif color == cs.COLOR_YELLOW:
        color_name = "yellow"
    else: 
        color_name = "blue"
    return color_name

def move_to_color():
    num = COLOR_POSITIONS[color]
    move_to(num)

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

def main():
    from pystubit.board import button_a, display
    while True:
        if button_a.is_pressed():
            pick()
            color = recognize_color
            display.scroll(color, delay=10)
            move_to_color(color)
            place()
            move_to(1)

main()
