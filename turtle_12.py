import turtle
from turtle import *
import colorsys

hideturtle()
speed(0)
bgcolor('black')
h = 0
for i in range(360):
    col = colorsys.hsv_to_rgb(h,1,1)
    pencolor(col)
    h += 0.005
    for j in range(2):
        forward(i*j*2)
        left(95)
turtle.done()