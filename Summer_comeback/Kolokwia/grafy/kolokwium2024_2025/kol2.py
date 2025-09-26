from kol2testy import runtests

#Miasta to wierzchołki 
#W niektórych miastach znajdują się ośrodki wypoczynkowe- po jednym w czasie każdej podróży- R tablica tych ośrodków 
#Zawsze startując z miasta startowego chcemy odwiedzić wszystkie ośrodki wypoczynkowe 
import heapq
from math import inf 
def edges_to_adj(E): 
    n = max(max(u,v) for u,v,_ in E)+1
    G = [[] for _ in range(n)]
    for u,v,w in E: 
        G[u].append((v,w))
        G[v].append((u,w))
    return G 
def lets_roll(start_city, flights, resorts): 
    G = edges_to_adj(flights)
    n = len(G)
    q = []
    d = [inf]*n
    d[start_city] = 0 
    remaining = len(resorts)
    is_resort = [False]*n 
    is_visited = [False]*n 
    for i in range(len(resorts)): 
        is_resort[resorts[i]] = True
    heapq.heappush(q,(0,start_city))
    cost = 0 

    while q: 
        dist, u  = heapq.heappop(q)
        if dist > d[u]: 
            continue
        #jeśli wierzchołek, który wyciągniemy z kolejki jest resortem:
        if is_resort[u]== True:
            is_visited[u] = True #Zaznaczamy, że został odwiedzony 
            cost += 2*dist #dodajemy koszt podróży 
            remaining -= 1
            if remaining == 0: 
                return cost 
            #Nie relaksujemy jego sąsiadów 
            continue
        #Nie jest resortem 
        for v, w in G[u]: #przechodzimy przez sąsiadów  
            if is_visited[v]: #jeśli jest resortem
                continue #nie przechodzimy  
            if d[v] > d[u] + w: #dokonujemy relaksacji 
                d[v] = d[u] + w
                heapq.heappush(q,(d[v],v))
    return cost

#gorsza złożoność, ale działa 

# def lets_roll(start_city,flight,resorts): 
#     G = edges_to_adj(flight)
#     n = len(G)
#     visited = [False]*n 
#     is_resort = [False]*n
#     for r in resorts: 
#         is_resort[r] = True 
#     count = 0 
#     def Dijkstra(G,start_city):
#         nonlocal count 
#         q = []
#         heapq.heappush(q,(0,start_city)) 
#         d = [inf]*n
#         d[start_city] = 0
#         while q: 
#             dist,u = heapq.heappop(q)
#             if is_resort[u]: 
#                 visited[u] = True 
#                 count += dist*2
#                 return 
#             for v,w in G[u]: 
#                 if not visited[v]:
#                     if d[v] > dist + w: 
#                         d[v] = dist+ w 
#                         heapq.heappush(q,(d[v],v))

    
#     for i in range(len(resorts)): 
#         Dijkstra(G,start_city)
#     return count 



    


runtests(lets_roll, all_tests = True)
