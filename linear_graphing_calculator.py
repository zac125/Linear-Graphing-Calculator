import turtle as t
import time
import math 

t.hideturtle()
t.speed(0)
t.up()
t.hideturtle()

#defining the round rectangle
def round_rectangle(center_x,center_y,width,height,cornersize):
    t.fillcolor("yellow")
    t.begin_fill()
    t.up()
    t.goto(center_x-width/2+cornersize,center_y-height/2)
    t.down()
    for _ in range(2):
        t.fd(width-2*cornersize)
        t.circle(cornersize,90)
        t.fd(height-2*cornersize)
        t.circle(cornersize,90)
    t.end_fill()
#making the rectangle
round_rectangle(0,0,250,450,20) 

#create X and Y axis
t.fillcolor("white")
t.begin_fill()
t.pencolor("black")
t.penup()
t.setposition(0,20)
t.pendown()
for i in range(4):
  t.forward(100)
  t.left(90)
  t.forward(100)
t.end_fill()
t.setposition(0, 120)
t.forward(100)
t.backward(200)
t.penup()
t.setposition(0, 220)
t.pendown()
t.setposition(0,120)
t.pencolor("light grey")
t.penup()
t.speed(0)
t.setposition(-100, 120)
t.pendown()
for i in range(20):
  t.forward(10)
  t.left(90)
  t.forward(100)
  t.backward(200)
  t.forward(100)
  t.right(90)
t.penup()
t.setposition(-100, 220)
t.pendown()
for i in range(10):
  t.forward(200)
  t.right(90)
  t.forward(10)
  t.right(90)
  t.forward(200)
  t.left(90)
  t.forward(10)
  t.left(90)
t.penup()
t.setposition(0, 120)
t.pendown()
t.pensize(3)
t.pencolor("black")
t.forward(100)
t.backward(200)
t.penup()
t.setposition(0, 220)
t.pendown()
t.setposition(0, 20)

#making line
m=float(input("enter your slope"))
angle=math.atan(m)
b=float(input("enter your y intercept"))
b=int(b+140)
t.goto(0,b)
x=0
#while 1==1:
y=m*x+b
t.goto(x,y)
t.lt(angle)
t.fd(180)
t.rt(180)
t.fd(320)