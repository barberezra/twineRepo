label s_terminus:
    if direction == "n":
        scene s_terminus with dissolve
        "You made it to the southern terminus!"
        "You have all of your items."
        "Time to start walking."
        scene desert park with fade
        $ distance += 18
        "You continue walking through scrub brush and washes until you find a marker for a spring."
        "This would be a good place to refill water."
        menu:
            "Refill":
                $ distance += 3
                $ hydration += 10
                show water with dissolve
                "That should last you for another day."
                hide water with dissolve
                jump desert_2
            "Continue":
                hide water with dissolve
                "The spring was too far anyway."
                jump desert_2

label desert_2:
    $ distance += 12
    s "A campsite! I think I should stay here for the night."
    scene night with fade
    "..."
    "..."
    scene desert park with fade
    "As the desert drags on, you notice a spur trail in about five miles."
    "Maybe you can resupply in the nearest town. It's been a couple days and probably doesn't hurt to stock up on food."
    menu:
        "Take the trail":
            $ distance += 5
            jump resupply_desert
        "Continue onwards":
            s "It's probably not a good idea to continue onwards with such little food in my pack."
            s "Oh well."
            $ distance += 10
            jump mountainPass

label resupply_desert:
    scene trailhead with fade
    $ distance += 7
    "You make it down to the trailhead, and to no one's surprise, there are some trail angels tending a barbecue next to their van."
    menu:
        "Talk to the trail angels":
            $ talked_to_angels = True
            s "Hey, guys, what's going on?"
            show donna with dissolve
            d "Oh, just some food for hungry hikers like yourself. You want some?"
            menu:
                "Yes":
                    s "Sure!"
                    show hot dog with dissolve
                    s "Thanks a lot."
                    $ inventory.append("hot dog")
                    hide hot dog with dissolve
            d "You want to stay the night at Hiker Heaven?"
            s "What's that?"
            d "It's our place."
            d "We open it up to all the hikers during the summer."
            d "Keeps us busy."
            s "Sure, if it's not a bother to you guys."
            d "No bother at all! We've been hosting hikers for decades. We even have a shower for you."
            s "I'll take you up on that offer, then."
            jump town

        "Continue into town":
            jump town