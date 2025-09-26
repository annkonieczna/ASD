#n projektów - p0, p1, . . . , pn−1
#Wykonanie każdego proejktu- jednostka czasu 
#Może wyoknywać dowolnie dużo projektów at the same time
# ich realizacja też trwa jedną jednostkę czasu 
# Niektóre projekty można wykonać tylko po wykonaniu innych 

# Pytanie: Ile czasu zajmie realizacja projektów 

# Pomysł: 
# Tworzymy drzewo i liczymy jego poziomy. Korzystamy z DFS/BFS 


from collections import  deque

def create_adj_list(L,n): 
    G = [[] for _ in range(n)]

    for p,q in L:

        G[q].append(p)
        



def projects(L,n):
    pass

    

