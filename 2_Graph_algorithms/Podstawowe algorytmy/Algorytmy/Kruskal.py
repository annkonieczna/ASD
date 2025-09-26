# Algorytm ma na celu znalezienie drzewa MST- drzewa które zawiera krawędzie 
# o najmniejszej wadze łączące wszystkie wierzchołki 
# W tym przypadku potrzebujemy grafu w reprezentacji listy krawędzi 

# O(ElogV)/O(ElogE)

class Node: 
    def __init__(self,value):
        self.parent = self 
        self.value = value 
        self.rank = 0 
#rank służy tylko do podejmowania decyzji, które drzewo przyczepić pod które 
# (mniejszy rank → przyczep do większego). (jest to órne ograniczenie wysokości drzewa)

#znajduje reprezentanta (korzeń) zbioru, w którym jest x.
def findset(x): 

    if x.parent != x: #jeśli x nie jest korzeniem (x.parent != x), wywołuje rekurencyjnie findset na 
    #rodzicu aż do korzenia

        x.parent = findset(x.parent)
    return x.parent 

#łączy zbiory, do których należą dwa punkty 
def union(x,y): 

    x = findset(x)

    y = findset(y)

    if x == y: 

        return 
    if x.rank > y.rank: #jeśli x.rank > y.rank → przyczepiamy root y pod x 

        y.parent = x 

    else: 

        x.parent = y 

        if x.rank == y.rank: 

            y.rank += 1 




def Kruskal(E): 

    A = [] # tablica drzewa MST 

    E.sort(key = lambda x: x[2]) #sortujemy po wagach krawędzi 

    n = max(max(u,v) for u,v,_ in E) + 1 #liczymy liczbę wierzchołków 

    V = [Node(i) for i in range(n)] #tworzymy n wierzchołków 


    for e in E: #przechodzimy przez wszystkie krawędzie 
        u,v,w = e 

        if findset(V[u]) != findset(V[v]): #jeśli są z innych 

            union(V[u],V[v])

            A.append(e)
    return A 





def Krukal(E): 

    A = []
    n = max(max(u,v) for u,v,_ in E) +1 

    V = [Node(i) for i in range(n)]

    for u,v,w in E: 
        
        if findset(V[v]) != findset(V[u]): #jeżeli należą do innych zbiorów 

            union(V[v],V[u]) #łączymy je w jeden zbiór 

            A.append((u,v,w))
    
    return A 




def Kruskal(E): 

    A = []

    E.sort(key=lambda x: x[2])

    n = max(max(u,v) for u,v,_ in E)

    V = [Node(i) for i in range(n)]

    for e in E: 

        u,v,w = e

        if findset(V[v]) != findset(V[u]): 

            union(V[u],V[v])

            A.append(e)
    return A 








