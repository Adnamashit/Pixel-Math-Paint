# Testa a LOGICA do jogo sem abrir janela (nao usa o Pyxel).
# Rode com:  py teste_logica.py
from jogo.modelos.dados_fases import FASES
from jogo.modelos.matriz import Matriz
from jogo.modelos.pintura import Pintura
from jogo.problemas.fabrica import TIPOS_POR_FASE

m = Matriz(3, 3)
m.definir(1, 2, "azul")
assert m.obter(1, 2) == "azul" and m.obter(0, 0) is None and not m.dentro_dos_limites(5, 5)
print("Matriz ok")

for fase in FASES:
    p = Pintura(fase)
    assert not p.pode_pintar(3, 3)                    # cor ainda bloqueada
    for cor in p.cores:
        p.liberar(cor)
    for l, c, cor in list(p.solucao.celulas()):
        if cor is not None:
            assert p.pintar(l, c) == cor
    assert p.esta_completa and p.progresso == 1.0
print("Pintura ok nas", len(FASES), "fases")

for numero, tipos in TIPOS_POR_FASE.items():
    for tipo in tipos:
        for _ in range(300):
            prob = tipo()
            assert prob.conferir(str(prob.resposta)) and not prob.conferir(str(prob.resposta + 1))
            assert all(linha.isascii() and len(linha) <= 44 for linha in prob.linhas)
print("Problemas ok (todas as respostas sao inteiras e conferem)")
