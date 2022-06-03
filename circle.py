import math

def circle(t,r):
    circumference=2* math.pi* r
    n= int(circumference/3)+1
    length= circumference/n
    polygone(t,n,length)