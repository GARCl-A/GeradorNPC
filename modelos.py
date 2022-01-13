import random
from listas import *

class NPC():
    def __init__(self):
        self._nome = None
        self._raça = None
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

    def set_nome(self,nome):
        self._nome = nome
    
    def set_raça(self,raça):
        self._raça = raça

    def set_alinhamento_CO(self,alinhamento_CO):
        self._alinhamento_CO = alinhamento_CO

    def set_alinhamento_BM(self,alinhamento_BM):
        self._alinhamento_BM = alinhamento_BM

    def set_caracteristicas_fisicas(self,caracteristicas_fisicas):
        self._caracteristicas_fisicas = caracteristicas_fisicas

    def set_caracteristicas_pessoais(self,caracteristicas_pessoais):
        self._caracteristicas_pessoais = caracteristicas_pessoais

    def set_classe(self,classe):
        self._classe = classe

    def set_riqueza(self,riqueza):
        self._riqueza = riqueza

    def set_genero(self,genero):
        self._genero = genero

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

    def gera_nome(self):
        if self._raça == None:
            self.gera_raça()
        if self._genero == None:
            self.gera_genero
        
        if self._raça == 'Anão' or self._raça == 'Draconato' or self._raça == 'Halfling' or self._raça == 'Gnomo' or self._raça =='Meio-Orc' or self._raça == 'Tiefling' or self._raça.find('Orc') != -1:
                if self._raça.find('Orc') != -1:
                    raça = 'Meio-Orc'
                else: 
                    raça = self._raça

                nomeG = nomes[raça][self._genero][random.randrange(0,len(nomes[raça][self._genero]))].strip()

        elif self._raça.find('Elfo') != -1 or self._raça == 'Humano':
            if self._raça.find('Elfo') != -1:
                raça = 'Elfo'
            else: 
                raça = self._raça

            nomeG = nomes[raça][self._genero][random.randrange(0,len(nomes[raça][self._genero]))].strip() + ' ' + nomes[raça]['Sobrenomes'][random.randrange(0,len(nomes[raça]['Sobrenomes']))].strip()

        else: 
            nomeG = self.gera_nome_aleatorio()

        self._nome = nomeG
    
    def gera_raça(self):
        numero = random.randrange(0,len(lista_raças))
        self._raça = lista_raças[numero]

    def gera_alinhamento_CO(self):
        numero = random.randrange(0,len(lista_alinhamento_CO))
        self._alinhamento_CO = lista_alinhamento_CO[numero]
    
    def gera_alinhamento_BM(self):
        numero = random.randrange(0,len(lista_alinhamento_BM))
        self._alinhamento_BM = lista_alinhamento_BM[numero]

    def gera_alinhamento(self):
        self._alinhamento = self._alinhamento_CO + ' | ' + self._alinhamento_BM
        
    def gera_caracteristicas_fisicas(self):
        caracteristicas = ''
        
        if self._raça == "Humano" or self._raça == "Anão" or self._raça == "Elfo" or self._raça =="Gnomo"or self._raça =="Halfling" or self._raça == "Gigante" or self._raça =="Meio-Elfo" or self._raça == "Golias":
            olhos = listaOlhos[random.randrange(0,len(listaOlhos))]
            cabelo = listacabelo[random.randrange(0,len(listacabelo))]
            barba = listabarba[random.randrange(0,len(listabarba))]
            corpelos = listacorpelos[random.randrange(0,len(listacorpelos))]
            altura = listaaltura[random.randrange(0,len(listaaltura))]
            corpo = listaporte[random.randrange(0,len(listaporte))]
            cor = listacornormais[random.randrange(0,len(listacornormais))]

            caracteristicas = olhos+", " +cabelo+", " +barba+"\n        " +corpelos+", " +altura+", " +corpo+", " +cor
        if self._raça == "Kobold" or self._raça == "Lizardfolk" or self._raça == "Draconato" or self._raça == "Tiefling" :
            olhos= listaOlhos[random.randrange(0,len(listaOlhos))]           
            altura= listaaltura[random.randrange(0,len(listaaltura))]
            corpo = listaporte[random.randrange(0,len(listaporte))]
            cor= listacordemoniolagarto[random.randrange(0,len(listacordemoniolagarto))]
            chifre= listachifres[random.randrange(0,len(listachifres))]
            rabo= listarabo[random.randrange(0,len(listarabo))]

            caracteristicas = olhos+", " +chifre+", " +rabo+"\n         " +altura+", " +corpo+", " +cor
        
        if self._raça == "Orc" or self._raça == "Goblin" or self._raça == "Gnoll" or self._raça =="Ikidaris"or self._raça =="Meio-Orc" or self._raça == "Forjados" or self._raça =="Genasi" :
            olhos = listaOlhos[random.randrange(0,len(listaOlhos))]
            cabelo = listacabelo[random.randrange(0,len(listacabelo))]
            barba = listabarba[random.randrange(0,len(listabarba))]
            corpelos = listacorpelos[random.randrange(0,len(listacorpelos))]
            altura = listaaltura[random.randrange(0,len(listaaltura))]
            corpo = listaporte[random.randrange(0,len(listaporte))]
            cor = listacordemoniolagarto[random.randrange(0,len(listacordemoniolagarto))]

            caracteristicas= olhos+", " +cabelo+", " +barba+"\n         " +corpelos+", " +altura+", " +corpo+", " +cor
        if self._raça == "Sprite" or self._raça == "Aasimar"  : 
            olhos= listaOlhos[random.randrange(0,len(listaOlhos))]
            cabelo= listacabelo[random.randrange(0,len(listacabelo))]
            barba= listabarba[random.randrange(0,len(listabarba))]
            corpelos= listacorpelos[random.randrange(0,len(listacorpelos))]
            altura= listaaltura[random.randrange(0,len(listaaltura))]
            corpo= listaporte[random.randrange(0,len(listaporte))]
            cor= listacornormais[random.randrange(0,len(listacornormais))]
            asa= listaasas[random.randrange(0,len(listaasas))]

            caracteristicas= olhos+", " +cabelo+", " +barba+"\n         " +corpelos+", " +altura+", " +corpo+", " +cor+", " +asa
        if   self._raça == "Leshy" :
            olhos= listaOlhos[random.randrange(0,len(listaOlhos))]
            altura= listaaltura[random.randrange(0,len(listaaltura))]
            corpo= listaporte[random.randrange(0,len(listaporte))]
            cor= listacornormais[random.randrange(0,len(listacornormais))]
            chifre= listachifres[random.randrange(0,len(listachifres))]

            caracteristicas= olhos+ ", " +altura + ", " +cor +"\n           " +chifre+", " +corpo
        if   self._raça == "Centauros": 
            olhos= listaOlhos[random.randrange(0,len(listaOlhos))]
            corpelos= listacorpelos[random.randrange(0,len(listacorpelos))]
            altura= listaaltura[random.randrange(0,len(listaaltura))]
            corpo= listaporte[random.randrange(0,len(listaporte))]
            cor= listacornormais[random.randrange(0,len(listacornormais))]
            chifre= listachifres[random.randrange(0,len(listachifres))]

            caracteristicas=olhos+", " +corpelos+", " +altura+"\n           " +corpo+", " +cor+", " +chifre
        if self._raça == "Kenku" or self._raça == "Aarakocra"  :    
            olhos= listaOlhos[random.randrange(0,len(listaOlhos))]
            altura= listaaltura[random.randrange(0,len(listaaltura))]
            corpo= listaporte[random.randrange(0,len(listaporte))]
            cor= listacornormais[random.randrange(0,len(listacornormais))]
            asa= listaasas[random.randrange(0,len(listaasas))]

            caracteristicas= olhos + ", " + altura  + ", " + corpo+"\n          " +cor

        self._caracteristicas_fisicas = caracteristicas

    def gera_caracteristicas_pessoais(self):
        while len(self._qualidades) <3:
            numero = random.randrange(0,len(listaqualidade))
            if listaqualidade[numero] not in self._qualidades:
                self._qualidades.append(listaqualidade[numero])
        while len(self._defeitos) < 3:
            numero = random.randrange(0,len(listadefeitos))
            antonimo = False
            if listadefeitos[numero] not in self._defeitos:
                for qualidade in listaqualidade:
                    if (listadefeitos[numero],qualidade) in listaantonimos or (qualidade,listadefeitos[numero]) in listaantonimos :
                        antonimo = True
                if not antonimo:
                    self._defeitos.append(listadefeitos[numero])
        self._caracteristicas_pessoais = self.trata_listas(self._qualidades) + '\n          ' +self.trata_listas(self._defeitos)

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
        self._ocupaçao = None

    def set_ocupacao(self,ocupacao):
        self._ocupaçao = ocupacao

    def gera_ocupacao(self):
        numero = random.randrange(0,len(ocupaçoes))
        self._ocupaçao = ocupaçoes[numero]

    def __str__(self):
        return f'''Nome: {self._nome}
Gênero: {self._genero}
Raça: {self._raça}
Classe: {self._classe}
Alinhamento: {self._alinhamento}
Características Físicas: {self._caracteristicas_fisicas}
Características Pessoais: {self._caracteristicas_pessoais}
Riqueza: {self._riqueza}
Ocupação: {self._ocupaçao}
-
'''

