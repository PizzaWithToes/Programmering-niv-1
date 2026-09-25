def TärningSpel():
    import random
    import TextColor
    Total = int(0)
    Försök = int(5)
    Målet = int(50) 
    while True:
        input(f'{TextColor.BB}{TextColor.LB}Slå tärningen{TextColor.RESET}\n')
        Försök -= 1
        randomNumber = random.randint(1,20)
        Total += randomNumber
        print(f'Du har {TextColor.R}{Försök}{TextColor.RESET} försök kvar.\n')
        print(f'Du rullade {TextColor.Y}{randomNumber}{TextColor.RESET} . Totalt ligger du på {TextColor.G}{Total}{TextColor.RESET}.\n')
        Kvar = Målet - Total
        if Kvar > 1:
            print(f'Bara {TextColor.B}{Kvar}{TextColor.RESET} kvar!\n')
        elif Kvar <= 0:
            print(f'Bara 0 kvar!')
        if Total >= Målet:
            print(f'{TextColor.G}Du vann!{TextColor.RESET}')
            break
        elif Försök < 1:
            print(f'{TextColor.R}Du förlorade{TextColor.RESET}')
            break
    Igen = input('Vill du köra igen?(Y/N)')
    if Igen == 'Y':
        return TärningSpel()
    elif Igen == 'N':
        print('ok!')

TärningSpel()