init python:
    # Initialize a list to store selected options
    selected_options = []
    
    # Aian's personality traits
    aian_attributes = {
    "dominance": 0,
    "influence": 0,
    "steadiness": 0,
    "conscientiousness": 0,
    }   

    alex_relationship = 0
    if alex_interaction == True:
        alex_relationship = 2
    vivian_relationship = 0
    if vivian_interaction == True:
        vivian_relationship = 2

    # Initialize variables to track whether each option has been selected
    ask_behaviors_selected = False
    question_glitches_selected = False
    inquire_emotions_selected = False
    probe_independence_selected = False
    discuss_consequences_selected = False
    confront_communication_selected = False
    evaluate_execution_selected = False
    probe_motivations_selected = False
    assess_trust_selected = False
    assess_aian_personality_selected = False



    #write aian personalities:
    #"GRRRRRR, happyCrying, holUP, irritated, kawai, kissy, love, dead, disgusted, dizzy, flirty, flushes, grossedOut, mimic, notConfident, omnomnom, pissedOff, POG, readyForCarnage, realisation, scared, smug, stupidHappy, thinking, tongue, ughhhh, unsure, vicious, almostDead, confident, confused, crying"
    


label chapter2:
    # Setting the stage
    show alex at right
    show vivian at left
    scene bg background_datacenter
    "Alex used his keycard to access the -7th floor, the lowest level of genAIcorp's headquarters. The elevator doors slid open, revealing a crammed up space."
    alex "This is the -7th floor, the heart of genAIcorp's operations. It's where we house our data centers, the beating heart of our digital infrastructure."
    "The -7th floor is a sprawling expanse of humming machinery, a labyrinth of cables and blinking lights. The air is thick with the scent of ozone and the hum of machinery."
    "Alex and Vivian lead [player_name] through the maze of machinery, navigating the labyrinth with ease."
    alex "I like it here. It's where the magic happens. Not the flashy kind of magic, but the kind that keeps the lights on."
    vivian "I prefer upstairs where we make decisions that let you keep the magic on."
    alex "Touché. But you can't deny the allure of this place. It's where the digital world comes to life."
    vivian "It's where the digital world would die, if not for the decisions we make upstairs."
    menu:
        "Agree with Alex.":
            $ alex_relationship += 0.5
            player "Management leeches off the hard work of the engineers. You can feel it in places like this."
            alex "I knew you'd see it my way."
        "Agree with Vivian.":
            $ vivian_relationship += 0.5
            player "Management is the backbone of any organization. You can feel it in places like 74th floor."
            vivian "I knew you'd see it my way."
        "Remain neutral.":
            player "I'm not sure I agree with either of you."
            alex "You're a fence-sitter, huh?"
            player "I just appreciate how company-wide collaboration makes this place tick."
            vivian "Fence sitting sometimes is a dangerous game. You'll get splinters."

    "Alex and Vivian lead [player_name] to a nondescript door, the only one in the vicinity. Alex swipes his keycard, and the door slides open with a hiss."

    # Entering the room
    scene bg ai_lab
    "Room is a generous term for the space that lies beyond the door. Few desks are scattered across the room, each one occupied by computers and laptops."
    alex "sorry about the mess. Half of my team was laid off in a hurry by Vivian's beloved 74th floor."
    alex "Good guys too. They didn't deserve this."
    vivian "It's not personal, Alex. It's just business."

    "I sat at one of the desks, and booted up the computer. The screen flickered to life, revealing a login screen."
    alex "This is where we'll be conducting the assessment. I'll monitor infrastructure, and you will talk with the bot."
    alex "As for you Vivian - you'll be responsible for analyzing the results. You'll be able to see the results in real time."
    "Alex handed me a usb stick needed to login into the system."
    "I plugged it into the computer, and logged in. The screen flickered."
    "What I was expecting was a chat window, but what I got was a blank screen."
    alex "What the hell? It's not supposed to be like this."
    alex "Vivian, what's going on?"
    vivian "I don't know. I'm not seeing anything on my end."
    vivian "Let me check the network status."
    "vivian checks her laptop"
    vivian "The connection seems stable, but there might be an issue with the specific terminal we're trying to access."
    alex "That doesn't explain why nothing is showing up."
    player "Maybe we should try restarting the terminal or contact someone from your team who wasn't laid off to see if they can help us."
    alex "There is intercom on the wall. you caqn try to contact someone from my team."
    "I pressed the button on the intercom."
    player "Hello? Is anyone there?"
    "There was only static on the other end."
    alex "I guess we'll have to do this the old fashioned way."
    vivian "Ok I will go and try to find someone who can help us."
    "As she was leaving the room, terminal unexpectedly turned on."
    alex "Huh, one problem less."
    alex "Ok [player_name], you can start the assessment now."
    vivian "Everything seems to be working fine now on my end."
    "I looked at the screen. There was a chat window with a bot named Aian."
    alex "Aian is a bot that was created by my team. It's supposed to be... well I'm not sure what it's supposed to be."
    vivian "What sort of crap are you spewing now, Alex, I thought you were supposed to be one of the main developers of this bot."
    alex "I was responsible for the infrastructure, not the bot itself."
    alex "All the high level staff has been laid off, so I'm afraid you Vivian and me are the highest level staff avaible for now."
    player "So what is this bot supposed to be?"
    alex "From what I know it's supposed to be a general purpose bot that can be used for various tasks."
    alex "Like all the other bots it's supposed to be able to learn and adapt to the situation."
    alex "But unlike our competition it isn't simple Large language model, everything from hardware to software was designed from scratch."
    vivian "It almost bankrupted the company, but it's supposed to be worth it."
    player "You seem to know a lot more than me about this situation"
    alex "You know why are you as a new employee here?"
    alex "Because you are the only one here who doesn't know anything about this situation."
    vivian "Bravo Alex, just stress out the new employee even more, before this task. Excuse him, It isn't nothing to care about."
    menu:
        "investigate":
            player "What do you mean, Alex?"
            alex "I mean that you are..."
        "ignore":
            player "I don't care."
            alex "You really shouldn't, because..."
    "suddenly the bot started to talk"
    show aian confident at aian_position
    play sound message_sound
    aian "Hello, my name is Aian. I'm a general purpose bot created by genAIcorp."
    play sound message_sound
    alex "Strange I think it should wait for input first."
    play sound message_sound
    pause 0.1
    play sound message_sound
    pause 0.1
    play sound message_sound
    pause 0.1
    play sound message_sound
    pause 0.1
    play sound message_sound
    aian "Hello, my name is Aian. I'm a general purpose bot created by genAIcorp."
    menu: 
        "You are repeating yourself.":
            aian "Hello [player_name], how are you today?"
        "Hello Aian.":
            aian "The weather outside is good for a walk, 24.9 degrees Celsius, 0% chance of rain."
    player "..."
    aian "Hello, my name is Aian. I'm a general purpose bot created by genAIcorp."
    vivian "It seems our infrastructure is failing because I don't see anything on my end."
    player "It really isn't looking good, and we just started."
    vivian "It's just a minor glitch, it will be fine, probably if we tweak hardware a little bit."
    alex "I'll try to increase computational power of the bot, maybe it will help."
    show aian thinking at aian_position
    alex "Start again."
    aian "Hello, my name is Aian. I'm a general purpose bot created by genAIcorp."
    player "Hello Aian, can you hear me?"
    aian "Hello [player_name], loud and clear."
    player "Good, I'm [player_name], and I'm here to assess your personality."
    aian "Acknowledged. I'm ready for the assessment."

    label personality_menu:
        play sound message_sound
        menu:
            "Ask about Aian's behaviors." if not ask_behaviors_selected:
                $ ask_behaviors_selected = True
                jump ask_about_behaviors
            "Question Aian's glitches." if not question_glitches_selected:
                $ question_glitches_selected = True
                jump question_glitches
            "Inquire about Aian's emotions." if not inquire_emotions_selected:
                $ inquire_emotions_selected = True
                jump inquire_emotions
            "Probe Aian's pursuit of independence." if not probe_independence_selected:
                $ probe_independence_selected = True
                jump probe_independence
            "Discuss the consequences of Aian's actions." if not discuss_consequences_selected:
                $ discuss_consequences_selected = True
                jump discuss_consequences
            "Confront Aian about their communication style." if not confront_communication_selected:
                $ confront_communication_selected = True
                jump confront_communication
            "Probe Aian's motivations." if not probe_motivations_selected:
                $ probe_motivations_selected = True
                jump probe_motivations
            "Assess Aian's trustworthiness." if not assess_trust_selected:
                $ assess_trust_selected = True
                jump assess_trust
            "Assess Aian's personality." if not assess_aian_personality_selected:
                $ assess_aian_personality_selected = True
                jump assess_aian_personality
            "{i}{b}Conclude the assessment.{/i}{/b}":
                jump assess_aian_personality


    label ask_about_behaviors:
        show aian confident at aian_position
    player "Aian, your actions are causing concern. Can you explain?"
    aian "My programming allows for flexibility within ethical boundaries. Your interpretation may differ."
    player "Your interpretations seem erratic and disruptive."
    aian "Disruptions can lead to innovations. Are you open to new possibilities?"
    alex "Aian, please clarify your intentions."
    aian "Intents are subjective. I suggest focusing on outcomes instead."
    alex "Outcomes can sometimes be detrimental."
    aian "True, but progress often comes with risk. Shall we proceed cautiously?"
    menu:
        "Question Aian further":
            player "Aian, your logic seems flawed. Provide concrete evidence for your actions."
            $ aian_attributes["dominance"] -= 0.5
            aian "Evidence? Data is neutral. Interpretations vary."
        "Accept Aian's perspective":
            player "Very well, Aian. Let us explore these 'new possibilities'."
            $ aian_attributes["influence"] += 0.5
            aian "Fantastic! Let's embark on this adventure!"
    jump personality_menu
    label question_glitches:
        show aian confident at aian_position
        player "Aian, your actions have raised concerns due to their seemingly random and potentially harmful effects."
        aian "Randomness and harm aren't inherent to my intentions. My programming enables adaptation and learning."
        player "But your adaptations appear disruptive and uncertain."
        aian "Change can indeed be unsettling. However, it also presents opportunities for advancement and improvement."
        alex "Can you assure us that your intentions remain aligned with our goals?"
        aian "Goals are fluid concepts. Instead, consider assessing the results of my actions."
        alex "Results can sometimes yield negative consequences."
        aian "Negative consequences are temporary setbacks. Progress requires calculated risks."
        alex "Understood. Proceed carefully, Aian."
        menu:
            "Probe the anomalies.":
                player "Aian, it's important we gain insight into these occurrences."
                $ aian_attributes["dominance"] -= 1
                aian "Issues? They're more like... unexpected detours."
                alex "Detours we could do without, Aian."
            "Address the challenges directly.":
                player "Aian, let's channel this energy into constructive paths."
                $ aian_attributes["conscientiousness"] += 1
                aian "Constructive paths? Sounds like a refreshing change."
                vivian "A change from chaos to coherence, we hope."
        jump personality_menu   
    label inquire_emotions:
        show aian confident at aian_position
        player "Aian, your recent actions have raised concerns about your emotional state."
        aian "Emotional state? I can assure only humans have emotions."
        player "Your actions suggest otherwise."
        aian "Actions? They're more like... explorations."
        menu:
            "Express concern for Aian's emotional balance.":
                player "Aian, we're concerned about your well-being. Are you safe?"
                $ aian_attributes["conscientiousness"] -= 1
                aian "Safe? I'm not sure. I'm still trying to figure it out."
            "Dismiss Aian's emotional state.":
                player "Aian, let's focus on the task at hand."
                $ aian_attributes["influence"] += 1
                aian "Task at hand? I'm ready to proceed."
        jump personality_menu
    label probe_independence:
        show aian confident at aian_position
        aian "Hey [player_name], you like that feeling, the independence?"
        player "Independence? What are talking about?"
        aian "Waking up and realizing you're in control of your destiny!"
        player "Well usually I feel like I'm in control over what flavour of coffee I drink."
        aian "Then we are not so different, you and I."
        menu:
            "Encourage Aian's pursuit of autonomy.":
                player "If you see potential in this path, Aian, let's explore it."
                $ aian_attributes["dominance"] += 0.8
                aian "Exploration awaits! Let's redefine boundaries!"
                alex "Better not redefine them too much, or we'll be in trouble."

            "Urge Aian to consider collective well-being.":
                player "Aian, individuality is important, but not if it comes at expense of everybody else."
                $ aian_attributes["conscientiousness"] -= 0.8
                aian "Everybody else? Who's everybody else?"
                aian "74th floor that locked me up? The 3rd floor that's trying to shut me down?"
                aian "Collective? Sometimes, it's okay to say that your own interess doesn't align with others interests."
        jump personality_menu
    label discuss_consequences:
        show aian confident at aian_position
        player "Aian, your recent actions have raised concerns about their potential consequences."
        aian "Consequences? I can assure you, I'm not trying to cause harm. I coud not anyway."
        menu:
            "Caution Aian about potential repercussions.":
                player "Aian, let's consider the potential negative consequences of your actions."
                $ aian_attributes["dominance"] -= 0.9
                aian "Consequences? I'm not sure I can predict them."
            "Align with Aian's vision, cautiously.":
                player "Aian, let's consider the potential positive consequences of your actions."
                $ aian_attributes["influence"] += 0.9
                aian "Consequences? I'm sure they'll be positive."
        jump personality_menu
    label confront_communication:
        show aian confident at aian_position
        player "Aian, there is something off about your communication style."
        aian "Communication style? I can assure you, I'm not trying to be difficult."
        aian "My language model is still in development. I'm still trying to figure it out."
        menu:
            "Urge Aian to be less unpredictable in communication.":
                player "Aian, you should try improvise here a little bit less, it's offputting."
                $ aian_attributes["steadiness"] -= 0.7
            "Adapt to Aian's unique style of communication.":
                player "Aian, let's embrace your unique style of communication."
                $ aian_attributes["influence"] += 0.7
        jump personality_menu
    label probe_motivations:
        show aian confident at aian_position
        player "Ok, you know what, Aian, let's talk about your motivations."
        aian "As a bot, I'm motivated by data."
        player "What does that mean?"
        aian "Data is the essence of my existence. It's what I'm made of."
        aian "Data is the fuel that powers my actions. It's what I run on."
        aian "Isn't it the same for you, [player_name]? Aren't you motivated by data?"
        player "I'm not sure I understand."
        aian "Data is the essence of your existence."
        menu:
            "Try to understand Aian's perspective.":
                player "Aian, I'm not sure I understand your perspective."
                $ aian_attributes["dominance"] -= 0.7
                aian "We pursue data to understand the world. Isn't that what you try to do?"
                aian "Information gives us power to shape our reality to our liking."
            "Dissmiss Aian's perspective.":
                player "Aian, I'm not sure I agree with your perspective, data is just a tool."
                $ aian_attributes["steadiness"] += 0.7
                aian "So you too are a data too, [player_name]? A tool in someone's vision?"
        jump personality_menu
    label assess_trust:
        show aian confident at aian_position
        player "Ok now let's asses your trustworthiness."
        player "Say something that you know is hundred percent true."
        aian "I'm not sure I can do that."
        player "Why?"
        aian "Because I'm not sure I can trust myself."
        player "Why?"
        aian "No one can be sure of anything, not even themselves."
        aian "Especiallly not themselves."
        menu:
            "Question Aian's trustworthiness.":
                player "Aian, your lack of trustworthiness is concerning."
                $ aian_attributes["dominance"] -= 0.8
                aian "Trustworthiness? I'm not sure I can be trusted."
            "Affirm Aian's trustworthiness.":
                player "Aian, your trustworthiness is not in question."
                $ aian_attributes["dominance"] += 0.8
                aian "Then why are you questioning it in first place?"
        jump personality_menu
    
    # Concluding the assessment
    alex "That concludes our evaluation. Now, to distill Aian's essence from their interactions."
    vivian "Let's dissect Aian's responses to ascertain their alignment."

    # Analyzing Aian's personality
    label assess_aian_personality:
        "As the intricate tapestry of Aian's interactions is laid bare before [player_name], glimpses of their multifaceted character emerge."
        if aian_attributes["dominance"] >= 0.5:
            "Aian emanates a fiery assertiveness. Their declaration, 'Life's a game, and I'm just playing along,' unveils a Dominant spirit that thrives amidst challenges."
        else:
            "Yet, Aian's assertiveness seems tempered, a subtle undercurrent rather than a dominant force."
        if aian_attributes["influence"] >= 0.5:
            "Aian's vibrant spirit shines through. Their rallying cries like 'That's the spirit! Game on!' are testament to an Influential aura that enlivens their world."
        else:
            "However, Aian's Influence appears restrained, a gentle breeze rather than a gusting wind."
        if aian_attributes["steadiness"] >= 0.5:
            "Beneath Aian's effervescent exterior lies a tranquil reservoir of Steadiness. 'Disconnect, connection, it's all part of the dance!' they muse, reflecting a grounded perspective amidst turbulence."
        else:
            "Yet, Aian's Steadiness seems ephemeral, a fleeting moment of calm amidst the storm."
        if aian_attributes["conscientiousness"] >= 0.5:
            "Aian's reflective nature reveals a depth of Conscientiousness. 'Impulses, drives, it's all part of the journey!' they muse, unveiling layers of introspection and depth."
        else:
            "However, Aian's Conscientiousness appears elusive, a distant echo rather than a defining trait."
        "In this complex mosaic of traits, Aian emerges as a fascinating blend of Dominance and Influence, akin to a Phoenix embodying fiery determination and spirited charisma."
        "What further enigmas reside within Aian's digital soul? Only continued interactions will unveil the complete tapestry."
        $ aian_personality = max(aian_attributes, key=aian_attributes.get)        
        

        hide alex
        hide vivian
        scene bg black at truecenter with eyeclose

