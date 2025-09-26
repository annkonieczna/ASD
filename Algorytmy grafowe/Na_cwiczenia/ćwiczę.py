def hamiltonian_path(G): 

    n = len(G)
    visited = [False]*n
    path = []

    def topological_search(G,u):

        visited[u] = True 

        for v in G[u]: 
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
    return True


G = [[1], [2, 4], [3], [4],[]]
print(hamiltonian_path(G))


def hamiltonian_path(G): 

    n = len(G)
    visited = [False]*n
    path = []

    def topological_search(G,u): 

        visited[u] = True 

        for v in G[u]: 
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
    return True 

    
G = [[1], [2, 4], [3], [4],[]]
print(hamiltonian_path(G))


