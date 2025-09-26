from egz1Btesty import runtests
from collections import deque

#Dobra uwaga: Krawędź (a,b) będzie krytyczna jeśli nie będzie się dało startując, z któregoś z sąsiadów a 
#dojść do b

#Dla każdego wierzchołka uruchamiamy BFS'a z zainicjalizowanymi sąsiadami tego wierzchołka 



def critical(V, E):
    G = edges_to_adjency(E,V)
    counter = 0 
    for u in range(V):
        sources = G[u]
        visited = BFS(G,u,sources)
        for v in G[u]: 
            if not visited[v]: 
                counter += 1 
    return counter 



def edges_to_adjency(E,V):
    n = V
    G = [[] for _ in range(n)]
    for u,v in E: 
        G[u].append((v))
    return G 


from collections import deque
def BFS(G,u,sources):
    n = len(G)
    visited = [False]*n 
    q = deque(sources)
    while q: 
        u = q.popleft() 
        for v in G[u]: 
            if not visited[v]: 
                visited[v] = True 
                q.append(v)
                
    
    return visited








#Złożoność O(E(V+E))

# def critical(V, E):
#     G = edges_to_adjency(E,V)
#     counter = 0 
#     for u,v in E:
#         visited = BFS(G,u,v)
#         if not visited[v]: 
#             counter += 1 
#     return counter 



# def edges_to_adjency(E,V):
#     n = V
#     G = [[] for _ in range(n)]
#     for u,v in E: 
#         G[u].append((v))
#     return G 

# from collections import deque
# def BFS(G,s,g):
#     n = len(G)
#     visited = [False]*n 
#     q = deque()
#     q.append(s)
#     visited[s] = True 
#     while q: 
#         u = q.popleft() 
#         for v in G[u]: 
#             if not visited[v]: 
#                 if u == s and v == g:
#                     continue
#                 visited[v] = True 
#                 q.append(v)
#                 
#     
    
#     return visited


        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)

    
