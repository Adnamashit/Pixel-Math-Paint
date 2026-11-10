
from jogo.configuracoes import TAMANHO_GRADE
from jogo.modelos.matriz import Matriz


class InfoFase:
    """Guarda as informações de uma fase: nome, assunto e a imagem."""

    def __init__(self, numero, nome, assunto, arte, legenda):
        self.numero = numero      
        self.nome = nome          
        self.assunto = assunto    
        self.arte = arte          
        self.legenda = legenda    

    def para_matriz(self):
        # conversor das letrinhas para cores <3
        matriz = Matriz(TAMANHO_GRADE, TAMANHO_GRADE, None)
        for l, linha in enumerate(self.arte):         # l = número da linha
            for c, letra in enumerate(linha):         # c = número da coluna
                if letra != ".":                      # '.' fica vazio (None)
                    matriz.definir(l, c, self.legenda[letra])
        return matriz

    def validar(self):
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
]

# Confere todas as fases assim que o arquivo é carregado.
for _fase in FASES:
    _fase.validar()