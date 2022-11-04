# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# side = length of the square.
import turtle
ac=turtle.Turtle()
i=0
def drawSquare(x, y, side):
    ac.penup()
    ac.goto(x,y)
    ac.pendown()
    for i in range(4):
        ac.forward(side)
        ac.right(90)
        i=i+1
drawSquare(0,0, 100)
turtle.done()
    