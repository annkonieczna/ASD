def list_to_edges(G):
    n =len(G)
    E = []
    for u in range(n):  
        for v, w in G[u]: 
            if u < v: 
                E.append((u,v,w))
    return E 





lista_sasiedztwa = [
    [(1, 4)],
    [(0, 4), (2, 2), (3, 7)],
    [(1, 2)],
    [(1, 7)]
]

print(list_to_edges(lista_sasiedztwa))