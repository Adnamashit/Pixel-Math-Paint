import pyxel 

from jogo.configuracoes import ALTURA, FPS, LARGURA, TITULO
from jogo.nucleo.cena import Cena 

class CenaTeste(Cena): #to fazendo herança aqui (passando Cena - uma classe - pra outra classe )
    "Testeeeee, só pra ver se o menu vai funcionar ;)"

    def atualizar (self):
        pass #ainda ntem nada

    def desenhar(self):
        pyxel.text(80, 90, "Pixel Math Paint", 7) #podia usar funçao pronta??
        pyxel.text(64,102, "Janela funcionando!", 10)

class App:
    def __init__(self):
        pyxel.init(LARGURA, ALTURA, title = TITULO, fps = FPS) #to importando do configuraçoes.py ;)
        pyxel.mouse(True) #setinha do mouse pro jogo funcionar

        self.cena = None #n fiz tela ativa ainda
        self.trocar_cena(CenaTeste(self)) #começa pela cena teste (n entendi mt bem a lógica disso)

        pyxel.run(self.atualizar, self.desenhar) #atualiza e desenha
    def trocar_cena(self, cena): #pra mudar a tela (menu, fase etc)
        self.cena = cena
        cena.ao_entrar()

    def atualizar(self):
        self.cena.atualizar()

    def desenhar(self):
        pyxel.cls(1)
        self.cena.desenhar()
