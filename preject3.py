import turtle, time, random
from utils import *


#1 starting variable positions
x1 = -100
y1 = 100
x2 = -100
y2 = 50
x3 = -100
y3 = -50
x4 = -100
y4 = -100

#2 setup and sprites
set_background("soccerfield")
t1 = create_sprite("JA MORANT", x1, y1)
t2 = create_sprite("lebron", x2, y2)
t3 = create_sprite("goat", x3, y3)
t4 = create_sprite("basketball", x4, y4)

#3 racing
for i in range(30):
     x1 += random.choice([40,25,25,25,-10])
     x2 += random.choice([15,15,15,15,15,15,30])
     x3 += 12
     x4 += random.randint(5,26)

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.5)
# Ja will win everytime unless he is injured (20%), or if the basketball gets the 26 speed (1/7).


#4 winners
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("JAAAAA MORAAAAAAAANT wins it agaaaaaain!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("Lebron wins another one!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
     print("Ja Morant's alter ego wins it!")
elif x4 >= x2 and x4 >= x3 and x4 >= x1:
     print("The ball wins it out of nowhere!!!")

turtle.exitonclick()
