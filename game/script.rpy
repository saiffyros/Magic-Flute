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

    DEFAULT_N = ""
    DEFAULT_T = ""
    DEFAULT_X = .5
    DEFAULT_Y = .5
    DEFAULT_S = 1

    def say(character = DEFAULT_N, texting = DEFAULT_T, posx = DEFAULT_X, posy = DEFAULT_Y, sec = DEFAULT_S):
        renpy.call_screen("balloon", character, texting, posx, posy)
        renpy.pause(sec)
        #renpy.hide_screen("balloon")

# label main_menu:
#     return

label start:

    show room1

    $ say("Jonas", "Um homem que não traz consigo uma imagem futura de si mesmo,\n ainda que opaca e confusa é tão monstruoso quanto um homem sem nariz.", .3, .8)
    $ say("Mauro", "E o que isso quer dizer?", .6, .35)
    $ say("Jonas", "Exatamente o que diz. Você entende o que eu quero dizer?", .45, .8)
    $ say("Mauro", "Sim, mas...", .6, .35)
    $ say("Jonas", "Mas você quer saber minha interpretação.", .45, .8)
    $ say("Mauro", "Estamos aqui pra compreender melhor \ncomo você vê o mundo.", .6, .35)
    $ say("Jonas", "...", .7, .8)
    $ say("Mauro", "Certo?", .6, .35)

    show screen overlay1

    $ say("Jonas", "É uma sensação de que algo está errado. \nsem saber precisar o que.", .99, .35)
    $ say("Jonas", "Mas eu sinto em toda esquina.", .9, .35)
    $ say("Jonas", "O cheiro das pessoas, o cheiro de cigarro,\n os olhares... tudo isso me incomoda.", .99, .35)
    $ say("Jonas", "Mas tem algo ainda pior.", .9, .35)
    $ say("Jonas", "Muito mais.", .9, .35)
    $ say("Mauro", "E o que é?", .4, .3)
    $ say("Jonas", "Há nas pessoas um desejo que ofende meu olfato.", .99, .35)
    $ say("Jonas", "Ao sair lá fora eu só vejo almas penadas,\n agarradas à fagulhas de felicidade e prazer.", .99, .35)
    $ say("Jonas", "Isso é tudo que conseguem.", .9, .35)
    $ say("Jonas", "Ninguém inspira respeito de verdade.", .9, .35)
    $ say("Mauro", "E apesar de tudo isso \nvocê não se compadece?\n Não pensa algo como....", .2, .35)
    $ say("Mauro", "Aí está, mais um ser humano tentando.", .4, .35)
    $ say("Jonas", "Tentando o que?", .9, .35)
    $ say("Mauro", "O que você acha?", .4, .35)
    $ say("Jonas", "Tentando...", .9, .35)
    $ say("Mauro", "Tentando o que Jonas?", .4, .35)

    show screen overlay2

    $ say("Jonas", "Tentando suportar o tormento que é \nestar preso a este mundo sujo.", .2, .9)
    $ say("Jonas", "Que nós mesmos criamos.", .2, .9)
    $ say("Mauro", "E no entanto você tem pena deles.", .4, .1)
    $ say("Jonas", "Ou será que é pena de mim mesmo \no que eu sinto?", .2, .9)
    $ say("Jonas", "Enfim...", .2, .9)
    $ say("Jonas", "Será que você pode me dar algum \noutro remédio?", .2, .9)

    show screen overlay3 with dissolve

    $ say("Mauro", "Podemos ver esta possibilidade\n na próxima consulta.", .4, .1)
    $ say("Mauro", "Aconteceu algo no trabalho?", .4, .1)
    $ say("Mauro", "Parece mais afetado do que de costume.", .4, .1)
    $ say("Jonas", "Nada digno de nota.", .2, .9)
    $ say("Mauro", "Continue mantendo o seu diário.", .4, .1)
    $ say("Mauro", "Vamos voltar a ele na próxima seção.", .4, .1)
    $ say("Jonas", "Ok...", .2, .9)

    jump start2

label start2:
    hide screen overlay1 with dissolve
    hide screen overlay2 with dissolve
    hide screen overlay3 with dissolve

    show background1:
        subpixel True
        xalign 1.0
        linear 3.0 xalign 0.0

    $ renpy.pause(3)

    $ say("Jonas", "Podemos ver esta possibilidade\n na próxima consulta.", .3, .1, 2.5)
    $ say("Jonas", "O que você acha Jonas?", .35, .25)
    $ say("Jonas", "O que está pensando Jonas?", .5, .35)
    $ say("Jonas", "Palhaço.", .7, .35)

    jump start3

label start3:
    show outside with dissolve
    $ say("Jonas", "Um homem que não traz consigo uma imagem futura de si mesmo,\n ainda que opaca e confusa é tão monstruoso quanto um homem sem nariz.", .7, .4)
    $ say("Jonas", "É óbvio que estou falando da ausência de\n planos e objetivos claros para o futuro.", .8, .2)
    show g6 with dissolve
    $ say("Jonas", "E ainda pago pra ouvir isso.", .8, .2)
    $ say("Jonas", "Vou ter que apagar o escrevi dele no diário.", .8, .2)

    show a22a:
        xalign 0.0

    play music "audio/ha_tempos.mp3"
    $ renpy.music.set_volume(0.05, .05, channel="music")

    show road
    show car

    $ say("", "Parece cocaína", .8, .2)
    $ say("", "Mas é só tristeza", .4, .2)
    $ say("", "Talvez tua cidade", .8, .2)
    $ say("", "Muitos temores nascem", .4, .2)
    $ say("", "Do cansaço e da solidão", .8, .2)
    $ say("", "Descompasso, desperdício", .4, .2)

    show a22a:
        subpixel True
        xalign 0.0
        linear 2.0 xalign 1.0
    stop music fadeout 3.0
    hide road
    pause 1.5
    hide car
    show car_04

    $ say("Jonas", "Uma igreja...", .8, .2)
    $ say("Jonas", "Igrejas são túmulos de Deus...", .8, .2)
    $ say("Jonas", "E no entanto, aqui estou.", .8, .2)
    $ say("Jonas", "Compelido a entrar.", .8, .2)
    $ say("Jonas", "Bem, não custa nada tentar.", .8, .2)

    show a21 with dissolve
    $ renpy.pause(1)
    show a21a with dissolve
    $ renpy.pause(1)
    show a21b with dissolve
    $ renpy.pause(1)
    show a21c with dissolve
    play sound "audio/door.mp3"
    $ renpy.pause(.5)
    show black_background with dissolve
    $ renpy.pause(5)

    ""

    call screen input_screen()

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

    key "mousedown_1" action Return()

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
