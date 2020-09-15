from listaobecnosci import AttendanceList
from listaobecnoscipdf import genPinTable
from view import view_menu
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from math import ceil

miesiac = view_menu()
lista = AttendanceList.loadDateShort("lista_pracownikow.xlsx", miesiac[0], miesiac[1])
listaKobiet = []
listaKobiet = lista[0]


for t in range(1, ceil(len(listaKobiet) / 3) + 1):
    print(ceil(len(listaKobiet) / 3))

    try:

        menList = genPinTable(listaKobiet[0], listaKobiet[1], listaKobiet[2], lista[2], miesiac[1], t)
        fileName = 'listaobecnosci' + str(miesiac[0]) + str(t) + '.pdf'
        #fileName = 'listaobecnosciTEST.pdf'
        pdf = SimpleDocTemplate(fileName, pagesize=letter, bottomMargin=0, topMargin=5, rightMargin=0, leftMargin=0)
        elems = []
        elems.append(menList)
        pdf.build(elems)
    except IndexError:
        if len(listaKobiet) == 1:
            listaKobiet.append("")
            listaKobiet.append("")
            menList = genPinTable(listaKobiet[0], listaKobiet[1], listaKobiet[2], lista[2], miesiac[1])
            fileName = 'listaobecnosci' + str(miesiac[0]) + str(t) + '.pdf'
            #fileName = 'listaobecnosciTEST.pdf'
            pdf = SimpleDocTemplate(fileName, pagesize=letter, bottomMargin=0, topMargin=5, rightMargin=0, leftMargin=0)
            elems = []
            elems.append(menList)
            pdf.build(elems)
            listaKobiet.clear()

            continue
        else:
            listaKobiet.append("")
            menList = genPinTable(listaKobiet[0], listaKobiet[1], listaKobiet[2], lista[2], miesiac[1])
            fileName = 'listaobecnosci' + str(miesiac[0]) + str(t) + '.pdf'
            #fileName = 'listaobecnosciTEST.pdf'
            pdf = SimpleDocTemplate(fileName, pagesize=letter, bottomMargin=0, topMargin=5, rightMargin=0, leftMargin=0)
            elems = []
            elems.append(menList)
            pdf.build(elems)
            listaKobiet.clear()
            continue

    for _ in range(3):
        del listaKobiet[0]



