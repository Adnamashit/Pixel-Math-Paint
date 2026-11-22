# Aqui ficam as fases do jogo. Cada imagem e uma matriz 16x16 escrita com letrinhas.
from jogo.configuracoes import TAMANHO_GRADE
from jogo.modelos.matriz import Matriz


class InfoFase:
    """Guarda as informações de uma fase: nome, assunto e a imagem."""

    def __init__(self, numero, nome, assunto, arte, legenda):
        self.numero = numero      # 1, 2, 3...
        self.nome = nome          # nome da imagem
        self.assunto = assunto    # assunto de matematica da fase
        self.arte = arte          # 16 textos de 16 letras ('.' = vazio)
        self.legenda = legenda    # qual cor do Pyxel cada letra representa

    def para_matriz(self):
        # conversor das letrinhas para cores <3
        matriz = Matriz(TAMANHO_GRADE, TAMANHO_GRADE, None)
        for l, linha in enumerate(self.arte):         # l = número da linha
            for c, letra in enumerate(linha):         # c = número da coluna
                if letra != ".":                      # '.' fica vazio (None)
                    matriz.definir(l, c, self.legenda[letra])
        return matriz

    def validar(self):
        # confere se o desenho e 16x16 e se todas as letras existem na legenda
        assert len(self.arte) == TAMANHO_GRADE, f"fase {self.numero}: precisa de 16 linhas"
        for i, linha in enumerate(self.arte):
            assert len(linha) == TAMANHO_GRADE, f"fase {self.numero}, linha {i}: tamanho {len(linha)}"
            for letra in linha:
                assert letra == "." or letra in self.legenda, f"fase {self.numero}: '{letra}' fora da legenda"


FASES = [
    InfoFase(1, "Coracao", "Matematica Basica", (
        "................",
        "..DDDD....DDDD..",
        ".DRRRRD..DRRRRD.",
        "DRRWWRRDDRRRRRRD",
        "DRWWRRRRRRRRRRRD",
        "DRWRRRRRRRRRRRRD",
        "DRRRRRRRRRRRRPPD",
        ".DRRRRRRRRRRPPD.",
        "..DRRRRRRRRPPD..",
        "...DRRRRRRPPD...",
        "....DRRRRPPD....",
        ".....DRRRPD.....",
        "......DRRD......",
        ".......DD.......",
        "................",
        "................",
    ), {"D": 2, "R": 8, "W": 7, "P": 14}),

    InfoFase(2, "Arvore", "Algebra Elementar", (
        "................",
        ".....FFFFFF.....",
        "...FFGGGGGGFF...",
        "..FGGGGAGGGGGF..",
        ".FGGAGGGGGGAGGF.",
        ".FGGGGGGGGGGGGF.",
        ".FGGGAGGGGGGGGF.",
        "..FGGGGGGGAGGF..",
        "..FFGGGGGGGGFF..",
        "...FFFFGGFFFF...",
        ".......BB.......",
        ".......BB.......",
        ".......BB.......",
        "......BBBB......",
        ".....BBBBBB.....",
        "................",
    ), {"F": 3, "G": 11, "B": 4, "A": 8}),

    InfoFase(3, "Foguete", "Algebra e Geometria", (
        "......RRRR......",
        ".....RRRRRR.....",
        ".....WWWWWW.....",
        "....WWWWWWWW....",
        "....WWBBBBWW....",
        "....WBBBBBBW....",
        "....WWBBBBWW....",
        "....WWWWWWWW....",
        "....WWWWWWWW....",
        "...RWWWWWWWWR...",
        "..RRWWWWWWWWRR..",
        "..RR.WWWWWW.RR..",
        "......YYYY......",
        ".....YYYYYY.....",
        ".....YY..YY.....",
        "......Y..Y......",
    ), {"R": 8, "W": 7, "B": 12, "Y": 10}),

    InfoFase(4, "Planeta", "Pre-Calculo", (
        "................",
        "................",
        "................",
        "......OOOO......",
        "....OOYYOOOO....",
        "...OYYYOOOOOO...",
        "..OYYOOOOOOOOD..",
        ".LLLLLLLLLLLLLL.",
        "LLOOOOOOOOOODDLL",
        ".LLLLLLLLLLLLLL.",
        "..ODDDOOOODDDD..",
        "...DDDDDDDDDD...",
        "....DDDDDDDD....",
        "......DDDD......",
        "................",
        "................",
    ), {"O": 9, "Y": 10, "L": 13, "D": 4}),

    InfoFase(5, "Robo", "Calculo I", (
        ".......YY.......",
        ".......DD.......",
        "..DDDDDDDDDDDD..",
        "..DGGGGGGGGGGD..",
        "..DGBBGGGGBBGD..",
        "..DGBBGGGGBBGD..",
        "..DGGGGGGGGGGD..",
        "..DGRRRRRRRRGD..",
        "..DDDDDDDDDDDD..",
        "......DGGD......",
        "...DDDDDDDDDD...",
        ".DDGGGGGGGGGGDD.",
        ".DGGGYYYYYYGGGD.",
        ".DDGGGGGGGGGGDD.",
        "...DDDDDDDDDD...",
        "..DDD......DDD..",
    ), {"Y": 10, "D": 5, "G": 6, "B": 12, "R": 8}),
]

# Confere todas as fases assim que o arquivo e carregado.
for _fase in FASES:
    _fase.validar()
