import random
import turtle

screen=turtle.Screen()
screen.bgcolor("white")
screen.title(" Catch the Turtle")
score=0


score_writer=turtle.Turtle()
score_writer.hideturtle()
score_writer.color("black")
score_writer.penup()
score_writer.goto( 0,255)
score_writer.write(arg=f"score:{score}", align="center", font=("arial", 24, "normal"))


time_writer=turtle.Turtle()
time_writer.hideturtle()
time_writer.penup()
time_writer.color("black")

time_writer.goto(x=0, y=220)
time_writer.write( arg="time:0",  move=False ,align="center",font=("arial",20,"normal"))


remaining_time=30
def countdown():
     global remaining_time
     if remaining_time>0:
        remaining_time-=1
        time_writer.clear()
        time_writer.write(f"time:{remaining_time} ", align="center",font=("arial",20,"normal"))
        screen.ontimer(countdown,t=1000)
     else:
        time_writer.clear()
        time_writer.write("game over",align="center",font=("arial",20,"normal"))

countdown()


turt=turtle.Turtle()
turt.shape("turtle")
turt.color("red")
turt.shapesize(2)
turt.penup()


def handle_click(x,y):
    global score
    score+=1
    score_writer.clear()
    score_writer.write(arg=f"score:{score}", align="center", font=("arial", 24, "normal"))

turt.onclick(handle_click)

def move_turtle():
 if remaining_time>0:
    turt.hideturtle()
    random_x=random.randint(-200,200)
    random_y=random.randint(-200,200)
    turt.goto(random_x,random_y)
    turt.showturtle()
    screen.ontimer(move_turtle,1000)
 else:
     turt.hideturtle()
move_turtle()


turtle.mainloop()