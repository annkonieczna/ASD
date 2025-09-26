from kol2testy import runtests
#BFS o mniejszej złożoności do sprawdzania spójności i tego czy ma cykle
#Mniejsza złożoność, bo graf, który sprawdzamy ma V-1 krawędzi, więc złożoność BFS(V+E), więc BFS(2V+1)~BFS(V)
#mądre kochani mądre
from collections import deque
def BFS(G,s,n):
    q = deque()
    q.append(s)
    visited = [False]*n
    parents = [None]*n 
    visited[s] = True 
    num_visited = 1

    while q: 
        u = q.popleft()

        for v,_ in G[u]: 
            if not visited[v]: 
                visited[v] = True 
                parents[v] = u 
                num_visited += 1 
                q.append(v)
            else: #jeżeli już odwiedzony to sprawdzam czy nie wracam krawędzią wsteczną, bo jeśli tak to mamy cykl 
                if v != parents[u]:
                    return False
    return num_visited == n



def beautree(G):
    n = len(G)
    E = adj_to_edges(G)
    E.sort(key = lambda x : x[2])

    l = 0  # wskaźniki na nasze okienko
    r = 0
    sum_w = 0 
    T = [deque() for _ in range(n)] # tymczasowe drzewo z wierzchołkami tylko w poddrzewie 
    while r < len(E): 
        if (r -l) < n-1: 
            u,v,w = E[r]
            T[u].append((v,w))
            T[v].append((u,v))
            r += 1 
            sum_w += w

        else: 
            u,v,w = E[l]
        
            if BFS(T,0,n):
                return sum_w
            T[u].popleft()
            T[v].popleft()
            sum_w -= w 
            l += 1 

    return None






    
def adj_to_edges(G):
    n = len(G)
    E = []
    for u in range(n): 
        for v,w in G[u]: 
            if u < v: 
                E.append((u,v,w))
    return E
# G = [ [(1,3), (2,1), (4,2)], # 0
# [(0,3), (2,5) ], # 1
# [(1,5), (0,1), (3,6)], # 2
# [(2,6), (4,4) ], # 3
# [(3,4), (0,2) ] ]
# print(beautree(G))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
