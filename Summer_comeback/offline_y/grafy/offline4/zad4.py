from zad4testy import runtests

#N wierzchołków
#Graf w postaci listy kraedzi (u,v,w)
def edges_to_adj(E,n):
    
    G = [[] for _ in range(n)]
    for u,v,w in E: 
        G[u].append((v,w))
        G[v].append((u,w))
    return G 

import heapq
from math import inf
def spacetravel( n, E, S, a, b ):
    G = edges_to_adj(E,n)
    supernode = n 
    G.append([])
    for s in S:
        G[s].append((supernode,0))
        G[supernode].append((s,0)) 
        
    dist = [inf]*(n+1)
    q = []
    dist[a] = 0 
    heapq.heappush(q,(0,a))

    while q: 
        distance, u = heapq.heappop(q)
        if distance > dist[u]: 
            continue
        for v,w in G[u]: 
            if dist[v] > distance + w: 
                dist[v] = distance + w
                heapq.heappush(q,(dist[v],v))
    if dist[b] == inf: 
        return None 
    return dist[b]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
