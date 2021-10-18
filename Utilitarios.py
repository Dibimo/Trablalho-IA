
def verifica_valores(ponto, node) -> bool:
    x_ponto = ponto[0]
    y_ponto = ponto[1]

    x_node = node[0]
    y_node = node[1]

    return (x_ponto == x_node) and (y_ponto == y_node)

def converter_para_hexadecimal(verde) -> str:
    red = 152
    green = verde
    blue = 123
    return '#%02x%02x%02x' % (red, green, blue)

def receber_valores(largura,altura):

    valores = []
    largura_altura = [largura,altura]
    textos = ["Insira o valor de x0 para iniciar! (x<10) : ",
              "Insira o valor de y0 para iniciar! (y<9) : ",
              "Insira o valor de x a ser encontrado! (x<10) : ",
              "Insira o valor de y a ser encontrado! (y<9) : ",
            ]
    
    for i in range(0,4):
        valor_incorreto = True
        while(valor_incorreto):

            if(len(valores) == i):
                valores.append(int(input(textos[i])))
            else:
                valores[i] = int(input(textos[i]))

            valor_incorreto = (valores[i] > largura_altura[i%2])
            if(valor_incorreto):
                print(f'Digite um valor até {largura_altura[i%2]}')

    return valores
