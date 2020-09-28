"""
from math import ceil

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from tableWorkersInPdf import genPinTable
"""
from functions import AttendanceList
from view import view_menu

miesiac = view_menu()
lista = AttendanceList.loadDateShort("lista_pracownikow.xlsx", miesiac[0], miesiac[1])

listaKobiet = []
listaKobiet = lista[0]
a = AttendanceList.generatorList(listaKobiet, lista[2], miesiac)
"""
for t in range(1, ceil(len(listaKobiet) / 3) + 1):
    print(ceil(len(listaKobiet) / 3))

    try:

        menList = genPinTable(listaKobiet[0], listaKobiet[1], listaKobiet[2], lista[2], miesiac[1], t, miesiac[2],
                              miesiac[3])
        fileName = 'listaobecnosci' + str(miesiac[0]) + str(t) + '.pdf'
        pdf = SimpleDocTemplate(fileName, pagesize=letter, bottomMargin=0, topMargin=5, rightMargin=0, leftMargin=0)
        elems = []
        elems.append(menList)
        pdf.build(elems)
    except IndexError:
        if len(listaKobiet) == 1:
            listaKobiet.append("")
            listaKobiet.append("")
            menList = genPinTable(listaKobiet[0], listaKobiet[1], listaKobiet[2], lista[2], miesiac[1], t, miesiac[2],
                                  miesiac[3])
            fileName = 'listaobecnosci' + str(miesiac[0]) + str(t) + '.pdf'
            pdf = SimpleDocTemplate(fileName, pagesize=letter, bottomMargin=0, topMargin=5, rightMargin=0, leftMargin=0)
            elems = []
            elems.append(menList)
            pdf.build(elems)
            listaKobiet.clear()

            continue
        else:
            listaKobiet.append("")
            menList = genPinTable(listaKobiet[0], listaKobiet[1], listaKobiet[2], lista[2], miesiac[1], t, miesiac[2],
                                  miesiac[3])
            fileName = 'listaobecnosci' + str(miesiac[0]) + str(t) + '.pdf'
            pdf = SimpleDocTemplate(fileName, pagesize=letter, bottomMargin=0, topMargin=5, rightMargin=0, leftMargin=0)
            elems = []
            elems.append(menList)
            pdf.build(elems)
            listaKobiet.clear()
            continue

    for _ in range(3):
        del listaKobiet[0]
        
"""
