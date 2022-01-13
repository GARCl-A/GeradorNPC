from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

pasta = os.path.dirname(__file__)

def cria_pdf():
    cnv = canvas.Canvas(pasta+"\\NPC'S.pdf",pagesize=A4)
    file = open("NPC'S.txt",mode = 'r', encoding='utf-8')
    lista = []
    for line in file:
        line = line.strip('\n')
        lista.append(line)
    y = 817
    qtd = 0
    for item in lista:
        if qtd < 3:
            cnv.drawString(50,y,item)
            y = y-20
        else:
            cnv.showPage()
            qtd = 0
            y = 817
            cnv.drawString(50,y,item)
            y = y-17
        if '-' == item:
            qtd = qtd +1

    cnv.save()
    print('Pdf salvo')

cria_pdf()