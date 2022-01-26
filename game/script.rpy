# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Eileen")

define pov = Character("[povname]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    scene small_apartment_kitchen


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    python:
        povname = renpy.input("Oh, you're finally here! I'm so sorry, but I seem to have forgotten your name. What was it, again? \n", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Pat Smith"

    pov "My name is [povname]!"

    b "You know, it's been such a long day. I'm glad to finally be back home so I can relax a bit."

    b "I've had a lot of issues with power outages lately. Maybe a big, strong guy like you could help fix that?"

    hide eileen happy
    scene small_apartment_kitchen_night
    show eileen_dark
    play music "scary-one.ogg" fadein 5

    b "Oh no! It happened again."

    b "It's really dark now. I can barely see anything"

    show eileenDark:
        xalign 0.75
        yalign 1 

    play music "scary-two.ogg" fadein 5

    b "Oh, which way is it? It's so hard to see!"

    b "Ok, ok. One second. I'm going to try and find a torch. Stay here, I'll be right back!"

    play music "scary-three.ogg" fadein 5

    "..."







    # This ends the game.

    return
