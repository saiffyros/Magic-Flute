define e = Character("Narrator")

image outside:
    "g2.png"
    pause 0.2
    "g3.png"
    pause 0.2
    "g4.png"
    pause 0.2
    "g5.png"
    pause 0.2
    "g4.png"
    pause 0.2
    "g3.png"
    pause 0.2
    "g2.png"
    pause 0.2
    repeat

transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 10 rotate 360
    repeat

image car:
    "car_06.png"
    pause 0.28
    "car_05.png"
    pause 0.28
    "car_04.png"
    pause 0.28
    repeat

image road:
    "a20a.png"
    subpixel True
    xalign 0.0
    linear 1.0 xalign 1.0
    repeat

image road2:
    "a20.png"
    subpixel True
    yalign 1.0 xalign 1.0
    linear 1.0 xalign 0.0 yalign 0.0
    repeat

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

# label main_menu:
#     return

label start:

    show room1

    $ say("João", "Vamos testar isso aqui", .8, .2, 5)
    $ say("Sara", "Eu sou um balão", .2, .8, 5)
    $ say("", "Olha aqui!!!!!")

    show screen overlay1

    $ say("João", "Vamos testar isso aqui", .8, .2, 5)
    $ say("Sara", "Eu sou um balão", .2, .8, 5)
    $ say("", "Olha aqui!!!!!")

    show screen overlay2

    $ say("João", "Vamos testar isso aqui", .8, .2, 5)
    $ say("Sara", "Eu sou um balão", .2, .8, 5)
    $ say("", "Olha aqui!!!!!")

    show screen overlay3 with dissolve

    $ say("João", "Vamos testar isso aqui", .8, .2, 5)
    $ say("Sara", "Eu sou um balão", .2, .8, 5)
    $ say("", "Olha aqui!!!!!")

    jump start2

label start2:
    hide screen overlay1 with dissolve
    hide screen overlay2 with dissolve
    hide screen overlay3 with dissolve

    show background1:
        subpixel True
        xalign 1.0
        linear 3.0 xalign 0.0

    $ say("João", "Vamos testar isso aqui", .8, .2, 5)
    $ say("Sara", "Eu sou um balão", .2, .8, 5)
    $ say("", "Olha aqui!!!!!")

    jump start3

label start3:
    show outside with dissolve
    pause 7.0
    $ say("João", "Vamos testar isso aqui", .8, .2, 5)
    show g6 with dissolve
    pause 5.0
    $ say("João", "Vamos testar isso aqui", .8, .2, 5)

    show a22a:
        xalign 0.0

    show road
    show car
    $ say("João", "Vamos testar isso aqui", .8, .2, 5)

    show a22a:
        subpixel True
        xalign 0.0
        linear 2.0 xalign 1.0
    hide road
    pause 1.5
    hide car
    show car_04

    $ say("João", "Vamos testar isso aqui", .8, .2, 5)

    show a21 with dissolve
    pause 1.0
    show a21a with dissolve
    pause 1.0
    show a21b with dissolve
    pause 1.0
    show a21c with dissolve
    play sound "audio/door.mp3"
    pause 0.5
    show black_background with dissolve
    pause 5.0

    call screen input_screen()

    ""
    return

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

screen input_screen():
    window:
        has vbox

        text "Enter your name."
        input default ""

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


screen main_menu():


    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    add "main_menu.png" #IMAGEM VAI AQUI

    # The main menu buttons.
    frame:
        style_prefix "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

style mm_button:
    size_group "mm"
