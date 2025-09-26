from zad3testy import runtests

from collections import deque
#Złożoność: O(V+E)
#Anna Konieczna 
#Algorytm najpierw 2-krotnie wykorzystuje zmodyfikowanego BFS'a by znaleźć wszystkie najkrótsze ścieżki z
#wierzchołka s oraz z wierzchołka t. Podczas wykonywania BFS'a algorytm również zapisuje ile jest możliwych 
#dróg o takiej samej wadze do danego wierzchołka. Jeśli dystance z s do t jest -1 to znaczy, że taka droga nie istnieje 
#i zwracamy None. Zapisujemy dystans najktórszej ścieżki z s do t i ile takich ścieżek jest. Natsępnie 
#przechodzimy przez wszystkie krawędzie grafu {u,v} i sprawdzamy czy droga z s do jednego wierzchołka krawędzi, 
#a nastepnie droga z drugiego wierzchołka do t ma taką samą długość jak najkrótsza ścieżka pomiędzy s a t i 
#jeśli ma to wtedy sprawdzamy czy łączna liczba tras z s do wierzchołka i z wierzchołka do t jest taka sama 
#jak liczba tras z wierzchołka s do t, wtedy wiemy, że usunięcie tej krawędzi wydłuży naszą najkrótszą ścieżkę 

#Jeśli krawędź {u, v} leży na jakiejś najkrótszej ścieżce z s do t, to musi spełniać 
# dist_s[u] + 1 + dist_t[v] == dist_s[t] lub symetrycznie dist_s[v] + 1 + dist_t[u] == dist_s[t]
def BFS(G,s): 
    n = len(G)
    count = [0]*n #liczymy ile najkrótszych ścieżek prowadzi do tego konkretnego wierzchołka 
    count[s] = 1
    q = deque([s])
    distance = [-1]*n 
    distance[s] = 0 
    while q: 
        u = q.popleft()
        for v in G[u]: 
            if distance[v] == -1: #dany wierzchołek nie został odwiedzony 
                distance[v] = distance[u] + 1  
                count[v] = count[u]
                q.append(v)
            #drugi przypadek: wierzchołek był już odwiedzony, ale da się go odwiedzić w takim samym czasie 
            elif distance[v] == distance[u] + 1: 
                count[v] += count[u]

    return distance, count 

def longer( G, s, t ):
    dist_s,count_s = BFS(G,s)
    dist_t,count_t = BFS(G,t)

    if dist_s[t] == -1: 
        return None 
    shortest_path = dist_s[t]
    total_paths= count_s[t] 
    n = len(G)
    for u in range(n): #Iterujemy po wszystkich krawędziach {u, v} grafu.
        for v in G[u]:
            if u < v: #Ponieważ graf jest nieskierowany, każda krawędź
                # występuje dwa razy w listach sąsiedztwa (v ∈ G[u] i u ∈ G[v]). 
                # Warunek u < v sprawia, że rozpatrzymy każdą krawędź tylko raz.
                if dist_s[u] + 1 + dist_t[v] == shortest_path: 
                    number = count_s[u]*count_t[v] #liczba takich najkrótszych ścieżek to count_s[u] * count_t[
                    if number == total_paths:
                        return (u,v)
                    #jeśli ta liczba równa się łącznej liczbie wszystkich najkrótszych ścieżek total_paths, to oznacza, że każda najkrótsza ścieżka s→t przechodzi przez krawędź {u, v} w tej orientacji.
                    #Wtedy usunięcie {u, v} eliminuje wszystkie najkrótsze ścieżki —
                    #  najkrótsza odległość rośnie — zwracamy (u, v).
                elif dist_t[u] + 1 + dist_s[v] == shortest_path:
                    number = count_t[u]*count_s[v]
                    if number == total_paths: 
                        return (u,v)
    return None
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True)
