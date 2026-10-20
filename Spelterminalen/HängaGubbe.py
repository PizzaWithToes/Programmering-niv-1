import random

ord = ['Jag', 'Vet', 'Inte']

randomOrd = random.choice(ord)
print(randomOrd)
buh = list('_')
for x in randomOrd:
    buh.insert('_')
    print(buh)
