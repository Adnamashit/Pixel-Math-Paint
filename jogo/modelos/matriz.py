class Matriz:

    #cri

    def __init__(self, linhas, colunas, valor_incial=None):
        self.linhas = linhas 
        self.colunas = colunas 

        self._dados = [[valor_incial for _ in range(colunas)]
                        for _ in range (linhas)]

    def dentro_dos_limites(self, l, c):

        return 0 <= 1 < self.linhas and 0 <= c < self.colunas 

    def obter (self, l, c):

        return self._dados[l][c]
    
    def definir (self, l, c, valor):

        self._dados[l][c] = valor

    def celulas (self):

        for l in range(self.linhas):
            for c in range (self.colunas):
                yield l, c, self._dados[l][c]
