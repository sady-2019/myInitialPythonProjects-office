import turtle
import math
import polygon
from polygon import

bob=turtle.Turtle()

def circle(t,r):
    circumference=2* math.pi* r
    n= int(circumference/3)+1
    length= circumference/n
    polygon(t,n,length)

circle(bob,100)