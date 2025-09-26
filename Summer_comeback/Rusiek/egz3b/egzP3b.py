from egzP3btesty import runtests 
from queue import PriorityQueue
from math import inf
class Node: 
    def __init__(self,value):
        self.parent = self 
        self.value = value 
        self.rank = 0 
def findset(x): 

    if x.parent != x: #jeśli x nie jest korzeniem (x.parent != x), wywołuje rekurencyjnie findset na 
    #rodzicu aż do korzenia

        x.parent = findset(x.parent)
    return x.parent 
def union(x,y): 

    x = findset(x)

    y = findset(y)

    if x == y: 

        return 
    if x.rank > y.rank: #jeśli x.rank > y.rank → przyczepiamy root y pod x 

        y.parent = x 

    else: 

        x.parent = y 

        if x.rank == y.rank: 

            y.rank += 1 
    
def adj_to_edges_minus_weights(G):
    n = len(G) 
    E = []
    for u in range(n): 
        for v,w in G[u]: 
            if u<v:
                E.append((u,v,-w))
    return E

def Kruskal(E): 
    M = [] #MST
    n = max(max(u,v) for u,v,_ in E)+1
    V = [Node(i) for i in range(n)]
    E.sort(key = lambda x: x[2])
    for u,v,w in E: 
        if findset(V[u]) != findset(V[v]): 
            union(V[u],V[v])
            M.append((u,v,w))
    return M 
def lufthansa ( G ):
    suma = 0 
     
    
    E = adj_to_edges_minus_weights(G)
    # print(E)
    all_weights = 0
    for _,_,w in E: 
        all_weights -= w
    # print(all_weights)
    M = Kruskal(E)
    # print(M)
    E.sort(key = lambda x: x[2])
    M.sort(key = lambda x: x[2])
    i = 0
    # while i < len(E): 
    #     if E[i][2] == M[i][2]:
    #         i += 1 
    #     else:
    #         break
    #     j = i 
    i = j = 0
    extra = None
    while i < len(E) and j < len(M):
        if E[i] == M[j]:
            i += 1
            j += 1
        else:
            extra = E[i]
            break

    if extra is None and i < len(E):
        extra = E[i]
    # D = [row[:] for row in G]
    
    for _,_,w in M: 
        suma -= w
    # print(suma)
    return all_weights- (suma -extra[2])
    
# G = [
#       [(1, 15), (2, 5),  (3, 10)],
#       [(0, 15), (2, 8),  (4, 5),  (5, 12)],
#       [(0, 5),  (1, 8),  (3, 5),  (4, 6)],
#       [(0, 10), (2, 5),  (4, 2),  (5, 11)],
#       [(1, 5),  (2, 6),  (3, 2),  (5, 2)],
#       [(1, 12), (4, 2),  (3, 11)]]
# print(Kruskal(adj_to_edges_minus_weights(G)))

# def tired(G): 
#     M = Kruskal(adj_to_edges_minus_weights(G))
#     print(G)
#     for u,v,w in M:  
#         G[u][v] = (v,-inf)
#         G[v][u] = (u,-inf)
#     return G
# print(lufthansa(G))





runtests ( lufthansa, all_tests=True )