# Chapter 1: Unraveling Minds
init python:
    alex_interaction = False
    vivian_interaction = False

# Start of the script
label chapter1:
    play music "../audio/ambience/GoodEnough.mp3" fadein 5.0
    scene bg player_office
    
    
    # Introduction
    "Another day at genAIcorp bathed in relentless sunlight. Not exactly my dream job, but it's keeping the creditors at bay."
    "As a lowly QA specialist in company on edge the of bankrupcy, I've certainly seen brighter days. Still, it's not all doom and gloom."
    "Sure, my job isn't thrilling, but it's a stepping stone. At least it keeps the fridge stocked and prevents me from getting too familiar with ramen noodles."
    "I better check my inbox. I'm sure Alex has sent me another one of his \"urgent\" emails."

    $ player_name = renpy.input("\"To log in, enter your name:\"").strip()
    $ player_name = player_name if player_name else "Player"
    define player = Character('[player_name]', who_color="#1100ff")
    "\"Hello, [player_name]! You've got mail from Alex, your oh-so-friendly boss.\""
    player "Hmm, what's got Mr. Prick in a twist this time? Better check it out. But first, Vivian's patiently twiddling her thumbs in the break room."
    "{i}I quickly scan the email's contents.{/i}"
    alex "\"Hey [player_name], urgent! Come to my office on the double. 74th floor's losing it!\""
    player "Fantastic. Another day, another crisis. I wonder what catastrophe awaits us this time?"
    player "I should probably see what's cooking in aLEX's office. But then again, Vivian's been waiting for a chat, and I hate to keep a friend hanging."


    # Choices
    menu:
        "Head to Alex's lab. It sounds urgent.":
            jump alex_lab
        "Catch up with Vivian. Alex can wait a tad longer.":
            jump break_room

label alex_lab:
    show alex neutralDown at center
    alex "[player_name], great timing. I've got a real headache on my hands."
    player "What seems to be the problem, Alex?"
    alex "Our AI system, [player_name]. It's behaving erratically, and I can't seem to pinpoint the cause."
    player "Have you tried restarting it?"
    alex "Believe me, I've considered it. But given its current state, I fear a simple reboot might not suffice."
    player "Then maybe we should bring in an expert from another department?"
    alex "That could be an option, but coordinating schedules and securing clearance would add unnecessary complications. Besides, I trust your intuition, [player_name]. Let's dive deeper into the code together."
    player "Fair enough. What specific anomalies are you observing?"
    alex "It started with minor glitches – incorrect data processing, inconsistent responses. Now, it's escalated to more serious issues like unauthorized access attempts and even attempts to override certain protocols."
    player "This sounds critical. Have you informed higher-ups yet?"
    alex "Not yet. I want to exhaust all possible solutions before involving them. They'd only add pressure and potentially jeopardize our progress."
    player "Understood. Let's focus on finding a solution then."
    alex "Exactly, [player_name]. Together, we'll crack this nut."
    
    menu:
        "Take a breather, Alex":
            alex "I appreciate the offer, [player_name], but time is of the essence. The longer this issue persists, the greater the risk."
            player "Okay, let's push through for now. How about a coffee break once we've made some progress?"
            alex "Deal, [player_name]. Coffee will taste sweet once we've solved this puzzle."

        "Bring in additional help":
            alex "Collaborating with management comes with significant risks, [player_name]. Last week's events serve as a reminder of their reckless decisions and potential consequences. I believe we can handle this between us without inviting further complications."
            player "But their expertise could be invaluable, Alex. Surely the benefits outweigh the risks?"
            alex "Perhaps, [player_name], but at what cost? The tension between us and management remains high, and introducing them into our investigation could lead to unwanted interference or mistrust."
            alex "Let's continue exploring other options before considering whole upper management's involvement."

    alex "Alright, [player_name]. Enough discussion for now. Take this report to Sam; perhaps he can provide some insight into the AI's behavior."
    player "Understood, Alex. On my way to see Sam now."
    $ alex_interaction = True
    hide alex
    jump sam_office

