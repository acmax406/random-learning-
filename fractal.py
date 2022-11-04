# Takes four inputs.
# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# startSide = length of the first square.
# k = number of times we want the fractal to repeat.
# HINT: Think Functions.
import turtle
ac=turtle.Turtle()

def fractal(x, y, startSide, k):
    # YOUR CODE BELOW THIS LINe
    for j in range(4):
        ac.forward(startSide)
        ac.right(90)
    for i in range(k):
        ac.forward(startSide/2)
        startSide=startSide*(0.5)**(0.5)
        ac.right(45)
        for l in range(4):
            ac.forward(startSide)
            ac.right(90)
        j=j+1
fractal(0,0,100,50)
turtle.done()