# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("[name]", color="#608a04")
define j = Character("Jeff", color="#eb8259")
define d = Character("Donna", color="#911ab3")
define h = Character("Hiker", color="#914f5d")

screen inventory_screen():
    frame:
        xalign 0.4
        yalign 0.03
        if inventory:
            text "Inventory: [', '.join(inventory)]"
        else:
            text "Inventory: Empty"

screen name_display():
    frame:
        xalign 0.1
        yalign 0.03
        text "Name: [name]"

screen distance_display():
    frame:
        xalign 0.9
        yalign 0.03
        text "Distance Hiked: [distance] miles"

default name = ""
default inventory = []
default distance = 0
default direction = "n"
default hydration = 0
default talked_to_angels = False
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene splash page
    "Welcome to the Thru-Hiker's Journey!"

    $ name = renpy.input("What's your name? \n")
    show screen name_display with dissolve
    "In this work, you navigate a virtual section of a long-distance trail."
    "Of course, you can't hike all of the trail, because that would take months."
    jump campo


label campo:
    scene bus station with dissolve
    show screen distance_display with dissolve
    show screen inventory_screen with dissolve
    "It's mid April and you've decided to set off on a thru-hike of the Trail."
    "Why did you choose to do this, again?"
    "You check your bus ticket and, to your surprise, all the information on it is correct!"
    "Time to hop on the bus and get to the southern terminus."
    jump bus

label bus:
    scene bus interior with dissolve
    "Your dream is coming true! A full thru-hike of the T, what could be better?"
    jump s_terminus