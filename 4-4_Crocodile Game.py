from pystubit.board import buzzer,button_a
from pyatcrobo2.parts import IRPhotoReflector,Servomotor
import random
import time

lot_num = 30
bad_lot_num = 3

ir = IRPhotoReflector('P0')
ir_threshold = 800 

servo = Servomotor('P13')

def bite():
    buzzer.on('C4')
    for i in range(3):
        servo.set_angle(100)
        time.sleep_ms(200)
        servo.set_angle(135)
        time.sleep_ms(200)
    buzzer.off()

def safe_sound():
    buzzer.on('C7',duration=200)
    time.sleep_ms(1000)
  
def start_sound():
    buzzer.on('C6',duration=200)
    buzzer.on('D6',duration=200)
    buzzer.on('E6',duration=200)

def reset():
    servo.set_angle(135)

def choice_bad_lot():
    lots = list(range(1,lot_num+1))
    bad_lots = []
    for i in range(bad_lot_num):
        num = random.choice(lots)
        bad_lots.append(num)
        lots.remove(num)
    return bad_lots

def play_game():
    lots = list(range(1,lot_num+1)) 
    bad_lots = choice_bad_lot()
  
    while True:
        value = ir.get_value()
        if value > ir_threshold:
            num = random.choice(lots)
            if num in bad_lots:
                bite()
                break
            else:
                safe_sound()
                lots.remove(num)

# Main program
reset()
while True:
    if button_a.was_pressed():
        start_sound()
        play_game()
        time.sleep_ms(1000)
        reset()
