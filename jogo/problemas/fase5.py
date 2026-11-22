"""Fase 5 - Calculo I."""
from jogo.problemas.base import Problema


class DerivadaNoPonto(Problema):
    categoria = "Derivada em um ponto"

    def montar(self):
        a, b, c, p = (self.sorteio.randint(1, 4), self.sorteio.randint(1, 5),
                      self.sorteio.randint(1, 9), self.sorteio.randint(1, 3))
        # f'(x) = 3a x^2 + 2b x + c
        return [f"f(x) = {a}x^3 + {b}x^2 + {c}x", f"Calcule f'({p})"], 3 * a * p * p + 2 * b * p + c


class IntegralDefinida(Problema):
    categoria = "Integral definida"

    def montar(self):
        a, n, b = 2 * self.sorteio.randint(1, 4), self.sorteio.randint(2, 5), self.sorteio.randint(1, 6)
        # integral de 0 ate n de (ax + b) dx = a*n^2/2 + b*n
        return [f"Calcule a integral de 0 ate {n}", f"de ({a}x + {b}) dx"], a * n * n // 2 + b * n


class LimiteFundamental(Problema):
    categoria = "Limite fundamental"

    def montar(self):
        b, k = self.sorteio.randint(1, 4), self.sorteio.randint(2, 5)
        denominador = "x" if b == 1 else f"{b}x"
        # lim sen(ax)/(bx) = a/b, com a = b*k
        return [f"lim x->0 de sen({b * k}x) / {denominador}", "Quanto vale o limite?"], k


class LimiteNoInfinito(Problema):
    categoria = "Limite no infinito"

    def montar(self):
        d, k = self.sorteio.randint(1, 4), self.sorteio.randint(2, 5)
        b, c, e = (self.sorteio.randint(1, 9) for _ in range(3))
        # so contam os termos de maior grau: (d*k)/d = k
        return ["Limite quando x -> infinito de",
                f"({d * k}x^2 + {b}x + {c}) / ({d}x^2 + {e})"], k


class PontoDeMinimo(Problema):
    categoria = "Ponto de minimo"

    def montar(self):
        a, m, c = self.sorteio.randint(1, 3), self.sorteio.randint(1, 9), self.sorteio.randint(1, 9)
        coef_a = "" if a == 1 else str(a)
        # f'(x) = 2a x - 2a m = 0  ->  x = m
        return [f"f(x) = {coef_a}x^2 - {2 * a * m}x + {c}", "Em qual x f tem seu minimo?"], m


class RegraDaCadeia(Problema):
    categoria = "Regra da cadeia"

    def montar(self):
        c = self.sorteio.randint(1, 3)
        # f'(x) = 3(x^2+c)^2 * 2x  ->  f'(1) = 6(1+c)^2
        return [f"f(x) = (x^2 + {c})^3", "Calcule f'(1)"], 6 * (1 + c) ** 2


class DerivadaSenoExp(Problema):
    categoria = "Derivada de sen e e^x"

    def montar(self):
        a, b = self.sorteio.randint(2, 9), self.sorteio.randint(2, 9)
        # f'(x) = a cos(x) + b e^x  ->  f'(0) = a + b
        return [f"f(x) = {a}sen(x) + {b}e^x", "Calcule f'(0)"], a + b


TIPOS = [DerivadaNoPonto, IntegralDefinida, LimiteFundamental, LimiteNoInfinito,
         PontoDeMinimo, RegraDaCadeia, DerivadaSenoExp]
