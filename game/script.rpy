# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    b "Hello! What do you think of my kitchen?"

    b "You know, it's been such a long day. I'm glad to finally be back home so I can relax a bit."

    b "I've had a lot of issues with power outages lately. Maybe a big, strong guy like you could help fix that?"

    hide eileen happy
    scene small_apartment_kitchen_night
    show eileenDark

    b "Oh no! It happened again."

    b "It's really dark now. I can barely see anything"

    show eileenDark:
        xalign 0.75
        yalign 1 

    b "Oh, which way is it? It's so hard to see!"

    # This ends the game.

    return
