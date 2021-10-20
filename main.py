from astar_python.astar import Astar
from Utilitarios import retorna_lista_cores, retorna_lista_labels, verifica_pontos_iguais, receber_valores
import matplotlib.pyplot as plt
import networkx as nx
import Matrizes

LARGURA_MATRIZ = 11
ALTURA_MATRIZ = 10

def main():
    matriz_de_pesos = Matrizes.matriz_de_pesos
    nomes = Matrizes.nomes

    ################# A* Rodando ######################

    x0, y0, x, y = receber_valores(LARGURA_MATRIZ,ALTURA_MATRIZ)

    mapa = Astar(matriz_de_pesos)
    caminho = mapa.run([x0, y0], [x, y])

    ################# gráfico #########################
    grafico = nx.grid_2d_graph(LARGURA_MATRIZ, ALTURA_MATRIZ)

    grafico.add_edges_from([
        ((x, y), (x+1, y+1))
        for x in range(LARGURA_MATRIZ - 1)
        for y in range(ALTURA_MATRIZ - 1)
    ] + [
        ((x+1, y), (x, y+1))
        for x in range(LARGURA_MATRIZ - 1)
        for y in range(ALTURA_MATRIZ - 1)
    ], weight=1.4)

    plt.figure(figsize=(10, 10))
    posicoes = {(x, y): (x, -y) for x, y in grafico.nodes()}

    ################# Pintar o caminho correto com cor diferente ################
    lista_de_cores = retorna_lista_cores(grafico,matriz_de_pesos,caminho,[105, 245, 112])
    nomes_nodos = retorna_lista_labels(grafico,nomes)
    
    nx.draw(grafico, pos=posicoes,
            node_color=lista_de_cores,
            with_labels=False,
            node_size=1000)
    
    nx.draw_networkx_labels(grafico,posicoes,labels=nomes_nodos)
    plt.show()

main()
