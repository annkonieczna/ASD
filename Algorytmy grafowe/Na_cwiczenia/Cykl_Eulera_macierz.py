# Cykl Eulera na grafie w rep. macierzowej.

# wersja improved (lepsza złożoność)
# z zapisaniem na jakim wierzchołku zakończył nam się for w visicie
# jak spowrotem wejdziemy do wierzchołka u to nie będziemy zaczynać od 0, a tam gdzie poprzednio skończył się
# dfs visit

# O(V^2)

# cykl Eulera przechodzi nam dokładnie raz przez każdą krawędź i wraca do wierzchołka startowego
#s- wierzchołek startowy 
def Euler_cycle(G,start_v): 
    n = len(G)
    cycle = [] # lista przechowująca kolejne wierzchołki cyklu eulera 
    last_neighbour = [] # tablica śledząca, do którego wierzchołka dotarliśmy w przeszukiwaniu sąsiadów każdego wierzchołka

def Euler_cycle_matrix(G,start_v): 
    n = len(G)
    cycle = []
    def is_connected(): 

        visited = [False]*n 
        stack = [start_v]
        visited[start_v] = True 
        counter = 1 
        while stack: 
            u = stack.pop() 
            # pobieramy ostatni wierzchołek ze stosu
            # i sprawdzamy jego sąsiadów 
            for v in range(n): 
                if G[u][v] > 0 and not visited[v]: 
                    visited[v] = True 
                    stack.append(v)
                    counter += 1 
        return counter == n 

    def DFS_visit(u): 
        nonlocal cycle    

        for v in range(n): 
            while G[u][v] > 0: 
                G[u][v] -= 1 
                G[v][u] -=1
                DFS_visit(v)
        cycle.append(u)
    
    if n == 0: 
        return None 
    
    if not is_connected(): 
        return None 
    
    for i in range(n): 
        degree = sum(G[i])
        if degree % 2 != 0: 
            return None 
    
    DFS_visit(start_v)
    return cycle[::-1]

G = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
print(Euler_cycle_matrix(G,0))
    


