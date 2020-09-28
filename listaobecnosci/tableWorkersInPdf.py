# -*- coding: utf-8 -*-
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from rotatedtext import verticalText
from functions import AttendanceList

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))


def genPinTable(person1, person2, person3, zmiana, month, nr, howManyDays, choice):

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
        ('BOX', (0, 0), (-1, -1), 2, colors.black)
    ])
    underNameTable.setStyle(underNameTableStyle)

    days = []
    ile = int(howManyDays)

    for i in range(1, ile + 1):
        days.append([i, '', '_ _:_ _', '', '', '_ _:_ _', '', '', '_ _:_ _', ''])

    daysTable = Table(
        days, (30, 70, 50, 56, 70, 50, 56, 70, 50, 56)
    )

    markDaysList = AttendanceList.markDay(ile, choice + 1)
    daysTableStyle = TableStyle(markDaysList)

    daysTable.setStyle(daysTableStyle)

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
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Oblique'),
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
