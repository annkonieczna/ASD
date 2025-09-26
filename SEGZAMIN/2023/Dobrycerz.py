from collections import deque
from math import inf 

def matrix_to_adj(G): 
    n = len(G)
    adj = [[] for _ in range(n)]
    
    for i in range(n): 
        for j in range(i+1,n):
            if G[i][j] != -1:
                adj[i].append((j,G[i][j]))
                adj[j].append((i,G[i][j]))
    return adj

#BFS-a z kolejką deque, gdzie stan to (czas_calkowity, aktualny_zamek, czas_od_noclegu
def BFS(G,s,t): 
    n = len(G)
     #minimalny koszt dotarcia do wierzchołka v z d godzinami od ostatniego noclegu
    dist = [[inf]*17 for _ in range(n)]
    q = deque()
    dist[s][0] = 0 
    q.append((s,0))

    while q: 

        u,d = q.popleft()
        curr_time = dist[u][d]
        if d > curr_time: 
            continue 
        for v,w in G[u]: 

            if d+ w <= 16: 

                if dist[v][w+d] > curr_time + w: 
                    dist[v][w+d] > curr_time + w
                    q.append((v,dist[v][w+d]))
            else: 
                if dist[v][w] > dist[u][d] + 8 + w: 
                    dist[v][w] = dist[u][d] + 8 + w
                    q.append((v,dist[v][w]))
    return min(dist[t])
G = [ [ -1, 3, 8,-1,-1,-1 ], # 0
[ 3,-1, 3, 6,-1,-1 ], # 1
[ 8, 3,-1,-1, 5,-1 ], # 2
[ -1, 6,-1,-1, 7, 8 ], # 3
[ -1,-1, 5, 7,-1, 8 ], # 4
[ -1,-1,-1, 8, 8,-1 ]]
print(BFS(matrix_to_adj(G),0,5))        
