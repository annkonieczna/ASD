# Obliczyć domknięcie przechodnie grafu G w postaci macierzowej.

# Domknięcie - każda para wierzchołków, w grafie w którym istnieje ścieżka, to ma krawędź bezspośrednio między
# swoimi wierzcholkami

# Graf domknięty - graf w którym istnieje bezpośrednia krawędź między każdym z wierzchołków,
# między którymi idzie ścieżka (na początku)

# Jeżeli w grafie G da się przejść między wierzchołkami, to w grafie domkniętym przechodnio
# te wierzchołki mają bezpośrenią krawędź między sobą.

# Po prostu algorytm Floyda-Warshalla -> jak da się przejść to będzie miał coś co nie jest nieskończonością

# i potem te nie-nieskończoności przestawiamy na 1 --> i mamy graf wynikowy




#Floyd Warshall- Najkrótsze odległości między wszystkimi parami wierzchołków (i, j).





def Floyd_washall(G): 

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







    


