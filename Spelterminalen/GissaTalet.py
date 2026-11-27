def GissaTalet():
    import random
    import os
    def clear():
        os.system('cls')
    Talet = random.randint(1,100)
    antalFörsök = 0
    maxFörsök = 5
    clear()

    while True:
        gissning = int(input('ange ett tal: '))
        clear()
        antalFörsök += 1
        print(antalFörsök)
        if not gissning.is_integer():
            print('SLUTA')
            continue
        if gissning > Talet:
            print('lägre')
        elif gissning < Talet:
            print('högre')
        elif gissning == Talet:
            print('du vann')
            break
            

GissaTalet()