import turtle
ac=turtle.Turtle()

def drawTiledSquare(x):
    ac.right(45)
    for i in range (4):
        ac.forward(x)
        ac.right(90)
        i=i+1

def squareWithinSquare(x):
    for i in range (4):
        ac.forward(x)
        ac.right(90)
        i=i+1
    ac.forward(x/2)
    drawTiledSquare(x*(0.5)**(0.5))
squareWithinSquare(200)
turtle.done()
    