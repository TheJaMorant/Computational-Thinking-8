# Section 1 - Your code
from utils import *
set_background("Ja_poster_alien (1)")

s1 = create_sprite("alien", 100, 100)
s2 = create_sprite("goat", -100, 100)
s3 = create_sprite("basketball", -100, -100)
s4 = create_sprite("goat", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Sawyer Steffensmeier",font = ("Arial", 30, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("red")
message2.write("#1 ranked Ja glazer",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()