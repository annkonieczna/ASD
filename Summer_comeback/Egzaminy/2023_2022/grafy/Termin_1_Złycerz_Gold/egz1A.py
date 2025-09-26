from egz1Atesty import runtests

# def gold(G,V,s,t,r):
#   n = len(G)
#   shortest_s = Dijkstra(G,s,n)
#   shortest_t = Dijkstra(G,t,n,lambda x: 2*x+r)
#   shortest_path = shortest_s[t]
#   for v in range(len(V)): 
#     if (shortest_t[v] + shortest_s[v])- V[v]< shortest_path:
#         shortest_path = (shortest_t[v] + shortest_s[v]) - V[v]
#   return shortest_path

  
# import heapq
# from math import inf
# def Dijkstra(G,s,n,function = lambda x:x): 
#   q = []
#   heapq.heappush(q,(0,s))
#   d = [inf]*n
#   d[s] = 0
#   while q: 
#     dist, u = heapq.heappop(q)
#     if dist > d[u]: 
#       continue
#     for v,w in G[u]: 
#       if d[v] > dist + function(w):
#         d[v] = dist + function(w)
#         heapq.heappush(q,(d[v],v))
#   return d 




import heapq
from math import inf 
def gold(G,V,s,t,r):
    d_s = Dijkstra(G,s)
    # print(d_s)
    minimum = d_s[t]
    d_t =Dijkstra(G,t,lambda x : 2*x +r) 
    for i in range(len(V)):
        # print(d_s[i],d_t[i])
        if (d_s[i] + d_t[i])-V[i] < minimum: 
            minimum = (d_s[i] + d_t[i])-V[i]
    return minimum
        
     
def Dijkstra(G,s,function= lambda x: x): 
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
            if d[v] > dist + function(w): 
                d[v] = dist + function(w)
                heapq.heappush(q,(d[v],v))
    return d 
        



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True)
