def HängaGubbe():
    #imports    
    import random
    import os
    import TextColor
    #variablar
    ordlista = ["python", "programmering", "dator", "utvecklare", "algoritm"]
    hemligtOrd = random.choice(ordlista)
    gissadeBokstäver = []
    felaktigaGissningar = 0
    maxFel = 6

    # clear definition
    def clear():
        os.system('cls')

    clear()
    print(f"{TextColor.LBB}Välkommen till Hänga gubbe!{TextColor.RESET}")

    while felaktigaGissningar < maxFel:
        # Visa ordet med understreck
        visat_ord = ""
        for x in hemligtOrd:
            if x in gissadeBokstäver:
                visat_ord += x + " "
            else:
                visat_ord += f"{TextColor.Y}_ {TextColor.RESET}"

        print("\nOrd: " + visat_ord.strip())
        print(f"\nFelaktiga gissningar kvar: {TextColor.R}{maxFel - felaktigaGissningar}{TextColor.RESET}")

        # Vinnst kondition
        if "_" not in visat_ord:
            print(f"{TextColor.G}Grattis! Du vann!{TextColor.RESET}")
            break

        gissning = input("\nGissa en bokstav: ").lower()
        # Anti cheat
        if len(gissning) != 1 or not gissning.isalpha():
            clear()
            print(f"{TextColor.R}Skriv en enda bokstav.{TextColor.RESET}")
            continue
        # Så att man inte kan gissa på samma bokstav igen :)
        if gissning in gissadeBokstäver:
            clear()
            print(f"{TextColor.R}Du har redan gissat på den bokstaven.{TextColor.RESET}")
            continue

        gissadeBokstäver.append(gissning)
        # Om man gissade rätt eller fel
        if gissning in hemligtOrd:
            clear()
            print(f"{TextColor.G}Rätt! '{gissning}' finns i ordet.{TextColor.RESET}")
        else:
            felaktigaGissningar += 1
            clear()
            print(f"{TextColor.R}Fel! '{gissning}' finns inte i ordet.{TextColor.RESET}")
    # Förlust
    if felaktigaGissningar == maxFel:
        clear()
        print(f"{TextColor.R}\nDu förlorade. Det hemliga ordet var: {hemligtOrd}{TextColor.RESET}")
    # Ifall programmet ska köras om eller inte
    while True:
        Igen = input('Vill du köra igen?(Y/N)').lower()
        if Igen == 'y':
            clear()
            return HängaGubbe()
        elif Igen == 'n':
            clear()
            break
        else:
            clear()
            print(f'{TextColor.R}Förstod inte kommandot.{TextColor.RESET}')
HängaGubbe()