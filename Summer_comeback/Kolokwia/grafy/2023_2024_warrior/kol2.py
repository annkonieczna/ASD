from kol2testy import runtests

def warrior( E, s, t):
  G = edges_to_adj(E)
  n = len(G)
  d = BFS(G,s,n)
  return min(d[t])
from math import inf
from collections import deque
def edges_to_adj(E):
  n = max(max(u,v) for u,v,_ in E) +1 
  G = [[] for _ in range(n)]
  for u,v,w in E: 
    G[u].append((v,w))
    G[v].append((u,w))
  return G 
  


def BFS(G,s,n):
  d = [[inf]*17 for _ in range(n)]
  q = deque()
  q.append((0,0,0,s))
  d[s][0] = 0 
  while q: 
    counter,dist,time_without_sleep,u = q.popleft()
    if counter > 0: 
      q.append((counter-1,dist,time_without_sleep,u))
      continue
    if dist > d[u][time_without_sleep]:
      continue
    for v,w in G[u]: 
      #Możemy iść dalej 
      if time_without_sleep + w <= 16: 
        if d[v][time_without_sleep+w] > dist+w:
          d[v][time_without_sleep+w] = dist+w
          q.append((w-1,dist+w,time_without_sleep+w,v))

      #idziemy spać 
      else: 
        if d[v][w] > d[u][time_without_sleep]+ 8 + w: 
          d[v][w] = d[u][time_without_sleep]+ 8 + w
          q.append((w-1,d[v][w],w,v))
      
  return d


    



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
