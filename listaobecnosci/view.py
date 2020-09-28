def view_menu():
    zmiana = input("""Która zmiana? 
    1. Dred
    2. Lukas Opielski
    Podaj nr i wciśnij ENTER
    """)
    choice = input("""Na jakie miesiąc? 
    1. Styczeń
    2. Luty
    3. Marzec
    4. Kwieceń
    5. Maj
    6. Czerwiec
    7. Lipiec
    8. Sierpień
    9. Wrzesień
    10. Pażdziernik
    11. Listopad
    12. Grudzień
    
    Podaj nr i wciśnij ENTER
    
    """)
    choice = int(choice) - 1
    month = [['styczeń', 31, ], ['luty', 28], ['marzec', 31], ['kwiecień', 30],
             ['maj', 31], ['czerwiec', 30], ['lipiec', 31], ['sierpień', 31],
             ['wrzesień', 30], ['październik', 31], ['listopad', 30],
             ['grudzień', 31]]

    return zmiana, month[choice][0], month[choice][1], choice
