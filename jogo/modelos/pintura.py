# NOVO: a classe Pintura controla o estado de UMA pintura em andamento.
from jogo.modelos.matriz import Matriz


class Pintura:
    """Guarda a imagem correta, o que ja foi pintado e quais cores estao liberadas."""

    def __init__(self, info_fase):
        self.info_fase = info_fase
        self.solucao = info_fase.para_matriz()     # Matriz com a cor certa de cada celula
        # Segunda Matriz: True/False dizendo se a celula ja foi pintada
        self.pintadas = Matriz(self.solucao.linhas, self.solucao.colunas, False)

        self.cores = []        # cores da imagem, na ordem em que aparecem
        self._totais = {}      # dicionario: cor -> quantas celulas tem essa cor
        for _, _, cor in self.solucao.celulas():
            if cor is None:
                continue
            if cor not in self._totais:
                self.cores.append(cor)
                self._totais[cor] = 0
            self._totais[cor] += 1

        self._restantes = dict(self._totais)   # cor -> quantas ainda faltam pintar
        self.liberadas = set()                 # cores ja desbloqueadas pelo jogador
        self.total_celulas = sum(self._totais.values())
        self.celulas_feitas = 0

    # --- cores ---
    def liberar(self, cor):
        self.liberadas.add(cor)

    def esta_liberada(self, cor):
        return cor in self.liberadas

    def total_da_cor(self, cor):
        return self._totais[cor]

    def restantes_da_cor(self, cor):
        return self._restantes[cor]

    # --- pintura ---
    def pode_pintar(self, l, c):
        # so pinta celula da imagem, de cor liberada e que ainda nao foi pintada
        if not self.solucao.dentro_dos_limites(l, c):
            return False
        cor = self.solucao.obter(l, c)
        return cor is not None and cor in self.liberadas and not self.pintadas.obter(l, c)

    def pintar(self, l, c):
        # pinta a celula e devolve a cor usada (ou None se nao era possivel)
        if not self.pode_pintar(l, c):
            return None
        cor = self.solucao.obter(l, c)
        self.pintadas.definir(l, c, True)
        self._restantes[cor] -= 1
        self.celulas_feitas += 1
        return cor

    @property
    def progresso(self):
        return self.celulas_feitas / self.total_celulas    # de 0.0 a 1.0

    @property
    def esta_completa(self):
        return self.celulas_feitas >= self.total_celulas
