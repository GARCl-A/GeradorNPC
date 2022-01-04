from tkinter import ttk
from tkinter import *
from listas import *
from classe import Pacifico,Vilao


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

        self.titulo = Label(self.container1, text="Gerador de NPCs")
        self.titulo["font"] = ("Times New Roman", "22", "bold")
        self.titulo.grid()

        self.checkNome = IntVar()
        self.Nome = Checkbutton(self.container2,font = self.fonte,variable=self.checkNome, onvalue=True, offvalue=False, command = self.AtualizaNome)
        self.Nome.grid(column=2, row=0, padx=10, sticky = 'w')
        self.valorNome = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
        self.valorNome.grid(column=1, row=0)
        self.Nome = Label(self.container2, text = 'Nome:', font=("Times New Roman", "12", "bold"))
        self.Nome.grid(column=0, row=0, padx=(15, 10), sticky = 'e')


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
        self.CaracteristicasF = Label(self.container2, text = 'Características Físicas:', font=("Times New Roman", "12", "bold"))
        self.CaracteristicasF.grid(column=0, row=5, padx=(15, 10), sticky = 'e')


        self.checkCaracteristicasP = IntVar()
        self.CaracteristicasP = Checkbutton(self.container2,font = self.fonte,variable=self.checkCaracteristicasP, onvalue=True, offvalue=False, command = self.AtualizaCP)
        self.CaracteristicasP.grid(column=2, row=6, padx=10, sticky = 'w')
        self.valorCaracteristicasP = Label(self.container2, text = 'Aleatório', font=self.fonte, bg = 'white', width = 20)
        self.valorCaracteristicasP.grid(column=1, row=6)
        self.CaracteristicasP = Label(self.container2, text = 'Características Pessoais:', font=("Times New Roman", "12", "bold"))
        self.CaracteristicasP.grid(column=0, row=6, padx=(15, 10), sticky = 'e')


        self.Riqueza = Label(self.container2, text = 'Riqueza:', font=("Times New Roman", "12", "bold"))
        self.Riqueza.grid(column=0, row =7,padx=(15, 10), sticky = 'e')
        self.varRiqueza = StringVar()
        self.varRiqueza.set('Aleatório')
        self.listaRiqueza = ttk.Combobox(self.container2,textvariable = self.varRiqueza,values=['Aleatório'] + riquezas, width = 21, justify = 'center', font= self.fonte, state = 'readonly')
        self.listaRiqueza.grid(column=1, row =7)

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
            

root = Tk()
Aplicacao(root)
root.mainloop()