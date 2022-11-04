import turtle
ac=turtle.Turtle()
t=100
angle=40
dist=0
x=1
z=0
while(t!=0):
    z=dist+z
    ac.forward(dist)
    ac.right(angle)
    dist=x
    x=z
    t=t-1
turtle.done()
