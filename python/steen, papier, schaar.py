speler1 = input("Speler1 geef je naam: ")
speler2 = input("Speler2 geef je naam: ")

while True:
  keuze1 = input(speler1 + " kies uit steen, papier of schaar: ")
  keuze2 = input(speler2 + " kies uit steen, papier of schaar: ")

  if keuze1 == keuze2:
    print("het is Gelijkspel!")
  
  elif keuze1 == "schaar"and keuze2 == "papier":
    print(speler1 + " wint!")
    break
  elif keuze1 == "schaar" and keuze2 == "steen":
    print(speler2 = " wint!")
    break
    
  elif keuze1 == "papier" and keuze2 == "steen":
    print(speler1 + " wint!")
    break
  elif keuze1 == "papier" and keuze2 == "schaar":
    print(speler2 + " wint!")
    break

  elif keuze1 == "steen" and keuze2 == "schaar":
    print(speler1 + " wint!")
    break
  elif keuze1 == "steen" and keuze2 == "papier": 
    print(speler2 + " wint!")
    break

  else:
    print("daar kunnen jullie niet uit kiezen")
  
