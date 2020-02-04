#import RPi.GPIO as GPIO
#from mfrc522 import SimpleMFRC522
from Function import *
'''nextround 2
player1 3
player2 4
player3 17
player4 27
player5 22
player6 11
player7 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
reader = SimpleMFRC522()'''
score1 = 0
wild = wild(2)
p1name = 'Not Playing'
p2name = 'Not Playing'
p3name = 'Not Playing'
p4name = 'Not Playing'
p5name = 'Not Playing'
p6name = 'Not Playing'
p7name = 'Not Playing'
p1 = score(0, p1name)
p2 = score(0, p2name)
p3 = score(0, p3name)
p4 = score(0, p4name)
p5 = score(0, p5name)
p6 = score(0, p6name)
p7 = score(0, p7name)
player1playing = input ('Is player 1 playing: ')
player2playing = 'no'
player3playing = 'no'
player4playing = 'no'
player5playing = 'no'
player6playing = 'no'
player7playing = 'no'
if len(player1playing) == 3:
    p1name = input ('What is player 1 name: ')
    player2playing = input ('Is player 2 playing: ')
    p1 = score(0, p1name)
    if len(player2playing) == 3:
        p2name = input ('What is player 2 name: ')
        player3playing = input ('Is player 3 playing: ')
        p2 = score(0, p2name)
        if len(player3playing) == 3:
            p3name = input ('What is player 3 name: ')
            player4playing = input ('Is player 4 playing: ')
            p3 = score(0, p3name)
            if len(player4playing) == 3:
                p4name = input ('What is player 4 name: ')
                player5playing = input ('Is player 5 playing: ')
                p4 = score(0, p4name)
                if len(player5playing) == 3:
                    p5name = input ('What is player 5 name: ')
                    player6playing = input ('Is player 6 playing: ')
                    p5 = score(0, p5name)
                    if len(player6playing) == 3:
                        p6name = input ('What is player 6 name: ')
                        player7playing = input ('Is player 7 playing: ')
                        p6 = score(0, p6name)
                        if len(player7playing) == 3:
                            p7name = input ('What is player 7 name: ')
                            p7 = score(0, p7name)
if len(player1playing) == 11:
    p1.add(1000)
if len(player2playing) == 11:
    p2.add(1000)
if len(player3playing) == 11:
    p3.add(1000)
if len(player4playing) == 11:
    p4.add(1000)
if len(player5playing) == 11:
    p5.add(1000)
if len(player6playing) == 11:
    p6.add(1000)
if len(player7playing) == 11:
    p7.add(1000)
while True:
    p1.read()
    wildcard = wild.cw
    if wildcard == range(3, 10) and wildcard != range(11, 13):
        print('The Wild card is', wildcard)
    elif wildcard == 11:
        print('Wild Card is Jack')
    elif wildcard == 12:
        print('Wild Card is Queen')
    elif wildcard == 13:
        print('Wild Card is King')
    elif wildcard == 14:
        break
    wild.add()
gamedone(p1, p2, p3, p4, p5, p6, p7, p1name, p2name, p3name, p4name, p5name, p6name, p7name, player1playing, player2playing, player3playing, player4playing, player5playing, player6playing, player7playing)