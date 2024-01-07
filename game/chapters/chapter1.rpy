# Chapter 1: Unraveling Minds

# Start of the script
label chapter1:

    scene bg player_office
    $ alex_interaction = False
    $ vivian_interaction = False
    
    # Introduction
    "Another sunny day at genAIcorp. Not my dream job, but it pays the bills. "
    "As a QA junior tester, I've seen better days, but hey, it's not all bad."
    "While I'm not exactly thrilled with my job, it's a stepping stone. "
    "I get to enjoy life's comforts, like, you know, not starving."
    "Ah, my email address. Almost forgot amidst the chaos of last week."
    
    $ player_name = renpy.input("\"To log in, enter your name:\"").strip()
    $ player_name = player_name if player_name else "Player"
    define player = Character('[player_name]', who_color="#1100ff")
    "\"Hello, [player_name]! You've got mail from Alex, your friendly boss.\""
    player "Hmm, what's got Mr. Prick in a twist this time? Better check it out. But first, Vivian's waiting for me in the break room."
    "{i}I dive into the email's contents.{/i}"
    alex "\"Hey [player_name], urgent! Come to my office on the double. 74th floor's losing it!\""
    player "Great, management's on the warpath. What's gone awry now?"
    player "I should see what's up. But Vivian's been waiting for a chat, and I hate to keep a friend waiting."

    # Choices
    menu:
        "Head to Alex's lab. It sounds urgent.":
            jump alex_lab
        "Catch up with Vivian. Alex can wait a tad longer.":
            jump break_room

label alex_lab:
    scene bg alex_office
    show alex neutralDown at center
    alex "[player_name], glad you're here. We've got a bit of a mess."
    player "What's going on, Alex?"
    show alex neutral at center
    alex "The AI system I've been working on is acting all kinds of wonky."
    player "You think someone's been messing with it?"
    show alex neutralDown at center
    alex "Nah, our security's tight. This feels different."
    player "Alright, spill the beans."
    show alex neutral at center
    alex "Honestly? It was running smoothly, and now it's just... off."
    
    menu:
        "Maybe take a breather, Alex? Grab a coffee or something.":
            show alex smile at center
            alex "I wish, but there's too much at stake. We've got to figure this out."
            player "Look, we'll sort it. Maybe we both need a coffee break after this."
            show alex neutralDown at center
            alex "Sounds good, but let's get through this first."
        "What about bringing in some extra help?":
            show alex laugh at center
            alex "Oh, you mean management? After last week's chaos? No thanks."
            show alex neutralDown at center
            alex "We're walking a tightrope here, [player_name]. Management's the last thing we need."
            player "Alright, let's brainstorm then."
            alex "Agreed. Let's bounce some ideas around."

    alex "Alright, enough chit-chat. Can you take this report to Sam? He might have some insights."
    player "On it. Heading to Sam's now."
    $ alex_interaction = True
    hide alex
    jump sam_office

label break_room:
    scene bg alex_office
    show vivian at center
    vivian "Hey, [player_name], look who finally decided to show up!"
    player "Missed me, Viv?"
    vivian "Oh, please! I just wanted to hear all about your Icelandic adventures."
    player "It was like a breath of fresh air!"
    
    menu:
        "Ask Vivian about her recent project updates.":
            vivian "You know, the usual. Debugging here, testing there. But enough about work!"
            player "Always the workaholic! Got any fun plans for the weekend?"
            vivian "Thinking of binging that new series everyone's talking about. Join me?"
        "Discuss the recent AI project hiccup.":
            vivian "You heard about it too? It's causing quite the buzz around here."
            player "After the layoffs, I wouldn't be surprised if someone's up to some mischief."
            vivian "Haha, always the detective! But our security's tighter than my jeans after the holidays."
        "Talk about the upcoming company event.":
            vivian "Speaking of which, have you seen the invite for the company bash next week?"
            player "I have! It's going to be epic. Are you going?"
            vivian "Wouldn't miss it for the world!"
    
    player "Ok, duty calls. Off to Alex's lab for me."
    "Just as I'm about to leave, a note on the table grabs my attention: \"[player_name], urgent! With Sam. Head there.\""
    hide vivian
    $ vivian_interaction = True
    jump sam_office


label sam_office:
    scene bg sam_office

    "Sam's office is elegant and spacious. A far cry from my cramped cubicle."
    show sam smile at center

    if alex_interaction:
        sam "[player_name], shut the door. I've heard from Alex about the situation with the AI."
        player "Yes, it's dire."
        sam "Indeed. He mentioned you're compiling a report. Hand it over. Let's see if we can salvage this mess."

    elif vivian_interaction:
        sam "[player_name], close the door. Vivian briefed me about the AI's erratic behavior."
        player "It's escalating."
        sam "Understood. She mentioned a report. Hand it to me. We need a solution, and fast."

    player "Here's what I have."

    "{i}The gravity of our predicament deepens. With each passing moment, the stakes grow higher.{/i}"
    "{i}The AI's fate, our team's future, and the company's reputation are on the line. It's daunting, but I'm all in.{/i}"

    hide sam
    show sam smile at left
    show vivian neutralDown at center
    vivian "[player_name], this is critical. The AI's a ticking time bomb."

    show alex neutralDown at right
    alex "We've done our homework. This isn't just a glitch. It's a catastrophe."

    sam "I'm piecing together a report. And I want you [player_name] to pass this list of questions to see if our friend still acts somewhat \"reliably\"."
    sam "We need to know if it's still capable of making decisions. If it's not, we're in deep trouble."
    sam "If it is, we can still salvage this mess. But we need to act fast."
    sam "I also want you Vivian and Alex to assist [player_name] in this endeavor. We need all hands on deck."
    alex "Clock's ticking. Let's rally."

    player "I hope we can pull this off."

    "{i}With Vivian and Alex by my side, we dive headlong into the AI maelstrom. This isn't a minor setback; it's a monumental challenge. But united, we stand.{/i}"
    hide sam
    hide vivian
    hide alex
    scene bg black at truecenter with eyeclose