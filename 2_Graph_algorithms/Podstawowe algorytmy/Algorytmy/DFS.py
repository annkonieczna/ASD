#Rekurencyjnie
#Złożoność O(E+V)

def DFS(G): 
    n = len(G)
    visited = [False]*n 
    parents = [None]*n


    def DFS_Visit(G,u): 
        
        visited[u] = True  

        for v in G[u]: 

            if not visited[v]: 
                
                parents[v] = u 
                DFS_Visit(G,v)
    for u in range(n): 
        if not visited[u]: 
            DFS_Visit(G,u)
    return parents 


def DFS(G): 
    n = len(G)
    visited = [False]*n
    parents = [None]*n 

    def DFS_Visit(G,u): 
        visited[u] = True 

        for v in G[u]: 
            
            if not visited[v]: 

                parents[v] = u

                DFS_Visit(G,v)
    
    for u in range(n): 
        if not visited[u]: 
            DFS_Visit(G,u)
    
    return parents 




def topo_sort(G): 

    n = len(G)
    visited = [False]*n
    parents = [None]*n
    sorted = [None]*n
    k = n-1

    def DFS_Visit(u):
        nonlocal k 

        visited[u] = True 

        for v in G[u]: 
            if not visited[v]: 
                parents[v] = u 
                DFS_Visit(v)
        sorted[k] = u
        k -= 1
        
    for u in range(n): 
        if not visited[u]: 
            DFS_Visit(u)

    return sorted


G = [
    [1, 2],
    [3],
    [3],
    []
]
print(topo_sort(G))





def DFS(G): 
    n = len(G)
    visited = [False]*n 
    parents = [None]*n

    def DFS_Visit(G,u): 
        visited[u] = True 
        for v in G[u]: 
            if not visited[v]: 
                parents[v] = u 
                DFS_Visit(G,v)
    
    for u in range(n): 
        if not visited[u]: 
            DFS_Visit(G,u)
    return parents






def topol_sort(G): 
    n = len(G)
    sorted = [None]*n
    visited = [False]*n
    k = n-1
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


G = [
    [1, 2],
    [3],
    [3],
    []
]
print(topol_sort(G))




def DFS_yay(G): 
    n = len(G)
    visited = [False]*n 
    parents = [None]*n 

    def DFS_Visit(G,u): 

        visited[u] = True 
        for v in G[u]: 
            if not visited[v]: 
                parents[v] = u 
                DFS_Visit(G,v)

    for u in range(n): 
        if not visited[u]: 
            DFS_Visit(G,u)
    return visited,parents


def topolo_sort(G): 
    n = len(G)
    visited = [False]*n
    k = n-1
    sorted = [None]*n

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

G = [
    [1, 2],
    [3],
    [3],
    []
]
print(topolo_sort(G))



def DFS(G): 
    n = len(G)
    visited = [False]*n 
    parents = [None]*n 

    def DFS_Visit(G,u): 
        visited[u] = True 
        
        for v in G[u]: 
            if not visited[v]: 
                parents[v] = u 
                DFS_Visit(G,v)
    for u in range(n): 
        if not visited[u]: 
            DFS_Visit(G,u)
    return visited, parents 

def topoh_sort(G): 
    n = len(G)
    k = n-1 
    topp = [None]*n
    visited = [False]*n 

    def DFS_Visit(G,u): 
        nonlocal k 
        visited[u] = True 

        for v in G[u]: 
            if not visited[v]: 
                DFS_Visit(G,v)
        topp[k] = u 
        k-= 1 
    
    for u in range(n): 
        if not visited[u]: 
            DFS_Visit(G,u)
    return topp


print(topoh_sort(G))

