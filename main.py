import random
import turtle

import colorgram
from turtle import Turtle,Screen
colour=[(201, 158, 116), (65, 98, 127), (147, 85, 63),
        (141, 161, 186), (124, 185, 170), (195, 139, 155), (227, 202, 118), (156, 165, 55), (131, 78, 86), (64, 40, 33),
        (79, 112, 92), (62, 169, 117), (30, 48, 66), (175, 95, 107), (195, 97, 77), (142, 29, 43), (108, 40, 30),
        (56, 33, 44), (11, 62, 49), (46, 58, 95), (170, 188, 217), (87, 129, 183), (228, 203, 9), (157, 209, 193),
        (218, 180, 172), (53, 155, 162), (219, 174, 184), (21, 82, 59), (165, 203, 212), (77, 81, 38), (18, 75, 105)]
turtle.colormode(255)
# rgb=[]
 #Colour Pick from a Picture
# colors = colorgram.extract('hirstPaint.jpeg', 35)
#
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r,g,b))
# print((rgb))

obj=Turtle()

obj.speed(30)
#obj.pensize(50)
obj.pu()
obj.hideturtle()
obj.setheading(230)
obj.forward(200)
obj.right(230)
#obj.setheading(180)
for j in range(0,10):
    x=obj.xcor()
    for i in range(0, 10):
        obj.dot(15,random.choice(colour))
        obj.forward(35)

    y=obj.ycor()
    obj.goto(x,y)
    obj.left(90)
    obj.forward(35)
    obj.right(90)
#     #obj.heading()



screen=Screen()
screen.exitonclick()