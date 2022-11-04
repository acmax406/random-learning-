import turtle
ac=turtle.Turtle()

# x = x co-ordinate of the starting point.
# y = y co-ordinate of the starting point.
# startLength = length of the first move.
# k = number of moves.

def spiralOut(startLength, k):
    # YOUR CODE BELOW THIS LINE
    s=0.2
    angle=15
    dist=1
    while(k!=0):
        turtle.speed(s)
        s=s+2
        ac.forward(dist)
        dist=dist+0.1
        ac.right(angle)
        k=k-1
    
def fractal(x, y, startLength, k):
    ac.penup()
    ac.goto(x,y)
    ac.pendown()
    # YOUR CODE BELOW THIS LINe
    for j in range(4):
        ac.forward(startLength)
        ac.right(90)
    for i in range(k):
        ac.forward(startLength/2)
        startLength=startLength*(0.5)**(0.5)
        ac.right(45)
        for l in range(4):
            ac.forward(startLength)
            ac.right(90)
        j=j+1
    ac.penup()
    ac.forward(startLength/2)
    ac.right(90)
    ac.forward(startLength/2)
    ac.pendown()
    
    s=0.5
    angle=15
    dist=startLength/startLength
    z=1000
    while(z!=0):
        turtle.speed(s)
        s=s+2
        ac.forward(dist)
        dist=dist+0.1
        ac.right(angle)
        z=z-1
fractal(0,100, 200, 3)
turtle.done
