import turtle

myT = turtle.Turtle()
myWn = turtle.Screen()
myT.color('blue')
myT.pensize(10)
myT.speed(500)
dist = 2
myT.shape('circle')

def left():
   myT.goto(myT.xcor()-dist,myT.ycor())

def right():
   myT.goto(myT.xcor()+dist,myT.ycor())

def up():
   myT.goto(myT.xcor(),myT.ycor()+dist)

def down():
   myT.goto(myT.xcor(),myT.ycor()-dist)

def quit():
   myWn.bye()

myWn.onkey(left,"a")
myWn.onkey(right,"d")
myWn.onkey(up,"w")
myWn.onkey(down,"s")
myWn.onkey(quit,"q")
myWn.listen()

turtle.mainloop()
