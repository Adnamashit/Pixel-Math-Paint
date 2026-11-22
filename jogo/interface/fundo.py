import random

import pyxel

from jogo.configuracoes import ALTURA, ARCO_IRIS, LARGURA


class PixelsCaindo:
    """Fundo animado do menu: quadradinhos coloridos caindo."""

    def __init__(self, quantidade=45):
        # cada gota: [x, y, velocidade, cor, tamanho]
        self.gotas = [[random.uniform(0, LARGURA), random.uniform(0, ALTURA),
                       random.uniform(0.3, 1.2), random.choice(ARCO_IRIS), random.choice([1, 2, 3])]
                      for _ in range(quantidade)]

    def atualizar(self):
        for gota in self.gotas:
            gota[1] += gota[2]
            if gota[1] > ALTURA:                     # saiu pela base: volta para o topo
                gota[0], gota[1] = random.uniform(0, LARGURA), -4

    def desenhar(self):
        for x, y, _, cor, tamanho in self.gotas:
            pyxel.rect(int(x), int(y), tamanho, tamanho, cor)
