import turtle
t = turtle.Turtle()
t.shape('turtle')
t.speed(3) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

def move_north():
  t.setheading(90)
  t.forward(100)

def move_northwest():
  t.setheading(135)
  t.forward(100)
  
def move_west():
  t.setheading(180)
  t.forward(100)
  
def move_southwest():
  t.setheading(225)
  t.forward(100)
  
def move_south():
  t.setheading(270)
  t.forward(100)
  
def move_southeast():
  t.setheading(315)
  t.forward(100)
    
def move_east():
  t.setheading(0)
  t.forward(100)
  
def move_northeast():
  t.setheading(45)
  t.forward(100)
  
screen = turtle.Screen()
screen.listen()

screen.onkey(move_north, "Up")
screen.onkey(move_northwest, "Q")
screen.onkey(move_west, "Left")
screen.onkey(move_southwest, "Z")
screen.onkey(move_south, "Down")
screen.onkey(move_southeast, "C")
screen.onkey(move_east, "Right")
screen.onkey(move_northeast, "E")

screen.mainloop()