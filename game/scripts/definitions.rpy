# FILEPATH: /c:/Users/marci/Desktop/aaaaaaa/game/scripts/definitions.rpy

# This script file contains various definitions and configurations for the game.
# It includes the following:
# - Font replacement map for italics and bold fonts
# - Picker class for character sprites
# - Day-night effects and corresponding tint matrices
# - Programmatically applying effects to background and character sprites based on time of day
# - Definition of characters and their layered images
# - Miscellaneous images such as parallax backgrounds and effects pool

init python:
    import re # regex for parsing file name
    import random


    message_sound = "audio/sfx/message.wav"




    # define italics and bold fonts
    # the arguments are: font file, boldness, italics
    config.font_replacement_map["fonts/Roboto/Roboto-Regular.ttf", True, False] = ("fonts/Roboto/Roboto-Bold.ttf", False, False)
    config.font_replacement_map["fonts/Roboto/Roboto-Regular.ttf", False, True] = ("fonts/Roboto/Roboto-Italic.ttf", False, False)
    config.font_replacement_map["fonts/Roboto/Roboto-Regular.ttf", True, True] = ("fonts/Roboto/Roboto-BoldItalic.ttf", False, False)

    ## for character sprites
    class Picker(object):
        def __init__(self, options):
            self.options =  [ i.split() for i in options ]

        def __call__(self, attributes):
            rv = set(attributes)

            for i in self.options:
                if i[0] in attributes:
                    rv.update(i[1:])

            return rv


    ## day-night effects
    # constants
    DAY = 'day'
    DUSK = 'dusk'
    NIGHT = 'night'
    SEPIA = 'sepia'
    DIM = 'dim'

    # https://www.twoandahalfstudios.com/2019/08/tds-making-of-3-day-night-and-sunset-reshading-images-in-renpy-with-im-matrixcolor
    tint_dark = im.matrix.tint(0.44, 0.44, 0.75) * im.matrix.brightness(-0.02)
    tint_sunset = im.matrix.tint(0.85, 0.60, 0.45) * im.matrix.brightness(0.10)
    # late night in front of glowing object
    tint_dim = im.matrix.tint(0.90, 0.90, 1) * im.matrix.brightness(-0.1)

    # programmatically apply effects
    for file in renpy.list_files():
        ## bg images inside game/images/bg 
        if file.startswith('images/bg'):
            image_path = re.sub(r'images/', '', file) # remove the `images/` prefix
            image_name = re.match(r'images/bg/(.+).png', file).group(1) # ex. images/bg/(bg living_room).png
            renpy.image(image_name + ' day', image_path) # only change the name in preparation for the ConditionSwitch
            renpy.image(image_name + ' dusk', im.MatrixColor(image_path, tint_sunset))
            renpy.image(image_name + ' night', im.MatrixColor(image_path, tint_dark))
            # sepia for flashback scenes
            renpy.image(image_name + ' sepia', im.Sepia(image_path))

            # hook the image to the `time_of_day` variable
            # loop over the times to construct the arguments to ConditionSwitch()
            args = []
            for time in [DAY, DUSK, NIGHT, SEPIA]:
                args.extend(['time_of_day == %s' % time.upper(), image_name + ' ' + time])
            renpy.image(image_name, ConditionSwitch(*args))

            """
            # if we were to write this out in plain Ren'Py code, it becomes:

                image bg hallway = ConditionSwitch(
                'time_of_day == DAY', 'bg hallway day',
                'time_of_day == DUSK', 'bg hallway dusk',
                'time_of_day == NIGHT', 'bg hallway night',
                'time_of_day == SEPIA', 'bg hallway sepia',
                )
            """

        ## do the same for character sprites
        if file.startswith('images/chara/'):
            image_path = re.sub(r'images/', '', file) # remove the `images/` prefix
            image_name = re.match(r'images/chara/.+/(.+).png', file).group(1) # ex. images/chara/vivian/(vivian_eyes_closed).png
            renpy.image(image_name + ' day', image_path) # only change the name in preparation for the ConditionSwitch
            renpy.image(image_name + ' dusk', im.MatrixColor(image_path, tint_sunset))
            renpy.image(image_name + ' night', im.MatrixColor(image_path, tint_dark))
            renpy.image(image_name + ' dim', im.MatrixColor(image_path, tint_dim))
            # sepia for flashback scenes
            renpy.image(image_name + ' sepia', im.Sepia(image_path))

            # hook the image to the `time_of_day` variable
            # loop over the times to construct the arguments to ConditionSwitch()
            # `effect` has higher precedence than `time_of_day`
            args = ['sprite_effect == DIM', image_name + ' dim']
            for time in [DAY, DUSK, NIGHT, SEPIA]:
                args.extend(['time_of_day == %s' % time.upper(), image_name + ' ' + time])
            renpy.image(image_name, ConditionSwitch(*args))

