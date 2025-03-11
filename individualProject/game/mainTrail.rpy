default giveHotDog = False
default generous = False
label town:
    $ distance += 4
    scene town with fade
    s "I think it's time to go to the store and restock on food."
    scene store with dissolve
    $ distance += 3
    $ inventory.append("food")
    "What else to get?"
    menu:
        "Bear can":
            show bear can with dissolve
            "I guess safety doesn't hurt."
            $ inventory.append("bear can")
            hide bear can with dissolve
        "Ice axe":
            show ice axe with dissolve
            "There could be some snow coming up."
            $ inventory.append("ice axe")
            hide ice axe with dissolve

    s "I've got all the stuff I need!"
    if talked_to_angels == True:
        s "Time to head back to Hiker Heaven, or whatever Donna called it."
    else:
        s "I wonder if this town has a place to stay".
    jump heaven

label heaven:
    scene heaven site with fade
    show jeff with dissolve
    $ distance += 2
    if talked_to_angels == True
        s "Hey, excuse me ... ?"
        j "Hey, [name]. Donna told me about you, coming off that spur this morning. Did you get what you needed?"
        s "Yeah, I did. I should be heading off tomorrow morning."
        j "Well, come on over here. I'll grab you a new Buff, yours is looking pretty ragged."
        show buff with dissolve
        $ inventory.append("Buff")
        j "Here you go."
        hide buff with dissolve
        j "Have a good evening, [name]."
    else:
        j "Welcome to Hiker Heaven! Make yourself comfortable."
        j "We have everything you need and more." 
        j "Well, you have yourself a good evening, [name]."
    
    scene night with fade
    "..."
    "..."
    jump trailMorning

label trailMorning:
    $ distance += 4
    scene heaven site with fade
    "Time to head out."
    scene trailhead with fade
    $ distance += 9
    "Let's keep hiking."
    $ distance += 12
    jump mountainPass

label mountainPass:
    scene pass with fade
    s "Of course it has to happen now."
    if talked_to_angels == True:
        s "No better time than after a resupply."
    else:
        s "I'm running out of food."
    $ distance += 6
    if hydration < 10:
        "Your vision starts to fade."
        s "I might have needed to fill up on water."
        return
    else:
        $ distance += 4
        scene pass top with dissolve
        s "I'm at the top! I can see everything!"
        if talked_to_angels == False:
            s "I'm getting really hungry, though."
        else:
            s "Time for a snack."
            $ inventory.remove("food")
            "Much better."
        show hiker with dissolve
        jump hiker_dialogue

label hiker_dialogue:
    h "Hey, man, I'm feeling a little hungry. Do you mind if I grab some food?"
    menu:
        "Sure, here's a hot dog!":
            $ inventory.remove("hot dog")
            $ generous = True
            s "Yeah, here you go!"
            h "Thanks, ...? What's your name?"
            s "I'm [name]."
            h "Nice to meet you, [name]."
            h "The rest of my tramily decided to head out early, so I'm hanging here before I catch up to them."
            h "Thanks for the food."
            s "No problem. I know how tight food can get out here."
        "Nah, I'm running low on food myself":
            h "No worries dude. It might get pretty snowy up here, just so you know."
            s "Thanks for the info."
    "The sky begins to darken, and you get a sudden urge to set up your tent."
    if generous == True:
        s "Hey, if you need anything else, let me know. I've got some more items, so don't hesitate to ask."
        h "For sure. See you around."
        hide hiker with dissolve
        jump final
    elif generous == False:
        s "See you later."
        hide hiker with dissolve
        jump final
label final:
    if talked_to_angels == True:
        "You're a good player, [name]. Keep that in mind."
        return
    else:
        "Maybe try being a bit more open to talking to people in the future."
        return