from math import pi

def pole_prostokata(bok_a, bok_b):
    return bok_b*bok_a


def pole_kwadratu(bok_a):
    return bok_a*bok_a

def pole_trojkata(podstawa, wysokosc):
    return podstawa*wysokosc/2

def pole_trapezu(bok_a, bok_b,h):
    return (bok_a+bok_b)*h/2

def pole_kola(r):
    return pi*r**2

while True:

    print("Pole:")
    print("1. Prostokąta")
    print("2. Kwadratu")
    print("3. Trójkąta")
    print("4. Trapezu")
    print("5. Koła")
    print("6. Zakończ program")
    wybor = int(input("Co chcesz obliczyć? Podaj index wyboru. "))

    if (wybor == 1 ):
        a = float(input("Podaj długość boku a "))
        b = float(input("Podaj długość boku b "))
        wynik = pole_prostokata(a, b)
        print("Pole wynosi:", wynik)

    if (wybor == 2 ):
        a = float(input("Podaj długość boku a "))

        wynik = pole_kwadratu(a)
        print("Pole wynosi:", wynik)

    if (wybor == 3 ):
        a = float(input("Podaj długość podstawy "))
        b = float(input("Podaj wysokosc "))
        wynik = pole_trojkata(a, b)
        print("Pole wynosi:", wynik)

    if (wybor == 4 ):
        a = float(input("Podaj długość podstawy "))
        b = float(input("Podaj długość drugiej podstawy "))
        h = float(input("Podaj wysokosc "))
        wynik = pole_trapezu(a, b, h)
        print("Pole wynosi:", wynik)

    if (wybor == 5 ):
        a = float(input("Podaj promień koła "))

        wynik = pole_kola(a)
        print("Pole wynosi:", wynik)

    if (wybor == 6 ):
        break
