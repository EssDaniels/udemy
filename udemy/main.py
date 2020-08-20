
wynik = 0
i = 0

while i < 3:
    x = int(input("Podaj liczbę dodatnią i jednocześnie parzystą: "))
    if x > 0:
        if x % 2 == 0:
            wynik += x
            print("Aktualny wynik: ", wynik)
            i += 1
    else:
        continue


