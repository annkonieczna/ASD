# Czy graf jest dwudzielny 
from collections import deque
def dwudz(G): 
    n = len(G)
    Q = deque()
    colour = [0 for _ in range(n)]

    colour[0] = 1 
    Q.append(0)
    while len(Q) > 0: 
        u = Q.pop.left()
        for i in range(n): 
            if G[u][i] == 1: 
                if colour[i] == 0: 
                    colour[i] = -1*colour[u]
                    Q.append(i)
                elif colour[i] == colour[u]: 
                    return False 
    return True 
