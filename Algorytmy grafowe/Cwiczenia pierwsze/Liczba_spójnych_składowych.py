# 

def spojne_sklad(G):
    n = len(G) 
    cnt = 0 
    visited = [False]*n
    def DFSVisit(G,u): 
        visited[u] = True 
        for u in G[u]: 
            if not visited[u]: 
                DFSVisit(G,u)
    for i in range(n):
        if not visited[i]:
            cnt += 1 
            DFSVisit(G,i)
    return cnt 




