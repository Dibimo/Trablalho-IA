from astar_python.astar import Astar
from Utilitarios import verifica_valores, receber_valores
import matplotlib.pyplot as plt
import networkx as nx

def main():
    ################### espaço amostral para percorrer #####################
    # distancia é sempre 1
    # 0 siguinifica custo 0 para percorrer
    # maiores valores implicam em desviar a rota, buscando um custo menor
    mat = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    ################# A* Rodando ######################

    x0, y0, x, y = receber_valores(10,9)

    mapa = Astar(mat)
    caminho = mapa.run([x0, y0], [x, y])

    ################# gráfico #########################
    G = nx.grid_2d_graph(11, 10)

    G.add_edges_from([
        ((x, y), (x+1, y+1))
        for x in range(10)
        for y in range(9)
    ] + [
        ((x+1, y), (x, y+1))
        for x in range(10)
        for y in range(9)
    ], weight=1.4)

    plt.figure(figsize=(6, 6))
    pos = {(x, y): (x, -y) for x, y in G.nodes()}

    ################# Pintar o caminho correto com cor diferente ################
    color_map = []
    for node in G:
        color = "orange"
        for ponto in caminho:
            if verifica_valores(ponto,node):
                
                color = "lightgreen"

        color_map.append(color)
    
    
    nx.draw(G, pos=pos,
            node_color=color_map,
            with_labels=True,
            node_size=600)
    plt.show()

main()
