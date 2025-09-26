def add_artificial_vertex(G): 

    n = len(G)
    G.append([])
    for i in range(n): 
        G[i].append((n,0))
        G[n].append((i,1))




