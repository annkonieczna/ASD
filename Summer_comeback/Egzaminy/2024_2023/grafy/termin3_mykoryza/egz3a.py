from egz3atesty import runtests

#Mamy graf w postaci listy sąsiedztwa 
#Tablicę T o dłogości k, 
from math import inf
from collections import deque 
# def mykoryza(G,T,d):
#   n = len(G)
#   mashrooms = [None]*n #Jaki grzyb opanował które drzewo 
#   time = [inf]*n # w jakim czasie opanowaliśmy to drzewo 
#   q = deque()
#   for i in range((len(T))):
#     mashrooms[T[i]] = i
#     time[T[i]] = 0 
#     q.append((T[i],i,0))
    
#   while q: 
#     tree, m,dist = q.popleft()
#     if dist > time[tree]: 
#       continue
#     for v in G[tree]: 
#       #PIerwszy raz tu docieramy
#       if mashrooms[v] == None:
#         mashrooms[v] = m
#         time[v] = dist + 1 
#         q.append((v,m,dist+1))
#   counter = 0
#   for elements in mashrooms: 
#     if elements ==d: 
#       counter += 1 
#   return counter 
        
# def bfs(adjacency_list, fungus_markers, B):
#     n = len(adjacency_list)
#     fungus_count = len(B)
#     time = [inf for _ in range(n)]
#     q = deque()

#     for i in range(fungus_count):
#         fungus_markers[B[i]] = i
#         time[B[i]] = 0
#         q.append(B[i])

#     while q:
#         u = q.popleft()

#         for v in adjacency_list[u]:
#             if time[v] > time[u] + 1:
#                 time[v] = time[u] + 1
#                 fungus_markers[v] = fungus_markers[u]
#                 q.append(v)
#             elif time[v] == time[u] + 1 and fungus_markers[u] < fungus_markers[v]:
#                 fungus_markers[v] = fungus_markers


# def mykoryza(G, T, d):
#     n = len(G)
#     markers = [inf for _ in range(n)]
#     bfs(G, markers, T)
#     answer = 0
#     for i in markers:
#         if i == d:
#             answer += 1

#     return answer


from collections import deque 


def mykoryza(G,T,d): 
  n = len(G)
  mashroom = [None]*n
  visited = [False]*n 
  q = deque()
  for i in range(len(T)):
    mashroom[T[i]] = i 
    q.append((i,T[i]))
    visited[T[i]] = True 
  
  while q: 
    m,u = q.popleft()
    for v in G[u]: 
      if not visited[v]:
        mashroom[v] = m 
        visited[v] = True 
        q.append((m,v))
  counter = 0 
  for i in range(n): 
    if mashroom[i] == d: 
      counter += 1 
  return counter 




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
