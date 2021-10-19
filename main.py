from astar_python.astar import Astar
from numpy import False_
from Utilitarios import converter_para_hexadecimal, retorna_cores, verifica_valores, receber_valores
import matplotlib.pyplot as plt
import networkx as nx

def main():
    ################### espaço amostral para percorrer #####################
    # distancia é sempre 1
    # 0 siguinifica custo 0 para percorrer
    # maiores valores implicam em desviar a rota, buscando um custo menor
    mat = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    nomes = [
        'A-0', 'B-0', 'C-0', 'D-0', 'E-0', 'F-0', 'G-0', 'H-0', 'I-0', 'J-0',
        'A-1', 'B-1', 'C-1', 'D-1', 'E-1', 'F-1', 'G-1', 'H-1', 'I-1', 'J-1',
        'A-2', 'B-2', 'C-2', 'D-2', 'E-2', 'F-2', 'G-2', 'H-2', 'I-2', 'J-2',
        'A-3', 'B-3', 'C-3', 'D-3', 'E-3', 'F-3', 'G-3', 'H-3', 'I-3', 'J-3',
        'A-4', 'B-4', 'C-4', 'D-4', 'E-4', 'F-4', 'G-4', 'H-4', 'I-4', 'J-4',
        'A-5', 'B-5', 'C-5', 'D-5', 'E-5', 'F-5', 'G-5', 'H-5', 'I-5', 'J-5',
        'A-6', 'B-6', 'C-6', 'D-6', 'E-6', 'F-6', 'G-6', 'H-6', 'I-6', 'J-6',
        'A-7', 'B-7', 'C-7', 'D-7', 'E-7', 'F-7', 'G-7', 'H-7', 'I-7', 'J-7',
        'A-8', 'B-8', 'C-8', 'D-8', 'E-8', 'F-8', 'G-8', 'H-8', 'I-8', 'J-8',
        'A-9', 'B-9', 'C-9', 'D-9', 'E-9', 'F-9', 'G-9', 'H-9', 'I-9', 'J-9',
        'A-10', 'B-10', 'C-10', 'D-10', 'E-10', 'F-10', 'G-10', 'H-10', 'I-10', 'J-10']

    print(nomes[0])

    ################# A* Rodando ######################

    x0, y0, x, y = receber_valores(10,9)

    mapa = Astar(mat)
    caminho = mapa.run([x0, y0], [x, y])
    cores_dos_nodos = retorna_cores(caminho, [105, 245, 112])
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

    plt.figure(figsize=(10, 10))
    pos = {(x, y): (x, -y) for x, y in G.nodes()}

    ################# Pintar o caminho correto com cor diferente ################
    color_map = []
    nomes_nodos = {}
    i = 0
    for node in G:
        color = "orange"
        nomes_nodos[node] = nomes[i]

        i += 1
        for ponto in caminho:
            if verifica_valores(ponto,node):
                color = cores_dos_nodos[node]
                color = converter_para_hexadecimal(color)
        color_map.append(color)    
    
    nx.draw(G, pos=pos,
            node_color=color_map,
            with_labels=False,
            node_size=1000)
    
    nx.draw_networkx_labels(G,pos,labels=nomes_nodos)
    plt.show()

main()
