#Idea: 
#Liczymy disc[u] i low[u] tak samo jak w mostach 

#Punkt artukulacji to wierzchołek, który spełnia jeden z 2 warunków:
#1. wierzchołek jest korzeniem i ma co najmniej 2 dzieci w drzewie DFS 
#2. nie jest korzeniem i isnieje dziecko v takie, że low[v] >=disc[u]

#czyli poddrzewo v nie ma krawędzi wstecznej, która wraca wyżej niż u

from math import inf

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

    return list(art_points)


G = [
    [3, 9],
    [2, 3],
    [1, 3, 4],
    [0, 1, 2],
    [2, 5, 6, 8],
    [4, 6],
    [4, 5, 7],
    [6, 8],
    [4, 7],
    [0]
]

print(articulation_points(G))



