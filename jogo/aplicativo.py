import pyxel

from jogo.armazenamento.armazenamento_progresso import ArmazenamentoProgresso, Progresso
from jogo.audio.efeitos_sonoros import EfeitosSonoros
from jogo.cenas.cena_fase import CenaFase
from jogo.cenas.cena_menu import CenaMenu
from jogo.cenas.cena_transicao import CenaTransicao
from jogo.cenas.cena_vitoria import CenaVitoria
from jogo.configuracoes import ALTURA, ARQUIVO_PROGRESSO, FPS, LARGURA, TITULO, TOTAL_FASES
from jogo.modelos.dados_fases import FASES


class App:
    """Controla a janela do Pyxel, a cena (tela) ativa e o progresso do jogador."""

    def __init__(self):
        pyxel.init(LARGURA, ALTURA, title=TITULO, fps=FPS, quit_key=pyxel.KEY_NONE)  # ESC nao fecha mais o jogo
        pyxel.mouse(True)                      # setinha do mouse pro jogo funcionar
        self.sons = EfeitosSonoros()
        self.sons.preparar()
        self.armazenamento = ArmazenamentoProgresso(ARQUIVO_PROGRESSO)
        self.progresso = self.armazenamento.carregar()   # le o arquivo de texto (se existir)
        self.cena = None                       # ainda nao ha tela ativa
        self.trocar_cena(CenaMenu(self))       # o jogo comeca pelo menu
        pyxel.run(self.atualizar, self.desenhar)

    def trocar_cena(self, cena):               # pra mudar a tela (menu, fase etc)
        self.cena = cena
        cena.ao_entrar()

    def atualizar(self):
        self.cena.atualizar()                  # repassa a logica para a tela ativa

    def desenhar(self):
        pyxel.cls(1)                           # limpa a janela (azul-marinho)
        self.cena.desenhar()

    # ---------- navegacao entre telas ----------
    def ir_para_menu(self):
        self.armazenamento.salvar(self.progresso)
        self.trocar_cena(CenaMenu(self))

    def novo_jogo(self):
        self.progresso = Progresso()           # zera acertos, erros e fase
        self.armazenamento.salvar(self.progresso)
        self.iniciar_fase(1)

    def continuar_jogo(self):
        self.iniciar_fase(self.progresso.fase_liberada)

    def iniciar_fase(self, numero):
        self.trocar_cena(CenaFase(self, numero))

    def concluir_fase(self, numero, pintura):
        # chamado quando a pintura termina: salva e vai para a transicao (ou para a vitoria)
        if numero >= TOTAL_FASES:
            self.progresso.concluido = True
            self.armazenamento.salvar(self.progresso)
            self.trocar_cena(CenaVitoria(self))
            return
        self.progresso.fase_liberada = max(self.progresso.fase_liberada, numero + 1)
        self.armazenamento.salvar(self.progresso)
        self.trocar_cena(CenaTransicao(self, FASES[numero - 1], pintura, FASES[numero]))
