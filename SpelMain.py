#Detta är spelterminalen, där alla spel jag har skapat importeras in!
#Ifall det är något spel du vill spela, så sker det här.

import TärningsSpel
def SpelTerminalStart():
    while True:
        Välkommen = input('Välkommen till spelterminalen. Skriv "HJÄLP" för hjälp.')
        if Välkommen == 'HJÄLP':
            print('Tillgängliga spel:\n 1. Tärning Spel')
        elif Välkommen == 'Tärning Spel':
            print('ok!')
            TärningsSpel.TärningSpel()
        else:
            print('Fel kommando, försök igen.')

SpelTerminalStart()