#Detta är spelterminalen, där alla spel jag har skapat importeras in!
#Ifall det är något spel du vill spela, så sker det här.

import TärningsSpel
import os
import TextColor
def SpelTerminalStart():
    os.system('cls')
    while True:
        Välkommen = input('Välkommen till spelterminalen. Skriv "HJÄLP" för hjälp.').lower()
        if Välkommen == 'hjälp':
            os.system('cls')
            print(f'{TextColor.Y}Tillgängliga spel{TextColor.RESET}:\n 1. Tärning Spel')
        elif Välkommen == 'tärning spel':
            os.system('cls')
            TärningsSpel.TärningSpel()
        else:
            os.system('cls')
            print(f'{TextColor.R}Fel kommando, försök igen.{TextColor.RESET}')

SpelTerminalStart()