class Vilao(NPC):
    def __init__(self):
        super().__init__()
        self._motivacao = None
        self._influencia = None
        self._poderes = None
    
    def set_motivacao(self,motivacao):
        self._motivacao = motivacao

    def set_influencia(self,influencia):
        self._influencia = influencia

    def set_poderes(self,poderes):
        self._poderes = poderes

    def gera_motivacao(self):
        numero = random.randrange(0,len(motivacoes))
        self._motivacao = motivacoes[numero]

    def gera_influencia(self):
        numero1 = random.randrange(0,len(tipo_influencia))
        numero2 = random.randrange(0,len(tamanho_influencia))
        self._influencia = tamanho_influencia[numero2] + " | " + tipo_influencia[numero1]

    def gera_poderes(self):
        numero = random.randrange(0,len(poderes))
        self._poderes = poderes[numero]

    def __str__(self):
        return f'''Nome: {self._nome}
Gênero: {self._genero}
Raça: {self._raça}
Classe: {self._classe}
Alinhamento: {self._alinhamento}
Características Físicas: {self._caracteristicas_fisicas}
Características Pessoais: {self._caracteristicas_pessoais}
Riqueza: {self._riqueza}
Motivação: {self._motivacao}
Influência: {self._influencia}
Poderes: {self._poderes}
-
'''

teste = Vilao()
teste.gera_raça()
teste.gera_caracteristicas_fisicas()
print(teste,'\n',teste._caracteristicas_fisicas)
