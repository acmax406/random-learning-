import turtle
ac=turtle.Turtle()
t=1000
s=0.2
angle=5
dist=5
while(t!=0):
    turtle.speed(s)
    s=s+2
    ac.forward(dist)
    dist=dist+0.2
    ac.right(angle)
    t=t-1
turtle.done()
