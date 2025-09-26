from egzP1btesty import runtests 

def turysta( E, D, L ):
    G = edges_to_adj_list(E)
    d = Dijkstra(G,D,L)

    return d[L][3]
def edges_to_adj_list(E):
    n = max(max(u,v) for u,v,_ in E ) +1 
    G = [[] for _ in range(n)]
    for u,v,w in E: 
        G[u].append((v,w))
        G[v].append((u,w))
    return G 

from math import inf
import heapq
def Dijkstra(G,s,t):
    n = len(G)
    q = []
    heapq.heappush(q,(0,0,s))
    d = [[inf]*4 for _ in range(n)]
    d[s][0]= 0
    while q: 
        dist, count, u = heapq.heappop(q)
        
        for v,w in G[u]: 
            # print(v,d[v])
            if v == t: 
                if count == 3: 
                    if d[v][3] > d[u][count] + w: 
                        d[v][3] = d[u][count] + w 
                        continue
                else: 
                    continue
            else: 
                if count < 3:
                    if d[v][count+1] > d[u][count] + w: 
                        d[v][count+1] = d[u][count]+ w
                        heapq.heappush(q,(d[v][count+1],count+1,v))
    return d 

runtests ( turysta )
