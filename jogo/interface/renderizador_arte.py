import pyxel


def desenhar_matriz(matriz, x, y, escala):
    """Desenha uma Matriz de cores como pixel art ampliada.
    Cada celula (linha, coluna) vira um quadrado de 'escala' pixels em
    x + coluna * escala, y + linha * escala. Celulas vazias (None) nao sao desenhadas."""
    for l, c, cor in matriz.celulas():
        if cor is not None:
            pyxel.rect(x + c * escala, y + l * escala, escala, escala, cor)
