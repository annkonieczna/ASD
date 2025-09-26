#Checemy znaleźć "najkrótszą" ścieżkę - 
#o najmniejszym możliwym iloczynie wag.
#Pomysł: zamiast liczyć a*b*c*d, liczymy
#log(abcd) = loga + logb + logc + logd.
#uwaga na wagi e < 1 (loge < 0) - trzeba
#użyć algorytmu Bellmana - Forda.


from math import log 

def Bellman_ford(G,s): 

    n = len(G)
    d = [float('inf')]*n
    parent= [None]*n
    d[s] = 0 

    
