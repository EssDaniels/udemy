from figury import *
from enum import IntEnum


Menu_Figury = IntEnum('Menu_Figury', "Prostokat Kwadrat Trojkat Trapez Kolo Exit")

while True:


    wybor = int(input(
    """Co chcesz obliczyć? Podaj index wyboru. 
    1. Prostokąta
    2. Kwadratu
    3. Trójkąta
    4. Trapezu
    5. Koła
    6. Zakończ program
    
    """))

    if (wybor == Menu_Figury.Prostokat):
        a = float(input("Podaj długość boku a "))
        b = float(input("Podaj długość boku b "))
        wynik = pole_prostokata(a, b)
        print("Pole wynosi:", wynik)

    if (wybor == Menu_Figury.Kwadrat ):
        a = float(input("Podaj długość boku a "))

        wynik = pole_kwadratu(a)
        print("Pole wynosi:", wynik)

    if (wybor == Menu_Figury.Trojkat ):
        a = float(input("Podaj długość podstawy "))
        b = float(input("Podaj wysokosc "))
        wynik = pole_trojkata(a, b)
        print("Pole wynosi:", wynik)

    if (wybor == Menu_Figury.Trapez):
        a = float(input("Podaj długość podstawy "))
        b = float(input("Podaj długość drugiej podstawy "))
        h = float(input("Podaj wysokosc "))
        wynik = pole_trapezu(a, b, h)
        print("Pole wynosi:", wynik)

    if (wybor == Menu_Figury.Kolo):
        a = float(input("Podaj promień koła "))

        wynik = pole_kola(a)
        print("Pole wynosi:", wynik)

    if (wybor == Menu_Figury.Exit ):
        break
