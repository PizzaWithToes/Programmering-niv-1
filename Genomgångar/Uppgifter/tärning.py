import random  

randomNumber = random.randint(1,10)
randomNumber2 = random.randint(1,10)

print(f'du rullade {randomNumber}')
print(f'din motståndare rullade {randomNumber2}')

if randomNumber > randomNumber2:
    print('Du vann')
else:
    print('Du förlorade')
