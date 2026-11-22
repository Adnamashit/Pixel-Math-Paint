class Matriz:
    """Tabela de linhas e colunas. Cada celula guarda um valor."""
    # No jogo usamos uma Matriz para a imagem (cada celula = uma cor)
    # e outra para saber quais celulas ja foram pintadas.

    def __init__(self, linhas, colunas, valor_inicial=None):   # (corrigido: era valor_incial)
        self.linhas = linhas
        self.colunas = colunas
        # lista de listas: cada lista de dentro e uma linha da tabela
        self._dados = [[valor_inicial for _ in range(colunas)]
                       for _ in range(linhas)]

    def dentro_dos_limites(self, l, c):
        # True se a linha l e a coluna c existem (comecam em 0)
        return 0 <= l < self.linhas and 0 <= c < self.colunas

    def obter(self, l, c):
        return self._dados[l][c]

    def definir(self, l, c, valor):
        self._dados[l][c] = valor

    def celulas(self):
        # percorre a tabela inteira, linha por linha, entregando (linha, coluna, valor)
        for l in range(self.linhas):
            for c in range(self.colunas):
                yield l, c, self._dados[l][c]

    def contar(self, condicao):
        # NOVO: conta quantas celulas satisfazem a condicao (uma funcao que recebe o valor)
        return sum(1 for _, _, valor in self.celulas() if condicao(valor))
