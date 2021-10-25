# from astar_python.astar import Astar
from astar import Astar
from Utilitarios import retorna_lista_cores, retorna_lista_labels, verifica_pontos_iguais, receber_valores
import matplotlib.pyplot as plt
import networkx as nx
import Matrizes

LARGURA_MATRIZ = 8
ALTURA_MATRIZ = 8

def main():
    # Atribuição das matrizes de pesos e nomes
    matriz_de_pesos = Matrizes.matriz_de_pesos
    nomes = Matrizes.nomes

    ################# A* Rodando ######################

    # Recebendo valores
    # x0, y0, x, y = receber_valores(LARGURA_MATRIZ - 1,ALTURA_MATRIZ - 1)
    x0, y0, x, y = 0,2,1,0

    # Gerando mapa de pontos
    mapa = Astar(matriz_de_pesos)

    # Encontrando o caminho entre os pontos estipulados
    caminho = mapa.run([x0, y0], [x, y])

    peso_destino = matriz_de_pesos[y][x]
    caminho = [[0,2],[0,1],[0,0],[1,0]]
    # caminho dele -> [[0, 2], [1, 3], [2, 3], [3, 2], [2, 1], [1, 0]]
    soma = 0
    for ponto in caminho:
        x_p,y_p = ponto
        peso = matriz_de_pesos[y_p][x_p]
        heuristico = mapa.heuristic(Astar.Node(x_p,y_p,peso),Astar.Node(x,y,peso_destino))
        soma += (peso)

    print(caminho)
    print(soma)

    ################# gráfico #########################
    # Gerando gráfico vazio
    grafico = nx.grid_2d_graph(LARGURA_MATRIZ, ALTURA_MATRIZ)


    # Criando janela
    plt.figure(figsize=(10, 10))

    # Gerando nodos
    posicoes = {(x, y): (x, -y) for x, y in grafico.nodes()}

    # Adicionando as linhas na vertical entre os nodos
    grafico.add_edges_from([
        ((x, y), (x+1, y+1))
        for x in range(LARGURA_MATRIZ - 1)
        for y in range(ALTURA_MATRIZ - 1)
    ] + [
        ((x+1, y), (x, y+1))
        for x in range(LARGURA_MATRIZ - 1)
        for y in range(ALTURA_MATRIZ - 1)
    ], weight=1.4)

    ################# Nomeando nodos ################
    nomes_nodos = retorna_lista_labels(grafico,nomes)

    ################# Colorindo gráfico ################
    lista_de_cores = retorna_lista_cores(grafico,matriz_de_pesos,caminho,[105, 245, 112])
    
    # Desenhando gráfico
    nx.draw(grafico, pos=posicoes,
            node_color=lista_de_cores,
            with_labels=False,
            node_size=1000)
    
    # Desenhando nomes dos nodos
    nx.draw_networkx_labels(grafico,posicoes,labels=nomes_nodos,font_size=12)
    plt.show()

main()
