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
        pass

    def gera_alinhamento(self):
        pass

    def gera_caracteristicas_fisicas(self):
        pass

    def gera_caracteristicas_pessoais(self):
        pass

    def gera_classe(self):
        pass

    def gera_riqueza(self):
        pass

    def gera_genero(self):
        pass

class Pacifico(NPC):
    def __init__(self):
        super().__init__()
        self._ocupaçao = None

    def set_ocupacao(self,ocupacao):
        pass

    def gera_ocupacao(self):
        pass

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
        pass

    def gera_influencia(self):
        pass

    def gera_poderes(self):
        pass