import random

ordlista = ["python", "programmering", "dator", "utvecklare", "algoritm"]
hemligtOrd = random.choice(ordlista)
gissadeBokstäver = []
felaktigaGissningar = 0
maxFel = 6

print("Välkommen till Hänga gubbe!")

while felaktigaGissningar < maxFel:
    # Visa ordet med understreck
    visat_ord = ""
    for x in hemligtOrd:
        if x in gissadeBokstäver:
            visat_ord += x + " "
        else:
            visat_ord += "_ "

    print("\nOrd: " + visat_ord.strip())
    print(f"Felaktiga gissningar kvar: {maxFel - felaktigaGissningar}")

    # Vinnst kondition
    if "_" not in visat_ord:
        print("Grattis! Du vann!")
        break

    gissning = input("Gissa en bokstav: ").lower()

    if len(gissning) != 1 or not gissning.isalpha():
        print("Skriv en enda bokstav.")
        continue
    
    gissadeBokstäver.append(gissning)

    if gissning in hemligtOrd:
        print(f"Rätt! '{gissning}' finns i ordet.")
    else:
        felaktigaGissningar += 1
        print(f"Fel! '{gissning}' finns inte i ordet.")

if felaktigaGissningar == maxFel:
    print(f"\nDu förlorade. Det hemliga ordet var: {hemligtOrd}")
