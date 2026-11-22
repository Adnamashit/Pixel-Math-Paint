import pyxel

from jogo.configuracoes import LARGURA

LARGURA_CARACTERE = 4   # cada letra da fonte do Pyxel tem 4 pixels de largura


def largura_texto(texto):
    return len(texto) * LARGURA_CARACTERE


def texto_centralizado(y, texto, cor, x=0, largura=LARGURA):
    # escreve o texto no meio da faixa [x, x + largura]
    pyxel.text(x + (largura - largura_texto(texto)) // 2, y, texto, cor)
