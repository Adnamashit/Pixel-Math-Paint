class Cena:

    def __init__(self, aplicativo):
        self.aplicativo = aplicativo

    def ao_entrar(self):
        pass

    def atualizar(self):
        raise NotImplementedError

    def desenhar(self):
        raise NotImplementedError
    
    