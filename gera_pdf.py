from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from modelos import Vilao, Neutro
from textwrap import wrap
from reportlab.lib.pagesizes import letter
import io

pasta = os.path.dirname(__file__)

def nome_pdf(nome):
    return f'{pasta}\{nome}.pdf'

def cria_pdf(npc,nome = "\\NPC'S.pdf" ):
    tipo = ''
    if type(npc) == Vilao:
        path = f'{pasta}\pdf\Base_vilão.pdf'
        tipo = 'vilao'
    if type(npc) == Neutro:
        path = f'{pasta}\pdf\Base_neutro.pdf'
        tipo = 'neutro'

   
    packet = io.BytesIO()

    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(130, 648, npc._nome)
    can.drawString(320, 646, str(npc._idade)) 
    can.drawString(133, 625, npc._raça)
    can.drawString(137, 602, npc._classe)
    can.drawString(168, 579, npc._alinhamento_CO)
    can.drawString(218, 579, npc._alinhamento_BM)
    can.drawString(145, 553, npc._riqueza)
    can.drawString(123, 524, npc._genero)
    can.setFont("Helvetica", 6.5)
    can.drawString(107, 106, npc._caracteristicas_fisicas)
    can.setFont("Helvetica", 8)
    can.drawString(105, 75, npc._caracteristicas_pessoais)

    if tipo == 'vilao':
        lista_influencia = npc._influencia.split("|")
        can.drawString(165, 454, npc._motivacao)
        can.drawString(248, 425, lista_influencia[0])
        can.drawString(347, 425, lista_influencia[1])
        can.drawString(142, 408, npc._poderes)
    elif tipo == 'neutro':
        can.drawString(171, 435, npc._ocupaçao)

    can.save()

    #Fazendo Merge
    packet.seek(0)
    ficha = PdfFileReader(packet)

    pdf_base = PdfFileReader(open(path, "rb"))
    output = PdfFileWriter()
    page = pdf_base.getPage(0)
    page.mergePage(ficha.getPage(0))
    output.addPage(page)
    outputStream = open(nome, "wb")
    output.write(outputStream)
    outputStream.close()




