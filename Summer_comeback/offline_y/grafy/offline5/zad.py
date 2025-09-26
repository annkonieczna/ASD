from zadtesty import runtests

#BFSSSSS


def matrix_to_adj(G): 
  n = len(G)
  graph = [[] for _ in range(n)]
  for i in range(n): 
    for j in range(i+1,n): 
      if G[i][j] != -1: #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        graph[i].append((j,G[i][j]))
        graph[j].append((i, G[i][j]))
  return graph
# G = [ [ -1, 3, 8,-1,-1,-1 ], # 0
# [ 3,-1, 3, 6,-1,-1 ], # 1
# [ 8, 3,-1,-1, 5,-1 ], # 2
# [ -1, 6,-1,-1, 7, 8 ], # 3
# [ -1,-1, 5, 7,-1, 8 ], # 4
# [ -1,-1,-1, 8, 8,-1 ]]



from collections import deque 
from math import inf 

def goodknight( Graph, s, t ):
  G = matrix_to_adj(Graph)
  n = len(G)
  d = [ [inf]*17 for _ in range(n)]
  q = deque([(0,0,0,s)])
  d[s][0] = 0
  while q: 
    counter,dist, time_without_sleep,u = q.popleft()
    
    if counter > 0:
      q.append((counter-1,dist,time_without_sleep,u))
      continue
    if dist > d[u][time_without_sleep]:
      continue

    for v,w in G[u]: 
      if time_without_sleep + w <= 16: 

        if d[v][time_without_sleep+w] > dist + w: 
          d[v][time_without_sleep+w] = dist + w
          q.append((w-1,d[v][time_without_sleep+w],time_without_sleep+w,v))
      else:
        if d[v][w] > dist+8+w:
          d[v][w] = dist+8+w
          q.append((w-1,d[v][w],w,v))
  return min(d[t])





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )

# G = [[(1, 3), (2, 8), (1, 3), (2, 8)], [(0, 3), (0, 3), (2, 3), (3, 6), (2, 3), (3, 6)], [(0, 8), (1, 3), (0, 8), (1, 3), (4, 5), (4, 5)], [(1, 6), (1, 6), (4, 7), (5, 8), (4, 7), (5, 8)], [(2, 5), (3, 7), (2, 5), (3, 7), (5, 8), (5, 8)], [(3, 8), (4, 8), (3, 8), (4, 8)]]

# # print(matrix_to_adj(G))
# from math import inf
# import heapq
# def goodknight( Graph, s, t ):
#   G = matrix_to_adj(Graph)
#   n = len(G)
#   distance = [ [inf]*17 for _ in range(n)]
#   q = []
#   heapq.heappush(q,(0,s,0))
#   distance[s][0] = 0

#   while q: 
#     dist,u,time_without_sleep = heapq.heappop(q)
#     current_time = distance[u][time_without_sleep]
#     if dist > current_time: 
#       continue 
#     if u ==t: 
#       return current_time
#     for v,w in G[u]: 
#       if time_without_sleep + w > 16: 
#         if distance[v][w] > 8 + w + distance[u][time_without_sleep]:
#            distance[v][w] = 8+ w + distance[u][time_without_sleep]
#            heapq.heappush(q,(distance[v][w],v,w))
#       else: 
#         if distance[v][time_without_sleep+w] > current_time + w: 
#           distance[v][time_without_sleep+w] = current_time + w
#           heapq.heappush(q,(distance[v][w+time_without_sleep],v,time_without_sleep+w))
    
     

#   return min(distance[t])