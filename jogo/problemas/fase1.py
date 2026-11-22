"""Fase 1 - Matematica basica."""
from jogo.problemas.base import Problema


class SomaSubtracao(Problema):
    categoria = "Soma e subtracao"

    def montar(self):
        a, b, c = self.sorteio.randint(20, 99), self.sorteio.randint(20, 99), self.sorteio.randint(1, 19)
        return [f"{a} + {b} - {c} = ?"], a + b - c


class MultiplicacaoSoma(Problema):
    categoria = "Multiplicacao"

    def montar(self):
        a, b, c = self.sorteio.randint(6, 15), self.sorteio.randint(3, 12), self.sorteio.randint(1, 20)
        return [f"{a} x {b} + {c} = ?"], a * b + c


class DivisaoSoma(Problema):
    categoria = "Divisao"

    def montar(self):
        divisor, quociente, c = self.sorteio.randint(3, 12), self.sorteio.randint(4, 15), self.sorteio.randint(1, 20)
        return [f"{divisor * quociente} / {divisor} + {c} = ?"], quociente + c


class Porcentagem(Problema):
    categoria = "Porcentagem"

    def montar(self):
        percentual = self.sorteio.choice([10, 20, 25, 50, 75])
        base = self.sorteio.choice([40, 80, 120, 160, 200, 240])
        return [f"Quanto e {percentual}% de {base}?"], base * percentual // 100


class Potencias(Problema):
    categoria = "Potencias"

    def montar(self):
        a, b = self.sorteio.randint(2, 9), self.sorteio.randint(2, 9)
        return [f"{a}^2 + {b}^2 = ?"], a * a + b * b


TIPOS = [SomaSubtracao, MultiplicacaoSoma, DivisaoSoma, Porcentagem, Potencias]
