import TärningsSpel
def SpelTerminalStart():
    while True:
        Välkommen = input('Välkommen till spelterminalen. Skriv "HJÄLP" för hjälp.')
        if Välkommen == 'HJÄLP':
            print('Lista av kommandon:\n 1. Tärnings Spel')
        elif Välkommen == 'TärningSpel':
            print('ok!')
            TärningsSpel.TärningSpel()
        elif Välkommen == 'EXIT':
            break

SpelTerminalStart()