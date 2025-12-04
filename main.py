usuari = 0
maquina = 0
mostrant_resultat = False

def on_button_pressed_a():
    global usuari
    if usuari < 2:
        usuari += 1
    else:
        usuari = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global maquina, mostrant_resultat
    mostrant_resultat = True
    maquina = randint(0, 2)
    basic.show_string("-")
    if maquina == 0:
        basic.show_icon(IconNames.TARGET)
    elif maquina == 1:
        basic.show_icon(IconNames.SQUARE)
    elif maquina == 2:
        basic.show_icon(IconNames.SCISSORS)
    
    basic.pause(1000)
    if maquina == usuari:
        basic.show_string("Empat")
    elif maquina == 0 and usuari == 1 or maquina == 1 and usuari == 2 or maquina == 2 and usuari == 0:
        basic.show_string("Usuari guanya")
    else:
        basic.show_string("IA guanya")
    
    mostrant_resultat = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if not mostrant_resultat:
        if usuari == 0:
            basic.show_icon(IconNames.TARGET)
        elif usuari == 1:
            basic.show_icon(IconNames.SQUARE)
        elif usuari == 2:
            basic.show_icon(IconNames.SCISSORS)
basic.forever(on_forever)
