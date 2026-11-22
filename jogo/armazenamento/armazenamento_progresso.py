# NOVO: salva e le o progresso do jogador em arquivo de TEXTO (sem banco de dados).
import os
from dataclasses import dataclass

from jogo.configuracoes import TOTAL_FASES


@dataclass
class Progresso:
    fase_liberada: int = 1
    acertos: int = 0
    erros: int = 0
    concluido: bool = False


class ArmazenamentoProgresso:
    def __init__(self, caminho):
        self.caminho = caminho

    def carregar(self):
        try:
            dados = {}
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    if "=" in linha:                       # formato chave=valor
                        chave, valor = linha.strip().split("=", 1)
                        dados[chave] = valor
            progresso = Progresso()
            progresso.fase_liberada = max(1, min(TOTAL_FASES, int(dados.get("fase", 1))))
            progresso.acertos = max(0, int(dados.get("acertos", 0)))
            progresso.erros = max(0, int(dados.get("erros", 0)))
            progresso.concluido = dados.get("concluido", "0") == "1"
            return progresso
        except (OSError, ValueError):
            return Progresso()      # arquivo nao existe ou esta estragado: comeca do zero

    def salvar(self, progresso):
        try:
            os.makedirs(os.path.dirname(self.caminho), exist_ok=True)
            with open(self.caminho, "w", encoding="utf-8") as arquivo:
                arquivo.write(f"fase={progresso.fase_liberada}\n")
                arquivo.write(f"acertos={progresso.acertos}\n")
                arquivo.write(f"erros={progresso.erros}\n")
                arquivo.write(f"concluido={1 if progresso.concluido else 0}\n")
        except OSError:
            pass
