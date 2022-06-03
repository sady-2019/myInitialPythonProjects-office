import turtle
import math

bob=turtle.Turtle()
def polygone(t,n,length):
    angle= 360/n
    for i in range (n):
        t.fd(length)
        t.rt(angle)

def circle(t,r):
    circumference=2* math.pi* r
    n= 100
    length= circumference/n
    polygone(t,n,length)

circle(bob,50)
