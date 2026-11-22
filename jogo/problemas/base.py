# NOVO: molde de todos os problemas de matematica.
import random


def assinado(n):
    """Formata um inteiro com sinal: 5 -> '+ 5', -3 -> '- 3'."""
    return f"+ {n}" if n >= 0 else f"- {-n}"


class Problema:
    """Cada subclasse e um TIPO de problema e implementa montar().
    montar() sorteia numeros e devolve o enunciado e a resposta (sempre inteira)."""

    categoria = "Problema"

    def __init__(self, sorteio=None):
        self.sorteio = sorteio or random
        self.linhas = []       # linhas do enunciado (texto)
        self.resposta = 0
        self.gerar_novo()

    def gerar_novo(self):
        # sorteia numeros novos para o mesmo tipo de problema
        self.linhas, self.resposta = self.montar()

    def montar(self):
        raise NotImplementedError   # cada tipo de problema escreve o seu

    def conferir(self, texto):
        # True se o que o jogador digitou e igual a resposta
        try:
            return int(texto.strip()) == self.resposta
        except ValueError:
            return False
