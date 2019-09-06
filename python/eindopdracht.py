def menu():
    print("dit is een test om te kijken welk cijfer meer gekozen word\nkies 1 of 2 asjeblieft")
    menu.keuze = input("wat kies je: ")


menu()

def keuzeverwerken():
    if str.isdigit(menu.keuze) == True:
        if menu.keuze == "1":
            print("je hebt functie 1 gekozen")
        elif menu.keuze == "2":
            print("je hebt functie 2 gekozen")
    else:
        print("kies 1 of 2")

keuzeverwerken()
