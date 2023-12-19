# Chapter 1: Unraveling Minds

# Define characters

# Start of the script
label chapter1:

    scene bg attack_socialMedia
    
    # Introduction
    "Another sunny day at genAIcorp. Not the best job in the world, but it pays the bills. I'm a QA junior tester, and I work on some kind of AI project. I'm not the best at my job, but I'm not the worst either."
    "I'm not sure if I like my job, but it help me to achive my lifetime goal of not working myself to death while still being able top enjoy luxuries such as not starving to death."
    "But enough of that I need to check my e-mail."
    "Good I have my name as my e-mail address, otherwise I would have forgotten it because of all the things happening here since last week."
    $ player_name = renpy.input("\"To login enter your name:\"").strip()
    $ player_name = player_name if player_name else "Player"
    define player = Character('[player_name]', who_color="#1100ff")
    "\"Hello, [player_name]! You have 1 new message from your boss, Alex.\""
    player "I wonder what mr. Prick wants, I better do whatever he wants now after I meet up with Vivian, I wouldn't want to upset only person that I can call a friend here."
    "{i}I open the e-mail and read it.{/i}"
    alex "\"Hello [player_name], I need you to come to my office ASAP. 74th floor is furious, They will skin us alive if we won't act NOW!!! \""
    player "Perfect, management is pissed off again, I wonder what happened this time, it really seems important"
    player "I should check it out, but I also promised Vivian to meet up with her in the break room after I'm done with my e-mails."



    # Choices
    menu:
        "Head to Alex's lab whatever he wants, it's probably important.":
            jump alex_lab
        "Catch up with Vivian in the break room. You can always go to Alex later.":
            jump break_room

label alex_lab:
    show alex neutralDown at center
    alex "[player_name], I'm glad you're here. We have a problem."
    player "What's going on?"
    show alex neutral at center
    alex "I've been working on a new AI system, but it's not working as expected."
    player "Of course it's not, management laid off half of the team last week, I would not be suprised if one of them sabotaged project."
    show alex neutralDown at center
    alex "I don't think so, company  made sure that they won't be able to access the system, and if they did, they would be caught no matter what."
    player "So what's the problem?"
    show alex neutral at center
    alex "I don't know, I've been working on this project for months, and it was working fine, but now it's not."
    menu:
        "Maybe you should take a break.":
            show alex smile at center
            alex "I can't, I need to fix this, I can't let down people that pay my bills, not to mention that I would be fired like half of the people that we called co-workers just week ago."
            player "I understand, but you need to take care of yourself, you can't work like this."
            show alex neutralDown at center
            alex "Not everyone is slackers like you, [player_name], and need vacation every other week."
            player "I'm not a slacker, I just know how to take care of myself."
            alex "Whatever, maybe if you were here week ago we would not be in this situation."
            player "I doubt that, I'm not a miracle worker."
        "Maybe you should ask management for help.":
            show alex laugh at center
            alex "Yeah, I'm sure they would be happy to help, especially now."
            show alex neutralDown at center
            alex "You know they laid off half of the team last week, we are already on chopping block. They would not hesitate to fire us if we would ask for help."
            player "I know, but we can't do this alone, we need help."
            alex "At least try not to go to any vatacions for a while, again. And maybe, just maybe we will be able to fix this."
            player "I'm not a slacker, I just know how to take care of myself."
            alex "Too bad you don't know how to take care of your work."
    alex "I'm sorry, I didn't mean to say that, I'm just stressed out. Were Iceland at least nice?"
    player "It was great, I needed that."
    alex "I'm glad to hear that."
    alex "Ok, let's get back to work, we need to fix this."
    alex "Take this raport, and give it to Sam, he will tell you what to do next."
    player "Ok, I will do that."
    jump sam_office


label break_room:
    show vivian at center
    vivian "Hey, [player_name], I'm glad you're here."
    player "Hey, Viv, what's up?"
    vivian "Before we start, I'm curious, how was vacations in Iceland?"
    player "It was great, I needed that."
    vivian "I'm glad to hear that."
    player "So what's up?"
    vivian "I've been working on a new AI system, but it's not working as expected."
    player "Of course it's not, management laid off half of the team last week, I would not be suprised if one of them sabotaged project."
    vivian "I don't think so, company  made sure that they won't be able to access the system, and if they did, they would be caught no matter what."
    player "So what's the problem?"
    vivian "I don't know, I've been working on this project for months, and it was working fine, but now it's not."
    
    player "Ok now I should really go to Alex's lab."
    "When you arrive at Alex's lab, you see note on the door urging you to go to Sam's lab."
    "\"[player_name], Thanks for taking my request seriously, I had to go to Sam's office, please meet me there.\""

    jump sam_office



label sam_office:
    scene bg background_desk






# label bad_ending:

#     scene bg_corporation_discord

#     player "Everything fell apart. EdgeAI is in chaos, and we're at the center of it."

#     "Try again.":
#         player "I need to go back and make different choices."

#         jump start

# label good_ending:

#     scene bg_corporation_harmony

#     player "Our concerns were heard, and things took a positive turn."

#     "Continue to Chapter 2":
#         player "I'm curious to see what happens next."

#         # Jump to the next chapter
#         jump chapter_2
