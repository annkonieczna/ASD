#Silnie spójne składowe w grafie skierowanym 

#Silnie spójna składowa dla grafu skierowanego: 
#maksymalny podgraf, w którym każdy wierzchołek jest osiągalny z innego wierzchołka w tym podgrafie 

#nie możemy dodać żadnego wierzchołka spoza podgrafu, bo wtedy warunek silnej spójności przestanie być spełniony
#Nie zachodzą na siebie – różne SCC w grafie są rozłączne (wierzchołki należą do jednej i tylko jednej SCC).


# 1. Wykonaj DFS zapamiętując czasy przetworzenia wierzchołków.
# 2. Odwróć kierunek krawędzi.
# 3. Wykonaj DFS ponownie, w kolejności malejących czasów przetwarzania z pierwszego DFS.


def DFS1(G): 

    n = len(G)
    times = [None]*n 
    visited = [False]*n
    time = 0 #czas kiedy wychodzimy z danego wierzchołka (dlatego dopiero go aktualniamy po przetworzeniu)

    def DFS_Visit(G,u): 
        nonlocal time 
        visited[u] = True 
         

        for v in G[u]: 
            if not visited[v]: 
                DFS_Visit(G,v)
        
        times[u] = (time,u) #krotka by potem móc sortować 
        time += 1

    for u in range(n): 
        if not visited[u]: 
            DFS_Visit(G,u)
    
    return times 

#transponujemy graf - odwracamy krawędzie 

def transpose_graph(G):

    n = len(G)
    G2 = [[] for _ in range(n)]

    for u in range(n): 
        for v in G[u]: 
            G2[v].append(u)

    return G2

def DFS2(G,times):

    n = len(G) 
    visited = [False]*n
    res = [] #silnie spójne składowe jako lista wierzchołków 
    def DFS_Visit2(G,u,comp): #component- buduje jedną silną składową 
        visited[u] = True 
        comp.append(u)

        for v in G[u]: 
            if not visited[v]: 
                DFS_Visit2(G,v,comp)
    
    for _,u in times: #są już posortowane malejąco po czasach, więc one nas już nie interesują 
        if not visited[u]: 
            comp = []
            DFS_Visit2(G,u,comp)
            res.append(comp)
    return res


        

def silnie_spojne_skladowe(G):
    times = DFS1(G)
    times.sort(reverse=True) #sortujemy malejąco po czasie
    graph_transponed = transpose_graph(G)
    return DFS2(graph_transponed,times)

G = [
    [1],
    [2],
    [0, 3],
    [4],
    [5],
    [6],
    [3]
]

print(silnie_spojne_skladowe(G))


def DFS1(G, u, visited, stack):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFS1(G, v, visited, stack)
    stack.append(u)   # <- na stos przy wyjściu


def DFS2(Gt, u, visited, comp):
    visited[u] = True
    comp.append(u)
    for v in Gt[u]:
        if not visited[v]:
            DFS2(Gt, v, visited, comp)


def transpose(G):
    n = len(G)
    Gt = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            Gt[v].append(u)
    return Gt


def kosaraju(G):
    n = len(G)
    visited = [False] * n
    stack = []

    # 1. Pierwszy DFS – wypełniamy stos wierzchołków wg czasu zakończenia
    for u in range(n):
        if not visited[u]:
            DFS1(G, u, visited, stack)

    # 2. Transpozycja grafu
    Gt = transpose(G)

    # 3. Drugi DFS w kolejności podanej przez stos
    visited = [False] * n
    scc = []

    while stack:   # wyciągamy ze stosu od końca
        u = stack.pop()
        if not visited[u]:
            comp = []
            DFS2(Gt, u, visited, comp)
            scc.append(comp)

    return scc







    

