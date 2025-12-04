let usuari = 0
let mostrant_resultat = false
let maquina = 0
input.onButtonPressed(Button.A, function () {
    if (usuari < 2) {
        usuari += 1
    } else {
        usuari = 0
    }
})
input.onButtonPressed(Button.B, function () {
    mostrant_resultat = true
    maquina = randint(0, 2)
    basic.showString("-")
    basic.pause(200)
    if (maquina == 0) {
        basic.showIcon(IconNames.Target)
    } else if (maquina == 1) {
        basic.showIcon(IconNames.Square)
    } else if (maquina == 2) {
        basic.showIcon(IconNames.Scissors)
    }
    basic.pause(1000)
    if (maquina == usuari) {
        basic.showString("Empat")
    } else if (maquina == 0 && usuari == 1 || maquina == 1 && usuari == 2 || maquina == 2 && usuari == 0) {
        basic.showString("Usuari guanya")
    } else {
        basic.showString("IA guanya")
    }
    mostrant_resultat = false
})
basic.forever(function () {
    if (!(mostrant_resultat)) {
        if (usuari == 0) {
            basic.showIcon(IconNames.Target)
        } else if (usuari == 1) {
            basic.showIcon(IconNames.Square)
        } else if (usuari == 2) {
            basic.showIcon(IconNames.Scissors)
        }
    }
})
