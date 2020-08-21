def wiadomosci_powitalna(imie):
    print("Cześć", imie , ". Co dzisiaj robisz?")


imiona = ["Dawidzie", "Klaudio"]


for imie in imiona:
    wiadomosci_powitalna(imie)

def pole_prostokata(bok_a, bok_b):
    return bok_a*bok_b

pole = pole_prostokata(2,4)

print(pole)

