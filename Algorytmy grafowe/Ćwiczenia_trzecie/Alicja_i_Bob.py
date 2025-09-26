# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi
# łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna).
# Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V, zamieniając się za kierownicą
# w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować
# algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała
# jak najmniej kilometrów.

#Graf reprezentuje sieć drogową, wierzchołki
#są miastami, krawędzie to drogi (długości w km).
#Alice i Bob się zmieniają po każdym mieście. 
#Wyznaczamy, kto zaczyna w mieście start i drogę
#tak, Żeby Alice jechała jak najmniej. Pomysł:
#1) Wariancja Dijkstry, wydłużamy długość tylko wtedy,
#gdy jedzie Alice. 2) Modyfikujemy graf - podwajamy
#wierzchołki, jeżeli jedzie Alice to zostawiamy
#oryginalną wagę, dla Boba waga krawędzi to 0.
#Na przemian są krawędzie dla Alice i Boba.

from math import inf
from queue import PriorityQueue
from queue import Queue

#zadanie 4
def Dijkstra_mod(G,start,who,end):
    n=len(G)
    d=[inf for _ in range(n)]
    d[start]=0
    Q=PriorityQueue()
    Q.put((0,start,who,[]))
    while not Q.empty():
        w,u,z,p=Q.get()
        if u==end:
            return d[end],p+[u]
        for v,c in G[u]:
            if z=='B':
                if d[v]>w:
                    d[v]=w
                Q.put((d[v],v,'A',p+[u]))
            elif d[v]>w+c:
                d[v]=w+c
                Q.put((d[v],v,'B',p+[u]))
            else:
                if not u in p: Q.put((d[u]+c,v,'B',p+[u]))




def relax(par,d,v,c,u):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def shortest(G,start,end):
    a1=Dijkstra_mod(G,start,'A',end)
    a2=Dijkstra_mod(G,start,'B',end)
    if a1[0]<a2[0]:
        return a1
    return a2
