#Detta är spelterminalen, där alla spel jag har skapat importeras in!
#Ifall det är något spel du vill spela, så sker det här.

import TärningsSpel
import HängaGubbe
import os
import TextColor

# clear definition
def clear():
    os.system('cls')

def SpelTerminalStart():
    clear()
    while True:
        Välkommen = input('Välkommen till spelterminalen. Skriv "HJÄLP" för hjälp.').lower()
        if Välkommen == 'hjälp':
            clear()
            print(f'{TextColor.Y}Tillgängliga spel{TextColor.RESET}:\n 1. Tärning Spel\n 2. Hänga Gubbe')
        elif Välkommen == 'tärning spel' or Välkommen == '1':
            clear()
            TärningsSpel.TärningSpel()
        elif Välkommen == 'hänga gubbe' or Välkommen == '2':
            clear()
            HängaGubbe.HängaGubbe()
        else:
            clear()
            print(f'{TextColor.R}Fel kommando, försök igen.{TextColor.RESET}')

SpelTerminalStart()