# # Jak znaleźć najkrótsze ścieżki z wierzchołka 
# s do wszystkich innych w acyklicznym grafie skierowanym?
# (mogą być wagi ujemne)

# Zacząć od sorta topologicznego
# Bellman-Ford, ale rozpatrujemy wierzchołki w kolejności topologicznej:
# najpierw robimy relaksację tych, które wychodzą z pierwszego, potem tych, które wychodzą z drugiego itp
# (bo po posortowaniu wszystkie, krawędzie, które możemy rozpatrzyć będą szły w prawo)
# w efekcie nigdy nie zaaktualizujemy tych, które były wcześniej

# O(V + E)

#1. Zaczynamy od sortowania topologicznego 

def DFS(G):
    
    n = len(G)
    visited = [False]*n
    sorted = [None]*n
    k = n-1 # Wskaźnik na ostatnią wolną pozycję w tablicy wynikowej

    def DFS_Visit(G,u): 
        nonlocal k 
        visited[u] = True 

        for v, _ in G[u]: 
            if not visited[v]: 
                DFS_Visit(G,v)
        
        sorted[k] = u # Umieszczamy wierzchołek w tablicy wynikowej
        k -= 1 
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)
    return sorted 


    
def bellman_ford(G,sorted): 

    n = len(G)
    d = [float("inf")]*n
    parents = [None]*n

    d[sorted[0]] = 0 

    for u in sorted: 
        
        for v,w in G[u]: 

            if d[v] > d[u] + w: 

                d[v] = d[u] + w 

                parents[v] = u 
#     # nie musimy weryfikować, bo w dag nie ma cykli 
    return d, parents


# #Kolejność topologiczna gwarantuje, że gdy przetwarzamy wierzchołek u, wszystkie możliwe ścieżki prowadzące do u zostały już rozpatrzone. Dlatego:

# # Każdy wierzchołek potrzebuje tylko jednego przetworzenia

# # Nie ma potrzeby wielokrotnej relaksacji (jak w klasycznym Bellmanie-Fordzie)

# # Wszystkie krawędzie są rozpatrywane dokładnie raz

# def path(G): 

#     sorted = DFS(G)

#     return bellman_ford(G,sorted)


G = [
    [(6, 2)],
    [(0, -5), (2, 10), (5, 0), (3, 8)],
    [],
    [(6, 3), (4, -2)],
    [],
    [(4, 2)],
    [(7, 4)],
    [],
]





def DFS(G): 

    n = len(G)
    visited = [False]*n
    sorted = [None]*n
    k = n-1 

    def DFS_visit(G,u): 

        nonlocal k 

        visited[u] = True 

        for v,_ in G[u]: 

            if not visited[v]: 
                DFS_visit(G,v)
        
        sorted[k] = u 
        k -=1 
    

    for u in range(n): 

        if not visited[u]: 

            DFS_visit(G,u)
    
    return sorted 



def Bellman_Ford(G,s,sorted): 

    n = len(G)

    d = [float('inf')]*n

    parent = [None]*n

    d[s] = 0 

    for u in sorted: 

        for v,w in G[u]: 

            if d[v] > d[u] + w: 

                d[v]  = d[u] + w
                parent[v] = u 
    
    return d, parent 

def path(G,s): 

    sorted = DFS(G)

    return Bellman_Ford(G,s,sorted)


print(path(G,1))








        






            
    



