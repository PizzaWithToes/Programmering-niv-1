import time
import math

x = 1
#Utskrift av alla tal mellan 1 och 10
while x <= 10:
    print(x)
    x += 1
    if x > 10:
        print('klart')
        break
#Utskrift av jämna tal

k = 0
while k < 10:
    k += 1
    if k%2 != 0:
        continue
    print(k)
    if k == 10:
        print('klart')

#Beräkning av summan 1+2+3+ .. n+
while True:
    n = int(input('n?, skriv ett tal mindre än eller lika med 0 för att avsluta:'))
    start = time.time()
    
    if n <= 0:
        break

    summa = 0
    l = 1

    while l <= n:
        summa += l
        l += 1
    
    slut = time.time()

    print(f'Summan blir {summa}. Det tog {round(slut - start)} sekunder att räkna ut')