# NOVO: tela final, depois da fase 5.
import pyxel

from jogo.configuracoes import ARCO_IRIS
from jogo.interface.botao import Botao
from jogo.interface.particulas import SistemaParticulas
from jogo.interface.renderizador_arte import desenhar_matriz
from jogo.interface.texto import texto_centralizado
from jogo.modelos.dados_fases import FASES
from jogo.nucleo.cena import Cena


class CenaVitoria(Cena):
    def __init__(self, aplicativo):
        super().__init__(aplicativo)
        self.particulas = SistemaParticulas()
        self.matrizes = [fase.para_matriz() for fase in FASES]
        self.botao_menu = Botao(88, 164, 80, 16, "Menu", aplicativo.ir_para_menu)

    def atualizar(self):
        if pyxel.frame_count % 8 == 0:
            self.particulas.confete(6)
        self.particulas.atualizar()
        self.botao_menu.atualizar()

    def desenhar(self):
        cor = ARCO_IRIS[(pyxel.frame_count // 3) % len(ARCO_IRIS)]
        texto_centralizado(14, "PARABENS!", cor)
        texto_centralizado(28, "Voce pintou todas as imagens!", 7)
        for i, matriz in enumerate(self.matrizes):             # as 5 imagens lado a lado
            desenhar_matriz(matriz, 4 + i * 50, 56, 3)
        progresso = self.aplicativo.progresso
        texto_centralizado(120, f"Acertos: {progresso.acertos}   Erros: {progresso.erros}", 11)
        texto_centralizado(136, "Do basico ao Calculo I. Voce e demais!", 13)
        self.botao_menu.desenhar()
        self.particulas.desenhar()
