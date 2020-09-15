# -*- coding: utf-8 -*-

import datetime

from rotatedtext import verticalText

dzisiaj = datetime.datetime.now()
print(dzisiaj.strftime("%A"))

x = datetime.datetime(2020, 3, 15)

print(x.strftime("%A"))


class Worker:
    name = ''


def worker(name='ktos'):
    person = Worker()
    person.name = name
    return person


fileName = 'listaobecnosci.pdf'

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

style = TableStyle([
    ('BACKGROUND', (0, 0), (5, 0), colors.green),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Vera'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
])

pdf = SimpleDocTemplate(fileName, pagesize=letter, bottomMargin=0, topMargin=5, rightMargin=0, leftMargin=0)


def genPinTable(person1, person2, person3, zmiana, month, nr=0):
    pinElemTable = None

    pinElemWidth = 580

    hourManySignTable = Table([

        [verticalText('Godziny pracy'), verticalText('Ilość godzin pracy'), verticalText('Podpis')]
    ], (70, 50, 56), (115))
    hourManySignTableStyle = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('FONTNAME', (0, 0), (-1, -1), 'Vera'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBEFORE', (0, 0), (2, -1), 1, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),

    ])
    hourManySignTable.setStyle(hourManySignTableStyle)
    noteTable = Table([
        ['a', 'a', 'a']
    ], (85, 40, 50))
    noteTableStyle = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('FONTNAME', (0, 0), (-1, -1), 'Vera'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBEFORE', (0, 0), (2, -1), 1, colors.black),
        ('LINEABOVE', (1, 0), (0, -1), 1, colors.red),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),

    ])

    dataNrTable = Table([
        [nr],
        [verticalText(month)]
    ], (30), (70))
    dataNrTableStyle = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('FONTNAME', (0, 0), (-1, -1), 'Vera'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),

        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),

    ])
    dataNrTable.setStyle(dataNrTableStyle)
    underNameTable = Table([
        [zmiana, person1, person2, person3],
        [dataNrTable, hourManySignTable, hourManySignTable, hourManySignTable],

    ], (30, 176, 176, 176), (30, 120))

    underNameTableStyle = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('FONTNAME', (0, 0), (-1, -1), 'Vera'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),

        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        # ('GRID', (1, 1), (-1, -1), 2, colors.black),

        ('BOX', (0, 0), (-1, -1), 2, colors.black)
    ])
    underNameTable.setStyle(underNameTableStyle)

    noteTable.setStyle(noteTableStyle)

    daysTopic = ['Day', 'noteTable', 'noteTable', 'noteTable']
    days = []

    for i in range(1, 32):
        days.append([i, '', '_ _:_ _', '', '', '_ _:_ _', '', '', '_ _:_ _', ''])

    daysTable = Table(
        days, (30, 70, 50, 56, 70, 50, 56, 70, 50, 56)
    )

    daysTableStyle = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('FONTNAME', (0, 0), (-1, -1), 'Vera'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),

        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 2, colors.black),

        ('BOX', (0, 0), (-1, -1), 2, colors.black)
    ])
    daysTable.setStyle(daysTableStyle)

    pinElemTable = Table([

        [underNameTable],

        [daysTable]
    ])

    underNameTableStyle = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('FONTNAME', (0, 0), (-1, -1),
         'Helvetica-Oblique'
         ),

        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    underNameTable.setStyle(underNameTableStyle)

    pinElemTableStyle = TableStyle([

        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

    ])
    pinElemTable.setStyle(pinElemTableStyle)

    return pinElemTable

"""
pracownik1 = worker("Klauida")
pracownik2 = worker("Dawid")
pracownik3 = worker("Karol")
p1 = genPinTable(pracownik1, 'I', "Kwiecień")

elems = []
elems.append(p1)
pdf.build(elems)
"""
