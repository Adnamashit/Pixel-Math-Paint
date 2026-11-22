import pyxel

from jogo.interface.texto import texto_centralizado


class Botao:
    def __init__(self, x, y, largura, altura, rotulo, acao):
        self.x, self.y, self.largura, self.altura = x, y, largura, altura
        self.rotulo = rotulo
        self.acao = acao        # funcao chamada quando o botao e clicado

    def mouse_em_cima(self):
        return (self.x <= pyxel.mouse_x < self.x + self.largura and
                self.y <= pyxel.mouse_y < self.y + self.altura)

    def atualizar(self):
        # devolve True se foi clicado (e ja executa a acao)
        if self.mouse_em_cima() and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.acao()
            return True
        return False

    def desenhar(self):
        fundo = 12 if self.mouse_em_cima() else 5      # muda de cor quando o mouse esta em cima
        pyxel.rect(self.x, self.y, self.largura, self.altura, fundo)
        pyxel.rectb(self.x, self.y, self.largura, self.altura, 7)
        texto_centralizado(self.y + (self.altura - 5) // 2, self.rotulo, 7, self.x, self.largura)
