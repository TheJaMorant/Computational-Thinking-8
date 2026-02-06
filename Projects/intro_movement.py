import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("JA MORANT",0,-200)
s2 = create_sprite("Ja 24",200,0)

# movement for ja
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s2.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)

# movement for 2024 ja
def move_up2():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x,y)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x,y)
    
def move_left2():
    x = s2.xcor() - 10
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right2(): 
    x = s2.xcor() + 10
    y = s2.ycor() 
    s2.goto(x,y)

# movement binds Ja 1
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")
# movement binds Ja 2
window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_right2, "Right")
window.onkeypress(move_left2, "Left")
# Show sprite
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()
# drawing 
def draw():
    s1.pendown()
def stop_drawing():
    s1.penup()
def erase():
    s1.clear
# miscellaneous
def reset(x,y):
    s1.goto(x,y)
def red_pen():
    s1.color("red")
def green_pen():
    s1.color("green")
# ---------------------------------------CONTROLS----------------------------------------
# drawing binds
window.onkeypress(draw,"c")
window.onkeyrelease(stop_drawing,"c")
# erase binds
window.onkeypress(erase,"e")
# spite invisible binds
window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")
# reset bind
window.onscreenclick(reset)
# colors
window.onkeypress(red_pen,"t")
window.onkeypress(green_pen,"g")

# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()