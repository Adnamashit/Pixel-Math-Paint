# NOVO: animacao entre uma fase e outra (onda de quadrados + imagem concluida).
import pyxel

from jogo.configuracoes import ARCO_IRIS
from jogo.interface.particulas import SistemaParticulas
from jogo.interface.renderizador_arte import desenhar_matriz
from jogo.interface.texto import texto_centralizado
from jogo.nucleo.cena import Cena

BLOCO = 16                  # lado de cada quadrado da onda
COLUNAS, LINHAS = 16, 12    # 16 x 12 blocos cobrem a janela inteira
FIM_CRESCIMENTO = 50        # ate este frame os blocos crescem; depois encolhem e revelam o conteudo


class CenaTransicao(Cena):
    def __init__(self, aplicativo, fase_concluida, pintura, proxima_fase):
        super().__init__(aplicativo)
        self.fase_concluida, self.pintura, self.proxima_fase = fase_concluida, pintura, proxima_fase
        self.tempo = 0                      # conta os frames da animacao
        self.particulas = SistemaParticulas()

    def ao_entrar(self):
        self.particulas.confete(60)

    def atualizar(self):
        self.tempo += 1
        self.particulas.atualizar()
        if self.tempo == 70:
            self.particulas.confete(40)
        if self.tempo > 110 and (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_RETURN)
                                 or pyxel.btnp(pyxel.KEY_SPACE)):
            self.aplicativo.iniciar_fase(self.proxima_fase.numero)

    def desenhar(self):
        pyxel.cls(0)
        if self.tempo >= FIM_CRESCIMENTO - 5:
            self._desenhar_conteudo()
        self._desenhar_onda()
        self.particulas.desenhar()

    def _desenhar_onda(self):
        # cada bloco (linha, coluna) comeca a crescer com atraso = linha + coluna:
        # isso forma uma onda diagonal que cobre a tela e depois se desfaz
        for bl in range(LINHAS):
            for bc in range(COLUNAS):
                atraso = bl + bc
                if self.tempo < FIM_CRESCIMENTO:
                    tamanho = max(0, min(BLOCO, self.tempo - atraso))
                else:
                    tamanho = max(0, min(BLOCO, BLOCO - (self.tempo - FIM_CRESCIMENTO - atraso)))
                if tamanho <= 0:
                    continue
                x = bc * BLOCO + (BLOCO - tamanho) // 2
                y = bl * BLOCO + (BLOCO - tamanho) // 2
                pyxel.rect(x, y, tamanho, tamanho, ARCO_IRIS[(bl + bc) % len(ARCO_IRIS)])

    def _desenhar_conteudo(self):
        cor = ARCO_IRIS[(pyxel.frame_count // 3) % len(ARCO_IRIS)]
        texto_centralizado(14, f"FASE {self.fase_concluida.numero} COMPLETA!", cor)
        pyxel.rectb(86, 38, 84, 84, 7)
        desenhar_matriz(self.pintura.solucao, 88, 40, 5)       # a imagem pronta, ampliada 5x
        texto_centralizado(130, f"Imagem: {self.fase_concluida.nome}", 7)
        texto_centralizado(146, f"Proxima: Fase {self.proxima_fase.numero} - {self.proxima_fase.assunto}", 10)
        if self.tempo > 110 and (pyxel.frame_count // 15) % 2 == 0:
            texto_centralizado(170, "Clique para continuar", 13)
