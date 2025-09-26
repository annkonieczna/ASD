class Node: 

    def __init__(self,value): 

        self.parent = self 
        self.rank = 0 

        self.value = value 

#znajduje reprezentanta zbioru 
def findset(x): 

    if x.parent != x: 

        x.parent = findset(x.parent)

#łączy zbiory 

def union(x,y): 

    x = findset(x)

    y = findset(y)

    if x.rank > y.rank: 

        y.parent =x 

    else: 
        x.parent = y 

        if x.rank == y.rank: 
            y.rank += 1 


def Kruskal(E,n): 

    A = []

    E.sort 

    V = [Node(i) for i in range(n)]

    for e in E: 

        u,v,w = e 
        if findset(V[u]) != findset(V[v]): 

            union(V[u],V[v])

            A +=[e]
    return A




class Node: 

    def __init__(self,value):

        self.parent = self 

        self.value = value 

        self.rank = 0 



def findset(x): 

    if x.parent != x: 

        findset(x.parent)

    return x.parent 



def union(x,y): 

    x = findset(x)

    y = findset(y)

    if x == y: 

        return 
    if x.rank > y.rank: 

        y.parent = x 

    else: 

        x.parent = y 

        if x.rank == y.rank: 

            y.rank += 1 



def Kruskal(E,n): 


    A = [] #lista krawędzi MST (minimalne drzewo spinające)

    E.sort(key = lambda x: x[2]) # sortujemy po wadze 

    
    




        