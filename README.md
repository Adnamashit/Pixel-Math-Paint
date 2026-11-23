# Pixel Math Paint

Jogo de pintura com matemática feito em **Python + Pyxel** para a disciplina de
**Algoritmos e Estruturas de Dados I** (FURG).

**Autora:** Amanda Ferreira Duarte

## Sobre o jogo

Uma imagem em pixel art (uma matriz 16x16) está escondida. Para revelar cada cor, o jogador
resolve um problema de matemática. Ao acertar, a cor é desbloqueada e aparecem **pontos** na tela:
é só clicar neles para pintar. Quando tudo estiver pintado, a imagem é revelada e o jogo passa
para a próxima fase, com uma animação de transição.

São **5 fases**, do básico ao Cálculo I:

| Fase | Imagem  | Matemática |
|:----:|---------|------------|
| 1 | Coração | Operações, divisão, porcentagem, potências |
| 2 | Árvore  | Equação do 1º grau, raiz, regra de três, PA |
| 3 | Foguete | Equação do 2º grau, determinante 2x2, Pitágoras, sistemas, logaritmo |
| 4 | Planeta | Trigonometria, exponencial, limites, somatório, combinatória |
| 5 | Robô    | Derivadas, integrais, limites, ponto de mínimo, regra da cadeia |

Os números dos problemas são sorteados a cada partida e as respostas são sempre inteiras.
Depois de 3 erros na mesma cor, o problema é trocado.

## Como executar

Requisitos: Python 3.12 ou 3.13 e Pyxel.

    pip install -r requirements.txt
    python main.py

Controles: mouse para clicar, teclado para digitar a resposta, `ENTER` confirma, `ESC` volta.

## Estrutura do projeto

    main.py                           ponto de entrada
    jogo/
      aplicativo.py                   App: janela do Pyxel, tela ativa e progresso
      configuracoes.py                constantes do jogo
      nucleo/cena.py                  classe base de todas as telas
      cenas/                          CenaMenu, CenaFase, CenaTransicao, CenaVitoria
      modelos/
        matriz.py                     classe Matriz
        dados_fases.py                InfoFase e as 5 imagens (matrizes de letras)
        pintura.py                    Pintura: células pintadas e cores liberadas
      problemas/                      Problema (classe base), fase1..fase5 e a fábrica
      interface/                      botão, caixa de problema, partículas, fundo
      armazenamento/                  progresso salvo em arquivo de texto
      audio/                          efeitos sonoros
    dados/progresso.txt               criado automaticamente (arquivo de texto)
    teste_logica.py                   testa a lógica sem abrir janela

## Conceitos de Algoritmos e Estruturas de Dados

- **Matrizes:** a imagem e o estado da pintura são matrizes 16x16 (classe `Matriz`). Para desenhar,
  o jogo percorre a matriz e transforma cada célula (linha, coluna) em um quadrado na janela.
  O clique do mouse faz o caminho inverso com divisão inteira:
  `coluna = (mouse_x - TELA_X) // TAMANHO_CELULA`.
- **Orientação a objetos:** herança (`Cena`, `Problema`), polimorfismo (cada problema implementa
  `montar()`), encapsulamento (`Pintura`) e uma fábrica (`FabricaProblemas`).
- **Persistência:** progresso salvo em arquivo de texto (`chave=valor`), sem banco de dados.
- **Listas, dicionários e conjuntos:** cores de cada fase, problema de cada cor, cores liberadas.

## STEAM no jogo

| Letra | Conceito | Onde aparece |
|:-----:|----------|--------------|
| **S** | Ciência | Imagens de árvore, foguete e planeta; trigonometria e cálculo, base da Física |
| **T** | Tecnologia | Python, biblioteca Pyxel, Git e GitHub |
| **E** | Engenharia | Projeto organizado em camadas (cenas, modelos, interface, armazenamento) |
| **A** | Artes | Pixel art feita em matrizes, paleta de cores, animações e sons |
| **M** | Matemática | Núcleo do jogo: 21 tipos de problema, do básico ao Cálculo I |
