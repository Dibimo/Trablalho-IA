N = None
################### espaço amostral para percorrer #####################
# distancia é sempre 1
# 0 siguinifica custo 0 para percorrer
# maiores valores implicam em desviar a rota, buscando um custo menor

matriz_de_pesos = [
    [1, 3, 3, 3, 3, 1, 2, N],
    [3, 3, 2, 2, 2, 1, N, 1],
    [1, N, 3, 3, 3, 1, 3, 1],
    [2, 3, 2, 3, 3, N, 2, 2],
    [3, 2, 1, 3, 3, 3, 1, 2],
    [3, 1, 2, 2, N, N, 2, 1],
    [3, 1, 1, N, 2, 1, 1, 2],
    [3, 1, 1, 2, 2, N, 3, 3],
]

nomes = [
    'A0', 'B0', 'C0', 'D0', 'E0', 'F0', 'G0', 'H0',
    'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
    'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
    'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
    'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
    'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
    'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
    'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7']
