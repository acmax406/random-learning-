# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# side = length of the square.
import turtle
ac=turtle.Turtle()
def squareInSquare(x, y, side):
    for i in range(4):
        ac.forward(side)
        ac.right(90)
    ac.forward(side/2)
    side=side*(0.5)**(0.5)
    ac.right(45)
    for i in range(4):
        ac.forward(side)
        ac.right(90)
squareInSquare(0,0,100)
turtle.done()
    