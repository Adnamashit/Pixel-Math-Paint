# constantes do jogo (tamanho de tela e tals)
import os

# Pasta principal do projeto e arquivo onde o progresso e salvo (texto simples)
PASTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO_PROGRESSO = os.path.join(PASTA_BASE, "dados", "progresso.txt")

TITULO = "Pixel Math Paint"
LARGURA = 256
ALTURA = 192
FPS = 30

TAMANHO_GRADE = 16         # minha imagem da matriz (16 linhas x 16 colunas)
TAMANHO_CELULA = 10        # cada celula da matriz vira um quadrado de 10x10 pixels
TELA_X, TELA_Y = 8, 24     # canto superior esquerdo da grade na janela
PAINEL_X = TELA_X + TAMANHO_GRADE * TAMANHO_CELULA + 8   # painel de cores, a direita da grade

TOTAL_FASES = 5
ERROS_PARA_NOVO_PROBLEMA = 3   # depois de 3 erros na mesma cor, o problema e trocado

ARCO_IRIS = [8, 9, 10, 11, 12, 14]   # cores da paleta do Pyxel usadas nos efeitos
