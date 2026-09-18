import random

Total = int(0)
Försök = int(5)
Målet = int(50)
while True:
    input('Slå tärningen')
    Försök -= 1
    randomNumber = random.randint(1,20)
    Total += randomNumber
    print(f'Du har {Försök} försök kvar.')
    print(f'Du rullade {randomNumber}. Totalt ligger du på {Total}.')
    Kvar = Målet - Total
    print('Bara', Kvar,'kvar!')
    if Total > Målet:
        print('Du vann!')
        break
    elif Försök < 1:
        print('Du förlorade')
        break

