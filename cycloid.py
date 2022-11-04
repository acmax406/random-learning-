import turtle

def drawPolygon(t,sides,size):
    vertex=[None]*sides
    angle=360/sides

    for i in range(sides):
        vertex[i]=t.pos()
        t.forward(size)
        t.right(angle)

    return vertex


def main():
    ac= turtle.Turtle()

    turtle.tracer(0,0)#this will stop animation
    ac.hideturtle()
    ac.pencolor("red")
    ac.penup()
    ac.setposition(10,100)
    ac.pendown()

	T.hideturtle()
	T.pensize(1)
	T.pencolor("red")
	turtle.bgcolor("black")

	T.penup()
	T.setposition(10, 100)
	T.pendown()



















    n=200
    v = drawPolygon(ac, n, 10)


    used=[False]*n
    for i in range(1,n):
        ac.penup()
        ac.setposition(v[i])
        ac.pendown
        while used[i]==False:
            used[i]=True
            nextVertex =(i*4)%n
            ac.setposition(v[nextVertex])
            i=nextVertex

    turtle.update()
main()
turtle.done()
