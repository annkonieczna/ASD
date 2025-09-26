#O(n^2)

def matrix_to_edges(G):
    n = len(G) 
    adj = []

    for i in range(n): 

        adj.append([])

    for i in range(n): 
        for j in range(n): 

            if G[i][j] == 1: 
                adj[i].append(j)
    return adj 

macierz = [
    [0, 4, 0, 0],
    [4, 0, 2, 7],
    [0, 2, 0, 0],
    [0, 7, 0, 0]
]

print(matrix_to_edges())
n = len(macierz)
lista_sasiedztwa = []
for i in range(n):
    lista_sasiedztwa.append([])

for i in range(n):
    for j in range(n):
        if macierz[i][j] != 0:
            lista_sasiedztwa[i].append((j, macierz[i][j]))











def matrix_to_adj(M): 
    n = len(M)
    G = [[] for i in range(n)]

    for i in range(n): 
        for j in range(n): 
            if M[i][j] != -1:
                G[i].append((j,M[i][j]))
                G[j].append((i,M[i][j]))
    return G
