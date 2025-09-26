# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , |E|} (wagi krawędzi są
# parami różne). 
# Proszę zaproponować algorytm, który dla danych wierzchołków x i y oblicza ścieżkę o
# najmniejszej sumie wag, która prowadzi z x do y po krawędziach o malejących wagach (jeśli ścieżki
# nie ma to zwracamy inf).

#Posortować listę krawędzi + Bellman-Ford na liście krawędzi (czyli imo najszybsza jego implementacja)
# O(ElogE) == O(ElogV)


# Najpierw sobie posortujemy. Chcemy znaleźć taką kolejność, że wagi są ściśle malejące 



def bellman_ford_on_edges(E,x,n):


    d = [float('inf')]*n
    parent = [None]*n

    d[x] = 0

    for u,v,w in E: 
        pass 


def weights(E,x,y): 

    # liczymy liczbę wierzchołków (Lista krawędzi E- jest w postaci (u,v,w)- od, do, waga )

    n = 0 
    
    for u,v,_ in E:

        n = max(n,u,v)
    
    n += 1 

    E.sort(key = lambda x:x[2], reverse = True )
    

    # key daje znać po czym sortujemy, my chcemy sortować po 3 elemencie krotki, index 2 












