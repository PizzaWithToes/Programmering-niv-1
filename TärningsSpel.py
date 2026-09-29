def TärningSpel():
    #imports
    import random
    import TextColor
    #variablar
    Total = int(0)
    Försök = int(5)
    Målet = int(50) 
    print(f'TIPS: Du kan skriva {TextColor.Y}EXIT{TextColor.RESET} för att avsluta spelet tidigt!')
    #loop
    while True:
        hej = input(f'{TextColor.BB}{TextColor.LB}Tryck på ENTER för att slå tärningen{TextColor.RESET}\n')
        #ifall spelaren skriver EXIT, avsluta spelet tidigt
        if hej == 'EXIT':
            break
        #här sker allting i spelet
        Försök -= 1
        randomNumber = random.randint(1,20)
        Total += randomNumber
        #här säger programmet vad som har hänt till spelaren
        print(f'Du har {TextColor.R}{Försök}{TextColor.RESET} försök kvar.\n')
        print(f'Du rullade {TextColor.Y}{randomNumber}{TextColor.RESET}. Totalt ligger du på {TextColor.G}{Total}{TextColor.RESET}.\n')
        # här säger programmet hur mycket som är kvar tills spelaren vinner
        Kvar = Målet - Total
        if Kvar > 1:
            print(f'Bara {TextColor.B}{Kvar}{TextColor.RESET} kvar!\n')
        elif Kvar <= 0:
            print(f'Bara 0 kvar!')
        #spelaren har vunnit!
        if Total >= Målet:
            print(f'{TextColor.G}Du vann!{TextColor.RESET}')
            break
        #spelaren har förlorat
        elif Försök < 1:
            print(f'{TextColor.R}Du förlorade{TextColor.RESET}')
            break
    #ifall programmet ska köras om eller inte
    while True:
        Igen = input('Vill du köra igen?(Y/N)')
        if Igen == 'Y':
            return TärningSpel()
        elif Igen == 'N':
            print('ok!')
            break
        else:
            print('Förstod inte kommandot. Se till att använda stor bokstav!')