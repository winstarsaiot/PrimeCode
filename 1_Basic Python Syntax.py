# Example 1
print("Hello World")
'''
# Example 2
x = "Hello World!"
print(x)

x = "Greeting World!"
print("After changing the value of x: " + x)
'''
'''
# Example 3
x = "Hello world!"
print(x)
print(type(x))

x = 12345
print(x)
print(type(x))

x = 12.3
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = False
print(x)
print(type(x))

food = ['milk', 'beef', 'egg', 'carrot']
print(food)
print(type(food))

print(food[0])
print(food[-1])
print(food[0:3])
print(food[0:4:2])

food.append('bacon')
print(food)

food.pop(2)
print(food)

food.remove('carrot')
print(food)

a = (1, 2, 3)
print(a)
print(type(a))

a = (4, 5, 6)
print(a)
(4, 5, 6)

contact = {'f_name':'Chris', 'l_name':'Wong', 'tel_no':'1234-5678'}
print(contact)
print(type(contact))

contact['sex'] = 'M'
print(contact)

contact.pop('sex')
print(contact)
'''
'''
# Example 4
x = 3
y = 2

z = x + y
print(z)

z = x - y
print(z)

z = x * y
print(z)

z = x / y
print(z)

z = x // y
print(z)

z = x % y
print(z)

z = x ** y
print(z)

x = '1'
y = '2'
z = x + y
print(z)

x = 1
y = '2'
z = x + y
print(z)
'''
'''
# Example 5
text = 'Python'
low = text.lower()
up = text.upper()
print(low)
print(up)
print(text)

text = 'tomato'
print(text.find('a'))
print(text.find('o'))
print(text.find('p'))

print(text.count('o'))

text = '    white_space'
print(text)
print(text.strip())

text = '    w h i t e _ s p a c e'
print(text)
print(text.strip())

text = '****Happy Birthday!!****'
print(text.strip('*'))

text = '{} and {} are {}.'
print(text.format('An apple', 'an orange', 'fruits'))
print(text.format('A cat', 'a dog', 'animals'))
'''
'''
# Example 6
x = input("type in something: ")
print(x)
'''
'''
# Example 7
x = input("type in 'k': ")
if x == 'k': # x equals to 'k'
    print("correct")

x = input("1 + 1 = ? : ")
if x == '2':
    print("correct!")
else:
    print("incorrect!")

value = input("input score: ")
value = int(value)

if value >= 90:
    print("A")
elif value > 70:
    print("B")
elif value > 50:
    print("C")
else:
    print("F")
'''
'''
# Example 8
A = True
B = False

print("A and B = " + str(A and B))
print("A or B = " + str(A or B))
print("not A = " + str(not A))
print("not B = " + str(not B))

A = True
B = False

if A and (not B):
    print("and")
if A or B:
    print("or")
if not B:
    print("not")
'''
'''
# Example 9
x = input("1 + 1 = ? : ")
while x != '2': # x not equal to '2'
    x = input("incorrect! please try again: ")
print("correct!")

while True: # not False:
    x = input("type in something: ")
    print(x)

count = 0
while count < 5:
    val = input("type in something: ")
    print(val)
    if val == 'b':
        count += 1
print()
print('end')

count = 0
while count < 5:
    val = input("type in something: ")
    if val == 'b':
        count += 1
    else:
        count = 0
    print("val: " + val + "  |  count: " + str(count))
    print()

print('end')

count = 0
while count < 10:
    count += 1
    print(count)
print('end')

for count in range(10):
    print(count)
print('end')

for count in range(1,10,2):
    print(count)
print('end')
'''
'''
# Example 10
import time
for count in range(10):
    print(count)
    time.sleep(1)
print('end')

from time import sleep
for count in range(10):
    print(count)
    sleep(1)
print('end')

from time import sleep as slp
for count in range(10):
    print(count)
    slp(1)
print('end')
'''
'''
# Example 11
def printWord():
  print("Hello")

printWord()

# This function is used for finding the grade according to the score obtained by student
def score_cal(value):
  if value >= 90:
      return "A"
  elif value > 70:
      return "B"
  elif value > 50:
      return "C"
  else:
      return "F"

value = input("input score: ")
value = int(value)
print(score_cal(value))
'''
'''
# Example 12
class Circle:
  def __init__(self, r=1):
    self.radius = r
    self.pi = 22/7

  def cal_circum(self):
    return 2*self.pi*self.radius

  def cal_area(self):
    return self.pi*self.radius**2

circle_1 = Circle()
print("Cirlce 1")
print("Radius: " + str(circle_1.radius))
print("Circumference: " + str(circle_1.cal_circum()))
print("Area: " + str(circle_1.cal_area()))

print("")
print("Cirlce 2")
circle_2 = Circle(3)
print("Radius: " + str(circle_2.radius))
print("Circumference: " + str(circle_2.cal_circum()))
print("Area: " + str(circle_2.cal_area()))

circle_2.radius = 5
print("")
print("After updating Circle 2 radiuis...")
print("Radius: " + str(circle_2.radius))
print("Circumference: " + str(circle_2.cal_circum()))
print("Area: " + str(circle_2.cal_area()))
'''
