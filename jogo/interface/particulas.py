import random

import pyxel

from jogo.configuracoes import ARCO_IRIS


class Particula:
    def __init__(self, x, y, vx, vy, vida, cor, gravidade=0.1):
        self.x, self.y, self.vx, self.vy = x, y, vx, vy
        self.vida, self.cor, self.gravidade = vida, cor, gravidade

    def atualizar(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravidade      # a gravidade puxa para baixo
        self.vida -= 1


class SistemaParticulas:
    """Efeitos visuais: explosao de quadradinhos e chuva de confete."""

    def __init__(self):
        self.itens = []

    def explosao(self, x, y, cor, quantidade=12, velocidade=2.0, vida=22):
        for _ in range(quantidade):
            self.itens.append(Particula(x, y, random.uniform(-velocidade, velocidade),
                                        random.uniform(-velocidade, velocidade),
                                        vida + random.randint(0, 8), cor))

    def confete(self, quantidade=40):
        for _ in range(quantidade):
            self.itens.append(Particula(random.uniform(0, 256), random.uniform(-20, 0),
                                        random.uniform(-0.5, 0.5), random.uniform(0.5, 1.5),
                                        random.randint(120, 200), random.choice(ARCO_IRIS), 0.01))

    def atualizar(self):
        for p in self.itens:
            p.atualizar()
        self.itens = [p for p in self.itens if p.vida > 0]    # tira as que "morreram"

    def desenhar(self):
        for p in self.itens:
            pyxel.rect(int(p.x), int(p.y), 2, 2, p.cor)
