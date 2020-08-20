szukanaLiczba = 12
x = 0


while 1:

    if szukanaLiczba == x:
        print("Gratuluję, udało się, szukana liczba to:", x)
        break
    else:
        x = int(input("Podaj szukaną liczbę: "))
        if x > szukanaLiczba:
            print("Zbyt wysoka liczba!")
        elif x < szukanaLiczba:
            print("Zbyt niska liczba")