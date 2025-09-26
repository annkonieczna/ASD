#Idea

#Algorytm znajduje najkrótszą ścieżkę z każdego wierzchołka do każdego w grafie 
#Reprezentacja grafu musi być macierzowa 
# Złożoność O(V^3) - opłaca się w grafach gęstych 
# Można go stosować z ujemnymi wagami 


def Floyd_Warshall(W): 

    n = len(W)
    parent = []    
    
    # szukamy se czy istnieje ścieżka z x do y przez dowolny pośredni k 
    for k in range(n): 
        for u in range(n): 
            for v in range(n): 
                
                s = W[u][k] + W[k][v]

                if W[u][v] > s: 

                    W[u][v] = s
    return W 


def Floyd_warshall(G): 

    n = len(G)
    D = [row[:] for row in G]

    #Szukasz czy istnieje ścieżka z x do y, przez dowolny pośredni k
    
    for k in range(n): 

        for x in range(n):

            for y in range(n): 

                s = D[x][k] + D[k][y]
                
                if D[x][y] > s: 

                    D[x][y] = s 

    for i in range(n): 
        for j in range(n): 

            if D[i][j] != float("inf"): 

                D[i][j] = 1 

    return D
