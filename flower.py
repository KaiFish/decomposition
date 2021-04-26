import turtle
import functions as f

t = f.getTurtle() #get turtle from functions
t.shape("turtle")
s = t.getscreen()
s.bgcolor("CornflowerBlue")

# s.tracer(20)        # uncomment to make animation go fast
t.color("ForestGreen")
t.pu()
t.goto(-420,-200)
t.pd()

t.begin_fill()
f.rect(830, 185)      #draw grass
t.end_fill()

t.color("DarkGreen")
t.pu()
t.goto(-5,-200)
t.pd()
t.begin_fill()
f.rect(200,10)        #draw stem
t.end_fill()

t.pu()
t.seth(90)
t.fd(75)
t.pd()
t.lt(30)
f.leaf("l")           #draw left leaf

t.seth(90)
t.pu()
t.fd(30)
t.seth(0)
t.fd(8)
t.lt(75)
t.pd()
f.leaf("r")           #draw right leaf

t.pu()
t.color("SaddleBrown")
t.seth(90)
t.goto(55,80)
t.pd()
t.begin_fill()
t.circle(55)        #draw flower center
t.end_fill()

t.pu()
t.color("Gold")
t.seth(270)
t.goto(0,30)
t.pd()
t.rt(15)
for i in range(30):     #draw petals
    f.petal(40, 80, 75)
    t.rt(205)


t.pu()
t.goto(-250,250)
t.pd()
f.cloud(60)               #draw cloud

t.pu()
t.goto(250,250)
t.pd()
f.sun()                   #draw sun

t.pu()
t.color("DarkGreen")
t.goto(325,-250)        #place turtle on the grass
t.turtlesize(5,5)
t.seth(180)
s.update()
turtle.done()