init:
    

    define vivian = Character("Vivian")
    # use this instead if we want side image
    # define vivian = Character("Vivian", image='vivian')

    ## changing time_of_day automatically changes the color of bg and sprites
    # valid values: [DAY, DUSK, NIGHT, SEPIA]
    default time_of_day = DAY
    # valid values: [None, DIM]
    default sprite_effect = None

    default persistent.bg_parallax = True

    ## character sprites
    define expressions = [
    "neutral eyes_center_blink brows_neutral mouth_neutral",
    "smile eyes_center_blink brows_neutral mouth_smile",
    "neutralAway eyes_away_blink brows_neutral mouth_neutral",
    "neutralDown eyes_down_blink brows_neutral mouth_neutral",
    "laugh eyes_laugh brows_raised mouth_laugh",
    "sadDown eyes_down_blink brows_worried mouth_pout"
    ]

    # blink
    image vivian_eyes_center_blink = DynamicBlink(
        "vivian_eyes_center",
        "vivian_eyes_closed"
        )

    image vivian_eyes_down_blink = DynamicBlink(
        "vivian_eyes_down",
        "vivian_eyes_closed"
        )

    image vivian_eyes_away_blink = DynamicBlink(
        "vivian_eyes_away",
        "vivian_eyes_closed"
        )

    layeredimage vivian:
        always "vivian_base"

        attribute blush
        attribute tears

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute neutralAway null
            attribute neutralDown null
            attribute laugh null
            attribute sadDown null

        attribute_function Picker(expressions)

    define sam = Character("Sam")
    ## character sprites

    # blink
    image sam_eyes_center_blink = DynamicBlink(
        "sam_eyes_center",
        "sam_eyes_closed"
        )

    image sam_eyes_down_blink = DynamicBlink(
        "sam_eyes_down",
        "sam_eyes_closed"
        )

    image sam_eyes_away_blink = DynamicBlink(
        "sam_eyes_away",
        "sam_eyes_closed"
        )

    layeredimage sam:
        always "sam_base"

        attribute blush
        attribute tears

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute neutralAway null
            attribute neutralDown null
            attribute laugh null
            attribute sadDown null

        attribute_function Picker(expressions)


    define alex = Character("Alex")
    ## character sprites

    # blink
    image alex_eyes_center_blink = DynamicBlink(
        "alex_eyes_center",
        "alex_eyes_closed"
        )

    image alex_eyes_down_blink = DynamicBlink(
        "alex_eyes_down",
        "alex_eyes_closed"
        )

    image alex_eyes_away_blink = DynamicBlink(
        "alex_eyes_away",
        "alex_eyes_closed"
        )

    layeredimage alex:
        always "alex_base"

        attribute blush
        attribute tears

        group eyes auto prefix "eyes"
        group brows auto prefix "brows"
        group mouth auto prefix "mouth"

        group expressions:
            attribute neutral default null
            attribute smile null
            attribute neutralAway null
            attribute neutralDown null
            attribute laugh null
            attribute sadDown null

        attribute_function Picker(expressions)    



    define aian_position = Position(xpos=0.5, ypos=0.90)  # adjust xpos and ypos as needed
    define aian = Character('Aian')
    ## character sprites
    define aianExpressions = [
        "GRRRRRR GRRRRRR",
        "happyCrying happyCrying",
        "holUP holUP",
        "irritated irritated",
        "kawai kawai",
        "kissy kissy",
        "love love",
        "dead dead",
        "disgusted disgusted",
        "dizzy dizzy",
        "flirty flirty",
        "flushes flushes",
        "grossedOut grossedOut",
        "mimic mimic",
        "notConfident notConfident",
        "omnomnom omnomnom",
        "pissedOff pissedOff",
        "POG POG",
        "readyForCarnage readyForCarnage",
        "realisation realisation",
        "scared scared",
        "smug smug",
        "stupidHappy stupidHappy",
        "thinking thinking",
        "tongue tongue",
        "ughhhh ughhhh",
        "unsure unsure",
        "vicious vicious",
        "almostDead almostDead",
        "confident confident",
        "confused confused",
        "crying crying"
    ]
    
    transform wobble:
        rotate 1.0
        linear 1.0 rotate -1.0
        linear 1.0 rotate 1.0
        repeat

    transform wobble2:
        xpos 0.04
        ypos 0.23
        linear 1.0 ypos 0.25
        linear 1.0 ypos 0.23
        repeat

    layeredimage aian:
        always "aian_base" at wobble
        group expressions:
            attribute GRRRRRR default "aian_GRRRRRR" at wobble2
            attribute happyCrying "aian_happyCrying" at wobble2
            attribute holUP "aian_holUP" at wobble2
            attribute irritated "aian_irritated" at wobble2
            attribute kawai "aian_kawai" at wobble2
            attribute kissy "aian_kissy" at wobble2
            attribute love "aian_love" at wobble2
            attribute dead "aian_dead" at wobble2
            attribute disgusted "aian_disgusted" at wobble2
            attribute dizzy "aian_dizzy" at wobble2
            attribute flirty "aian_flirty" at wobble2
            attribute flushes "aian_flushes" at wobble2
            attribute grossedOut "aian_grossedOut" at wobble2
            attribute mimic "aian_mimic" at wobble2
            attribute notConfident "aian_notConfident" at wobble2
            attribute omnomnom "aian_omnomnom" at wobble2
            attribute pissedOff "aian_pissedOff" at wobble2
            attribute POG "aian_POG" at wobble2
            attribute readyForCarnage "aian_readyForCarnage" at wobble2
            attribute realisation "aian_realisation" at wobble2
            attribute scared "aian_scared" at wobble2
            attribute smug "aian_smug" at wobble2
            attribute stupidHappy "aian_stupidHappy" at wobble2
            attribute thinking "aian_thinking" at wobble2
            attribute tongue "aian_tongue" at wobble2
            attribute ughhhh "aian_ughhhh" at wobble2
            attribute unsure "aian_unsure" at wobble2
            attribute vicious "aian_vicious" at wobble2
            attribute almostDead "aian_almostDead" at wobble2
            attribute confident "aian_confident" at wobble2
            attribute confused "aian_confused" at wobble2
            attribute crying "aian_crying" at wobble2
            
        attribute_function Picker(aianExpressions)



    image bg background_datacenter = "images/bg/bg background_datacenter.png"
    image bg background_desk = "images/bg/bg background_desk.png"
    image bg sam_office = "images/bg/bg sam_office.png"
    image bg player_office = "images/bg/bg player_office.png"
    image bg alex_office = "images/bg/bg alex_office.png"
    image bg ai_lab = "images/bg/bg ai_lab.png"

    ## miscellaneous images
    define parallax_bg_size = (2200, 1237) # needs to be bigger than the screen size (1920, 1080)
    image bg black = Solid('#000', xysize=parallax_bg_size)
    image bg white = Solid('#fff', xysize=parallax_bg_size)

    image effects pool:
        'ripple1'
        pause 1.0
        'ripple2'
        pause 1.0
        repeat

    # XXX: for some reason, not equivalent to image bg pool = Tile('tile pool', size=(2200, 1097 * 2))
    image bg pool = im.Tile('cg/pool/tile pool.png', size=(2200, 1097 * 2))