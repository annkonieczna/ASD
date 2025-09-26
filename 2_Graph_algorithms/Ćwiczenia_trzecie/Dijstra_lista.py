from queue import PriorityQueue


def Dijkstra(G,s): 


    n = len(G)
    parent = [None]*n
    dist = [float("inf")]*n 
    #tworzymy kolejkę priorytetowa minimum 
    q = PriorityQueue()

    q.put((0,s))
    dist[s] = 0 

    while not q.empty(): 

        distance, u = q.get()

        for v, weight in G[u]: 
            if dist[v] > dist[u] + weight: 
                dist[v] = dist[u] + weight

                parent[v] = u 
                q.put((dist[v],v))
    return dist, parent 

G = [[(1, 5)], 
    [(0, 5), (2, 21), (3, 1)], 
    [(1, 21), (4, 7)], 
    [(1, 1), (4, 13), (5, 16)], 
    [(2, 7), (3, 13), (6, 4)], 
    [(3, 16), (6, 1)], 
    [(4, 4), (5, 1)]]
print(Dijkstra(G,0))










from heapq import heappop, heappush

def dijkstra(G, s):
    n = len(G)

    d = [float('inf')] * n  # oszacowanie odległości ze źródła do d
    parents = [None] * n    # poprzednik w najkrótszej ścieżce

    PQ = [(0, s)] # (waga, nr)

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        # jeżeli b jest jakimś wierzchołkiem, do którego odległości szukamy
        # if u == b: break # jezeli wyciagniemy b to znaczy, ze byl juz przetworzony wczesniej (oraz wierzcholki z mniejszym od niego kosztem tez) i mozemy przerwac
        
        if u_w > d[u]: continue # skip niepotrzebnego przypadku (i dzięki temu nie psuje się złożoność)
        # zastępuje tablicę przetworzeń punktów

        for v, w in G[u]: # relax
            c = d[u] + w
            if d[v] > c: # zbędny visited bo mamy bazowo inf w tablicy d
                d[v] = c
                parents[v] = u
                heappush(PQ, (c, v)) #(odl, numer)

    return d, parents




from queue import PriorityQueue
def Dijkstra(G,s):

    n = len(G)

    d = [float("inf")]*n

    parents = [None]*n 

    q = PriorityQueue()

    d[s] = 0 

    q.put((0,s))

    while not q.empty(): 

        distance,u = q.get()

        for v,w in G[u]: 

            if d[v] > d[u] + w: 
                d[v] = d[u] + w

                parents[v] = u 
                q.put((d[v],v))

    return d, parents

G = [[(1, 5)], 
    [(0, 5), (2, 21), (3, 1)], 
    [(1, 21), (4, 7)], 
    [(1, 1), (4, 13), (5, 16)], 
    [(2, 7), (3, 13), (6, 4)], 
    [(3, 16), (6, 1)], 
    [(4, 4), (5, 1)]]
print(Dijkstra(G,0))

# Złożoność ElogV 
# znajdowanie najkrótszych ścieżek w grafie ważonym (bez ujemnych cykli) z punktu startowego s 





