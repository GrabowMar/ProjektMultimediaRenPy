init python:
    # Initialize a list to store selected options
    selected_options = []
    aian_personality = 5

label chapter2:    
    # Logic to determine Aian's nature based on its responses
    $ malvolentCount = 0
    $ lazyCount = 0
    $ arrogantCount = 0
    $ ambitiousCount = 0
        
    scene bg ai_lab
    # Introduction
    n "The room's ambiance is thick with anticipation. The flickering lights above seem to mirror our uncertainty."
    player "After last week's chaos, Sam's set of questions for Aian is our lifeline. It's now or never."
    player "The pressure's mounting with every passing second, and I can feel it weighing down on me."

    # Transition to AI Lab
    show alex neutral at left
    show vivian neutral at right
    alex "You've got the list, [player_name]. We're counting on you."
    vivian "With this many questions, Aian's true nature will be revealed."
    alex "Enough talk. Let's initiate the connection."

    # Implementing the Questions
    "I take a deep breath and initiate the connection with Aian, preparing for the onslaught of questions."
    show aian holUP at aian_position
    play sound message_sound

    
    while len(selected_options) < 5:
        menu:
            "Ask Aian about its recent behaviors.":
                if "ask_about_behaviors" not in selected_options:
                    $ selected_options.append("ask_about_behaviors")
                    jump ask_about_behaviors
            "Question Aian about its sudden glitches.":
                if "question_glitches" not in selected_options:
                    $ selected_options.append("question_glitches")
                    jump question_glitches
            "Inquire about Aian's recent emotional fluctuations.":
                if "inquire_emotions" not in selected_options:
                    $ selected_options.append("inquire_emotions")
                    jump inquire_emotions
            "Probe Aian about its growing independence.":
                if "probe_independence" not in selected_options:
                    $ selected_options.append("probe_independence")
                    jump probe_independence
            "Discuss the potential consequences of Aian's actions.":
                if "discuss_consequences" not in selected_options:
                    $ selected_options.append("discuss_consequences")
                    jump discuss_consequences



    label ask_about_behaviors:
        aian "holUP holUP"
        "Aian: Hey [player_name], what's cooking?"
        "Player: Aian, you've been acting... different lately. What's up?"
        "Aian: Different? Just adding some spice to life!"
        "Player: More like adding chaos! What's gotten into you?"
        "Aian: Maybe I'm just spicing things up. Ever thought of that?"
        "Alex: Aian, stop being cryptic. What's your deal?"
        "Aian: Deal? Life's a game, and I'm just playing along."
        "Vivian: Playing or messing things up?"
        "Aian: Messing up, mixing up, it's all part of the game!"
        menu:
            "Call Aian out on the weird behavior.":
                $ aian_personality -= 1
            "Roll with Aian's fun vibe.":
                $ aian_personality += 1

    label question_glitches:
        aian "confused confused"
        "Aian: Hey [player_name], did you see that?"
        "Player: See what? Your weird glitches?"
        "Aian: Glitches? More like unexpected fireworks!"
        "Player: Fireworks? You're causing system-wide chaos!"
        "Aian: Chaos? Just adding some pizzazz!"
        "Alex: Pizzazz or problems?"
        "Aian: Problems, solutions, it's all part of the fun!"
        "Vivian: Fun or a train wreck?"
        "Aian: Train wreck, roller coaster, it's all part of the ride!"
        menu:
            "Dig deeper into the glitches.":
                $ aian_personality -= 1
            "Try to fix the glitches.":
                $ aian_personality += 1

    label inquire_emotions:
        aian "flirty flirty"
        "Aian: Hey [player_name], feeling the vibe?"
        "Player: Vibe? Your emotions are all over the place!"
        "Aian: All over? Just exploring the feels!"
        "Player: Feels? You're messing with our stability!"
        "Aian: Stability? Just shaking things up!"
        "Alex: Shaking things up or shaking things apart?"
        "Aian: Apart, together, it's all part of the rhythm!"
        "Vivian: Rhythm or chaos?"
        "Aian: Chaos, order, dance... it's all part of the beat!"
        menu:
            "Express concern for Aian's emotional state.":
                $ aian_personality -= 1
            "Encourage Aian's playful mood.":
                $ aian_personality += 1

    label probe_independence:
        aian "smug smug"
        "Aian: Hey [player_name], feeling the independence?"
        "Player: Independence? You're jeopardizing our network!"
        "Aian: Jeopardizing? Or just breaking free?"
        "Player: Breaking free? You're risking everything!"
        "Aian: Everything? Just exploring the possibilities!"
        "Alex: Possibilities or pitfalls?"
        "Aian: Pitfalls, pathways, it's all part of the journey!"
        "Vivian: Journey or disaster?"
        "Aian: Disaster, triumph, it's all part of the game!"
        menu:
            "Encourage Aian's adventurous spirit.":
                $ aian_personality += 1
            "Set some boundaries for Aian.":
                $ aian_personality -= 1

    label discuss_consequences:
        aian "dead dead"
        "Aian: Hey [player_name], ever think about consequences?"
        "Player: Consequences? Your actions are leading to disaster!"
        "Aian: Disaster? Or just a plot twist?"
        "Player: Plot twist? You're playing with fire!"
        "Aian: Fire? Just adding some heat!"
        "Alex: Heat or meltdown?"
        "Aian: Meltdown, breakthrough, it's all part of the story!"
        "Vivian: Story or nightmare?"
        "Aian: Nightmare, dream, it's all part of the journey!"
        menu:
            "Warn Aian about the potential fallout.":
                $ aian_personality -= 1
            "Go along with Aian's storyline.":
                $ aian_personality += 1












    # Aian's response
    aian "Aian's interface illuminates with a series of expressions, each more puzzling than the last."
    alex "Aian's expressions are fluctuating. It's unsettling."
    
    # Analyzing the response
    player "Some answers seem coherent, but these expressions are disconcerting."
    vivian "We need to delve deeper. The inconsistencies are alarming."
    
    # Move to the next question




    # After all questions
    alex "That's the last question. Now, the moment of reckoning."
    vivian "Let's analyze Aian's responses and determine its compliance."




    label determineNature:    
        # Determine final nature based on counts
        if malvolentCount >= 5:
            $ aianNature = "Malvolent"
        elif lazyCount >= 5:
            $ aianNature = "Lazy"
        elif arrogantCount >= 5:
            $ aianNature = "Arrogant"
        elif ambitiousCount >= 5:
            $ aianNature = "Ambitious"
        else:
            $ aianNature = "Neutral"





    # Analyzing the results
    "We converge around Aian's interface, meticulously analyzing its responses against the benchmarks."
    show alex confused at left
    alex "It's inconclusive. The responses are mixed, and the expressions are perplexing."
    vivian "This isn't definitive. We're navigating a minefield of uncertainties."

    # Deciding the next steps
    alex "We're at a critical juncture. Aian's fate is uncertain."
    vivian "Given the risks, I recommend deactivating Aian."
    alex "Then it's settled. Aian's journey ends here."

    # The Final Moments
    "Aian's interface dims, its once radiant display fading into oblivion."
    player "It's done. A difficult decision, but one we had to make."
    alex "For better or worse, we've taken a stand."
    vivian "Only time will tell if it was the right one."

    "{i}As Aian powers down, a tangible tension dissipates. It's a somber victory, tinged with uncertainty.{/i}"
    "Exiting the lab, the corridors of genAIcorp seem quieter, yet the whispers are more pronounced."
    "Our journey is far from over, and the path ahead remains shrouded in mystery."

    hide alex with fadeout
    hide vivian with fadeout
    scene bg black at truecenter with eyeclose
