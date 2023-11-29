'''
Este código cria um tabuleiro 10x10 com células vivas e mortas distribuídas aleatoriamente. Em seguida, ele atualiza o tabuleiro para as próximas 5 gerações, desenhando o tabuleiro na tela após cada atualização. As células vivas são representadas por quadrados pretos e as células mortas são representadas por quadrados brancos

'''
import tkinter as tk
import numpy as np
import time

def update(board):
    new_board = board.copy()
    rows, cols = board.shape
    for i in range(rows):
        for j in range(cols):
            total = np.sum(board[max(i-1, 0):min(i+2, rows), max(j-1, 0):min(j+2, cols)]) - board[i, j]
            if board[i, j] == 1:
                if total < 2 or total > 3:
                    new_board[i, j] = 0
            elif total == 3:
                new_board[i, j] = 1
    return new_board

def draw_board(canvas, board):
    rows, cols = board.shape
    cell_size = 20
    canvas.delete('all')
    for i in range(rows):
        for j in range(cols):
            if board[i, j] == 1:
                canvas.create_rectangle(j*cell_size, i*cell_size, (j+1)*cell_size, (i+1)*cell_size, fill='black')

def main():
    board = np.random.choice([0, 1], size=(10, 10))
    root = tk.Tk()
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()
    draw_board(canvas, board)
    for i in range(10):
        board = update(board)
        draw_board(canvas, board)
        root.update()
        time.sleep(0.5)  # Pausa por 0.1 segundo
    root.mainloop()

if __name__ == "__main__":
    main()


'''
O Jogo da Vida é um autômato celular que foi inventado pelo matemático britânico John Horton Conway em 1970. O "jogo" é na verdade uma simulação que ocorre em uma grade infinita bidimensional de células quadradas. Cada célula tem dois estados possíveis: viva ou morta. Cada célula interage com suas oito células vizinhas, que são as células diretamente adjacentes horizontalmente, verticalmente ou diagonalmente.

Aqui estão as regras do Jogo da Vida:
1. Qualquer célula viva com menos de dois vizinhos vivos morre, como se por subpopulação.
2. Qualquer célula viva com dois ou três vizinhos vivos vive para a próxima geração.
3. Qualquer célula viva com mais de três vizinhos vivos morre, como se por superpopulação.
4. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva, como se por reprodução.

Estas regras são aplicadas a cada célula simultaneamente em cada ponto no tempo, com o estado inicial (primeira geração) da simulação especificado pelo jogador. O jogo não tem jogadores no sentido convencional - uma vez que o estado inicial é definido, a evolução do jogo é determinada inteiramente pelas regras.

O Jogo da Vida, um autômato celular desenvolvido pelo matemático britânico John Horton Conway, tem várias implicações interessantes e aplicações em diversas áreas da ciência³. Ele foi criado para reproduzir, através de regras simples, as alterações e mudanças em grupos de seres vivos³.

Algumas das implicações e aplicações do Jogo da Vida incluem:

1. **Modelagem de sistemas biológicos**: O Jogo da Vida pode ser usado para modelar e estudar a dinâmica de populações de organismos vivos. Ele pode ajudar a entender como populações crescem, diminuem e evoluem ao longo do tempo.

2. **Computação e lógica**: O Jogo da Vida é Turing completo, o que significa que ele pode simular uma máquina de Turing universal. Isso implica que qualquer coisa que possa ser computada teoricamente pode ser computada dentro do Jogo da Vida.

3. **Arte e visualização**: O Jogo da Vida também é usado em arte digital e visualizações, devido aos padrões complexos e belos que podem emergir das suas regras simples.

4. **Estudo de sistemas complexos e caos**: O Jogo da Vida é um exemplo clássico de um sistema onde regras simples podem levar a comportamentos complexos. Isso o torna um modelo útil para estudar a teoria do caos e a emergência de complexidade.

5. **Ensino de programação e algoritmos**: O Jogo da Vida é frequentemente usado como um projeto de programação em cursos de ciência da computação. Ele ajuda os alunos a aprender sobre conceitos importantes como matrizes bidimensionais, loops aninhados e a implementação de regras baseadas em condições¹.

Por fim, é importante notar que, embora o Jogo da Vida seja uma simplificação da realidade, ele oferece uma maneira poderosa de explorar como regras simples podem levar a comportamentos complexos¹.

'''
