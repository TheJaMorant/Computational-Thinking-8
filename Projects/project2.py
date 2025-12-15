HardRock = 0
HeavyMetal = 0
indie = 0
pop = 0
Hiphop = 0
jazz = 0
country = 0
edm = 0
classical = 0
input("WELCOME TO THE MUSIC GENRE QUIZ!")

answer1=input("First, do you like music that makes you A sad, B happy, C energized, or D, no specific emotion")
if answer1 == "A":
    indie += 1
    country += 1   
elif answer1 == "B":
    Hiphop += 1
    jazz += 1
    HeavyMetal += 1
    pop += 1
    edm += 1
elif answer1 == "C":
    HardRock += 1
    HeavyMetal += 1
    edm += 1   
elif answer1 == "D":
    classical += 1
    jazz += 1
    pop += 1
    Hiphop += 1


answer2=input("Next, what musical elements do you enjoy? A instrument solos, B vocals, C good riffs, D cool/weird sounds")
if answer2 == "A":
    jazz += 1
    HeavyMetal += 1   
elif answer2 == "B":
    Hiphop += 1
    pop += 1
    country += 1
    HardRock += 1


answer3=input("Are you more into A heavy music with lots of sound, B light minimalistic songs, or C songs that focus on one sound (Vocals, solo, a gimmick)")
if answer3 == "A":
    HeavyMetal += 2
    indie += 2
    classical += 1
    jazz += 1
    edm += 2
elif answer3 == "B" :
    pop += 2
    country += 1
elif answer3 == "C" :
    Hiphop += 2
    indie += 1


answer4=input("Do you prefer A electric instruments, or B acoustic instruments?")
if answer4 == "A" :
    HeavyMetal += 2
    indie += 1
    HardRock += 2
    country += 1
elif answer4 == "B" :
    jazz += 2
    classical += 2
    pop += 1
    indie += 1


answer5=input("When listening to music, do you: A blast your music, B play it at a normal volume, or C have it as low as possible")
if answer5 == "A" :
    HardRock += 2
    HeavyMetal += 2
    edm += 2
    country += 1
    Hiphop += 1
elif answer5 == "B" :
    pop += 2
    jazz += 2
    indie += 1
elif answer5 == "C":
    classical += 2


input("READY TO SEE YOUR RESULTS?")
    

if HardRock > HeavyMetal and HardRock > indie and HardRock > pop and HardRock > Hiphop and HardRock > jazz and HardRock > edm and HardRock > classical :
    print("Looks like you're a hard rock person! You should check out bands like Ghost, Guns n' Roses, and Ozzy Ozbourne.")   

elif HeavyMetal > HardRock and HeavyMetal > indie and HeavyMetal > pop and HeavyMetal > Hiphop and HeavyMetal > jazz and HeavyMetal > edm and HeavyMetal > classical :
    print("Looks like you're a Heavy Metal person! You should check out bands like Metallica, Slayer, and Kublai Khan TX.") 

elif indie > HeavyMetal and indie > HardRock and indie > pop and indie > Hiphop and indie > jazz and indie > edm and indie > classical :
    print("Looks like you're an Indie person! You should check out bands like Sufjan Stevens, Wilco, and Tame Impala.")

elif pop > HeavyMetal and pop > HardRock and pop > indie and pop > Hiphop and pop > jazz and pop > edm and pop > classical :
    print("Looks like you're a pop person! You check out bands like Taylor Swift, Micheal Jackson, and Drake.")

elif  Hiphop > HeavyMetal and Hiphop > HardRock and Hiphop > indie and Hiphop > pop and Hiphop > jazz and Hiphop > edm and Hiphop > classical :
    print("Looks like you're a hiphop person! You should check out bands like Tupac, Kendrick Lamar, and Ice Cube.")

elif jazz > HeavyMetal and jazz > HardRock and jazz > indie and jazz > Hiphop and jazz > pop and jazz > edm and jazz > classical :
    print("Looks like you're a Jazz person. You should listen to composers like Thelonious Monk, Joe Henderson, and John Poultrain.")

elif country > HeavyMetal and country > HardRock and country > indie and country > Hiphop and country > jazz and country > edm and country > classical :
    print("Looks like you're a country person. You should listen to bands like Morgan Wallen, Keith Anderson, and The Zac Brown Band. ")
elif edm > HeavyMetal and edm > HardRock and edm > indie and edm > Hiphop and edm > jazz and edm > pop and edm > classical :
    print("Looks like you're an EDM guy. You should check out bands like Marshmallow, Avicci, and Skrillex.")
elif classical > HeavyMetal and classical > HardRock and classical > indie and classical > Hiphop and classical > jazz and classical > pop and classical > edm :
    print("Looks like you're a Classical person! You should check out bands like Beethoven, Bach, Mozart.")
else:
    print("Looks like you don't have a stand-out music genre to look at. This may mean you don't listen to music that much, or you may listen to all kinds of it!")

