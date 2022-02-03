import random
from listas import *
import os, os.path

class NPC():
    def __init__(self):
        self._nome = None
        self._raca = None
        self._alinhamento = None
        self._alinhamento_CO = None
        self._alinhamento_BM = None
        self._caracteristicas_fisicas = None
        self._caracteristicas_pessoais = None
        self._qualidades = []
        self._defeitos = []
        self._classe = None
        self._riqueza = None
        self._genero = None
        self._classe_jog = True
        self._idade = None
        self._imagem = None

    def set(self,atributo, valor):
        if atributo == 'idade':
            valor = int(valor)
        atributo = '_' + atributo
        setattr(self,atributo,valor)

    def gera_nome_aleatorio(self):
        letras = random.randrange(1,4) + random.randrange(1,4) + random.randrange(1,4)
        nome = ""
        index = 0
        for i in range(letras):
            if index % 2 == 0:
                numero = random.randrange(len(consoantes))
                nome += consoantes[numero]
                index += 1
            else:
                numero = random.randrange(len(vogais))
                nome += vogais[numero]
                index += 1
        return nome.title()

    def gera_pasta(self):
        dir = os.path.dirname(__file__)
        pasta = f'{dir}\imagens\{self._raca}\{self._raca+self._genero}'
        tamanho = len([name for name in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, name))])
        self._imagem_numero = random.randrange(0,tamanho)
        caminho = pasta+f'\{self._imagem_numero}.jpg'
        self._imagem = caminho

    def troca_imagem(self):
        self._imagem_numero += 1
        dir = os.path.dirname(__file__)
        pasta = f'{dir}\imagens\{self._raca}\{self._raca+self._genero}'
        tamanho = len([name for name in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, name))])
        if self._imagem_numero > tamanho-1:
            self._imagem_numero = 0
        caminho = pasta+f'\{self._imagem_numero}.jpg'
        self._imagem = caminho

    def gera_idade(self):
        base = random.randrange(0,21) + random.randrange(0,21) + random.randrange(0,21)
        modificador = random.randrange(0,10)
        if modificador < 2:
            base = base - random.randrange(0,20)
            if base < 16:
                base = 16

        elif modificador > 8:
            base = base + random.randrange(0,21)

        if self._raca == None:
            self.gera_raca()

        self._idade = int(base*coeficientes[self._raca])

    def gera_nome(self):
        if self._raca == None:
            self.gera_raca()

        if self._genero == None:
            self.gera_genero()
        
        if self._raca == 'Anão' or self._raca == 'Draconato' or self._raca == 'Halfling' or self._raca == 'Gnomo' or self._raca =='Meio-Orc' or self._raca == 'Tiefling' or self._raca.find('Orc') != -1:
                if self._raca.find('Orc') != -1:
                    raca = 'Meio-Orc'
                else: 
                    raca = self._raca

                nomeG = nomes[raca][self._genero][random.randrange(0,len(nomes[raca][self._genero]))].strip()
        elif self._raca.find('Elfo') != -1 or self._raca == 'Humano':
            if self._raca.find('Elfo') != -1:
                raca = 'Elfo'
            else: 
                raca = self._raca

            nomeG = nomes[raca][self._genero][random.randrange(0,len(nomes[raca][self._genero]))].strip() + ' ' + nomes[raca]['Sobrenomes'][random.randrange(0,len(nomes[raca]['Sobrenomes']))].strip()
        else: 
            nomeG = self.gera_nome_aleatorio()

        self._nome = nomeG
    
    def gera_raca(self):
        numero = random.randrange(0,len(lista_racas))
        self._raca = lista_racas[numero]

    def gera_alinhamento_CO(self):
        numero = random.randrange(0,len(lista_alinhamento_CO))
        self._alinhamento_CO = lista_alinhamento_CO[numero]
    
    def gera_alinhamento_BM(self):
        numero = random.randrange(0,len(lista_alinhamento_BM))
        self._alinhamento_BM = lista_alinhamento_BM[numero]

    def gera_alinhamento(self):
        if self._alinhamento_BM == None:
            self.gera_alinhamento_BM()
        if self._alinhamento_CO == None:
            self.gera_alinhamento_CO()
        if self._alinhamento == None:
            self._alinhamento = self._alinhamento_CO + ' | ' + self._alinhamento_BM
        
    def gera_caracteristicas_fisicas(self):
        caracteristicas = ''
        if self._raca == None:
            self.gera_raca()
        if self._genero == None:
            self.gera_genero()
        if self._idade == None:
            self.gera_idade()

        lista_caracteristicas_fisicas = []
        olhos = listaOlhos[random.randrange(0,len(listaOlhos))].capitalize()
        lista_caracteristicas_fisicas.append(olhos)
        porte = listaporte[random.randrange(0,len(listaporte))].capitalize()
        lista_caracteristicas_fisicas.append(porte)
        altura = listaaltura[random.randrange(0,len(listaaltura))].capitalize()
        lista_caracteristicas_fisicas.append(altura)

        if self._raca in grupo1 + grupo3 + grupo4 + grupo5:
            cabelo = listacabelo[random.randrange(0,len(listacabelo))].capitalize()
            lista_caracteristicas_fisicas.append(cabelo)
            corpelos = listacorpelos[random.randrange(0,len(listacorpelos))].capitalize()
            lista_caracteristicas_fisicas.append(f'Pelo/cabelo {corpelos}')
            if self._genero == "Masculino" and self._idade > 16*coeficientes[self._raca]:
                barba = listabarba[random.randrange(0,len(listabarba))].capitalize()
                lista_caracteristicas_fisicas.append(barba)

        if self._raca in grupo1 + grupo4:
            cor = listacornormais[random.randrange(0,len(listacornormais))].capitalize()
            lista_caracteristicas_fisicas.append(f'Pele {cor}')
        elif self._raca in grupo2 + grupo3 + grupo5 + grupo6 + grupo7:
            cor = listacorexoticas[random.randrange(0,len(listacorexoticas))]
            lista_caracteristicas_fisicas.append(f'Pele {cor}')

        if self._raca in grupo4 + grupo7:
            asa = listaasas[random.randrange(0,len(listaasas))].capitalize()
            lista_caracteristicas_fisicas.append(asa)

        if self._raca in grupo2 + grupo5:
            chifre = listachifres[random.randrange(0,len(listachifres))].capitalize()
            lista_caracteristicas_fisicas.append(chifre)
            rabo = listarabo[random.randrange(0,len(listarabo))].capitalize()
            lista_caracteristicas_fisicas.append(rabo)

        self._caracteristicas_fisicas = ", ".join(lista_caracteristicas_fisicas)

    def gera_caracteristicas_pessoais(self):
        if self._alinhamento == None:
            self.gera_alinhamento()

        while len(self._qualidades) <3:
            numero = random.randrange(0,len(listaqualidade))
            if (listaqualidade[numero].capitalize() not in self._qualidades) and ((listaqualidade[numero],self._alinhamento_BM) not in listaproibidos) and ((listaqualidade[numero],self._alinhamento_CO) not in listaproibidos):
                self._qualidades.append(listaqualidade[numero].capitalize())

        while len(self._defeitos) < 3:
            numero = random.randrange(0,len(listadefeitos))
            antonimo = False
            if (listadefeitos[numero].capitalize() not in self._defeitos) and ((listadefeitos[numero],self._alinhamento_BM) not in listaproibidos) and ((listadefeitos[numero],self._alinhamento_CO) not in listaproibidos):
                for qualidade in listaqualidade:
                    if (qualidade,listadefeitos[numero]) in listaantonimos :
                        antonimo = True
                if not antonimo:
                    self._defeitos.append(listadefeitos[numero].capitalize())

        self._caracteristicas_pessoais = ", ".join(self._qualidades + self._defeitos )

    def gera_classe(self):
        if self._classe_jog:
            lista = classes_npc + classes_jog
            numero = random.randrange(0,len(lista))
            self._classe = lista[numero]
        else:
            numero = random.randrange(0,len(classes_npc))
            self._classe = classes_npc[numero]

    def gera_riqueza(self):
        numero = random.randrange(0,len(riquezas))
        self._riqueza = riquezas[numero]

    def gera_genero(self):
        numero = random.randrange(0,2)
        if numero == 0: self._genero = 'Masculino' 
        else: self._genero = 'Feminino'

    def trata_listas(self,lista):
        base = ", ".join(lista)
        return base

class Neutro(NPC):
    def __init__(self):
        super().__init__()
        self._ocupacao = None

    def gera_ocupacao(self):
        numero = random.randrange(0,len(ocupacoes))
        self._ocupacao = ocupacoes[numero]

class Vilao(NPC):
    def __init__(self):
        super().__init__()
        self._motivacao = None
        self._influencia = None
        self._poderes = None

    def gera_motivacao(self):
         while self._motivacao == None:
            numero = random.randrange(0,len(motivacoes))
            motivacao = motivacoes[numero]
            if ((motivacao,self._alinhamento_CO) not in listaproibidos) and ((motivacao,self._alinhamento_BM) not in listaproibidos) :
                self._motivacao = motivacao

    def gera_influencia(self):
        numero1 = random.randrange(0,len(tipo_influencia))
        numero2 = random.randrange(0,len(tamanho_influencia))
        self._influencia = tamanho_influencia[numero2] + " | " + tipo_influencia[numero1]

    def gera_poderes(self):
        numero = random.randrange(0,len(poderes))
        self._poderes = poderes[numero]