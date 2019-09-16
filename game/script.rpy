

define e = Character("Narrator")

image room1:
    "renatoExample_Animation03.png"
    pause 0.28
    "renatoExample_Animation04.png"
    pause 0.28
    "renatoExample_Animation05.png"
    pause 0.28
    "renatoExample_Animation06.png"
    pause 0.28
    "renatoExample_Animation05a.png"
    pause 0.28
    "renatoExample_Animation04a.png"
    pause 0.28
    repeat

image fishRotating:
    "fishBackgrouding_06.png"
    pause 0.28
    "fishBackgrouding_07.png"
    pause 0.28
    "fishBackgrouding_08.png"
    pause 0.28
    "fishBackgrouding_09.png"
    pause 0.28
    "fishBackgrouding_10.png"
    pause 0.28
    "fishBackgrouding_11.png"
    pause 0.28
    "fishBackgrouding_12.png"
    pause 0.28
    "fishBackgrouding_13.png"
    pause 0.28
    repeat
image background1 = "background.png"

init python:

    DEFAULT_X = .5
    DEFAULT_Y = .5
    DEFAULT_S = 6
    DEFAULT_N = ""
    DEFAULT_T = ""

    def say(character = DEFAULT_N, texting = DEFAULT_T, posx = DEFAULT_X, posy = DEFAULT_Y, sec = DEFAULT_S):
        renpy.show_screen("balloon", character, texting, posx, posy)
        renpy.pause(sec)
        renpy.hide_screen("balloon")

label start:

    show room1

    $ say("John", "Hello, let's test this feature", .8, .2, 5)
    $ say("Sara", "Hello, How are you?", .2, .8, 5)
    $ say("", "Talk to me!!!!!")

    show screen overlay1

    $ say("John", "Hello, let's test this feature", .8, .2, 5)
    $ say("Sara", "Hello, How are you?", .2, .8, 5)
    $ say("", "Talk to me!!!!!")

    show screen overlay2

    $ say("John", "Hello, let's test this feature", .8, .2, 5)
    $ say("Sara", "Hello, How are you?", .2, .8, 5)
    $ say("", "Talk to me!!!!!")

    show screen overlay3 with dissolve


    $ say("John", "Hello, let's test this feature", .8, .2, 5)
    $ say("Sara", "Hello, How are you?", .2, .8, 5)
    $ say("", "Talk to me!!!!!")

    jump start2

label start2:
    hide screen overlay1 with dissolve
    hide screen overlay2 with dissolve
    hide screen overlay3 with dissolve

    show background1:
        subpixel True
        xalign 1.0
        linear 4.0 xalign 0.0

    pause 4.0

    $ say("John", "Hello, let's test this feature", .8, .2, 5)
    $ say("Sara", "Hello, How are you?", .2, .8, 5)
    $ say("", "Talk to me!!!!!")



screen balloon(text1, text2, posx1, posy1):

    vbox:
        xalign posx1
        yalign posy1
        if text1 != "":
            frame:
                xalign posx1 + 0.01
                text text1
        frame:
            text text2
            xpadding 15
            ypadding 15

    key "mousedown_1" action Hide("balloon")

################################################################

screen overlay1:
    add "overlay1.png":
        xalign .75
        yalign .5

screen overlay2:
    add "overlay2.png":
        xalign .05
        yalign .5

    add "fishRotating":
        xalign .05
        yalign .5

screen overlay3:
    add "overlay2a.png":
        xalign .05
        yalign .5

    add "fishRotating":
        xalign .05
        yalign .5
