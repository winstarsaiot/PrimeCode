import time
import random
import _thread
from pyatcrobo2.parts import Servomotor, IRPhotoReflector
from pystubit.board import buzzer, display, Image, button_a

TIME_LIMIT = 30000
is_goal = False
over_time_limit = False

def goalkeeper():
    servo = Servomotor('P13')

    while not is_goal and not over_time_limit:
        angle = random.randint(6, 12) * 10
        servo.set_angle(angle)
        time.sleep_ms(200)

def judgment():
    global is_goal
    
    irp = IRPhotoReflector('P0')
    threshold = irp.get_value() + 200
    
    while not is_goal and not over_time_limit:
        time.sleep_ms(1)
        val = irp.get_value()
        if val > threshold:
            is_goal = True

def play_melody():
    melody = (
        ("A5" , 600),
        ("C6" , 900),
        ("A5" , 300),
        ("C6" , 300),
        ("A5" , 300),
        ("C6" , 300),
        ("A5" , 300),
        ("F5" , 1200),
        ("A5" , 300),
        ("A5" , 300),
        ("A5" , 300),
        ("G5" , 1200),
        ("G5" , 300),
        ("G5" , 300),
        ("G5" , 300),
        ("A5" , 1200),
        ("F5" , 600),
    )
    
    while not is_goal and not over_time_limit:
        for sound in melody:
            buzzer.on(sound[0], duration=sound[1])
            if is_goal or over_time_limit:
                break

def signboard():
    message = "GAME"

    while not is_goal and not over_time_limit:
        for word in message:
            display.show(word)
            if is_goal or over_time_limit:
                break

def start_game():
    global is_goal, over_time_limit
    
    is_goal = False
    over_time_limit = False
        
    _thread.start_new_thread(goalkeeper, ())
    _thread.start_new_thread(judgment, ())
    _thread.start_new_thread(play_melody, ())
    _thread.start_new_thread(signboard, ())
    
    start_time = time.ticks_ms()
    while not is_goal and not over_time_limit:
        if time.ticks_diff(time.ticks_ms(), start_time) > TIME_LIMIT:
            over_time_limit = True

    time.sleep_ms(1000)
    show_result()

def show_result():
    if is_goal:
        display.show(Image.HAPPY, color=(0, 31, 0))
        buzzer.on("C7", duration=200)
        buzzer.on("A6", duration=600)
    else:
        display.show(Image.SAD, color=(0, 0, 31))
        buzzer.on("C4", duration=800)
    time.sleep_ms(1000)
    display.clear()
    
while True:
    if button_a.is_pressed():
        for num in range(3, -1, -1):
            display.show(str(num))
        start_game()
