import turtle
bob=turtle.Turtle()
def polygone(t,n,length):
    angle= 360/n
    for i in range (n):
        t.fd(length)
        t.rt(angle)



