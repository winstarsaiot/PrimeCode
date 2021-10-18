import time
from pystubit.board import button_a, button_b

class BarcodeScanner:
    from pystubit.board import buzzer
    from pyatcrobo2.parts import IRPhotoReflector, Servomotor

    POSITIONS = (30, 70, 110, 150)
    THRESHOLD = 1600
    
    def __init__(self, pin_irp, pin_servo):
        self.irp = self.IRPhotoReflector(pin_irp)
        self.servo = self.Servomotor(pin_servo)
        self.servo.set_angle(self.POSITIONS[0])

    def scan_barcode(self):
        barcode_binary = "0b"
        for pos in self.POSITIONS:
            self.servo.set_angle(pos)
            time.sleep_ms(300)
            val = self.irp.get_value()
            self.buzzer.on("C5", duration=100)
            barcode_binary += "0" if val < self.THRESHOLD else "1"
        barcode_decimal = int(barcode_binary, 2)
        self.servo.set_angle(self.POSITIONS[0])
        return barcode_decimal


class Register:
    PRODUCT_DATA = {
        1: {"name": "Carrots", "price": 300},
        2: {"name": "Onions", "price": 200},
        3: {"name": "Tofu", "price": 100},
        4: {"name": "Eggs", "price": 230},
        5: {"name": "Milk", "price": 240},
        6: {"name": "Apple juice", "price": 320},
        7: {"name": "Sausage", "price": 430},
        8: {"name": "Bacon", "price": 380},
        9: {"name": "Potato chips", "price": 200},
        10: {"name": "Ice cream", "price": 150},
        11: {"name": "Chocolate", "price": 350},
        12: {"name": "Sugar", "price": 250},
        13: {"name": "Soy sauce", "price": 500},
        14: {"name": "Rice", "price": 2000},
        15: {"name": "Tissues", "price": 400},   
    }
    
    def __init__(self, scanner):
        self.scanner = scanner
        self.total = 0
    
    def scan(self):
        product_num = self.scanner.scan_barcode()
        try:
            product = self.PRODUCT_DATA[product_num] 
        except KeyError:
            print("Read error.")
            return
        name = product["name"]
        price = product["price"]
        print(product["name"], ":", product["price"])
        self.total += price
    
    def show_total(self):
        if self.total != 0:
            print("total:" + self.total)
            self.total = 0


def main():
    scanner = BarcodeScanner("P2", "P15")
    register = Register(scanner)

    while True:
        if button_a.is_pressed():
            register.scan()
        if button_b.is_pressed():
            register.show_total()

main()
