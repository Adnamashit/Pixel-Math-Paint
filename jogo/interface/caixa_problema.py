# NOVO: a janela onde o jogador le o problema e digita a resposta.
import random

import pyxel

from jogo.configuracoes import ERROS_PARA_NOVO_PROBLEMA
from jogo.interface.botao import Botao
from jogo.interface.texto import largura_texto

# teclas de 0 a 9 (teclado normal e teclado numerico)
TECLAS_NUMERICAS = [(getattr(pyxel, f"KEY_{i}"), str(i)) for i in range(10)] + \
                   [(getattr(pyxel, f"KEY_KP_{i}"), str(i)) for i in range(10)]

CAIXA_X, CAIXA_Y, CAIXA_LARGURA, CAIXA_ALTURA = 24, 28, 208, 136


class CaixaProblema:
    def __init__(self, problema, cor, indice, total, sons, ao_acertar, ao_errar, ao_fechar):
        self.problema, self.cor = problema, cor
        self.indice, self.total = indice, total
        self.sons = sons
        # "ao_..." sao funcoes que a CenaFase entrega para a caixa chamar nos eventos
        self.ao_acertar, self.ao_errar, self.ao_fechar = ao_acertar, ao_errar, ao_fechar
        self.texto = ""             # o que o jogador digitou
        self.mensagem = ""
        self.cor_mensagem = 8
        self.tremor = 0             # frames da animacao de erro (a caixa treme)
        self.erros_seguidos = 0
        self.tempo_acerto = 0       # frames mostrando "Correto!" antes de fechar
        self.botao_voltar = Botao(CAIXA_X + CAIXA_LARGURA - 62, CAIXA_Y + 104, 54, 14, "Voltar", ao_fechar)

    def atualizar(self):
        if self.tempo_acerto > 0:                    # acertou: espera um pouco e fecha
            self.tempo_acerto -= 1
            if self.tempo_acerto == 0:
                self.ao_acertar()
            return
        if self.tremor > 0:
            self.tremor -= 1
        if self.botao_voltar.atualizar():
            return
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.ao_fechar()
            return
        for tecla, digito in TECLAS_NUMERICAS:
            if pyxel.btnp(tecla) and len(self.texto) < 9:
                self.texto += digito
        if (pyxel.btnp(pyxel.KEY_MINUS) or pyxel.btnp(pyxel.KEY_KP_MINUS)) and self.texto == "":
            self.texto = "-"                          # sinal de menos so no comeco
        if pyxel.btnp(pyxel.KEY_BACKSPACE, 12, 3):
            self.texto = self.texto[:-1]              # apaga a ultima letra
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_KP_ENTER):
            self._confirmar()

    def _confirmar(self):
        if self.texto in ("", "-"):
            return
        if self.problema.conferir(self.texto):
            self.tempo_acerto = 30
            self.mensagem, self.cor_mensagem = "Correto! Cor desbloqueada!", 11
            self.sons.tocar(self.sons.ACERTO)
            return
        self.ao_errar()
        self.sons.tocar(self.sons.ERRO)
        self.tremor = 12
        self.erros_seguidos += 1
        self.texto = ""
        self.mensagem, self.cor_mensagem = "Resposta incorreta. Tente de novo!", 8
        if self.erros_seguidos % ERROS_PARA_NOVO_PROBLEMA == 0:
            self.problema.gerar_novo()                # muitos erros: sorteia outro problema
            self.mensagem = "Muitos erros: novo problema!"

    def desenhar(self):
        pyxel.dither(0.5)                             # escurece o fundo (meio transparente)
        pyxel.rect(0, 0, 256, 192, 0)
        pyxel.dither(1.0)
        deslocamento = random.randint(-2, 2) if self.tremor > 0 else 0
        x, y = CAIXA_X + deslocamento, CAIXA_Y
        pyxel.rect(x, y, CAIXA_LARGURA, CAIXA_ALTURA, 0)
        pyxel.rectb(x, y, CAIXA_LARGURA, CAIXA_ALTURA, 7)
        pyxel.text(x + 10, y + 8, f"DESBLOQUEAR COR {self.indice}/{self.total}", 10)
        pyxel.rect(x + CAIXA_LARGURA - 22, y + 6, 12, 12, self.cor)
        pyxel.rectb(x + CAIXA_LARGURA - 22, y + 6, 12, 12, 7)
        pyxel.text(x + 10, y + 20, self.problema.categoria.upper(), 12)
        for i, linha in enumerate(self.problema.linhas):
            pyxel.text(x + 12, y + 36 + i * 9, linha, 7)
        pyxel.rectb(x + 12, y + 80, CAIXA_LARGURA - 24, 16, 13)
        pyxel.text(x + 18, y + 85, "Resposta:", 13)
        cursor = "_" if (pyxel.frame_count // 10) % 2 == 0 else ""     # cursor piscando
        pyxel.text(x + 18 + largura_texto("Resposta: "), y + 85, self.texto + cursor, 10)
        pyxel.text(x + 12, y + 108, self.mensagem, self.cor_mensagem)
        pyxel.text(x + 12, y + 124, "ENTER confirma | ESC volta", 13)
        self.botao_voltar.x = x + CAIXA_LARGURA - 62
        self.botao_voltar.desenhar()
