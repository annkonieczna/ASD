
def adj_to_matrix(G): 

    n = len(G)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):

        for j, w in G[i]: 

            G[i][j] = w 
    return matrix 