from egz2btesty import runtests
# def edges_to_adj(E,n): 
#   G = [[] for _ in range(n)]  
#   for u,v,w,type in E: 
#     if type == 'I': 

#       G[u].append((v,w,0))
#       G[v].append((u,w,0))
#     else: 
#       G[u].append((v,w,1))
#       G[v].append((u,w,1))
#   return G
# from collections import deque 
# from math import inf
# def BFS(G,s,n): 
#   q = deque()
#   d = [[inf]*2 for _ in range(n)]
#   d[s][0] = 0
#   d[s][1] = 0 
#   for v,w,type in G[s]: 
#     q.append((w-1,w,v,type))

#   while q: 
#     counter, dist,u,type_u = q.popleft()
#     if counter > 0: 
#       q.append((counter-1,dist,u,type_u))
#       continue #!!!!!!!!!!
#     if dist > d[u][type_u]: 
#       continue
    
#     for v,w,type_v in G[u]: 
#       if type_v != type_u: 
#         cost = 20 
#       elif type_v == 1:
#         cost = 10 
#       else: 
#         cost = 5 
      
#       if d[v][type_v] > dist+ w + cost:
#         d[v][type_v] = dist+ w + cost
#         q.append((w+cost-1, dist+cost+w,v,type_v)) 
        
#   return d

  
# def tory_amos( E, A, B ):
#   n = max(max(u,v) for u,v,_,_ in E)+1
#   G = edges_to_adj(E,n)
#   d = BFS(G,A,n)

#   return min(d[B])
from math import inf 
from collections import deque 
def edges_to_adj(E,n):  
  G = [[] for _ in range(n)]
  for u,v,w,type in E: 
    if type == "I":
      G[u].append((v,w,0))
      G[v].append((u,w,0))
    else:
      G[u].append((v,w,1))
      G[v].append((u,w,1))
  return G
# E = [(0, 1, 5, 'P'), (1, 3, 1, 'I'), (3, 4, 1, 'I'), (2, 4, 1, 'P'), (2, 5, 1, 'I'), (0, 5, 5, 'P')]
# print(edges_to_adj(E,6))
def BFS(G,s,n):
  d = [[inf]*2 for _ in range(n)]
  q = deque()
  # q.append((0,0,s,0))
  # q.append((0,0,s,1)) !!!!!!!!!!! tak nie wolno nununu
  for v,w,type_v in G[s]: 
    q.append((w-1,w,v,type_v))
  d[s][0] = 0 
  d[s][1] = 0 
  while q:
    counter,dist,u,type_u = q.popleft()
    if counter > 0: 
      q.append((counter-1,dist,u,type_u))
      continue
    if d[u][type_u] < dist: 
      continue

    for v,w,type_v in G[u]: 
      
      if type_u == type_v: 
        if type_u == 0:
          cost = 5 
        else: 
          cost = 10 
      else: 
        cost = 20 
      if d[v][type_v] > dist + w + cost:
        d[v][type_v] = dist + w + cost 
        q.append((w-1,d[v][type_v],v,type_v)) 
  return d 
        
      

def tory_amos(E,A,B):
  n = max(max(u,v) for u,v,_,_ in E) +1
  G = edges_to_adj(E,n)
  d = BFS(G,A,n)
  print(d)
  return min(d[B])
  
# print(tory_amos(E,5,3))



# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
