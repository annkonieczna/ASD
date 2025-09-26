from collections import deque
#deque - double ended queue 


def BFS(Graph,start):
    Q = deque[start]
    n = len(Graph)
    distance = [None]*n 
    distance[start] = 0 
    parent = [-1]*n #-1 brak rodzica
    counter = [0]*n
    counter[start] = 1 # liczy ile jest najkrótszych ścieżek z s do v 



    while Q: 
        vertex = Q.popleft() 

        for neighbour in Graph[vertex]: 
            if not distance[neighbour]:
                distance[neighbour] = distance[vertex] + 1
                counter[neighbour] = counter[vertex] 
                Q.aappend(neighbour)
            elif distance[neighbour] == distance[vertex] +1: 
                counter[neighbour] += counter[vertex]
    return distance, counter

def longer(G,s,t): 
    dist_s,count_s = BFS(G,s)
    dist_t,count_t = BFS(G,t)

    if dist_s[t] is None: 
        return None 
    
    shortest_length = dist_s[t]
    total_paths = count_s[t]

    n = len(G)

    for u in range(G): 
        for v in G[u]: 
            if u <v: 
                pass





# Jan Kowalski
# Algorytm znajduje najkrótszą odległość z s do t za pomocą BFS. Następnie, wykonując dodatkowe BFS-y, liczymy ile różnych najkrótszych ścieżek prowadzi z s do każdego wierzchołka oraz z każdego do t.
# Krawędź {u, v} leży na jakiejś najkrótszej ścieżce z s do t wtedy i tylko wtedy, gdy: dist[s][u] + 1 + dist[v][t] == dist[s][t].
# Jeśli przez daną krawędź przechodzi *wszystkie* najkrótsze ścieżki z s do t (czyli po jej usunięciu nie da się złożyć innej najkrótszej ścieżki), to jej usunięcie spowoduje wydłużenie drogi.
# Złożoność to O(V + E), ponieważ używamy tylko kilku BFS-ów i prostego przeglądu krawędzi.

# Jan Kowalski
# Algorytm znajduje najkrótszą odległość z s do t za pomocą BFS. Następnie, wykonując dodatkowe BFS-y, liczymy ile różnych najkrótszych ścieżek prowadzi z s do każdego wierzchołka oraz z każdego do t.
# Krawędź {u, v} leży na jakiejś najkrótszej ścieżce z s do t wtedy i tylko wtedy, gdy: dist[s][u] + 1 + dist[v][t] == dist[s][t].
# Jeśli przez daną krawędź przechodzi *wszystkie* najkrótsze ścieżki z s do t (czyli po jej usunięciu nie da się złożyć innej najkrótszej ścieżki), to jej usunięcie spowoduje wydłużenie drogi.
# Złożoność to O(V + E), ponieważ używamy tylko kilku BFS-ów i prostego przeglądu krawędzi bez dodatkowych struktur danych.

from collections import deque

def bfs_with_count(G, start):
    n = len(G)
    dist = [None] * n
    count = [0] * n
    dist[start] = 0
    count[start] = 1
    q = deque()
    q.append(start)
    while q:
        u = q.popleft()
        for v in G[u]:
            if dist[v] is None:
                dist[v] = dist[u] + 1
                count[v] = count[u]
                q.append(v)
            elif dist[v] == dist[u] + 1:
                count[v] += count[u]
    return dist, count

def longer(G, s, t):
    dist_s, count_s = bfs_with_count(G, s)
    dist_t, count_t = bfs_with_count(G, t)

    if dist_s[t] is None:
        return None

    shortest_len = dist_s[t]
    total_paths = count_s[t]

    n = len(G)
    for u in range(n):
        for v in G[u]:
            if u < v:  # rozpatrujemy każdą krawędź tylko raz
                # Sprawdź czy krawędź (u, v) leży na jakiejś najkrótszej ścieżce
                if dist_s[u] + 1 + dist_t[v] == shortest_len:
                    through_edge = count_s[u] * count_t[v]
                    if through_edge == total_paths:
                        return (u, v)
                elif dist_s[v] + 1 + dist_t[u] == shortest_len:
                    through_edge = count_s[v] * count_t[u]
                    if through_edge == total_paths:
                        return (u, v)
    return None



G = [ [1, 2],
      [0, 2],
      [0, 1] ]
print(longer(G, 0, 2))



