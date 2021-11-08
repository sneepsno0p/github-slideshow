# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
trtl.colormode(255)
B = rand.randint(0,255)
R = rand.randint(0,255)
O = rand.randint(0,255)
spot_shape="circle"
size = rand.randint(1,10)
spot = trtl.Turtle()
def do_stuff():
  trtl.colormode(255)
  B = rand.randint(0,255)
  R = rand.randint(0,255)
  O = rand.randint(0,255)
  spot_shape="circle"
  size = rand.randint(1,10)
  spot.shapesize(size)
  spot.shape(spot_shape)
  spot.color(B,R,O)
  spot.fillcolor(B,R,O)
#-----game configuration----
score = 0
font_setup = ("Comic Sans MS",30,"bold",)
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
spot.shapesize(size)
spot.shape(spot_shape)
spot.color(B,R,O)
spot.fillcolor(B,R,O)
 
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(380,330)
score_writer.hideturtle()
 
counter =  trtl.Turtle()
counter.penup()
counter.goto(233,260)
counter.hideturtle()
  
def change_position():
  new_xpos = rand.randint(-400,400)
  new_ypos = rand.randint(-300,300)
  spot.goto(new_xpos, new_ypos)
 
 
#-----game functions-------- 
def spot_clicked(x,y):
  spot.hideturtle()
  spot.penup()
  global timer
  if timer_up == False:
    update_score()
    do_stuff()
    change_position()
    spot.showturtle()
  else:
    spot.hideturtle()
 
def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)
 
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
  
 
#-----events----------------
wn = trtl.Screen()
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval) 
wn.bgcolor("pink") 
wn.mainloop()
