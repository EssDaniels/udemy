import os
from subprocess import Popen

from docxtpl import DocxTemplate

LIBRE_OFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"


def dataToTemplate(nr_group, name_template_list, t, month, data_list):
    doc = DocxTemplate(name_template_list)
    context = {
        'g': nr_group,
        'n': t,
        'miesiac': month,
        'pracownik1': data_list[0],
        'pracownik2': data_list[1],
        'pracownik3': data_list[2]
    }
    s = str(t)
    nazwapliku = "lista_obecnosci" + "_" + nr_group + "_" + s + ".docx"
    doc.render(context)
    doc.save(nazwapliku)

    def convert_to_pdf(input_docx, out_folder):
        p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',
                   out_folder, input_docx])
        print([LIBRE_OFFICE, '--convert-to', 'pdf', input_docx])
        p.communicate()

    sample_doc = nazwapliku
    out_folder = 'Zmiana ' + nr_group
    convert_to_pdf(sample_doc, out_folder)
    os.remove(nazwapliku)
