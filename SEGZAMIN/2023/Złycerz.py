# Idziemy po grafie 
# Waga krawędzi - liczba sztabek złota do zapłaty 

# W każdym wierzchołku znajduje się zamek i nasz złodziej może pobrać z niego całe złoto ale od tej pory musi
#przejazd po krawędziach staje się 2 razy droższy i musi zapłacić na każdej krawędzi r złota łapówki 

#tablica V zawiera liczbę sztabek złota w kolejnych zamkach 


from math import inf 
from queue import PriorityQueue


def Dijkstra(G,s, cost_fn): 

    n = len(G)
    dist = [inf]*n
    dist[s] = 0
    q = PriorityQueue()
    q.put((0,s))

    while not q.empty(): 

        distance,u = q.get()
        if distance > dist[u]:
            continue

        for v, t in G[u]:

            if dist[v] > distance + cost_fn(t):
                dist[v] = distance + cost_fn(t)
                q.put((dist[v],v))
    return dist

def gold( G,V,s,t,r ):
    #liczymy ścieżkę bez rabunku
    n = len(G)
    dist_s = Dijkstra(G,s)
    min_without_rob = dist_s[t]
    #sprawdzamy każdy wierzchołek v w grafie jako potencjalny zamek do obrabowania
    for v in range(n):

        #sprawdzamy czy zamek V zawiera jakiekolwiek złoto
        if V[0] == 0: 
            continue
        #szukamy najtańszej ścieżki do v bez rabunku
        to_v = Dijkstra(G,s, lambda w: w)[v]
        from_v = Dijkstra(G,v,lambda w: 2*w+r)[t]

        total_cost = to_v + from_v - V[v]
        min_cost =min(min_cost, total_cost) 


    return min_cost if min_cost >= 0 else -abs(min_cost)




# Idziemy po grafie 
# Waga krawędzi - liczba sztabek złota do zapłaty 

# W każdym wierzchołku znajduje się zamek i nasz złodziej może pobrać z niego całe złoto ale od tej pory musi
#przejazd po krawędziach staje się 2 razy droższy i musi zapłacić na każdej krawędzi r złota łapówki 

#tablica V zawiera liczbę sztabek złota w kolejnych zamkach 


# from math import inf 
# from queue import PriorityQueue


# def Dijkstra(G,s, cost_fn): 

#     n = len(G)
#     dist = [inf]*n
#     dist[s] = 0
#     q = PriorityQueue()
#     q.put((0,s))

#     while not q.empty(): 

#         distance,u = q.get()
#         if distance > dist[u]:
#             continue

#         for v, t in G[u]:

#             if dist[v] > distance + cost_fn(t):
#                 dist[v] = distance + cost_fn(t)
#                 q.put((dist[v],v))
#     return dist

# def gold( G,V,s,t,r ):
#     #liczymy ścieżkę bez rabunku
#     n = len(G)
#     dist_s = Dijkstra(G,s)
#     min_without_rob = dist_s[t]
#     #sprawdzamy każdy wierzchołek v w grafie jako potencjalny zamek do obrabowania
#     for v in range(n):

#         #sprawdzamy czy zamek V zawiera jakiekolwiek złoto
#         if V[0] == 0: 
#             continue
#         #szukamy najtańszej ścieżki do v bez rabunku
#         to_v = Dijkstra(G,s, lambda w: w)[v]
#         from_v = Dijkstra(G,v,lambda w: 2*w+r)[t]

#         total_cost = to_v + from_v - V[v]
#         min_cost =min(min_cost, total_cost) 


#     return min_cost if min_cost >= 0 else -abs(min_cost)




