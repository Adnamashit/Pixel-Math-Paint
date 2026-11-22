"""Fase 4 - Pre-calculo."""
import math

from jogo.problemas.base import Problema


class Trigonometria(Problema):
    categoria = "Trigonometria"
    # (funcao, angulo em graus, numerador, denominador do valor)
    TABELA = [("sen", 30, 1, 2), ("cos", 60, 1, 2), ("sen", 90, 1, 1), ("cos", 0, 1, 1),
              ("tg", 45, 1, 1), ("cos", 180, -1, 1), ("sen", 0, 0, 1), ("cos", 90, 0, 1)]

    def montar(self):
        (f1, ang1, num1, den1), (f2, ang2, num2, den2) = self.sorteio.sample(self.TABELA, 2)
        k1, k2 = self.sorteio.choice([2, 4, 6, 8, 10]), self.sorteio.choice([2, 4, 6, 8, 10])
        linhas = [f"{k1}*{f1}({ang1}) + {k2}*{f2}({ang2}) = ?", "(angulos em graus)"]
        return linhas, k1 * num1 // den1 + k2 * num2 // den2


class Exponencial(Problema):
    categoria = "Equacao exponencial"

    def montar(self):
        base = self.sorteio.choice([2, 3])
        k = self.sorteio.randint(3, 6) if base == 2 else self.sorteio.randint(2, 4)
        c = self.sorteio.randint(1, 5)
        return [f"{base}^(x - {c}) = {base ** k}", "Quanto vale x?"], k + c


class LimiteFatoracao(Problema):
    categoria = "Limite (fatoracao)"

    def montar(self):
        a, b = self.sorteio.sample(range(1, 10), 2)
        # (x-a)(x-b)/(x-a) -> (x-b) -> a-b quando x tende a a
        return [f"lim (x^2 - {a + b}x + {a * b}) / (x - {a})", f"quando x tende a {a}"], a - b


class Somatorio(Problema):
    categoria = "Somatorio"

    def montar(self):
        n = self.sorteio.choice([10, 12, 15, 20, 25, 30, 40, 50])
        return [f"Some os inteiros de 1 ate {n}:", f"1 + 2 + 3 + ... + {n}"], n * (n + 1) // 2


class Combinatoria(Problema):
    categoria = "Analise combinatoria"

    def montar(self):
        n, k = self.sorteio.randint(6, 10), self.sorteio.choice([2, 3])
        return [f"Um grupo tem {n} pessoas. De quantas", f"formas escolher {k} para um comite?"], math.comb(n, k)


class FuncaoComposta(Problema):
    categoria = "Funcao composta"

    def montar(self):
        a, b, c, p = (self.sorteio.randint(2, 5), self.sorteio.randint(1, 9),
                      self.sorteio.randint(1, 6), self.sorteio.randint(2, 5))
        return [f"f(x) = {a}x + {b}   g(x) = x^2 - {c}", f"Calcule f(g({p}))"], a * (p * p - c) + b


TIPOS = [Trigonometria, Exponencial, LimiteFatoracao, Somatorio, Combinatoria, FuncaoComposta]
