import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print("place your 3")
reader.write(3)
x = 0
for x in range(0,9):
  print("place your next 3 card")
  reader.write(3)
print("place your 3")
reader.write(3)
x = 0
for x in range(0,9):
  print("place your next 4 card")
  reader.write(4)
print("place your 5")
reader.write(5)
x = 0
for x in range(0,9):
  print("place your next 5 card")
  reader.write(5)
print("place your 6")
reader.write(6)
x = 0
for x in range(0,3):
  print("place your next 6 card")
  reader.write(6)
print("place your 7")
reader.write(7)
x = 0
for x in range(0,9):
  print("place your next 7 card")
  reader.write(7)
print("place your 8")
reader.write(8)
x = 0
for x in range(0,9):
  print("place your next 8 card")
  reader.write(8)
print("place your 9")
reader.write(9)
x = 0
for x in range(0,9):
  print("place your next 9 card")
  reader.write(9)
print("place your 10")
reader.write(10)
x = 0
for x in range(0,9):
  print("place your next 10 card")
  reader.write(10)
print("place your J")
reader.write("J")
x = 0
for x in range(0,9):
  print("place your next J card")
  reader.write("J")
print("place your Q")
reader.write("Q")
x = 0
for x in range(0,9):
  print("place your next Q card")
  reader.write("Q")
print("place your K")
reader.write("K")
x = 0
for x in range(0,9):
  print("place your next K card")
  reader.write("k")
