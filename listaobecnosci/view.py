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
    month = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
             'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

    return zmiana, month[choice]
