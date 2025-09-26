# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można
# osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy dany graf
# zawiera dobry początek.

def find_entrance(G): 
    n = len(G)
    visited = [False]*n
    def DFSVisit(G,u): 
        visited[u] = True 
        for v in G[u]:
            DFSVisit(G,v)

    for u in range(n): 
        if not visited[u]: 
            DFSVisit(G,u)
            visited[u] = False 

