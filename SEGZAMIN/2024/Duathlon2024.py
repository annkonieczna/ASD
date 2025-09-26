#1 opcja: 
# a) Biegniemy od wierzchołka s do wybranego roweru 
# b)Jedziemy na tym rowerze do mety t 

# 2 opcja: 
# Biegniemy do mety bez roweru 


#Zawodnik nie może zmienić roweru gdy go wybierze


#Trasa- graf ważony (wierzchołki- punkty orientacyjne)

#Krawędź ma czas w minutach- ile czasu zajmie pokonanie krawędzi 

#W każdym punkcie - jest jeden, kilka lub 0 rowerów 

# Rower jest opisany przez liczby p i q

# Drogę, którą Luiza, by przeszła w x minut na rowerze(p,q) luiza przejedzie tę drogę w czasie x*p/q (o ile  p< q), 
#trzea to sprawdzić 


# Funkcja armstrong(B,G,s,t)- 
#B- lista B opisuje dostępne rowery. Zawiera trójki postaci (i,p,q)- i numer wierzchołka na którym jest rower 
#Zwraca zaokrągloną w dół liczbę minut 


#Graf G ma wierzchołki od :) do n-1 i jest reprezentowany 

from math import inf, floor
from queue import PriorityQueue

G = [ (0,1,6), (1,4,7), (4,3,4),
 (3,2,4), (2,0,3), (0,3,6) ]
def num_of_vertix(G):
    n = len(G)
    
    for u,v,w in G: 
        num_of_vertix = max(num_of_vertix,u,v)

    return num_of_vertix+1

def edges_to_adj(G): 
    count = num_of_vertix(G)

    Graph = [ [] for _ in range(count)]

    for u,v,w in G: 
        Graph[u].append((v,w))
        Graph[v].append((u,w))
    return Graph 


    





def Dijkstra(G,s, weight_multiplier= 1.0): 

    n = num_of_vertix
    Graph = edges_to_adj(G)
    dist = [inf]*n 
    q = PriorityQueue()
    dist[s] = 0 
    q.put((0,s))

    while not q.empty(): 

        distance, u = q.get()

        for v,w in Graph[u]:
            cost = w*weight_multiplier

            if dist[v] > dist[u] + cost: 
                dist[v] = dist[u] + cost
                

                q.put((dist[v],v))
    return dist



def armstrong(B,G,s,t):

    #liczymy bieg bez roweru dla każdego wierzchołka 

    run_dist = Dijkstra(G,s)
    # Najlepszy czas — początkowo tylko bieg
    min_time = run_dist[t]

    for i, p, q in B: 

        if p < q: 
            ratio = p/q

            bike_dist = Dijkstra(G,i, weight_multiplier = ratio)
            total_time = run_dist[i] + bike_dist[t]
            min_time = min(bike_dist,total_time)
    
    return floor(min_time)





from math import inf, floor
from queue import PriorityQueue


def num_of_vertix(G):
    n = len(G)

    count = max(max(u,v) for u,v,_ in G)
    
    return count+1

def edges_to_adj(G): 
    count = num_of_vertix(G)

    Graph = [ [] for _ in range(count)]

    for u,v,w in G: 
        Graph[u].append((v,w))
        Graph[v].append((u,w))
    return Graph 
def Dijkstra(G,s, weight_multiplier= 1.0): 

    n = num_of_vertix(G)
    Graph = edges_to_adj(G)
    dist = [float("inf")]*n 
    q = PriorityQueue()
    dist[s] = 0 
    q.put((0,s))

    while not q.empty(): 

        distance, u = q.get()
        if distance > dist[u]:
            continue
        for v,w in Graph[u]:
            cost = w*weight_multiplier

            if dist[v] > dist[u] + cost: 
                dist[v] = dist[u] + cost
                

                q.put((dist[v],v))
    return dist





def armstrong( B, G, s, t):
  #liczymy bieg bez roweru dla każdego wierzchołka 

  run_dist = Dijkstra(G,s)
  # Najlepszy czas — początkowo tylko bieg
  min_time = run_dist[t]

  

  for i, p, q in B: 

    if p < q: 
      ratio = p/q

      bike_dist = Dijkstra(G,i, weight_multiplier = ratio)
      total_time = run_dist[i] + bike_dist[t]
      min_time = min(min_time,total_time)
  return floor(min_time)























