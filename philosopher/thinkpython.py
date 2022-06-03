# import turtle
#
# bob=turtle.Turtle()
# print(bob)
#
# bob.fd(100)
# bob.rt(90)
#
# bob.fd(100)
# bob.rt(90)
#
# bob.fd(100)
# bob.rt(90)
#
# bob.fd(100)
#
# turtle.mainloop()

#exercise, page 38, Think Python

import turtle
bob=turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# square(bob)
# turtle.mainloop()

#exercise 2

def square2(t, lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)

# square2(bob,100)
# turtle.mainloop()

def polygon(t,lenght,side):
    for i in range(side):
        t.fd(lenght)
        t.lt(360/side)

# polygon(bob,100,6)
# turtle.mainloop()
import math
def circle(t,r,s):
    for i in range (s):
        t.fd(2*3.1416*r)
        t.lt(360/s)

circle(bob,1,36)
turtle.mainloop()
