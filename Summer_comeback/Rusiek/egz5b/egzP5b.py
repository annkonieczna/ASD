from egzP5btesty import runtests 
from math import inf
def koleje (B):
    n = 0 
    for i in range(len(B)): 
        B[i] = (min(B[i][0],B[i][1]),max(B[i][0],B[i][1]))

    
    B.sort(key= lambda x : (x[0],x[1]))
    last = (None,None)
    K = []
    for p,k in B:
        i,j = last 
        if i==p and j== k:
            continue 
        last = (p,k)
        K.append(last)


    n = max((max(u,v) for u,v in K)) +1 
    G = [[] for _ in range(n)]
    for u,v in K: 
        G[u].append(v)
        G[v].append(u)   
    
    
    
    return articulation_points(G)
def articulation_points(G): 
    n = len(G)
    disc = [inf]*n
    low = [inf]*n
    parents = [None]*n
    art_points = set() #by uniknąć duplikatów 
    time = 0

    def DFS_Visit(G,u): 
        nonlocal time 

        low[u] = disc[u] = time 
        time += 1 
        children = 0 

        for v in G[u]: 
            

            if disc[v] == inf: 
                parents[v] = u 
                children += 1
                DFS_Visit(G,v)

                low[u] = min(low[v],low[u])

                #warunek 1: nie jest korzeniem i low[v] >= disc[u]
                if parents[u] is not None and low[v] >= disc[u]: 
                    art_points.add(u)

            #warunek 2: jest korzeniem i ma 2 dzieci 
            if children >= 2 and parents[u] == None: 
                art_points.add(u)
            #krawędz wsteczna
            elif parents[u] != v: 
                low[u] = min(low[u], disc[v])
    
    for u in range(n): 
        if disc[u] == inf: 
            DFS_Visit(G,u)

    return len(list(art_points))

runtests ( koleje, all_tests=True)