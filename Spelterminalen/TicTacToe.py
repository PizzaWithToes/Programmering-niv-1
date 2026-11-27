import os
def clear():
    os.system('cls')

inteLedigaPlatser = []
Brädan = ['1','2','3','4','5','6','7','8','9'] 
def displayBoard():
    print(f' ------------')
    print(f'| {Brädan[0]} | {Brädan[1]} | {Brädan[2]} |')
    print(f' ------------')
    print(f'| {Brädan[3]} | {Brädan[4]} | {Brädan[5]} |')
    print(f' ------------')
    print(f'| {Brädan[6]} | {Brädan[7]} | {Brädan[8]} |')
    print(f' ------------')


def play(playerTurn):
    Val = 0
    while True:
        displayBoard()
        if playerTurn == 'X' and Brädan[Val] == 'O' or Brädan[Val] == 'X':
            print('hej')
        Val = int(input(f'Din tur {playerTurn}, skriv ett nummer vart du vill lägga'))
        Val -= 1
        inteLedigaPlatser.append(Val+1)
        Brädan[Val] = playerTurn

        print(inteLedigaPlatser)

        if playerTurn == 'X':
            playerTurn = 'O'
        else: playerTurn = 'X'
    
play('X')