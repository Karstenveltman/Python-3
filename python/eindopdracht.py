def readfile():
    with open("filenaam.txt") as f:
      bestandsdata = f.read().split('\n')

    dictionary = {}

    for item in bestandsdata:
        if not item == '':
            woord1, woord2 = item.split("=")
            dictionary[woord1] = woord2
    return dictionary

allenamen = readfile()

def menu():
    print("Dit is een test om te kijken wat populairder is, kat of hond.")
    menu.naam = str(input("voer hier je naam in: "))



def verwerken():
    allenamen[menu.naam] = ""



def keuze():
    kies = str(input("\nkies kat of hond: "))
    if kies == "hond":
        print("minder goeie keuze")
        return "hond"
    elif kies == "kat":
        print("goeie keuze")
        return "kat"
    while kies != "hond" and "kat":
        kies = str(input("\nkies kat of hond: "))
        if kies == "hond":
            print("minder goeie keuze")
            return "hond"
        elif kies == "kat":
            print("goeie keuze")
            return "kat"
        


def addtofilehond(newkey):
    with open('filenaam.txt', 'a') as f:
        f.write(newkey + "=" + "hond" + "\n")

def addtofilekat(newkey):
    with open('filenaam.txt', 'a') as f:
        f.write(newkey + "=" + "kat" + "\n")

menu()
verwerken()
a = keuze()

if a == "hond":
    addtofilehond(menu.naam)
    
elif a == "kat":
    addtofilekat(menu.naam)






    



