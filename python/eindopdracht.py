def readfile():
    with open("filenaam.txt") as f:
      bestandsdata = f.read().split('\n')

    dictionary = {}

    for item in bestandsdata:
        if not item == '':
            woord1, woord2 = item.split("=")
            dictionary[woord1] = woord2
    return dictionary

print(readfile())

def menu():
    print("Dit is een test om te kijken wat populairder is, kat of hond.")
    menu.naam = str(input("voer hier je naam in: "))

menu()

def verwerken():
    allenamen[menu.naam] = ""

verwerken()

def keuze():
    kies = str(input("\nkies kat of hond: "))
    if kies == "hond":
        print("minder goeie keuze")
        return "hond"
    elif kies == "kat":
        print("goeie keuze")
        return "kat"
    else:
        keuze()



a = keuze()    
if a == "hond":
    allenamen[menu.naam] = "hond"
    
elif a == "kat":
    allenamen[menu.naam] = "kat"



    



