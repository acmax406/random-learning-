import turtle
def drawPolygon(t, sides, size):
    angle= 360.0/sides
    for i in range (sides):
        t.forward(size)
        t.right(angle)

def main():
    T=turtle.Turtle()
    turtle.tracer(0,0)
    T.pensize(1)
    T.pencolor("red")
    turtle.bgcolor("black")
    drawPolygon(T, 5, 60)
    turtle.done()#turtle.bye() ...use this instead of done to close automatically
    # end of the program
main()

