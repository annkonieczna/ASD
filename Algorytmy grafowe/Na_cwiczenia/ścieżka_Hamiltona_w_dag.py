## Znaleźć ścieżkę Hamiltona w DAGu (jest acykliczny - nie ma w nim oczywiście cyklu Hamiltona) listą sąsiedztwa

# Jeżeli jest ścieżka Hamiltona (w posortowanym topologicznie grafie), mogę iść po kolei z i-tego wierzchołka do 
# i+1 -ego (i jest to możliwe)

# Sortujemy topologicznie dagi O(V + E)


# 0. Chcemy znaleźć ścieżkę Hamiltona, czyli ścieżkę, 
# która przechodzi przez każdy wierzchołek dokładnie jeden raz 
#1.Znajdujemy porządek topologiczny grafu 

#Porządek topologiczny to takie uporządkowanie wierzchołków, że dla każdej krawędzi skierowanej 
#wierzchołek u występuje przed v w uporządkowaniu. W DAG-u zawsze istnieje co najmniej jeden porządek topologiczny.


def hamilton_path(G): 

    n = len(G)
    visited = [False]*n
    path =  []
    # lista, do której dodajemy wierzchołki w kolejności post-order 
    # (wierzchołek dodajemy po przetworzeniu wszystkich jego sąsiadów

    def topological_search(G,u): 

        visited[u] = True 
        for v in G[u]: # przechodzimy przez wszystkich sąsiadów wierzchołka u 
            if not visited[v]: 
                topological_search(G,v)
        path.append(u)

    for u in range(n): 
        if not visited[u]: 
            topological_search(G,u)
    
    path.reverse()

    for i in range(n-1): 
        if not path[i+1] in G[path[i]]: 
            return False 
        
    return True, path 

G = [[1], [2, 4], [3], [4],[]]
print(hamilton_path(G))



# from collections import deque

# def TopologicalSort(G):
#     def DFSVisit(G, u):
#         nonlocal visited
#         nonlocal path

#         visited[u] = True
#         for v in G[u]:
#             if not visited[v]:
#                 DFSVisit(G, v)

#         path.append(u)
    
#     n = len(G)
#     visited = [False for _ in range(n)]
#     path = []

#     for u in range(n):
#         if not visited[u]:
#             DFSVisit(G, u)
    
#     return path

# def HamiltonPath(G):
#     result = TopologicalSort(G)
#     result.reverse()

#     n = len(G)
#     for ver in range(n-1):
#         if result[ver+1] not in G[result[ver]]: return False
    
#     return True


def hamiltonian_path(G): 

    n = len(G)
    visited = [False]*n
    path = []

    def topological_search(G,u): 

        visited[u] = True 

        for v in G[u]: 
            if not visited[u]: 
                topological_search(G,v)
        path.append(u)
        
    for u in G: 
        if not visited[u]: 
            topological_search(G,u)
    
    path.reverse()

    for i in range(n-1): 

        if not path[i+1] in G[path[i]]: 
            return False 
    return True 
