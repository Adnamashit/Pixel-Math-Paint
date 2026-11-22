"""Fase 2 - Algebra elementar."""
from jogo.problemas.base import Problema


class EquacaoPrimeiroGrau(Problema):
    categoria = "Equacao do 1o grau"

    def montar(self):
        a, x, b = self.sorteio.randint(2, 9), self.sorteio.randint(-8, 12), self.sorteio.randint(1, 20)
        return [f"{a}x + {b} = {a * x + b}", "Quanto vale x?"], x


class EquacaoDoisLados(Problema):
    categoria = "Equacao com x nos dois lados"

    def montar(self):
        a, c = self.sorteio.randint(5, 9), self.sorteio.randint(2, 4)
        x, b = self.sorteio.randint(-5, 9), self.sorteio.randint(1, 15)
        d = (a - c) * x + b     # garante que x seja a solucao
        return [f"{a}x + {b} = {c}x + {d}", "Quanto vale x?"], x


class RaizQuadrada(Problema):
    categoria = "Raiz quadrada"

    def montar(self):
        n, m = self.sorteio.randint(4, 15), self.sorteio.randint(1, 9)
        return [f"raiz({n * n}) + {m} = ?"], n + m


class RegraDeTres(Problema):
    categoria = "Regra de tres"

    def montar(self):
        quantidade, preco_unitario = self.sorteio.randint(2, 6), self.sorteio.randint(2, 9)
        outra = self.sorteio.randint(quantidade + 1, 12)
        return [f"Se {quantidade} canetas custam R$ {quantidade * preco_unitario},",
                f"quanto custam {outra} canetas?"], outra * preco_unitario


class ProgressaoAritmetica(Problema):
    categoria = "Progressao aritmetica"

    def montar(self):
        a1, razao, n = self.sorteio.randint(1, 9), self.sorteio.randint(2, 7), self.sorteio.randint(8, 15)
        return [f"Numa PA com a1 = {a1} e razao {razao},", f"qual e o termo a{n}?"], a1 + (n - 1) * razao


TIPOS = [EquacaoPrimeiroGrau, EquacaoDoisLados, RaizQuadrada, RegraDeTres, ProgressaoAritmetica]
