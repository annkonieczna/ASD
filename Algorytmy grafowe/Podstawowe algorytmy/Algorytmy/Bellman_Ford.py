def bellman_ford(G, s):
    n = len(G)
    d = [float('inf')] * n
    parents = [None] * n

    d[s] = 0

    for _ in range(n - 1):
        for u in range(n): # tu jest iteracja po wszystkich krawędziach po prostu (co prawda ze stałą)
            for v, w in G[u]: # relaksacja
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    parents[v] = u

    for u in range(n): # weryfikacja
        for v, w in G[u]:
            if d[v] > d[u] + w: # można uznać, że zaprzecza warunkowi z góry, więc są błędne koszty, ale to nie jest idealne wytłumaczenie
                return None

    return d, parents

G = [
    [(1, -4)], #0
    [(3, 5), (2, 4)], #1
    [(3, 2)], #2
    [(4, 3)], #3
    [] #4
]

print(bellman_ford(G, 0))


#Algorytm szukający najkrótszych ścieżek w grafach ważonych (mogą być ujemne cykle) 
#Złożoność O(VE)

def Bellman_Ford(G,s): 

    n = len(G)
    d = [float("inf")]*n
    parents = [None]*n 

    d[s] = 0 

    for _ in range(n-1): 

        for u in range(n): 
            for v,w in G[u]: 

                if d[v] > d[u] + w: 

                    d[v] = d[u] + w
                    parents[v] = u 
    
    for u in range(n): 

        for v,w in G[u]:

            if d[v] > d[u] + w: 

                return None 
    return d, parents 

from math import inf

def Bellman_Ford(G,s): 
    n = len(G)

    d = [inf]*n
    d[s] = 0 
    parents = [None]*n
    #n-1 razy dokonujemy relaksacji 
    for i in range(n-1): 
        for u in range(n): 
            for v, w in G[u]: 
                if d[v] > d[u] + w: 
                    d[v] = d[u] + w
                    parents[v] = u 
    
    for u in range(n): 
        for v,w in G[u]: 
            if d[v] > d[u] + w:
                return None 
    
    return d






from math import inf 

def belly_ford(G,s): 

    n = len(G)
    d = [inf]*n
    parents =[None]*n 
    d[s] = 0 

    for _ in range(n-1): #n-1 razy dokonujemy relaksacji krawędzi 
        for u in range(n): 
            for v,w in G[u]: 
                if d[v] > d[u] + w: 
                    d[v] = d[u] + w 
                    parents[v] = u 
    
    for u in range(n): 
        for v,w in G[u]: 
            if d[v] > d[u] + w: 
                return "Ujemny cykl"
    
    return d, parents 


G = [
    [(1, -4)], #0
    [(3, 5), (2, 4)], #1
    [(3, 2)], #2
    [(4, 3)], #3
    [] #4
]

print(belly_ford(G,0))




def belly(G,s): 
    n = len(G)
    d = [inf]*n 
    d[s] = 0 

    for k in range(n-1): 
        for u in range(n): 
            for v,w in G[u]: 
                if d[v] > d[u] + w: 
                    d[v] = d[u] + w 
    for u in range(n): 
        for v,w in G[u]: 
            if d[v] > d[u] + w: 
                return "Ujemny cykl"
    return d 
print(belly(G,0))














