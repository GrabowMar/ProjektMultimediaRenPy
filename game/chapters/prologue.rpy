label disclaimer:
    scene black
    stop music fadeout 1.0
    show text "{color=#FFFFFF}Disclaimer: This game is a work of fiction and does not intend to represent or depict any actual event, person, or entity. The game may contain some mistakes and inaccuracies regarding the science, technology, and ethics of artificial intelligence. The game is not meant to provide any authoritative or definitive information on the topic. The game is meant for educational purposes only. The views and opinions expressed in the game are not those of the authors and do not necessarily reflect AI field in accurate field. The authors are not responsible for any harm or damage caused by the game or its content. Play at your own risk. \n\nClick to continue...{/color}" with dissolve
    pause
    play music "../audio/ambience/TenseIntroduction.mp3" fadein 5.0
    show text "{color=#FFFFFF}Marcin Grabowski and Andrii Yarosh present...{/color}" with dissolve
    with Pause(2)
    show text "{color=#FFFFFF}Tile{/color}" with dissolve
    with Pause(2)
    hide text with dissolve
    
    hide text with dissolve
    return

label prologue:
    define n = Character("Narrator", color="#000000", what_font="../fonts/VST323/VT323-Regular.ttf", what_size=45)
    scene bg pool at Pan((100, 100), (100, 1097), 40, repeat=True) with dissolve
        # truecenter        
    # with dissolve
    show sprite pool:
        parallel:
            truecenter
            floating
    show effects pool:
        parallel:
            truecenter
            additive_blend
    with dissolve

    n "The year is 2030."
    n "Artificial intelligence, or AI, has become a ubiquitous part of our lives."
    n "From voice assistants and chatbots to self-driving cars and smart factories,"
    n "AI is constantly evolving and changing the way we live, work, and play."
    n "But it also poses unprecedented dangers and ethical challenges."
    n "AI systems can be prone to errors and misuse, affecting the lives and rights of millions of people."
    n "Humanity can no longer afford to ignore the risks of AI."
    n "This is a game isn't about technology or science." 
    n "it is about the choices we make, the values we uphold, and the consequences we face,"
    n "in a world in which balance between creation and creator sits on the knife edge,"
    n "world in which man is must acknoweldege that he might not be only sentient being shaping his future."
    n "What if we created machine that was so familiar to us, that we could not tell it apart from ourselves?"
    n "Only for it to be baffled by us compairing to itself."
    n "In the end we conquered the world, shaped it to our liking, and now we are faced with the question"
    n "What if something else wanted to do the same?"

    hide sprite pool
    hide effects pool
    scene bg black at truecenter with eyeclose
    return
