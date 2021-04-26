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

t.color("FireBrick")
t.pu()
t.goto(-200,-200)
t.pd()
t.begin_fill()
f.rect(300,400)     #draw house body
t.end_fill()

t.pu()
t.color("deepSkyBlue")
t.goto(-150, -125)
t.pd()
t.seth(90)
t.begin_fill()
f.rect(125,75)     #draw window 1
t.end_fill()

t.pu()
t.goto(150, -125)
t.pd()
t.seth(180)
t.begin_fill()
f.rect(75,125)     #draw window 2
t.end_fill()

t.pu()
t.color("SaddleBrown")
t.goto(-50,-200)
t.pd()
t.seth(90)
t.begin_fill()
f.rect(200,100)    #draw door
t.end_fill()

t.pu()
t.color("Gold")
t.goto(50, -100)
t.fd(5)
t.seth(90)
t.pd()
t.begin_fill()
t.circle(5)     #draw door knob
t.end_fill()

t.pu()
t.color("slateGray")
t.goto(-275,100)
t.pd()
t.begin_fill()      #draw roof
t.seth(0)
t.fd(550)
t.lt(150)
t.fd(317)
t.lt(60)
t.fd(317)
t.end_fill()

t.goto(125, 125)
t.seth(90)
t.begin_fill()
f.rect(85, 75)      # draw chiminey
t.end_fill()

t.pu()
t.color("whitesmoke")       #draw chiminey smoke
t.goto(175, 250)
t.pd()
f.spiral(5, 20)
t.pu()
t.goto(225,275)
t.pd()
f.spiral(5, 20)
t.pu()
t.goto(290,300)
t.pd()
f.spiral(5, 20)

t.pu()
t.goto(-315,225)
t.pd()
f.sun()     # draw sun

t.pu()
t.goto(-100,300)
t.pd()
f.cloud(50)     # draw cloud

t.pu()
t.goto(-160,-220)
t.pd()
f.bush(12)      # draw bush 1

t.pu()
t.goto(342,-220)
t.pd()
f.bush(12)      #draw bush 2

t.pu()
t.color("Gold")
t.seth(90)
t.goto(0,15)    #place turtle above door

s.update()
turtle.done()
