# NOVO: a tela principal do jogo. Aqui a Matriz vira imagem na janela.
import pyxel

from jogo.configuracoes import (LARGURA, PAINEL_X, TAMANHO_CELULA, TAMANHO_GRADE,
                                TELA_X, TELA_Y, TOTAL_FASES)
from jogo.interface.caixa_problema import CaixaProblema
from jogo.interface.particulas import SistemaParticulas
from jogo.modelos.dados_fases import FASES
from jogo.modelos.pintura import Pintura
from jogo.nucleo.cena import Cena
from jogo.problemas.fabrica import FabricaProblemas

# medidas do painel de cores (a direita da grade)
AMOSTRA_Y0, AMOSTRA_PASSO, AMOSTRA_LARGURA, AMOSTRA_ALTURA = 34, 22, 72, 20


class CenaFase(Cena):
    def __init__(self, aplicativo, numero_fase):
        super().__init__(aplicativo)          # chama o __init__ da Cena (heranca)
        self.info = FASES[numero_fase - 1]
        self.pintura = Pintura(self.info)
        # um problema para cada cor da imagem (dicionario: cor -> problema)
        problemas = FabricaProblemas.criar_conjunto(numero_fase, len(self.pintura.cores))
        self.problemas = dict(zip(self.pintura.cores, problemas))
        self.caixa = None                     # caixa de problema aberta (ou None)
        self.particulas = SistemaParticulas()
        self.tempo_final = 0                  # contagem regressiva quando a pintura termina

    # ---------------- logica ----------------
    def atualizar(self):
        self.particulas.atualizar()
        if self.tempo_final > 0:              # pintura completa: espera a comemoracao
            self.tempo_final -= 1
            if self.tempo_final == 0:
                self.aplicativo.concluir_fase(self.info.numero, self.pintura)
            return
        if self.caixa:                        # com o problema aberto, so ele recebe entrada
            self.caixa.atualizar()
            return
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.aplicativo.ir_para_menu()
            return
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self._tratar_clique(pyxel.mouse_x, pyxel.mouse_y)

    def _tratar_clique(self, mx, my):
        # 1) clicou numa cor bloqueada do painel? abre o problema
        for i, cor in enumerate(self.pintura.cores):
            y = AMOSTRA_Y0 + i * AMOSTRA_PASSO
            if PAINEL_X <= mx < PAINEL_X + AMOSTRA_LARGURA and y <= my < y + AMOSTRA_ALTURA:
                if not self.pintura.esta_liberada(cor):
                    self._abrir_caixa(i, cor)
                return
        # 2) clicou numa celula da grade? tenta pintar
        celula = self._celula_em(mx, my)
        if celula:
            self._pintar(*celula)

    def _celula_em(self, mx, my):
        # converte a posicao do mouse (em pixels) em (linha, coluna) da matriz.
        # A divisao inteira (//) descobre em qual quadradinho o mouse esta.
        coluna = (mx - TELA_X) // TAMANHO_CELULA
        linha = (my - TELA_Y) // TAMANHO_CELULA
        if mx >= TELA_X and my >= TELA_Y and 0 <= linha < TAMANHO_GRADE and 0 <= coluna < TAMANHO_GRADE:
            return linha, coluna
        return None

    def _pintar(self, linha, coluna):
        cor = self.pintura.pintar(linha, coluna)
        if cor is None:
            return                            # nao era possivel pintar essa celula
        self.aplicativo.sons.tocar(self.aplicativo.sons.CLIQUE)
        centro_x = TELA_X + coluna * TAMANHO_CELULA + 5
        centro_y = TELA_Y + linha * TAMANHO_CELULA + 5
        self.particulas.explosao(centro_x, centro_y, cor, quantidade=8, velocidade=1.5, vida=14)
        if self.pintura.esta_completa:
            self.aplicativo.sons.tocar(self.aplicativo.sons.VITORIA)
            self.particulas.confete(80)
            self.tempo_final = 90             # ~3 segundos de comemoracao

    def _abrir_caixa(self, indice, cor):
        self.aplicativo.sons.tocar(self.aplicativo.sons.CLIQUE)
        self.caixa = CaixaProblema(
            self.problemas[cor], cor, indice + 1, len(self.pintura.cores), self.aplicativo.sons,
            ao_acertar=lambda: self._liberar_cor(cor),
            ao_errar=self._ao_errar,
            ao_fechar=self._fechar_caixa)

    def _liberar_cor(self, cor):
        self.pintura.liberar(cor)
        self.aplicativo.progresso.acertos += 1
        self.caixa = None
        self.particulas.explosao(PAINEL_X + 10, AMOSTRA_Y0 + 10, cor, quantidade=24, velocidade=3, vida=25)

    def _ao_errar(self):
        self.aplicativo.progresso.erros += 1

    def _fechar_caixa(self):
        self.caixa = None

    # ---------------- desenho ----------------
    def desenhar(self):
        self._desenhar_cabecalho()
        self._desenhar_grade()
        self._desenhar_painel()
        self.particulas.desenhar()
        if self.caixa:
            self.caixa.desenhar()

    def _desenhar_cabecalho(self):
        pyxel.rect(0, 0, LARGURA, 20, 0)
        pyxel.text(6, 4, f"FASE {self.info.numero}/{TOTAL_FASES} - {self.info.assunto.upper()}", 10)
        pyxel.rect(6, 13, LARGURA - 12, 3, 5)                                      # barra de fundo
        pyxel.rect(6, 13, int((LARGURA - 12) * self.pintura.progresso), 3, 11)     # barra de progresso

    def _desenhar_grade(self):
        # Percorre a matriz linha por linha e desenha cada celula como um quadrado:
        #   x = TELA_X + coluna * TAMANHO_CELULA
        #   y = TELA_Y + linha  * TAMANHO_CELULA
        p = self.pintura
        sobre = None if (self.caixa or self.tempo_final) else self._celula_em(pyxel.mouse_x, pyxel.mouse_y)
        pyxel.rectb(TELA_X - 1, TELA_Y - 1, TAMANHO_GRADE * TAMANHO_CELULA + 2,
                    TAMANHO_GRADE * TAMANHO_CELULA + 2, 7)
        for l in range(TAMANHO_GRADE):
            for c in range(TAMANHO_GRADE):
                x, y = TELA_X + c * TAMANHO_CELULA, TELA_Y + l * TAMANHO_CELULA
                cor = p.solucao.obter(l, c)
                if p.esta_completa and cor is None:
                    continue                                           # fase pronta: some o fundo
                if cor is not None and p.pintadas.obter(l, c):
                    pyxel.rect(x, y, TAMANHO_CELULA, TAMANHO_CELULA, cor)     # ja pintada
                    continue
                # ainda escondida: quadrado escuro em xadrez (nao revela a silhueta)
                pyxel.rect(x, y, TAMANHO_CELULA, TAMANHO_CELULA, 0 if (l + c) % 2 == 0 else 1)
                if cor is not None and p.esta_liberada(cor):           # ponto para clicar
                    pyxel.circ(x + 5, y + 5, 2, cor)
                    pyxel.circb(x + 5, y + 5, 3, 13 if cor == 7 else 7)
        if sobre and p.pode_pintar(*sobre):                            # destaque sob o mouse
            pyxel.rectb(TELA_X + sobre[1] * TAMANHO_CELULA, TELA_Y + sobre[0] * TAMANHO_CELULA,
                        TAMANHO_CELULA, TAMANHO_CELULA, 7)

    def _desenhar_painel(self):
        p = self.pintura
        pyxel.text(PAINEL_X, 25, "CORES", 10)
        for i, cor in enumerate(p.cores):
            y = AMOSTRA_Y0 + i * AMOSTRA_PASSO
            bloqueada = not p.esta_liberada(cor)
            sobre = (PAINEL_X <= pyxel.mouse_x < PAINEL_X + AMOSTRA_LARGURA
                     and y <= pyxel.mouse_y < y + AMOSTRA_ALTURA)
            pyxel.rect(PAINEL_X, y, AMOSTRA_LARGURA, AMOSTRA_ALTURA, 0)
            pyxel.rectb(PAINEL_X, y, AMOSTRA_LARGURA, AMOSTRA_ALTURA, 7 if (bloqueada and sobre) else 13)
            if bloqueada:                                              # cor escondida: "?"
                pyxel.rect(PAINEL_X + 4, y + 4, 12, 12, 5)
                pyxel.text(PAINEL_X + 8, y + 7, "?", 7)
                pyxel.text(PAINEL_X + 22, y + 7, "RESOLVER", 14)
            else:
                pyxel.rect(PAINEL_X + 4, y + 4, 12, 12, cor)
                pyxel.rectb(PAINEL_X + 4, y + 4, 12, 12, 7)
                feitas = p.total_da_cor(cor) - p.restantes_da_cor(cor)
                pyxel.text(PAINEL_X + 22, y + 7, f"{feitas}/{p.total_da_cor(cor)}", 7)
        pyxel.text(PAINEL_X, 152, f"Acertos: {self.aplicativo.progresso.acertos}", 11)
        pyxel.text(PAINEL_X, 160, f"Erros:   {self.aplicativo.progresso.erros}", 8)
        pyxel.text(PAINEL_X, 178, "ESC = menu", 13)
