#Idea: Cykl Eulera w grafie to taki cykl, który przechodzi przez każdą krawędź dokładnie 
# raz i wraca do wierzchołka początkowego.

#Wykonujemy DFS "usuwając na bierząco odwiedzone krawędzie i nie zabraniając wielokrotnego 
# wejścia do tego samego wierzchołka 
#Po przetworzeniu wierzchołka dajemy go na poczatek cyklu 



def Eulerian_cycle(G,s=0): 

    #if is Eulerian?
    for element in G: 
        if len(element) % 2 != 0: 
            return "not Eulerian"
    n = len(G)
    graph = [neighbours[:] for neighbours in G] #kopiujemy naszą listę sąsiedztwa 

    stack =[s] #trzyma ścieżkę w czasie DFS 
    cycle= []

    while stack: 
        u = stack[-1] #apparently stack[-1] będzie oznaczało ostatni element wtf, czyli patrzymy na szczyt 
        #stosu na element, na którym właśnie jesteśmy 
        #Nie usuwamy go ze stosu, sprawdzamy czy możemy iść dalej(czy mamy jakiś sąsiadów jeszcze)

        if graph[u]: 

            v = graph[u].pop() #usuwamy z grafu tego sąsiada 
            graph[v].remove(u) #usuwamy w drugą stronę 
            stack.append(v)

        else: 
            cycle.append(stack.pop())

    return cycle[::-1]

G = [
    [3, 9],
    [2, 3],
    [1,4],
    [0, 1],
    [2, 8],
    [6,9],
    [5, 7],
    [6, 8],
    [4, 7],
    [0,5]
]
G2 = [
    [1, 2, 3, 4],   # 0 -> stopień 4
    [0, 2, 5, 6],   # 1 -> stopień 4
    [0, 1, 3, 7],   # 2 -> stopień 4
    [0, 2, 4, 8],   # 3 -> stopień 4
    [0, 3, 5, 9],   # 4 -> stopień 4
    [1, 4, 6, 10],  # 5 -> stopień 4
    [1, 5, 7, 11],  # 6 -> stopień 4
    [2, 6, 8, 12],  # 7 -> stopień 4
    [3, 7, 9, 12],  # 8 -> stopień 4
    [4, 8, 10, 12], # 9 -> stopień 4
    [5, 9, 11, 12], # 10 -> stopień 4
    [6, 10, 12,13],    # 11 -> stopień 4
    [7, 8, 9, 10, 11, 13], # 12 -> stopień 6
    [12, 11]        # 13 -> stopień 2
]
G1 = [  # graf z cyklem Eulera
    [1, 2],
    [0, 2],
    [0, 1]
]

print(Eulerian_cycle(G2))




