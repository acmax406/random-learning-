import turtle
ac=turtle.Turtle()

def drawSquare(x):
    for i in range(4):
        ac.forward(x)
        ac.right(90)
def fractle(x):
    drawSquare(x)
    for j in range(50):
        ac.forward(x/2)
        x=x*(0.5)**(0.5)
        ac.right(45)
        drawSquare(x)
        j=j+1

fractle(400)
turtle.done()
