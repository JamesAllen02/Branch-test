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
    
    play music "happy-one.ogg" fadein 5

    python:
        povname = renpy.input("Oh, you're finally here! I'm so sorry, but I seem to have forgotten your name. What was it, again? \n", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Pat Smith"
    

    pov "Oh, right! Of course.. my name is [povname]!"

    b "You know, it's been such a long day. I'm glad to finally be back home so I can relax a bit."

    b "I've had a lot of issues with power outages lately. Maybe a big, strong guy like you could help fix that?"

    hide eileen happy
    scene small_apartment_kitchen_night
    show eileen_dark
    play music "scary-one.ogg" fadein 5

    b "Oh no! It happened again."

    b "It's really dark now. I can barely see anything"

    hide eileen_dark
    show eileen_dark:
        xalign 0.75
        yalign 1 

    play music "scary-two.ogg" fadein 5

    b "Oh, which way is it? It's so hard to see!"

    b "Ok, ok. One second. I'm going to try and find a torch. Stay here, I'll be right back!"

    hide eileen_dark

    play music "scary-three.ogg" fadein 5

    pause 0.5

    "..."

    "..."

    "She's gone for a few minutes..."

    b "Oh, hey! So sorry about that. I couldn't find it anywhere!"

    show eileen_red

    b "By the way, did I tell you? You look very... tasty.."

    b "And all that searching made me a bit hungry... so good that we're right by the kitchen.."

    b "Actually, [povname]... ever since I saw you for the first time, I've had this urge.."


   
    
    
    
    
    
    "You wonder if you should leave"
    
    menu:

        "Leave.":
            jump choice1_yes

        "No, I stay":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        "you leave."

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        "You stayed"

        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 
   
   
    # This ends the game.

    return
