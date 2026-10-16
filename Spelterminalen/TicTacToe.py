Brädan = ['1','2','3','4','5','6','7','8','9'] 
def displayBoard():
    print(f' ------------')
    print(f'| {Brädan[0]} | {Brädan[1]} | {Brädan[2]} |')
    print(f' ------------')
    print(f'| {Brädan[3]} | {Brädan[4]} | {Brädan[5]} |')
    print(f' ------------')
    print(f'| {Brädan[6]} | {Brädan[7]} | {Brädan[8]} |')
    print(f' ------------')

while True:
    displayBoard()
    Val = input('Din tur, skriv ett nummer vart du vill lägga')