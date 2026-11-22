# NOVO: a Fabrica escolhe quais problemas aparecem em cada fase.
import random

from jogo.problemas import fase1, fase2, fase3, fase4, fase5

TIPOS_POR_FASE = {1: fase1.TIPOS, 2: fase2.TIPOS, 3: fase3.TIPOS, 4: fase4.TIPOS, 5: fase5.TIPOS}


class FabricaProblemas:
    @staticmethod
    def criar_conjunto(fase, quantidade, sorteio=random):
        # sorteia 'quantidade' problemas de tipos DIFERENTES (um para cada cor da imagem)
        tipos = sorteio.sample(TIPOS_POR_FASE[fase], quantidade)
        return [tipo(sorteio) for tipo in tipos]
