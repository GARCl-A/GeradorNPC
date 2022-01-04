import random
from listas import *

class NPC():
    def __init__(self):
        self._nome = None
        self._raça = None
        self._alinhamento = None
        self._caracteristicas_fisicas = None
        self._caracteristicas_pessoais = None
        self._classe = None
        self._riqueza = None
        self._genero = None
        self._classe_jog = True

    def set_nome(self,nome):
        pass
    
    def set_raça(self,raça):
        pass

    def set_alinhamento(self,alinhamento):
        pass

    def set_caracteristicas_fisicas(self,caracteristicas_fisicas):
        pass

    def set_caracteristicas_pessoais(self,caracteristicas_pessoais):
        pass

    def set_classe(self,classe):
        pass

    def set_riqueza(self,riqueza):
        pass

    def set_genero(self,genero):
        pass

    def gera_nome(self):
        pass
    
    def gera_raça(self):
        numero = random.randrange(0,len(lista_raças))
        self._raça = lista_raças[numero]

    def gera_alinhamento(self):
        numero1 = random.randrange(0,len(lista_alinhamento_CO))
        numero2 = random.randrange(0,len(lista_alinhamento_BM))
        self._alinhamento = lista_alinhamento_CO[numero1] + " " + lista_alinhamento_BM[numero2]
        
    def gera_caracteristicas_fisicas(self):
        pass

    def gera_caracteristicas_pessoais(self):
        pass

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

class Pacifico(NPC):
    def __init__(self):
        super().__init__()
        self._ocupaçao = None

    def set_ocupacao(self,ocupacao):
        pass

    def gera_ocupacao(self):
        numero = random.randrange(0,len(ocupaçoes))
        self._ocupaçao = ocupaçoes[numero]

class Vilao(NPC):
    def __init__(self):
        super().__init__()
        self._motivacao = None
        self._influencia = None
        self._poderes = None
    
    def set_motivacao(self,motivacao):
        pass

    def set_influencia(self,influencia):
        pass

    def set_poderes(self,poderes):
        pass

    def gera_motivacao(self):
        numero = random.randrange(0,len(motivacoes))
        self._motivacao = motivacoes[numero]

    def gera_influencia(self):
        pass

    def gera_poderes(self):
        pass

teste = Vilao()
teste.gera_raça()
teste.gera_alinhamento()
teste.gera_classe()
teste.gera_riqueza()
teste.gera_motivacao()
teste.gera_genero()
print(vars(teste))