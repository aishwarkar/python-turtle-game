import turtle 
import random

# create the stage or window
stage = turtle.Screen()
stage.bgcolor("light green")

# create player
player = turtle.Turtle()
player.shape("turtle")
player.color("yellow")
player.penup

# create target
bubble = turtle.Turtle()
bubble.shape("circle")
bubble.color("white")
bubble.penup()
bubble.setpos(random.randint(-200,200),random.randint(-200,200))
bubble.setheading(random.randint(0,360))
bubble.pendown()

# moving player with key presses
speed = 7

def turnleft():
  player.left(20)
def turnright():
  player.right(20)
def moveforward():
  player.forward(speed)
  
# assigning key presses to player
stage.listen()
stage.onkey(turnleft, "Left")
stage.onkey(turnright, "Right")
stage.onkey(moveforward, "Space")

# have bubble constantly moving and stay on stage
while True:
  bubble.forward(12)
  if bubble.xcor() > 200:
    bubble.setheading(random.randint(90,270))
  if bubble.xcor() < -200:
    bubble.setheading(random.randint(-90,90))
  if bubble.ycor() > 200:
    bubble.setheading(random.randint(180,360))
  if bubble.ycor() < -200:
    bubble.setheading(random.randint(0,180))
  if player.distance(bubble.xcor(), bubble.ycor()) < 20:
    stage.bgcolor("dark blue")
    break

# mainloop constantly updates screen and should be last line of code
stage.mainloop()