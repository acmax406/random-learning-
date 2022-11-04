import turtle
import random

def drawPolygon(t, sides, len):
    vertices = [None]*sides
    angle= 360/sides
    for i in range(sides):
        vertices[i]=t.pos()
        t.forward(len)
        t.right(angle)
    return vertices

def main():
    T= turtle.Turtle()
    turtle.tracer(0,0)
    T.hideturtle()
    
    
    for y in range (2):
        multiplier=y
        
        numVertices = 235
        sideLength =2000/numVertices
        
        T.penup()
        T.pencolor("red")
        T.setposition(0, 300)
        T.write( multiplier , False, "center", font=("Arial", 50, "bold"))
        T.setposition(0,275)
        T.pendown()
        v=drawPolygon(T, numVertices, sideLength)
        T.clear()
        T.penup()
        current=1
        T.setpos(v[current])
        T.pendown()
        
        hit= [None]*numVertices 
        
        for i in range(200):
            current =i
            T.penup()
            T.setpos(v[current])
            T.pendown()
            # keep going(doubling current)
            # as long as there is no current line going out from v[current]
            while hit[current] is None:
                
                hit[current]= True 
                #calculate double my location V[x]----->V[2x]
                #take remainder from 200
                y=(random.random(),random.random(),random.random())
                
                T.pencolor(y)#giving it multiple random color
                nextvertex = (current * multiplier)% numVertices #go to double my location
                T.setpos(v[nextvertex])
                current = nextvertex
               
               
        
    turtle.update()
   
    
main()
turtle.done()