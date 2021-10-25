import Matrizes

def verifica_pontos_iguais(ponto, node) -> bool:
    x_ponto = ponto[0]
    y_ponto = ponto[1]

    x_node = node[0]
    y_node = node[1]

    return (x_ponto == x_node) and (y_ponto == y_node)

def converter_para_hexadecimal(rgb) -> str:
    for i in range(0,3):
        if(rgb[i] > 255):
            rgb[i] = 255
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    return '#%02x%02x%02x' % (red, green, blue)

def receber_valores(largura,altura) -> list:

    valores = []
    largura_e_altura = [largura,altura]
    textos = [f"Insira o valor de x0 para iniciar! (x<={largura}) : ",
              f"Insira o valor de y0 para iniciar! (y<={altura}) : ",
              f"Insira o valor de x a ser encontrado! (x<={largura}) : ",
              f"Insira o valor de y a ser encontrado! (y<={altura}) : ",
            ]
    
    for i in range(0,4):
        valor_incorreto = True
        while(valor_incorreto):

            if(len(valores) == i):
                valores.append(int(input(textos[i])))
            else:
                valores[i] = int(input(textos[i]))

            valor_incorreto = (valores[i] > largura_e_altura[i%2])
            if(valor_incorreto):
                print(f'Digite um valor até {largura_e_altura[i%2]}')

    return valores

def retorna_valores_cores(caminho,rgb) -> dict:
    quantidade_de_nodos = len(caminho)
    invervalos = [int(pixel/(quantidade_de_nodos)) for pixel in rgb]
    cores = {}
    for i in range(0,quantidade_de_nodos):
        x,y = caminho[i]
        cores[(x,y)] = converter_para_hexadecimal([(pixel * (i+2)) for pixel in invervalos])

    return cores

def retorna_lista_labels(grafico,nomes):
    nomes_nodos = {}
    matriz_pesos = Matrizes.matriz_de_pesos
    i = 0
    for nodo in grafico:
        x,y = nodo
        peso = matriz_pesos[y][x] if matriz_pesos[y][x] != None else 'N'
        nomes_nodos[nodo] = f'{nomes[i]} {peso}'
        i += 1
    return nomes_nodos

def retorna_lista_cores(grafico,matriz_de_pesos,caminho,cor_rgb):
    valores_cores_caminho = retorna_valores_cores(caminho, cor_rgb)
    lista_de_cores = []
    temp = [
        [1,0],
        [3,1],
        [5,4],
        [6,5],
        [4,7],
        [7,6]
    ]
    for nodo in grafico:
        cor_nodo = "orange"
        x, y = nodo
        if([x,y] in temp):
            cor_nodo = "#4b83c4"
        if(x == 0 and y == 2):
            cor_nodo = "#9e4bc4"
        if([x, y] in caminho):
            cor_nodo = valores_cores_caminho[nodo]
        if(matriz_de_pesos[y][x] == None):
            cor_nodo = "#bd2b2b"
            # print((x,y))
        lista_de_cores.append(cor_nodo)
    return lista_de_cores

