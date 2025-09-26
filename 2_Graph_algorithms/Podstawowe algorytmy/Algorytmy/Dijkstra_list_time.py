# from queue import PriorityQueue

# def Dijkstra(G, s):

#     n = len(G)
#     q = PriorityQueue()
#     dist = [float("inf")]*n
#     parent = [None]*n
# #     dist[s] = 0
# #     q.put((0,s))

# #     while not q.empty(): 
 
# #         distance, u = q.get()

# #         for v, time in G[u]: 

# #             if dist[v] > dist[u] + time: 
# #                 dist[v] = dist[u] + time

# #                 parent[v] = u
# #                 q.put((dist[v],v))

# #     return dist, parent

# from queue import PriorityQueue

# from math import inf 

# def Dijkstra(G,s): 

#     n = len(G)
#     q = PriorityQueue()
#     dist = [inf]*n
#     dist[s] = 0 
#     q.put((0,s))
#     parents = [None]*n

#     while not q.empty(): 
#         distance, u = q.get()

#         for v,value in G[u]: 
#             if dist[v] > dist[u] + value:
#                 dist[v] = dist[u] + value

#                 q.put((dist[v],v))

#                 parents[v] = u

#     return dist, parents



# G = [[(1, 5)], 
#     [(0, 5), (2, 21), (3, 1)], 
#     [(1, 21), (4, 7)], 
#     [(1, 1), (4, 13), (5, 16)], 
#     [(2, 7), (3, 13), (6, 4)], 
#     [(3, 16), (6, 1)], 
#     [(4, 4), (5, 1)]]
# print(Dijkstra(G,0))




# def Dijkstra(G,s): 

#     n = len(G)
#     dist = [inf]*n
#     q = PriorityQueue()
#     dist[s] = 0 
#     q.put((0,s))

#     while not q.empty(): 

#         distance, u = q.get()

#         if distance > dist[u]: 
#             continue
#         for v,w in G[u]: 

#             if dist[v] > distance + w: 
#                 dist[v] = distance + w 

#                 q.put((dist[v],v))

#     return dist 

# from collections import deque

# def BFS(G,s): 

#     n = len(G)
#     visited = [False]*n
#     visited[s]= True 
#     parents = [None]*n
#     dist = [-1]*n
#     q = deque()
#     q.append(s)
#     dist[s] = 0 

#     while q: 
#         u = q.popleft()

#         for v in G[u]: 
#             if not visited[v]: 
#                 parents[v] = u
#                 dist[v] = dist[u] + 1
#                 visited[v] = True   

#                 q.append(v)
#     return dist, parents


# def DFS(G):

#     n = len(G)
#     visited = [False]*n 
#     parents = [None]*n


#     def DFS_Visit(G,u): 
#         visited[u] = True 
        
#         for v in G[u]: 
#             if not visited[v]: 
#                 parents[v] = u 

#                 DFS_Visit(G,v)

#     for u in range(n): 

#         if not visited[u]: 
#             DFS_Visit(G,u)
#     return parents




import heapq 

from math import inf 

def Dijkstra_speed(G,s): 
    n = len(G)
    distance = [inf]*n
    q = [] #kolejka prioretytowa
    distance[s] = 0 
    heapq.heappush(q,(0,s))
    parents = [None]*n

    while q: 
        dist, u = heapq.heappop(q)
        if dist > distance[u]: 
            continue

        for v,w in G[u]:

            if dist + w < distance[v]:
                distance[v] = dist + w
                parents[v] = u 
                heapq.heappush(q,(distance[v],v))
    return distance, parents

# G = [
#         [(1, 4), (2, 2)],       # krawędzie z 0
#         [(0, 4), (3, 5)],       # krawędzie z 1
#         [(0, 2), (3, 8), (4, 10)], # krawędzie z 2
#         [(1, 5), (2, 8), (4, 2)],  # krawędzie z 3
#         [(2, 10), (3, 2)]       # krawędzie z 4
#     ]

# G = [[(1, 5), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)], [(0, 5), (2, 21), (3, 1)], [(1, 21), (4, 7), (0, 0), (1, 0), (3, 0), (4, 0), (5, 0), (6, 0)], [(1, 1), (4, 13), (5, 16), (0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0)], [(2, 7), (3, 13), (6, 4)], [(3, 16), (6, 1)], [(4, 4), (5, 1)]]
# G = [[(1, 5), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)], [(0, 5), (2, 21), (3, 1)], [(1, 21), (4, 7), (0, 0), (1, 0), (3, 0), (4, 0), (5, 0), (6, 0)], [(1, 1), (4, 13), (5, 16), (0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0)], [(2, 7), (3, 13), (6, 4)], [(3, 16), (6, 1)], [(4, 4), (5, 1)]]
G = [[(1, 5), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)], [(0, 5), (2, 21), (3, 1)], [(1, 21), (4, 7), (0, 0), (1, 0), (3, 0), (4, 0), (5, 0), (6, 0)], [(1, 1), (4, 13), (5, 16), (0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0)], [(2, 7), (3, 13), (6, 4)], [(3, 16), (6, 1)], [(4, 4), (5, 1)]]
print(Dijkstra_speed(G,4))



def Didididi(G,s): 
    n = len(G)
    d = [inf]*n 
    q = []
    heapq.heappush(q,(0,s))
    d[s] = 0 
    while q: 
        dist, u = heapq.heappop(q)
        if dist > d[u]: 
            continue
        for v,w in G[u]: 
            if d[v] > dist + w: 
                d[v] = dist+w
                heapq.heappush(q,(d[v],v))
    return d 

G = [[(1, 5), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)], [(0, 5), (2, 21), (3, 1)], [(1, 21), (4, 7), (0, 0), (1, 0), (3, 0), (4, 0), (5, 0), (6, 0)], [(1, 1), (4, 13), (5, 16), (0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0)], [(2, 7), (3, 13), (6, 4)], [(3, 16), (6, 1)], [(4, 4), (5, 1)]]
print(Didididi(G,4))
                







            




































