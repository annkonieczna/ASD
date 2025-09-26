
def matrix_to_edges(G): 

    n = len(G)

    edges = []
    for i in range(n): 

        for j in range(i +1, n): #Ten zakres gwarantuje, że rozpatrujemy 
            #tylko połowę macierzy (nad przekątną) — gdzie i < j

            if G[i][j] != 0: 
                edges.append((i,j,G[i][j]))
    return edges

G = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

print(matrix_to_edges(G))
