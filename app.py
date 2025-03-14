import turtle
#import winsound
wnd=turtle.Screen()
wnd.title("PING PONG")
wnd.bgcolor("skyblue")
wnd.setup(width= 800, height=600)
wnd.tracer(0)
score_a=0
score_b=0
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0     Player B: 0",align="center",font=("courier",24,"normal"))

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("black")
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1

#Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=40
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=40
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=40
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=40
    paddle_b.sety(y)

wnd.listen()
wnd.onkeypress(paddle_a_up,"w")
wnd.onkeypress(paddle_a_down,"s")
wnd.onkeypress(paddle_b_up,"Up")
wnd.onkeypress(paddle_b_down,"Down")



while True:
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #Borders
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        #winsound.PlaySound("pong1.wav",winsound.SND_ASYNC)
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        #winsound.PlaySound("pong1.wav",winsound.SND_ASYNC)
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx*=-1
        #winsound.PlaySound("pong2.wav",winsound.SND_ASYNC)
        score_a+=1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1
        #winsound.PlaySound("pong2.wav",winsound.SND_ASYNC)
        score_b+=1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        #winsound.PlaySound("pong1.wav",winsound.SND_ASYNC)
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
        #winsound.PlaySound("pong1.wav",winsound.SND_ASYNC)
    wnd.update()
