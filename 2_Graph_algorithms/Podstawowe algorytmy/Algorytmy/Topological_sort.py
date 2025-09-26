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

# Złożoność: O(V+E)
def top_sort(G): 

    n = len(G)
    visited = [False]*n 
    k = n-1 
    sorted = []

    def DFS_Visit(G,u): 
        nonlocal k 

        visited[u] = True 

        for v in G[u]: 
            if not visited[v]: 
                
                DFS_Visit(G,v)
        sorted[k] = u 
        k -= 1 
    
    for u in range(n): 

        if not visited[u]: 
            DFS_Visit(G,u)
    
    return sorted 