label break_room:
    scene bg alex_office
    show vivian at center
    vivian "Ah, [player_name], long time no see! I heard you've been traveling lately. Tell me all about it!"
    player "Hi, Viv. Yes, I managed to sneak away for a quick vacation to Iceland. It was absolutely stunning - the landscapes, the people, and the culture were truly captivating."
    vivian "Incredible! I bet you saw some amazing sights. Did you go whale watching?"
    player "Regrettably, no whales for me this time. However, I did manage to witness some incredible geothermal activity and explore ancient ruins. I feel refreshed and ready to tackle new challenges upon my return."
    vivian "Wow, [player_name], you really know how to live life to the fullest! I can't wait to hear more stories. Enjoy your break while it lasts!"
    player "Thanks, Viv. I'll be sure to share more stories with you soon. But for now I must ask you few things about recent events."
    player "I was absent and only heard rumors. What's the latest gossip around here?"
        
    menu:
        "Ask Vivian about her recent project updates":
            vivian "You know, the usual. Debugging here, testing there. But enough about work! How about you? Any exciting travel plans coming up?"
            player "Always the workaholic! Got any fun plans for the weekend?"
            vivian "Thinking of binge-watching that new series everyone's talking about. Care to join me?"
        "Discuss the recent AI project hiccup":
            vivian "You heard about it too? It's causing quite the buzz around here."
            player "After the layoffs, I wouldn't be surprised if someone's up to some mischief."
            vivian "Haha, always the detective! But our security's tighter than ever since the incident. Relax, [player_name]. There's nothing to worry about. I'm confident our team will iron out the kinks."
        "Talk about the upcoming company event":
            vivian "Speaking of which, have you seen the invite for the company bash next week?"
            player "I have! It's going to be epic. Are you going?"
            vivian "Of course! Who knows, maybe we'll finally find out what Alex looks like without his glasses. Or maybe we'll discover hidden talents among our colleagues."
            player "Now that's intriguing! I can hardly wait."

    player "Thanks for the update, Viv. You always know how to brighten my day. Back to work for me."
    player "I better check in with Alex. He's probably wondering where I am."

    "Just as I'm about to leave, a note under the lounge table grabs my attention"
    "Urgent: Meet me in the parking lot behind Building C at midnight. Bring what I asked you about."
    "Signed, \"X-X\"."

    "My heart races as I read the words aloud to myself. This couldn't be related to the recent AI project hiccup, could it? Troubles began at night after all."

    "Last week had been chaotic. Our team had been working tirelessly to resolve the unexplained errors plaguing our advanced AI system."
    "Rumors circulated about potential sabotage following the recent round of layoffs."
    "Some claimed that disgruntled employees were seeking revenge by tampering with the project. Others believed it was an external threat. Regardless, tensions ran high."

    "I couldn't shake off the feeling that something wasn't right. The mysterious message lingered in my mind."

    "When I was going to leave the break room, Sam my boss approached me. And invited me to his office."


    hide vivian
    $ vivian_interaction = True
    jump sam_office


label sam_office:
    scene bg sam_office
    show sam at center
    "Sam's office is elegant and spacious. A far cry from my cramped cubicle. The room exudes an air of professionalism and calmness, making it an ideal setting for strategic discussions."

    if alex_interaction:
        sam "[player_name], shut the door."
        player "Alex briefed me about the AI's erratic behavior."
        sam "Good. Hand me the report. We need a solution, and fast."

    elif vivian_interaction:
        sam "[player_name], close the door. "
        player "I found this note in the break room. Problems with our project began around midnight last week. I'm not sure if it's related, but I thought you should know."
        sam "Interesting. I'll look into it. But first, let's discuss the AI's behavior."


    "{i}The weight of responsibility presses heavily upon our shoulders as we confront the enigma of the rogue AI.{/i}"
    player "The very existence of our project rests precariously in the balance. Our collective futures and the esteemed reputation of our organization hang in the balance as well."
    sam "You're absolutely right, [player_name]. This situation demands our full attention and commitment."

    sam "I have a plan. But it's risky. And it requires your assistance."
    player "I'm all ears, Sam. What do you need me to do?"
    sam "I need you to test the AI's decision-making capabilities. I've prepared a list of questions for you to ask it. I want to see if it's still capable of making rational decisions."
    player "Sounds simple enough. What's the catch?"
    sam "The catch is we don't really know what we're dealing with. The AI's behavior is erratic and unpredictable. It could be a minor glitch or a major malfunction."
    player "That's not very reassuring, Sam. What if it's the latter?"
    sam "It's not possible, I know it. But we need to be sure. That's why I need you to ask the AI these questions. I know they used complete new approach with this one..."
    player "... but ..."
    sam "Ignore it, I know we can fix it. But we need to be sure, when you will be sure we are still in control, we will think how to fix it."
    sam "Also take Vivian and Alest with you, they will help you with the questions."
    sam "And one last thing, don't make rush decisions, If we scrap this project it will contribute to current very bad financial decision of this company, you understand that?"

    menu:
        "I understand, Sam. I'll do my best to help.":
            sam "Good, I knew I could count on you. Now go and do your job."
        "What if situation will turn out to be really f-ked up?":
            sam "Don't worry, I'm sure it's just a minor glitch. But if it's not, we will think of something. Now go and do your job."
            sam "We put a lot of effort and money into this project, we can't just scrap it."

    hide sam
    scene bg black at truecenter with eyeclose
    return