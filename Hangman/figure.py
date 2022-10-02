from random import choice
from turtle import *

HEAD = (0, 100)
HIP = (0, 0)
SHOULDER = (0, 70)
LLEG = (-20, -40)
RLEG = (20, -40)
LARM = (-20, 40)
RARM = (20, 40)

speed(0)
ht() #hide the turtle
color('black')
pu() #penup

# head
def head():
    goto(HEAD) #head
    dot(50)

# torso
def torso():
    pd()
    pensize(12)
    goto(HIP)

# Left Leg
def lleg():
    goto(LLEG)

# Right Leg
def rleg():
    goto(HIP)
    goto(RLEG)

# Left Arm
def larm():
    goto(HIP)
    goto(SHOULDER)
    goto(LARM)
# Right Arm
def rarm():
    goto(SHOULDER)
    goto(RARM)

# colors = ['red', 'blue', 'white', 'yellow', 'orange']
body_parts = [head, torso, lleg, rleg, larm, rarm]
# while True:
#     for bp in body_parts:
#         color(choice(colors))
#         bp()

# for bp in body_parts:
#     bp()
