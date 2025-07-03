import turtle
t = turtle.Turtle()
t.shape('turtle')
t.speed(3) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

turtle.bgpic('../maze_circular.png')

def move():
    t.forward(15)

def turn_left_start():
    global angle
    angle += 5

def turn_stop():
    global angle
    angle += 0

def turn_right_start():
    global angle
    angle -= 5


def update_frame():
    # initial values
    heading = 0
    heading += angle
    t.setheading(heading)
    screen.ontimer(update_frame, 50)

# MAIN CODE
angle = 0

screen = turtle.Screen()
screen.setup(800, 800)
screen.ontimer(update_frame, 50)

# Move
screen.onkey(move, "Up")

# Turning logic
screen.onkeypress(turn_left_start, "Left")
screen.onkeyrelease(turn_stop, "Left")

screen.onkeypress(turn_right_start, "Right")
screen.onkeyrelease(turn_stop, "Right")

screen.listen()
screen.mainloop()