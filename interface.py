import os
path = os.sys.path[0] + '\\'
from tkinter import ttk
from PIL import ImageTk, Image 
from tkinter import *
from listas import *
from modelos import Neutro,Vilao

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


        self.Raça = Label(self.container2, text = 'Raças:', font=("Times New Roman", "12", "bold"))
        self.Raça.grid(column=0, row =2, padx=(15, 10), sticky = 'e')
        self.varRaça = StringVar()
        self.varRaça.set('Aleatório')
        self.listaRaça = ttk.Combobox(self.container2,textvariable = self.varRaça,values=['Aleatório'] + lista_raças, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaRaça.grid(column=1, row =2)


        self.Classe = Label(self.container2, text = 'Classes:', font=("Times New Roman", "12", "bold"))
        self.Classe.grid(column=0, row =3,padx=(15, 10), sticky = 'e')
        self.varClasse = StringVar()
        self.varClasse.set('Aleatório')
        self.listaClasse = ttk.Combobox(self.container2,textvariable = self.varClasse,values=['Aleatório'] + classes_npc, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaClasse.grid(column=1, row =3)
        self.valorCheckClasse = IntVar()
        self.checkClasse = Checkbutton(self.container2,text = 'Habilitar Classes de jogador',font = self.fonte,variable=self.valorCheckClasse, onvalue=True, offvalue=False, command = self.AtualizaClasse)
        self.checkClasse.grid(column=2, row =3, padx=10, sticky = 'w')


        self.Alinhamento = Label(self.container2, text = 'Alinhamento:', font=("Times New Roman", "12", "bold"))
        self.Alinhamento.grid(column=0, row =4,padx=(15, 10), sticky = 'e')
        self.varAlinhamento1 = StringVar()
        self.varAlinhamento1.set('Aleatório')
        self.listaAlinhamento1 = ttk.Combobox(self.container2,textvariable = self.varAlinhamento1,values=['Aleatório'] + lista_alinhamento_CO, width = 9, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaAlinhamento1.grid(column=1, row =4, sticky = 'w')
        self.varAlinhamento2 = StringVar()
        self.varAlinhamento2.set('Aleatório')
        self.listaAlinhamento2 = ttk.Combobox(self.container2,textvariable = self.varAlinhamento2,values=['Aleatório'] + lista_alinhamento_BM, width = 9, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaAlinhamento2.grid(column=1, row =4, sticky = 'e')


        self.checkCaracteristicasF = IntVar()
        self.CaracteristicasF = Checkbutton(self.container2,font = self.fonte,variable=self.checkCaracteristicasF, onvalue=True, offvalue=False, command = self.AtualizaCF)
        self.CaracteristicasF.grid(column=2, row=5, padx=10, sticky = 'w')
        self.valorCaracteristicasF = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
        self.valorCaracteristicasF.grid(column=1, row=5)
        self.LCaracteristicasF = Label(self.container2, text = 'Características Físicas:', font=("Times New Roman", "12", "bold"))
        self.LCaracteristicasF.grid(column=0, row=5, padx=(15, 10), sticky = 'e')


        self.checkCaracteristicasP = IntVar()
        self.CaracteristicasP = Checkbutton(self.container2,font = self.fonte,variable=self.checkCaracteristicasP, onvalue=True, offvalue=False, command = self.AtualizaCP)
        self.CaracteristicasP.grid(column=2, row=6, padx=10, sticky = 'w')
        self.valorCaracteristicasP = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
        self.valorCaracteristicasP.grid(column=1, row=6)
        self.LCaracteristicasP = Label(self.container2, text = 'Características Pessoais:', font=("Times New Roman", "12", "bold"))
        self.LCaracteristicasP.grid(column=0, row=6, padx=(15, 10), sticky = 'e')


        self.Riqueza = Label(self.container2, text = 'Riqueza:', font=("Times New Roman", "12", "bold"))
        self.Riqueza.grid(column=0, row =7,padx=(15, 10), sticky = 'e')
        self.varRiqueza = StringVar()
        self.varRiqueza.set('Aleatório')
        self.listaRiqueza = ttk.Combobox(self.container2,textvariable = self.varRiqueza,values=['Aleatório'] + riquezas, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaRiqueza.grid(column=1, row =7)


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

    def AtualizaCF(self):
        if(self.checkCaracteristicasF.get() == False):
            self.valorCaracteristicasF.destroy()
            self.valorCaracteristicasF = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorCaracteristicasF.grid(column=1, row=5)

        elif(self.checkCaracteristicasF.get() == True):
            self.valorCaracteristicasF.destroy()
            self.valorCaracteristicasF = Entry(self.container2, width = 23, font = self.fonte, justify = 'center')
            self.valorCaracteristicasF.grid(column=1, row=5)
            self.valorCaracteristicasF.delete(0,END)

    def AtualizaCP(self):
        if(self.checkCaracteristicasP.get() == False):
            self.valorCaracteristicasP.destroy()
            self.valorCaracteristicasP = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorCaracteristicasP.grid(column=1, row=6)

        elif(self.checkCaracteristicasP.get() == True):
            self.valorCaracteristicasP.destroy()
            self.valorCaracteristicasP = Entry(self.container2, width = 23, font = self.fonte, justify = 'center')
            self.valorCaracteristicasP.grid(column=1, row=6)
            self.valorCaracteristicasP.delete(0,END)

    def AtualizaClasse(self):
        if(self.valorCheckClasse.get() == False):
            self.listaClasse.destroy()
            self.listaClasse = ttk.Combobox(self.container2,textvariable = self.varClasse,values=['Aleatório'] + classes_npc, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
            self.listaClasse.grid(column=1, row =3)

        elif(self.valorCheckClasse.get() == True):
            self.listaClasse.destroy()
            self.listaClasse = ttk.Combobox(self.container2,textvariable = self.varClasse,values=['Aleatório'] + classes_npc + classes_jog, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
            self.listaClasse.grid(column=1, row =3)

    def AtualizaM(self):
        if(self.checkMotivação.get() == False):
            self.valorMotivação.destroy()
            self.valorMotivação = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorMotivação.grid(column=1, row=0)

        elif(self.checkMotivação.get() == True):
            self.valorMotivação.destroy()
            self.valorMotivação = Entry(self.container4, width = 23, font = self.fonte, justify = 'center')
            self.valorMotivação.grid(column=1, row=0)
            self.valorMotivação.delete(0,END)

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
        if(self.checkOcupação.get() == False):
            self.valorOcupação.destroy()
            self.valorOcupação = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorOcupação.grid(column=1, row=0)

        elif(self.checkOcupação.get() == True):
            self.valorOcupação.destroy()
            self.valorOcupação = Entry(self.container4, width = 23, font = self.fonte, justify = 'center')
            self.valorOcupação.grid(column=1, row=0)
            self.valorOcupação.delete(0,END)

    def AtualizaConjunto(self):
        if self.conjunto.get() == 1:

            self.checkMotivação = IntVar()
            self.Motivação = Checkbutton(self.container4,font = self.fonte,variable=self.checkMotivação, onvalue=True, offvalue=False, command = self.AtualizaM)
            self.Motivação.grid(column=2, row=0, padx=10, sticky = 'w')
            self.valorMotivação = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorMotivação.grid(column=1, row=0)
            self.LMotivação = Label(self.container4, text = 'Motivação:', font=("Times New Roman", "12", "bold"))
            self.LMotivação.grid(column=0, row=0, padx=(15, 10), sticky = 'e')

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
            self.Motivação.destroy()
            self.LMotivação.destroy()
            self.valorMotivação.destroy()
            self.Influencia.destroy()
            self.LInfluencia.destroy()
            self.valorInfluencia.destroy()
            self.Poder.destroy()
            self.LPoder.destroy()
            self.valorPoder.destroy()

            self.checkOcupação = IntVar()
            self.Ocupação = Checkbutton(self.container4,font = self.fonte,variable=self.checkOcupação, onvalue=True, offvalue=False, command = self.AtualizaOc)
            self.Ocupação.grid(column=2, row=0, padx=10, sticky = 'w')
            self.valorOcupação = Label(self.container4, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
            self.valorOcupação.grid(column=1, row=0)
            self.LOcupação = Label(self.container4, text = 'Ocupação:', font=("Times New Roman", "12", "bold"))
            self.LOcupação.grid(column=0, row=0, padx=(15, 10), sticky = 'e')
    
    def Gerar(self,master=None):
        global npc

        if self.conjunto.get() == 1: 
            npc = Vilao()
            vilao = True
            neutro = False

            if self.checkMotivação.get() == False:
                npc.gera_motivacao()
            else: npc.set_motivacao(self.valorNome.get())

            if self.checkInfluencia.get() == False:
                npc.gera_influencia()
            else: npc.set_influencia(self.valorNome.get())

            if self.checkPoder.get() == False:
                npc.gera_poderes()
            else: npc.set_poderes(self.valorNome.get())

        else: 
            npc = Neutro()
            vilao = False
            neutro = True

            if self.checkOcupação.get() == False:
                npc.gera_ocupacao()
            else: npc.set_ocupacao(self.valorNome.get())


        if self.varGenero.get() == 'Aleatório':
            npc.gera_genero()
        else: npc.set_genero(self.varGenero.get())

        if self.varRaça.get() == 'Aleatório':
            npc.gera_raça()
        else: npc.set_raça(self.varRaça.get())

        if self.checkNome.get() == False:
            npc.gera_nome()
        else: npc.set_nome(self.valorNome.get())

        if self.checkCaracteristicasF.get() == False:
            npc.gera_caracteristicas_fisicas()
        else: npc.set_caracteristicas_fisicas(self.valorCaracteristicasF.get())

        if self.checkCaracteristicasP.get() == False:
            npc.gera_caracteristicas_pessoais()
        else: npc.set_caracteristicas_pessoais(self.valorCaracteristicasP.get())

        npc._classe_jog = self.valorCheckClasse.get()
        if self.varClasse.get() == 'Aleatório':
            npc.gera_classe()
        else: npc.set_classe(self.varClasse.get())

        if self.varAlinhamento1.get() == 'Aleatório':
            npc.gera_alinhamento_CO()
        else: npc.set_alinhamento_CO(self.varAlinhamento1.get())

        if self.varAlinhamento2.get() == 'Aleatório':
            npc.gera_alinhamento_BM()
        else: npc.set_alinhamento_BM(self.varAlinhamento2.get())

        npc.gera_alinhamento()

        if self.varRiqueza.get() == 'Aleatório':
            npc.gera_riqueza()
        else: npc.set_riqueza(self.varRiqueza.get())

        print(npc)
        
        #Nova interface

        janelaNpc = Toplevel(master)
        janelaNpc.title('NPC')

        imagem1 = ImageTk.PhotoImage(Image.open(path + "imagens\\humano1.jpg"))
        Label(janelaNpc, image=imagem1, text = 'teste').pack()

        Label(janelaNpc, text = npc._nome, font=("Times New Roman", "22", "bold")).pack(pady = (20,40))

        janelaC0 = Frame(janelaNpc)
        janelaC0.pack(anchor = 'w', padx = 20)
        janelaC1 = Frame(janelaNpc)
        janelaC1.pack(anchor = 'w', padx = 20)
        janelaC2 = Frame(janelaNpc)
        janelaC2.pack(anchor = 'w', padx = 20)
        janelaC3 = Frame(janelaNpc)
        janelaC3.pack(anchor = 'w', padx = 20)
        janelaC4 = Frame(janelaNpc)
        janelaC4.pack(anchor = 'w', padx = 20)
        janelaC5 = Frame(janelaNpc)
        janelaC5.pack(anchor = 'w', padx = 20)
        janelaC6 = Frame(janelaNpc)
        janelaC5.pack(anchor = 'w', padx = 20)
        janelaC7 = Frame(janelaNpc)
        janelaC7.pack(anchor = 'w', padx = 20, pady = (0,40))
        if vilao:
            janelaC8 = Frame(janelaNpc)
            janelaC8.pack(anchor = 'w', padx = 20)
            janelaC9 = Frame(janelaNpc)
            janelaC9.pack(anchor = 'w', padx = 20)

        Label(janelaC0, text = 'Gênero: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 1, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC0, text = npc._genero, font=("Times New Roman", "12")).grid(column = 1, row = 1, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC1, text = 'Raça: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 2, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC1, text = npc._raça, font=("Times New Roman", "12")).grid(column = 1, row = 2, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC2, text = 'Classe: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 3, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC2, text = npc._classe, font=("Times New Roman", "12")).grid(column = 1, row = 3, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC3, text = 'Alinhamento: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 4, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC3, text = npc._alinhamento, font=("Times New Roman", "12")).grid(column = 1, row = 4, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC4, text = 'Características Físicas: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 5, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC4, text = npc._caracteristicas_fisicas, font=("Times New Roman", "12")).grid(column = 1, row = 5, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC5, text = 'Características Pessoais: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 6, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC5, text = npc._caracteristicas_pessoais, font=("Times New Roman", "12")).grid(column = 1, row = 6, padx = (2,10), pady = 1, sticky = 'w')

        Label(janelaC6, text = 'Riqueza: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 7, padx = (10,2), pady = 1, sticky = 'w')
        Label(janelaC6, text = npc._riqueza, font=("Times New Roman", "12")).grid(column = 1, row = 7, padx = (2,10), pady = 1, sticky = 'w')
        
        if vilao:
            Label(janelaC7, text = 'Motivação: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 8, padx = (10,2), pady = 1, sticky = 'w')
            Label(janelaC7, text = npc._motivacao, font=("Times New Roman", "12")).grid(column = 1, row = 8, padx = (2,10), pady = 1, sticky = 'w')

            Label(janelaC8, text = 'Influência: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 9, padx = (10,2), pady = 1, sticky = 'w')
            Label(janelaC8, text = npc._influencia, font=("Times New Roman", "12")).grid(column = 1, row = 9, padx = (2,10), pady = 1, sticky = 'w')

            Label(janelaC9, text = 'Poderes: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 10, padx = (10,2), pady = 1, sticky = 'w')
            Label(janelaC9, text = npc._poderes, font=("Times New Roman", "12")).grid(column = 1, row = 10, padx = (2,10), pady = 1, sticky = 'w')
        elif neutro:
            Label(janelaC7, text = 'Ocupação: ', font=("Times New Roman", "12", "bold")).grid(column = 0, row = 8, padx = (10,2), pady = 1, sticky = 'w')
            Label(janelaC7, text = npc._ocupaçao, font=("Times New Roman", "12")).grid(column = 1, row = 8, padx = (2,10), pady = 1, sticky = 'w')

        Button(janelaNpc, text = "Salvar", font=("Times New Roman", "13", "bold"), width=10, command = self.Salvar).pack(anchor = 'se', padx = 20, pady = 10)

    def Salvar(self):
        global npc
        arquivo = open(path + "NPC's.txt","a", encoding="utf-8")
        arquivo.writelines(str(npc))
    
            

root = Tk()
Aplicacao(root)
root.mainloop()