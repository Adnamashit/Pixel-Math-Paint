"""Fase 3 - Algebra e geometria (inclui determinante de matriz)."""
from jogo.problemas.base import Problema, assinado


class EquacaoSegundoGrau(Problema):
    categoria = "Equacao do 2o grau"

    def montar(self):
        while True:     # sorteia raizes inteiras, diferentes de zero e de soma nao nula
            r1, r2 = self.sorteio.randint(-6, 6), self.sorteio.randint(-6, 6)
            if r1 != 0 and r2 != 0 and r1 < r2 and r1 + r2 != 0:
                break
        b, c = -(r1 + r2), r1 * r2      # x^2 - (soma)x + (produto) = 0
        return [f"x^2 {assinado(b)}x {assinado(c)} = 0", "Qual e a MAIOR raiz?"], r2


class Determinante(Problema):
    categoria = "Determinante 2x2"

    def montar(self):
        a, b, c, d = (self.sorteio.randint(-3, 9) for _ in range(4))
        return [f"| {a:>2}  {b:>2} |", f"| {c:>2}  {d:>2} |", "Qual e o determinante?"], a * d - b * c


class Pitagoras(Problema):
    categoria = "Teorema de Pitagoras"
    TERNOS = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (9, 12, 15), (7, 24, 25)]

    def montar(self):
        cateto_a, cateto_b, hipotenusa = self.sorteio.choice(self.TERNOS)
        return [f"Triangulo retangulo, catetos {cateto_a} e {cateto_b}.", "Quanto mede a hipotenusa?"], hipotenusa


class SistemaLinear(Problema):
    categoria = "Sistema linear"

    def montar(self):
        x, y = self.sorteio.randint(1, 9), self.sorteio.randint(1, 9)
        return [f"x + y = {x + y}", f"x - y = {x - y}", "Quanto vale x * y?"], x * y


class Logaritmo(Problema):
    categoria = "Logaritmo"

    def montar(self):
        base = self.sorteio.choice([2, 3, 5, 10])
        expoente = self.sorteio.randint(2, 5)
        return [f"Qual o logaritmo de {base ** expoente}", f"na base {base}?"], expoente


TIPOS = [EquacaoSegundoGrau, Determinante, Pitagoras, SistemaLinear, Logaritmo]
