from networkx.algorithms.bipartite.basic import color
from astar_python.astar import Astar
import matplotlib.pyplot as plt
import networkx as nx

def main():
    ################### espaço amostral para percorrer #####################
    #0 siguinifica custo 0 para percorrer
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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    ################# A* Rodando ######################
    
    
    x0= int(input("Insira o valor de x0 para iniciar! (x<10) : "))
    y0= int(input("Insira o valor de y0 para iniciar! (y<9) : "))
    x= int(input("Insira o valor de x a ser encontrado! (x<10) : "))
    y= int(input("Insira o valor de y a ser encontrado! (y<9) : "))
    
    mapa = Astar(mat)
    #caminho = mapa.run([0,0],[10,9])
    caminho = mapa.run([x0,y0],[x,y])
    ################# gráfico #########################
    G = nx.grid_2d_graph(11, 10)

    G.add_edges_from ([
        ((x, y), (x+1, y+1))
        for x in range(10)
        for y in range(9)
    ] + [
        ((x+1, y), (x, y+1))
        for x in range(10)
        for y in range(9)
    ], weight=1.4)

    plt.figure(figsize=(6, 6))
    pos = {(x, y): (y, -x) for x, y in G.nodes()}
    
    ################# Pintar o caminho correto com cor diferente ################
    color_map=[]
    for node in G:
        color="orange"
        for selecionado in caminho:
           
            if selecionado[0]==node[0] and selecionado[1]==node[1]:
               
                color="blue"
        
        color_map.append(color)    
    
    nx.draw(G, pos=pos,
            node_color=color_map,
            with_labels=True,
            node_size=600)


    #Mostrar o gráfico
    plt.show()
    

main()   