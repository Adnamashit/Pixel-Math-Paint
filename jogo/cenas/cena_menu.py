# NOVO: o menu inicial, com a imagem se pintando sozinha.
import math
import random

import pyxel

from jogo.configuracoes import ARCO_IRIS, LARGURA
from jogo.interface.botao import Botao
from jogo.interface.fundo import PixelsCaindo
from jogo.interface.texto import texto_centralizado
from jogo.modelos.dados_fases import FASES
from jogo.nucleo.cena import Cena

TEXTO_AJUDA = [
    "1. Clique em uma cor '?' no painel",
    "2. Resolva o problema de matematica",
    "3. Digite a resposta e aperte ENTER",
    "4. Clique nos pontos para pintar",
    "5. Pinte tudo e revele a imagem!",
    "",
    "5 fases: do basico ao Calculo I",
]
PREVIA_X, PREVIA_Y, PREVIA_ESCALA = 96, 30, 4


class CenaMenu(Cena):
    def __init__(self, aplicativo):
        super().__init__(aplicativo)
        self.fundo = PixelsCaindo()
        self.mostrando_ajuda = False
        self.fase_demo = 0
        self._nova_demonstracao()
        rotulo_continuar = f"Continuar (Fase {aplicativo.progresso.fase_liberada})"
        self.botoes = [
            Botao(68, 104, 120, 16, "Novo jogo", aplicativo.novo_jogo),
            Botao(68, 124, 120, 16, rotulo_continuar, aplicativo.continuar_jogo),
            Botao(68, 144, 120, 16, "Como jogar", self._abrir_ajuda),
            Botao(68, 164, 120, 16, "Sair", pyxel.quit),
        ]

    def _abrir_ajuda(self):
        self.mostrando_ajuda = True

    def _nova_demonstracao(self):
        # prepara a imagem que se pinta sozinha: lista das celulas, em ordem aleatoria
        matriz = FASES[self.fase_demo % len(FASES)].para_matriz()
        self.celulas_demo = [(l, c, cor) for l, c, cor in matriz.celulas() if cor is not None]
        random.shuffle(self.celulas_demo)
        self.quantidade_demo = 0       # quantas celulas ja foram "pintadas"
        self.espera_demo = 0

    def atualizar(self):
        self.fundo.atualizar()
        if self.quantidade_demo < len(self.celulas_demo):
            self.quantidade_demo += 2
        else:
            self.espera_demo += 1
            if self.espera_demo > 60:                  # mostra pronta e passa para a proxima imagem
                self.fase_demo += 1
                self._nova_demonstracao()
        if self.mostrando_ajuda:
            if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_ESCAPE)
                    or pyxel.btnp(pyxel.KEY_RETURN)):
                self.mostrando_ajuda = False
            return
        for botao in self.botoes:
            if botao.atualizar():
                break

    def desenhar(self):
        self.fundo.desenhar()
        titulo = "PIXEL MATH PAINT"
        x0 = (LARGURA - len(titulo) * 6) // 2
        for i, letra in enumerate(titulo):             # cada letra "pula" e muda de cor
            y = 10 + int(math.sin(pyxel.frame_count * 0.15 + i * 0.5) * 2)
            cor = ARCO_IRIS[(i + pyxel.frame_count // 4) % len(ARCO_IRIS)]
            pyxel.text(x0 + i * 6 + 1, y + 1, letra, 0)
            pyxel.text(x0 + i * 6, y, letra, cor)
            pyxel.text(x0 + i * 6 + 1, y, letra, cor)
        pyxel.rect(PREVIA_X - 2, PREVIA_Y - 2, 68, 68, 0)
        pyxel.rectb(PREVIA_X - 2, PREVIA_Y - 2, 68, 68, 7)
        for l, c, cor in self.celulas_demo[:self.quantidade_demo]:
            pyxel.rect(PREVIA_X + c * PREVIA_ESCALA, PREVIA_Y + l * PREVIA_ESCALA,
                       PREVIA_ESCALA, PREVIA_ESCALA, cor)
        texto_centralizado(98, "Pinte com matematica!", 13)
        for botao in self.botoes:
            botao.desenhar()
        if self.mostrando_ajuda:
            self._desenhar_ajuda()

    def _desenhar_ajuda(self):
        pyxel.dither(0.5)
        pyxel.rect(0, 0, 256, 192, 0)
        pyxel.dither(1.0)
        pyxel.rect(36, 36, 184, 120, 0)
        pyxel.rectb(36, 36, 184, 120, 7)
        texto_centralizado(44, "COMO JOGAR", 10)
        for i, linha in enumerate(TEXTO_AJUDA):
            pyxel.text(46, 62 + i * 10, linha, 7)
        texto_centralizado(142, "Clique para voltar", 13)
