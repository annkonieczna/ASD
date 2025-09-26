#Złożoność czasowa: θ(V+E)

#Złożoność pamięciowa: θ(V) - Informacja o kolejce i przechowywanych wierzchołkach 

#Idea algorytmu: 

#Przeszukiwanie wszerz 
# Odwiedza wszystkie wierzchołki osiągalne z danego wierzchołka wyjściowego, poziom 

#Każda krawędż to kanał z wodą, biorę kamień i wrzucam go do wierzchołka 1 i rozchodzą się fale 

#Każdy wierzchołek ma pola: 
#1. visited - czy fala doszła do tego wierzchołka 
#2. parent - skąd ta fala doszła
#3. d - odległość 
#4. kolejka - gdzie fala jest obecnie 

#Zastosowania: 
# 1. Znajdowanie najkrótszej ścieżki w grafie nieważonym

# 2. Sprawdzanie spójności grafu


from collections import deque
#deque - double ended queue 


# def BFS(Graph,start):
#     Q = deque[start]
#     n = len(Graph)
#     visited = [False]*n
#     result = []
#     distance = [None]*n 
#     distance[start] = 0 
#     parent = [-1]*n #-1 brak rodzica
#     counter = 1


#     while Q: 
#         vertex = Q.popleft()

#         if not visited[vertex]: 

#             for neighbour in Graph[vertex]: 
#                 if not visited[neighbour]: 
#                     visited[neighbour] = True 
#                     distance[neighbour] = distance[vertex] + 1 
#                     parent[neighbour] = vertex 
#                     Q.aappend(neighbour)
#     return distance, counter







# from collections import deque

# def bfs_with_count(G, start):
#     n = len(G)
#     dist = [None] * n
#     count = [0] * n
#     dist[start] = 0
#     count[start] = 1
#     q = deque()
#     q.append(start)
#     while q:
#         u = q.popleft()
#         for v in G[u]:
#             if dist[v] is None:
#                 dist[v] = dist[u] + 1
#                 count[v] = count[u]
#                 q.append(v)
#             elif dist[v] == dist[u] + 1:
#                 count[v] += count[u]
#     return dist, count

# def longer(G, s, t):
#     dist_s, count_s = bfs_with_count(G, s)
#     dist_t, count_t = bfs_with_count(G, t)

#     if dist_s[t] is None:
#         return None

#     shortest_len = dist_s[t]
#     total_paths = count_s[t]

#     n = len(G)
#     visited_edges = set()
#     for u in range(n):
#         for v in G[u]:
#             if (v, u) in visited_edges:
#                 continue
#             visited_edges.add((u, v))
#             # Sprawdź czy krawędź (u, v) leży na jakiejś najkrótszej ścieżce
#             if dist_s[u] + 1 + dist_t[v] == shortest_len:
#                 # Ile ścieżek przechodzi przez (u,v)?
#                 through_edge = count_s[u] * count_t[v]
#                 if through_edge == total_paths:
#                     return (u, v)
#             elif dist_s[v] + 1 + dist_t[u] == shortest_len:
#                 through_edge = count_s[v] * count_t[u]
#                 if through_edge == total_paths:
#                     return (v, u)
#     return None


# #BFS'ik 
# #służy do znajdowania najkrótszych ścieżek w grafach nieważonych lub sprawdzania spójności grafu 
# # złożoność O(V+E)

# #Idea: Odwiedza wszystkie możliwe wierzchołki z wierzchołka wyjściowego 
# #Używa kolejki deque

# from collections import deque

# def BFS(G,s): 

#     n = len(G)

#     visited = [False]*n 
#     parents = [None]*n 
#     q = deque[s]
#     visited[s] = True
#     distance = [None]*n # optional
#     distance[s] = 0  #optional 
    
#     while q: 

#         u = q.popleft()
#         for v in G[u]: 

#             if not visited[v]: 

#                 visited[v] = True
#                 parents[v] = u 
#                 distance[v] = distance[u] + 1 

#                 q.append(v)
#     return parents  




# from collections import deque

# def BFS(G,s): 

#     n = len(G)
#     visited = [False]*n
#     distance = [-1]*n
#     parents = [None]*n
#     q = deque()
#     q.append(s)
#     distance[s] = 0 
#     visited[s] = True

#     while q: 
#         u = q.popleft()

#         for v in G[u]: 
#             if not visited[v]: 
#                 visited[v] = True
#                 distance[v] = distance[u]+1
#                 parents[v] = u
#                 q.append(v)
#     return distance, parents 



from collections import deque 


def BFS(G,s): 
    n = len(G)
    visited = [False]*n
    q = deque()
    q.append(s)
    distance = [-1]*n
    distance[s] = 0 
    parent = [None]*n
    visited[s] = True

    while q: 
        u = q.popleft()
        for v in G[u]: 
            if not visited[v]: 
                visited[v] = True 
                q.append(v)
                parent[v] = u 
                distance[v] = distance[u] + 1 

    
    return distance, visited, parent 





from collections import deque 


def BFS_HIHI(G,s): 
    n = len(G)
    visited = [False]*n 
    parents = [None]*n 
    distance = [-1]*n
    q = deque([s])
    distance[s] = 0 
    visited[s] = True 

    while q: 
        u = q.popleft()

        for v in G[u]: 
            if not visited[v]: 
                visited[v] = True 
                parents[v] = u 
                distance[v] = distance[u] + 1 
                q.append(v)
    
    return visited, parents, distance 

def get_path(G,s):
    n = len(G)
    _,parents,distance = BFS_HIHI(G,s)
    maxi = -1
    end = None 

    for i in range(n):
        if distance[i] > maxi: 
            maxi = distance[i]
            end = i

    path = []
    while end is not None: #zakończy się jak dojdziemy do startowego 
        path.append(end)
        end = parents[end]
    return path[::-1]

 



    










    














    

    



