# NOVO: sons simples criados por codigo (nao precisa de arquivo de audio).
import pyxel


class EfeitosSonoros:
    CLIQUE, ACERTO, ERRO, VITORIA = 0, 1, 2, 3

    def preparar(self):
        # sounds[n].set(notas, timbres, volumes, efeitos, velocidade)
        pyxel.sounds[self.CLIQUE].set("a3", "p", "5", "f", 6)
        pyxel.sounds[self.ACERTO].set("c3e3g3c4", "s", "6", "f", 8)
        pyxel.sounds[self.ERRO].set("g1e1c1", "s", "6", "f", 12)
        pyxel.sounds[self.VITORIA].set("c3e3g3c4e4g4c4", "p", "6", "f", 10)

    def tocar(self, som):
        pyxel.play(3, som)    # toca no canal 3
