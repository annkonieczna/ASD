def edges_to_adjency_list(G):

    #szukamy liczby wierzchołków
    n = max(max(u,v) for u,v,_ in G) + 1

    adj = [[] for _ in range(n)]

    for u,v,w in G:
        adj[u].append((v,w))
        adj[v].append((u,w))
    return adj,n


G = [ (1,5,10), (4,6,12), (3,2,8),
(2,4,4) , (2,0,10), (1,4,5),
(1,0,6) , (5,6,8) , (6,3,9)]

print(edges_to_adjency_list(G))






















def edges_to_adj(E): 

    n = max(max(u,v) for u,v,_ in E) + 1 

    G = [ [] for _ in range(n)]

    for u,v,w in E: 

        G[u].append((v,w))
        G[v].append((u,w))

    return G




