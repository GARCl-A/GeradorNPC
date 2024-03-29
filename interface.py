import os
path = os.sys.path[0] + '\\'
from tkinter import ttk
from PIL import ImageTk
import PIL.Image
from tkinter import *
from listas import *
from modelos import Neutro,Vilao
from gera_pdf import cria_pdf, nome_pdf

class Aplicacao:
    def __init__(self,master=None):
        master.title('Gerador de NPCs')

        self.fonte = ("Times New Roman", "11")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1["padx"] = 20
        self.container1.grid(column=0, row=0)

        self.container2 = Frame(master)
        self.container2["pady"] = 20
        self.container2["padx"] = 20
        self.container2.grid(column=0, row=1, sticky="w", pady = (40,0))

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.grid(column=0, row=2, pady = (10,10))

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4.grid(column=0, row=3, pady = (20,10))

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5.grid(column=0, row=4, pady = (40,10))

        self.titulo = Label(self.container1, text="Gerador de NPCs")
        self.titulo["font"] = ("Times New Roman", "22", "bold")
        self.titulo.grid()

        self.checkNome = IntVar()
        self.Nome = Checkbutton(self.container2,font = self.fonte,variable=self.checkNome, onvalue=True, offvalue=False, command = self.AtualizaNome)
        self.Nome.grid(column=2, row=0, padx=10, sticky = 'w')
        self.valorNome = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
        self.valorNome.grid(column=1, row=0)
        self.LNome = Label(self.container2, text = 'Nome:', font=("Times New Roman", "12", "bold"))
        self.LNome.grid(column=0, row=0, padx=(15, 10), sticky = 'e')


        self.Genero = Label(self.container2, text = 'Gênero:', font=("Times New Roman", "12", "bold"))
        self.Genero.grid(column=0, row =1,padx=(15, 10), sticky = 'e')
        self.varGenero = StringVar()
        self.varGenero.set('Aleatório')
        self.listaGenero = ttk.Combobox(self.container2,textvariable = self.varGenero,values=['Aleatório','Masculino','Feminino'], width = 21, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaGenero.grid(column=1, row =1)

        self.checkIdade = IntVar()
        self.Idade = Checkbutton(self.container2,font = self.fonte,variable=self.checkIdade, onvalue=True, offvalue=False, command = self.AtualizaIdade)
        self.Idade.grid(column=2, row=2, padx=10, sticky = 'w')
        self.valorIdade = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
        self.valorIdade.grid(column=1, row=2)
        self.LIdade = Label(self.container2, text = 'Idade:', font=("Times New Roman", "12", "bold"))
        self.LIdade.grid(column=0, row=2, padx=(15, 10), sticky = 'e')


        self.Raca = Label(self.container2, text = 'Raças:', font=("Times New Roman", "12", "bold"))
        self.Raca.grid(column=0, row =3, padx=(15, 10), sticky = 'e')
        self.varRaca = StringVar()
        self.varRaca.set('Aleatório')
        self.listaRaca = ttk.Combobox(self.container2,textvariable = self.varRaca,values=['Aleatório'] + lista_racas, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaRaca.grid(column=1, row =3)


        self.Classe = Label(self.container2, text = 'Classes:', font=("Times New Roman", "12", "bold"))
        self.Classe.grid(column=0, row =4,padx=(15, 10), sticky = 'e')
        self.varClasse = StringVar()
        self.varClasse.set('Aleatório')
        self.listaClasse = ttk.Combobox(self.container2,textvariable = self.varClasse,values=['Aleatório'] + classes_npc, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaClasse.grid(column=1, row =4)
        self.valorCheckClasse = IntVar()
        self.checkClasse = Checkbutton(self.container2,text = 'Habilitar Classes de jogador',font = self.fonte,variable=self.valorCheckClasse, onvalue=True, offvalue=False, command = self.AtualizaClasse)
        self.checkClasse.grid(column=2, row =4, padx=10, sticky = 'w')


        self.Alinhamento = Label(self.container2, text = 'Alinhamento:', font=("Times New Roman", "12", "bold"))
        self.Alinhamento.grid(column=0, row =5,padx=(15, 10), sticky = 'e')
        self.varAlinhamento1 = StringVar()
        self.varAlinhamento1.set('Aleatório')
        self.listaAlinhamento1 = ttk.Combobox(self.container2,textvariable = self.varAlinhamento1,values=['Aleatório'] + lista_alinhamento_CO, width = 9, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaAlinhamento1.grid(column=1, row =5, sticky = 'w')
        self.varAlinhamento2 = StringVar()
        self.varAlinhamento2.set('Aleatório')
        self.listaAlinhamento2 = ttk.Combobox(self.container2,textvariable = self.varAlinhamento2,values=['Aleatório'] + lista_alinhamento_BM, width = 9, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaAlinhamento2.grid(column=1, row =5, sticky = 'e')


        self.checkCaracteristicasF = IntVar()
        self.CaracteristicasF = Checkbutton(self.container2,font = self.fonte,variable=self.checkCaracteristicasF, onvalue=True, offvalue=False, command = self.AtualizaCF)
        self.CaracteristicasF.grid(column=2, row=6, padx=10, sticky = 'w')
        self.valorCaracteristicasF = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
        self.valorCaracteristicasF.grid(column=1, row=6)
        self.LCaracteristicasF = Label(self.container2, text = 'Características Físicas:', font=("Times New Roman", "12", "bold"))
        self.LCaracteristicasF.grid(column=0, row=6, padx=(15, 10), sticky = 'e')


        self.checkCaracteristicasP = IntVar()
        self.CaracteristicasP = Checkbutton(self.container2,font = self.fonte,variable=self.checkCaracteristicasP, onvalue=True, offvalue=False, command = self.AtualizaCP)
        self.CaracteristicasP.grid(column=2, row=7, padx=10, sticky = 'w')
        self.valorCaracteristicasP = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
        self.valorCaracteristicasP.grid(column=1, row=7)
        self.LCaracteristicasP = Label(self.container2, text = 'Características Pessoais:', font=("Times New Roman", "12", "bold"))
        self.LCaracteristicasP.grid(column=0, row=7, padx=(15, 10), sticky = 'e')


        self.Riqueza = Label(self.container2, text = 'Riqueza:', font=("Times New Roman", "12", "bold"))
        self.Riqueza.grid(column=0, row =8,padx=(15, 10), sticky = 'e')
        self.varRiqueza = StringVar()
        self.varRiqueza.set('Aleatório')
        self.listaRiqueza = ttk.Combobox(self.container2,textvariable = self.varRiqueza,values=['Aleatório'] + riquezas, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaRiqueza.grid(column=1, row =8)


        self.conjunto = IntVar()
        self.conjunto.set(1)
        Radiobutton(self.container3,text="Vilão",font = ("Times New Roman", "13"), padx = 5, variable=self.conjunto, value=1, command = self.AtualizaConjunto).grid(column= 1, row= 1,padx = 40)
        Radiobutton(self.container3,text="Neutro",font = ("Times New Roman", "13"), padx = 5, variable=self.conjunto, value=2, command = self.AtualizaConjunto).grid(column= 3, row= 1,padx = 40)
        self.AtualizaConjunto()


        self.BGerar = Button(self.container5, text = "Gerar", font=("Times New Roman", "13", "bold"), width=50, command = self.Gerar)
        self.BGerar.grid(column = 0, row = 0)

    def AtualizaNome(self):
        if(self.checkNome.get() == False):
            self.valorNome.destroy()
            self.valorNome = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorNome.grid(column=1, row=0)

        elif(self.checkNome.get() == True):
            self.valorNome.destroy()
            self.valorNome = Entry(self.container2, width = 23, font = self.fonte, justify = 'center')
            self.valorNome.grid(column=1, row=0)
            self.valorNome.delete(0,END)

    def AtualizaIdade(self):
        if(self.checkIdade.get() == False):
            self.valorIdade.destroy()
            self.valorIdade = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorIdade.grid(column=1, row=2)

        elif(self.checkIdade.get() == True):
            self.valorIdade.destroy()
            self.valorIdade = Entry(self.container2, width = 23, font = self.fonte, justify = 'center')
            self.valorIdade.grid(column=1, row=2)
            self.valorIdade.delete(0,END)

    def AtualizaCF(self):
        if(self.checkCaracteristicasF.get() == False):
            self.valorCaracteristicasF.destroy()
            self.valorCaracteristicasF = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorCaracteristicasF.grid(column=1, row=6)

        elif(self.checkCaracteristicasF.get() == True):
            self.valorCaracteristicasF.destroy()
            self.valorCaracteristicasF = Entry(self.container2, width = 23, font = self.fonte, justify = 'center')
            self.valorCaracteristicasF.grid(column=1, row=6)
            self.valorCaracteristicasF.delete(0,END)

    def AtualizaCP(self):
        if(self.checkCaracteristicasP.get() == False):
            self.valorCaracteristicasP.destroy()
            self.valorCaracteristicasP = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorCaracteristicasP.grid(column=1, row=7)

        elif(self.checkCaracteristicasP.get() == True):
            self.valorCaracteristicasP.destroy()
            self.valorCaracteristicasP = Entry(self.container2, width = 23, font = self.fonte, justify = 'center')
            self.valorCaracteristicasP.grid(column=1, row=7)
            self.valorCaracteristicasP.delete(0,END)

    def AtualizaClasse(self):
        if(self.valorCheckClasse.get() == False):
            self.listaClasse.destroy()
            self.listaClasse = ttk.Combobox(self.container2,textvariable = self.varClasse,values=['Aleatório'] + classes_npc, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
            self.listaClasse.grid(column=1, row =4)

        elif(self.valorCheckClasse.get() == True):
            self.listaClasse.destroy()
            self.listaClasse = ttk.Combobox(self.container2,textvariable = self.varClasse,values=['Aleatório'] + classes_npc + classes_jog, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
            self.listaClasse.grid(column=1, row =4)

    def AtualizaM(self):
        if(self.checkMotivacao.get() == False):
            self.valorMotivacao.destroy()
            self.valorMotivacao = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorMotivacao.grid(column=1, row=0)

        elif(self.checkMotivacao.get() == True):
            self.valorMotivacao.destroy()
            self.valorMotivacao = Entry(self.container4, width = 23, font = self.fonte, justify = 'center')
            self.valorMotivacao.grid(column=1, row=0)
            self.valorMotivacao.delete(0,END)

    def AtualizaIn(self):
        if(self.checkInfluencia.get() == False):
            self.valorInfluencia.destroy()
            self.valorInfluencia = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorInfluencia.grid(column=1, row=1)

        elif(self.checkInfluencia.get() == True):
            self.valorInfluencia.destroy()
            self.valorInfluencia = Entry(self.container4, width = 23, font = self.fonte, justify = 'center')
            self.valorInfluencia.grid(column=1, row=1)
            self.valorInfluencia.delete(0,END)

    def AtualizaPoder(self):
        if(self.checkPoder.get() == False):
            self.valorPoder.destroy()
            self.valorPoder = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorPoder.grid(column=1, row=2)

        elif(self.checkPoder.get() == True):
            self.valorPoder.destroy()
            self.valorPoder = Entry(self.container4, width = 23, font = self.fonte, justify = 'center')
            self.valorPoder.grid(column=1, row=2)
            self.valorPoder.delete(0,END)

    def AtualizaOc(self):
        if(self.checkOcupacao.get() == False):
            self.valorOcupacao.destroy()
            self.valorOcupacao = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorOcupacao.grid(column=1, row=0)

        elif(self.checkOcupacao.get() == True):
            self.valorOcupacao.destroy()
            self.valorOcupacao = Entry(self.container4, width = 23, font = self.fonte, justify = 'center')
            self.valorOcupacao.grid(column=1, row=0)
            self.valorOcupacao.delete(0,END)

    def AtualizaConjunto(self):
        if self.conjunto.get() == 1:

            self.checkMotivacao = IntVar()
            self.Motivacao = Checkbutton(self.container4,font = self.fonte,variable=self.checkMotivacao, onvalue=True, offvalue=False, command = self.AtualizaM)
            self.Motivacao.grid(column=2, row=0, padx=10, sticky = 'w')
            self.valorMotivacao = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorMotivacao.grid(column=1, row=0)
            self.LMotivacao = Label(self.container4, text = 'Motivação:', font=("Times New Roman", "12", "bold"))
            self.LMotivacao.grid(column=0, row=0, padx=(15, 10), sticky = 'e')

            self.checkInfluencia = IntVar()
            self.Influencia = Checkbutton(self.container4,font = self.fonte,variable=self.checkInfluencia, onvalue=True, offvalue=False, command = self.AtualizaIn)
            self.Influencia.grid(column=2, row=1, padx=10, sticky = 'w')
            self.valorInfluencia = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorInfluencia.grid(column=1, row=1)
            self.LInfluencia = Label(self.container4, text = 'Influência:', font=("Times New Roman", "12", "bold"))
            self.LInfluencia.grid(column=0, row=1, padx=(15, 10), sticky = 'e')

            self.checkPoder = IntVar()
            self.Poder = Checkbutton(self.container4,font = self.fonte,variable=self.checkPoder, onvalue=True, offvalue=False, command = self.AtualizaPoder)
            self.Poder.grid(column=2, row=2, padx=10, sticky = 'w')
            self.valorPoder = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorPoder.grid(column=1, row=2)
            self.LPoder = Label(self.container4, text = 'Poder:', font=("Times New Roman", "12", "bold"))
            self.LPoder.grid(column=0, row=2, padx=(15, 10), sticky = 'e')

        if self.conjunto.get() == 2:
            self.Motivacao.destroy()
            self.LMotivacao.destroy()
            self.valorMotivacao.destroy()
            self.Influencia.destroy()
            self.LInfluencia.destroy()
            self.valorInfluencia.destroy()
            self.Poder.destroy()
            self.LPoder.destroy()
            self.valorPoder.destroy()

            self.checkOcupacao = IntVar()
            self.Ocupacao = Checkbutton(self.container4,font = self.fonte,variable=self.checkOcupacao, onvalue=True, offvalue=False, command = self.AtualizaOc)
            self.Ocupacao.grid(column=2, row=0, padx=10, sticky = 'w')
            self.valorOcupacao = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorOcupacao.grid(column=1, row=0)
            self.LOcupacao = Label(self.container4, text = 'Ocupação:', font=("Times New Roman", "12", "bold"))
            self.LOcupacao.grid(column=0, row=0, padx=(15, 10), sticky = 'e')
    
    def Gerar(self,master=None):
        global npc

        if self.conjunto.get() == 1: 
            npc = Vilao()
            vilao = True
            neutro = False

            if self.varAlinhamento1.get() == 'Aleatório':
                npc.gera_alinhamento_CO()
            else: npc.set('alinhamento_CO',self.varAlinhamento1.get())

            if self.varAlinhamento2.get() == 'Aleatório':
                npc.gera_alinhamento_BM()
            else: npc.set('alinhamento_BM',self.varAlinhamento2.get())

            npc.gera_alinhamento()

            if self.checkMotivacao.get() == False:
                npc.gera_motivacao()
            else: npc.set('motivacao',self.valorMotivacao.get())

            if self.checkInfluencia.get() == False:
                npc.gera_influencia()
            else: npc.set('influencia',self.valorInfluencia.get())

            if self.checkPoder.get() == False:
                npc.gera_poderes()
            else: npc.set('poderes',self.valorPoder.get())

        else: 
            npc = Neutro()
            vilao = False
            neutro = True

            if self.varAlinhamento1.get() == 'Aleatório':
                npc.gera_alinhamento_CO()
            else: npc.set('alinhamento_CO',self.varAlinhamento1.get())

            if self.varAlinhamento2.get() == 'Aleatório':
                npc.gera_alinhamento_BM()
            else: npc.set('alinhamento_BM',self.varAlinhamento2.get())

            npc.gera_alinhamento()
            if self.checkOcupacao.get() == False:
                npc.gera_ocupacao()
            else: npc.set('ocupacao',self.valorOcupacao.get())

        if self.varGenero.get() == 'Aleatório':
            npc.gera_genero()
        else: npc.set('genero',self.varGenero.get())

        if self.varRaca.get() == 'Aleatório':
            npc.gera_raca()
        else: npc.set('raca',self.varRaca.get())

        if self.checkNome.get() == False:
            npc.gera_nome()
        else: npc.set('nome',self.valorNome.get())

        if self.checkIdade.get() == False:
            npc.gera_idade()
        else: npc.set('idade',self.valorIdade.get())

        if self.checkCaracteristicasF.get() == False:
            npc.gera_caracteristicas_fisicas()
        else: npc.set('caracteristicas_fisicas',self.valorCaracteristicasF.get())

        if self.checkCaracteristicasP.get() == False:
            npc.gera_caracteristicas_pessoais()
        else: npc.set('caracteristicas_pessoais',self.valorCaracteristicasP.get())

        npc._classe_jog = self.valorCheckClasse.get()
        if self.varClasse.get() == 'Aleatório':
            npc.gera_classe()
        else: npc.set('classe',self.varClasse.get())

        if self.varRiqueza.get() == 'Aleatório':
            npc.gera_riqueza()
        else: npc.set('riqueza',self.varRiqueza.get())

        npc.gera_pasta()

        JanelaNPC(npc,vilao,neutro,master)
    
class JanelaNPC:
    def __init__(self,personagem,vilao,neutro,master=None):

        self._npc = personagem
        self._vilao = vilao
        self._neutro = neutro
        
        self.CriaJanela(master)

    def CriaJanela(self,master):
        self._janelaNpc = Toplevel(master)
        self._janelaNpc.title('NPC')

        Label(self._janelaNpc, text = self._npc._nome, font=("Times New Roman", "22", "bold")).grid(pady = (20,40))

        img = PIL.Image.open(self._npc._imagem)
        rimg = img.resize((250,327), PIL.Image.ANTIALIAS)
        fimg = ImageTk.PhotoImage(rimg)

        self.imagem = Label(self._janelaNpc, text = "adicionando", image = fimg)
        self.imagem.image = fimg
        self.imagem.bind('<Button-1>', self.mudaImagem)
        self.imagem.bind("<Enter>",self.Hover)
        self.imagem.bind("<Leave>",self.RemoveHover)
        self.imagem.grid(sticky = "ne",pady=(30,0),padx=20, column = 1, row =1)

        containerjanela = Frame(self._janelaNpc)
        containerjanela.grid(sticky = "w",column = 0, row =1)
        janelaC0 = Frame(containerjanela)
        janelaC0.grid(sticky = 'w', padx= 20, column = 0, row =1)
        janelaC1 = Frame(containerjanela)
        janelaC1.grid(sticky = 'w', padx= 20, column = 0, row =2)
        janelaC2 = Frame(containerjanela)
        janelaC2.grid(sticky = 'w', padx= 20, column = 0, row =3)
        janelaC3 = Frame(containerjanela)
        janelaC3.grid(sticky = 'w', padx= 20, column = 0, row =4)
        janelaC4 = Frame(containerjanela)
        janelaC4.grid(sticky = 'w', padx= 20, column = 0, row =5)
        janelaC5 = Frame(containerjanela)
        janelaC5.grid(sticky = 'w', padx= 20, column = 0, row =6)
        janelaC6 = Frame(containerjanela)
        janelaC6.grid(sticky = 'w', padx= 20, column = 0, row =7)
        janelaC7 = Frame(containerjanela)
        janelaC7.grid(sticky = 'w', padx = 20, pady = (0,40), column = 0, row =8)
        if self._vilao:
            janelaC7.grid(sticky = 'w', padx = 20, pady = 0, column = 0, row =8)
            janelaC8 = Frame(containerjanela)
            janelaC8.grid(sticky = 'w', padx= 20, column = 0, row =9)
            janelaC9 = Frame(containerjanela)
            janelaC9.grid(sticky = 'w', padx= 20, pady = (0,40), column = 0, row =10)

        Label(janelaC0, text = 'Gênero: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 1, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC0, text = self._npc._genero, font=("Times New Roman", "12")).grid(column = 1, row = 1, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC0, text = 'Idade: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 2, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC0, text = self._npc._idade, font=("Times New Roman", "12")).grid(column = 1, row = 2, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC1, text = 'Raça: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 3, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC1, text = self._npc._raca, font=("Times New Roman", "12")).grid(column = 1, row = 3, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC2, text = 'Classe: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 4, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC2, text = self._npc._classe, font=("Times New Roman", "12")).grid(column = 1, row = 4, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC3, text = 'Alinhamento: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 5, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC3, text = self._npc._alinhamento, font=("Times New Roman", "12")).grid(column = 1, row = 5, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC4, text = 'Características Físicas: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 6, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC4, text = self._npc._caracteristicas_fisicas, font=("Times New Roman", "12")).grid(column = 1, row = 6, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC5, text = 'Características Pessoais: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 7, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC5, text = self._npc._caracteristicas_pessoais, font=("Times New Roman", "12")).grid(column = 1, row = 7, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC6, text = 'Riqueza: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 8, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC6, text = self._npc._riqueza, font=("Times New Roman", "12")).grid(column = 1, row = 8, padx = (2,10), pady = 1, sticky = 'w')
        
        if self._vilao:
            Label(janelaC7, text = 'Motivação: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 9, padx = (10,2), pady = 1, sticky = 'w')
            Label(janelaC7, text = self._npc._motivacao, font=("Times New Roman", "12")).grid(column = 1, row = 9, padx = (2,10), pady = 1, sticky = 'w')

            Label(janelaC8, text = 'Influência: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 10, padx = (10,2), pady = 1, sticky = 'w')
            Label(janelaC8, text = self._npc._influencia, font=("Times New Roman", "12")).grid(column = 1, row = 10, padx = (2,10), pady = 1, sticky = 'w')

            Label(janelaC9, text = 'Poderes: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 11, padx = (10,2), pady = 1, sticky = 'w')
            Label(janelaC9, text = self._npc._poderes, font=("Times New Roman", "12")).grid(column = 1, row = 11, padx = (2,10), pady = 1, sticky = 'w')
        elif self._neutro:
            Label(janelaC7, text = 'Ocupação: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 9, padx = (10,2), pady = 1, sticky = 'w')
            Label(janelaC7, text = self._npc._ocupacao, font=("Times New Roman", "12")).grid(column = 1, row = 9, padx = (2,10), pady = 1, sticky = 'w')

        self.hover = Label(self._janelaNpc, text = '', font=("Times New Roman", "10"))
        self.hover.grid(column = 1, row = 2, padx = (2,10), pady = (0,30))
        Button(self._janelaNpc, text = "Salvar", font=("Times New Roman", "13", "bold"), width=10, command = self.Salvar).grid(sticky = 'se',column = 1, row = 3, padx = 20, pady = 10)
        self.salvando = Label(self._janelaNpc, text = '', font=("Times New Roman", "12"))

    def mudaImagem(self,event):
        self._npc.troca_imagem()
        img = PIL.Image.open(self._npc._imagem)
        rimg = img.resize((250,327), PIL.Image.ANTIALIAS)
        fimg = ImageTk.PhotoImage(rimg)
        self.imagem['image'] = fimg
        self.imagem.image = fimg
        self.imagem.grid(sticky = "ne",pady=(30,0),padx=20, column = 1, row =1)
    def Hover(self,event):
        self.hover['text'] = 'Clique para mudar a imagem!'
    def RemoveHover(self,event):
        self.hover['text'] = ''  

    def Salvar(self):
        self.salvando['text'] = 'Salvando...'
        self.salvando.grid(sticky = 'se',column = 1, row = 4, padx = 20, pady = 10)
        arquivo = nome_pdf(self._npc._nome)
        cria_pdf(self._npc,arquivo)
        root.after(1000,self.salvo)
    def salvo(self):
        self.salvando['text'] = 'Salvo!'
        
root = Tk()
Aplicacao(root)
root.mainloop()