# -*- coding: utf-8 -*-

data = [
    ['worker1', 'worker2', 'worker3'],
    ['lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień'],
    ['dawid', 'klaudia', 'karol', 'ja', '1000'],

]

fileName = 'pdfTable.pdf'

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

pdf = SimpleDocTemplate(
    fileName,
    pagesize=letter,
    encoding='UTF-8'


)



table = Table(data)
table.setStyle(style)
rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige
    ts = TableStyle(
        [('BACKGROUND', (0, i), (-1, i), bc)]
    )
    table.setStyle(ts)

ts = TableStyle(
    [('BOX', (0, 0), (-1, -1), 2, colors.black),
     ('GRID', (0, 1), (-1, -1), 2, colors.black)
     ]
)
table.setStyle(ts)

elems = []
elems.append(table)
pdf.build(elems)
