import turtle, math, time, random
from utils import *

# Section 1: Setup---------------------------------------------------------
# basketball court background
set_background("bball_layout")
# TODO - set the starting value for your variables
x = 0
y = 0
energy = 1000
dunks = 0
sprite_list = []

# S1 is ja morant
s1 = create_sprite("Ja 24", x, y)

# Section 2: Controls------------------------------------------------------
# movement definitions
def up():
    global energy
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
    energy -= 90

def down():
    global energy
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    energy -= 90

def right():
    global energy
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)
    energy -= 90

def left():
    global energy
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    energy -= 90

# movement binds
window.onkeypress(up,"w")
window.onkeypress(down,"s")
window.onkeypress(right,"d")
window.onkeypress(left,"a")

# Section 3: Game Loop----------------------------------------------------------
window.listen()
for i in range(10000000000):
    # getting to the end adds a dunk
    if x >= 350 or x <= -320:
        dunks += 1
    
    # constantly losing energy
    
    energy -= 0.05

    # game ends if you run out of energy
    if energy == 0:
        break
    time.sleep(0.01)
    window.update()
    

# end of game terminal messages -----------------------------------------------------
input("Game Over, Ready to see your score?")
print(f"You had {dunks} dunks!")
