ålder = int(input('Hur gammal är du?'))

if ålder == 17:
    print('Du är lika gammal som de flesta i EE25')
else: 
    print('Du är inte lika gammal som de flesta i EE25')

if ålder != 43:
    print('Du är inte lika gammal som Per')
else: 
    print('Du är lika gammal som Per')

if ålder <= 13:
    print('Du är ganska ung')
elif ålder < 18:
    print('Du får inte ta körkort')
elif ålder < 20:
    print('Du får ta körkort')
else:
    print('Du får handla på systembolaget')


namn = input('Vad är ditt namn?')
if namn == 'Linus':
    print('Kung')
elif namn == 'Lajnus':
    print('Så stavar man det inte >:(')
elif namn == 'Linkan':
    print('Close enough')
else:
    print('Ok du är inte Linus')

if ålder == 17 and namn == 'Linus':
    print('Du är Linus')
else:print('Du är definitivt inte Linus')

## test
import random

randomNumber1 = random.randint(0,100)
randomNumber2 = random.randint(0,100)
if randomNumber1 > 50:
    print('Ditt första nummer var', randomNumber1, 'vilket är högre än 50')
else:
    print('Ditt första nummer var', randomNumber1, 'vilket är inte högre än 50')

if randomNumber2 > 50:
    print('Ditt andra nummer var', randomNumber2, 'vilket är högre än 50')
else:
    print('Ditt andra nummer var', randomNumber2, 'vilket är inte högre än 50')

sammanlagt = randomNumber1 + randomNumber2
print('Sammanlagt blir detta', sammanlagt)

if sammanlagt > 175:
    print('Dina två nummer blir mer än 175 när man slår ihop dem')
elif sammanlagt > 150:
    print('Dina två nummer blir mer än 150 när man slår ihop dem')
elif sammanlagt > 125:
    print('Dina två nummer blir mer än 125 när man slår ihop dem')
elif sammanlagt > 100:
    print('Dina två nummer blir mer än 100 när man slår ihop dem')
else:
    print('Dina två nummer blir mindre än 100 när man slår ihop dem')