from egz1atesty import runtests
import heapq
from math import inf,floor 
# def edges_to_adj(E,n):
#   G = [[] for _ in range(n)]
#   for u,v,w in E: 
#     G[u].append((v,w))
#     G[v].append((u,w))
#   return G

# def Dijkstra(G,s,n): 
#   q = []
#   distance = [inf]*n
#   distance[s] = 0 
#   heapq.heappush(q,(0,s))
#   while q: 
#     d,u = heapq.heappop(q)
#     if d > distance[u]: 
#       continue
#     for v,w in G[u]: 
#       if distance[v] > d + w: 
#         distance[v] = d + w
#         heapq.heappush(q,(distance[v],v))
#   return distance




# def armstrong( B, E, s, t):
#   n = max(max(u,v) for u,v,_ in E)+1
#   G = edges_to_adj(E,n)
#   distance_wo_bike_s = Dijkstra(G,s,n)
#   #PIerwsza opcja pokonnujemy całą drogę na piechtę
#   shortest_path = distance_wo_bike_s[t]
#   #Druga opcja od s do jakiegoś wierzchołka u idziemy a od u do t jedziemy na rowerze 
#   distance_w_bike_to_t = Dijkstra(G,t,n)

#   for i,p,q in B: 
#       if p < q: 
#         ratio = p/q
#         if distance_wo_bike_s[i] + distance_w_bike_to_t[i]*ratio <shortest_path: 
#           shortest_path = distance_wo_bike_s[i] + distance_w_bike_to_t[i]*ratio



#   return floor(shortest_path)

import heapq
from math import inf,floor
def edges_to_adj(E): 
    n = max(max(u,v) for u,v,_ in E) + 1 
    G = [[] for _ in range(n)]
    for u,v,w in E: 
        G[u].append((v,w))
        G[v].append((u,w))
    return G

def Dijkstra(G,s):
    n = len(G)
    q = []
    d = [inf]*n
    d[s] = 0 
    heapq.heappush(q,(0,s))
    while q: 
        dist, u = heapq.heappop(q)
        if dist > d[u]: 
            continue
        for v,w in G[u]: 
            if d[v] > dist + w: 
                d[v] = dist + w  
                heapq.heappush(q,(d[v],v))
    return d
    

def armstrong(B,E,s,t): 
    G = edges_to_adj(E)
    dist_s = Dijkstra(G,s)
    shortest_path = dist_s[t]
    dist_t = Dijkstra(G,t)
    for i,p,q in B: 
        if p < q: 
            if dist_s[i] + dist_t[i]*(p/q) < shortest_path: 
                shortest_path = dist_s[i] + dist_t[i]*(p/q)
    return floor(shortest_path)
  
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
