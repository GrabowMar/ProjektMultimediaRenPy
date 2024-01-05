# Chapter 1: Unraveling Minds

# Start of the script
label chapter1:

    scene bg attack_socialMedia
    
    # Introduction
    "Another sunny day at genAIcorp. Not my dream job, but it pays the bills. As a QA junior tester, I've seen better days, but hey, it's not all bad."
    "While I'm not exactly thrilled with my job, it's a stepping stone. I get to enjoy life's comforts, like, you know, not starving."
    "But, enough chit-chat. Time to check those emails."
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
    show alex neutralDown at center
    alex "[player_name], good you're here. We've got a situation."
    player "What’s the scoop?"
    show alex neutral at center
    alex "My new AI system's acting up. Big time."
    player "Given last week's layoffs, I wouldn't be shocked if someone's tampered with it."
    show alex neutralDown at center
    alex "No, it's secure. This is different."
    player "So, what's the deal?"
    show alex neutral at center
    alex "Honestly, I don't know. It was smooth sailing, and now it's... not."
    
    menu:
        "Take a chill pill, Alex. Maybe step back?":
            show alex smile at center
            alex "Wish I could. But I can't let the team down. And neither should you."
            player "Hey, self-care's essential. Ever consider it?"
            show alex neutralDown at center
            alex "Not all of us can jet off on vacations, [player_name]."
            player "It's not about the trips. It's about balance."
            alex "If you'd been more present last week, maybe we wouldn't be in this mess."
            player "Doubtful. I can't work miracles."
        "Why not loop in management?":
            show alex laugh at center
            alex "Right, because they're in such a helpful mood after the layoffs?"
            show alex neutralDown at center
            alex "We're on thin ice, [player_name]. Pushing management now would sink us."
            player "We need a plan. Together."
            alex "Then maybe curb the vacations, and focus on the job."
            player "It's not about the vacations. It's about perspective."
            alex "And yours needs a bit of tweaking."

    alex "Sorry, that came out wrong. Stress talking. Was Iceland at least fun?"
    player "Absolutely. Refreshing."
    alex "Good for you."
    alex "Back to business. Take this report to Sam. He'll guide us further."
    player "Got it. Off to Sam’s."

    hide alex
    jump sam_office

label break_room:
    show vivian at center
    vivian "Hey, [player_name], good you're here."
    player "What's cooking, Viv?"
    vivian "How was Iceland? Refreshing?"
    player "Exactly what the doctor ordered."
    vivian "Glad to hear. Now, about this AI project..."
    player "Given the recent layoffs, someone might have a grudge."
    vivian "Doubtful. Security’s top-notch. But it's puzzling."
    player "Alright, gotta head to Alex’s lab."
    "As I approach, a note catches my eye: \"[player_name], urgent! With Sam. Meet there.\""
    hide vivian
    jump sam_office

label sam_office:
    scene bg sam_office

    "Sam's office feels like a pressure cooker. Papers everywhere, screens flashing, and an intensity you could cut with a knife."
    show sam smile at center
    sam "[player_name], close the door. It's bad."
    player "What's rattled you, Sam?"
    sam "The AI's rogue. It's not just malfunctioning—it's spiraling out of control."
    player "This is a nightmare. After all our hard work?"
    sam "Focus, [player_name]. You need to find anomalies. We're on the brink."
    player "I'm on it, Sam."
    sam "Hurry. We need answers. Fast."

    sam "Here's everything we know. Get to the bottom of this."
    player "Got it."

    "{i}As the door clicks shut, a cold silence fills the room. The weight of the AI's fate, our team's future, and the company's standing hangs heavy. It’s daunting, but I’m all in.{/i}"

    hide sam
    show sam smile at left
    show vivian neutralDown at center
    vivian "[player_name], we're in deep. The AI's a ticking time bomb."

    show alex neutralDown at right
    alex "We've dug deep. This isn't just a glitch. It's a disaster waiting to happen."

    player "I’m compiling a report. We need to act."

    show vivian neutralDown at center
    vivian "How can we help?"

    show alex neutralDown at right
    alex "Time's ticking. Let's get to work."

    player "Agreed. We'll tackle this as a team."

    "{i}With Vivian and Alex at my side, we plunge into the AI crisis. It's not just a technical hiccup; it's a full-blown crisis. But together, we'll face it head-on.{/i}"
    scene bg black at truecenter with eyeclose