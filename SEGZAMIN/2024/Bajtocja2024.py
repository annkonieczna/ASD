#indyjski rozmiar szyn - 1676 
# rozmiar przylądkowy - 1067 

#Najkrótsza trasa z A do B 
# Potencjalnie przez inne stacje 

#Pomiedzy stacjami pociąg jedzie z prędkością jednego km na jednostkę czasu 

# Odległości pomiedzy stacjami- liczby naturalne <=  10 

#Ruszając ze stacji A pociąg ma dopasowany rozkład kół do pierwszej linii, którą się porusza



#Opcje: 

#1. Pociąg wjeżdza na stacje i wyjeżdza z niej indyjską linią - 5 jednostek czasu 

#2. Opcja przylądkowya - 10 jednostek czasu 

#3. Zmiana rozstawu kół- 20 jed. czasu 




#Funkcja: 

#Na wejściu otrzymuje: 
# tablicę E- opis linii kolejowych. Jest to lista krotek: (x, y, d, typ), 
# gdzie x i y to numery stacji połączonych linią kolejową
# d ∈ {1, …, 10} to długość linii zaś typ to jej rozstaw
# typ: 
#a)typ == 'I' to linia ma rozstaw indyjski
#b) Jeśli typ == 'P' to linia ma rozstaw przylądkowy
#Punkty A i B 

#Każda linia kolejowa jest dwukierunkowa (ma tor w kierunku x->y i tor w kierunku y->x).

#. Może się zdarzyć, że pewne stacje są połączone zarówno linią indyjską jak i linią przylądkową

#ZWraca najkrótszy czas przejazdu pomiedzy A do B 

from queue import PriorityQueue
from math import inf 

def edges_to_adj(E): 

    n = max(max(x,y) for x,y,_,_ in E ) +1 

    G = [[] for _ in range(n)]

    for x, y, d, t in E:
        if t =='I': 
            t_id = 0
        else: 
            t_id = 1

        G[x].append((y,d,t_id))
        G[y].append((x,d,t_id)) 
    return G 

def tory_amos(E,A,B):

    G = edges_to_adj(E)
    n = len(G)
    q = PriorityQueue()

    dist = [[inf,inf] for _ in range(n)]

    #rozważamy wszystkie możliwe wyjazdy ze stacji A 
    for v,d,t_id in G[A]: 
        dist[v][t_id] = d 
        q.put((dist[v][t_id],v,t_id))
    
    while not q.empty(): 

        time, u, t = q.get()
        # już mamy lepszy czas 
        if dist[u][t] < time: 
            continue

        for v,d,next_t in G[u]:

            if t == next_t: 
                if t == 0: 
                    cost = 5
                else: 
                    cost = 10 
            else: 
                cost = 20 

            new_time = cost + d 

            if dist[v][next_t] > new_time + time:

                dist[v][next_t] = new_time + time 
                q.put((dist[v][next_t],v,next_t))
    return min(dist[B]) if min(dist[B])<inf else -1 


E = [(0, 1, 5, 'P'), (1, 3, 1, 'I'), (3, 4, 1, 'I'),
 (2, 4, 1, 'P'), (2, 5, 1, 'I'), (0, 5, 5, 'P')]
A = 5
B = 3

print(tory_amos(E,A,B))








