import turtle
t = turtle.Turtle()
t.shape('turtle')
t.speed(3) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

def move():
    t.forward(15)

def speed_up_start():
    global speed
    speed += 2

def speed_stop():
    global speed
    speed += 0

def slow_down_start():
    global speed
    speed -= 2

def turn_left_start():
    global angle
    angle += 5

def turn_stop():
    global angle
    angle += 0

def turn_right_start():
    global angle
    angle -= 5

# def update_frame():
#     # initial values
#     heading = 0
#     heading += angle

#     position = 0
#     position += speed

#     t.setheading(heading)
#     t.forward(position)
#     screen.ontimer(update_frame, 50)

def update_frame():
    # initial values
    heading = 0
    heading += angle
    t.setheading(heading)
    screen.ontimer(update_frame, 50)

# MAIN CODE
angle = 0

screen = turtle.Screen()
screen.ontimer(update_frame, 50)

# Move
screen.onkey(move, "Up")
# screen.onkeypress(speed_up_start, "Up")
# screen.onkeyrelease(speed_stop, "Up")

# screen.onkeypress(slow_down_start, "Down")
# screen.onkeyrelease(speed_stop, "Down")

# Turning logic
screen.onkeypress(turn_left_start, "Left")
screen.onkeyrelease(turn_stop, "Left")

screen.onkeypress(turn_right_start, "Right")
screen.onkeyrelease(turn_stop, "Right")

screen.listen()
screen.mainloop()