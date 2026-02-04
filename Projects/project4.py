import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background 
set_background("Ja_poster_alien (1)")


# TODO - create at least two variables and set their starting value.
basketballs = 0
RookieJa = 45
Ja26 = 100 
Ja21 = 150
Ja22 = 200
Ja23 = 250
Ja25 = 300
Ja24 = 350


# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -300,200)
message_sprite.hideturtle()




# Section 2 - controls
# hitting space gives a basketball
def click () :
    global basketballs
    basketballs += 1
    x = random.randint (-200,200)
    y = random.randint (-200, 200)
    create_sprite ("basketball", x, y)


window.onkeypress(click, "space")
# r spawns a rookie Ja if you have enough basketballs, Rookie Ja spawns basketball automatically
def spawn_rookie () :
    global RookieJa, basketballs
    if basketballs >= RookieJa:
        RookieJa += 150
        x = random.choice ([-300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300])
        y = random.choice ([-300, -150, 0, 150, 300])
        create_sprite ("RookieJa", x, y)
        window.listen()
        for i in range(1000000000):
            basketballs += 1
            time.sleep(0.01)
            window.update()

window.onkeypress(spawn_rookie, "r")



# hit 1 to get 2026 Ja if you have enough basketballs, he spawns in balls quicker
def spawn_Ja26 () :
    global Ja26, basketballs
    if basketballs >= Ja26:
        Ja26 += 300
        x = random.choice ([-300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300])
        y = random.choice ([-300, -150, 0, 150, 300])
        create_sprite ("RookieJa", x, y)
        window.listen()
        for i in range(1000000000):
            basketballs += 5
            time.sleep(0.01)
            window.update()
window.onkeypress(spawn_Ja26, "1")


# hit 2 to get 2024 Ja if you have enough basketballs, and he spawns in balls quicker
def spawn_Ja24 () :
    global Ja24, basketballs
    if basketballs >= Ja24:
        Ja24 += 1000
        x = random.choice ([-300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300])
        y = random.choice ([-300, -150, 0, 150, 300])
        create_sprite ("Ja 24", x, y)
        window.listen()
        for i in range(1000000000):
            basketballs += 25
            time.sleep(0.01)
            window.update()

window.onkeypress(spawn_Ja24, "2")


# Sprite says how many basketballs you have
window.listen()
for i in range(1000000000):

    message_sprite.clear()
    message_sprite.write(f"Basketballs: {basketballs}")

    time.sleep(0.01)
    window.update()