from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from modelos import *
from textwrap import wrap

pasta = os.path.dirname(__file__)

def nome_pdf(nome):
    return f'\\{nome}.pdf'

def cria_pdf(npc,nome = "\\NPC'S.pdf" ):
    cnv = canvas.Canvas(pasta+nome,pagesize=A4)
    y = 817
    t = cnv.beginText()
    t.setFont('Helvetica-Bold', 10)
    t.setCharSpace(0.5)
    t.setTextOrigin(50, 800)
    wraped_text = "\n".join(wrap(str(npc), 80)) # 80 is line width
    t.textLines(str(npc))
    cnv.drawText(t)
    cnv.showPage()

    cnv.save()