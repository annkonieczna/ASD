#zadanie 3
from math import log
def Bellman_Ford(Gr,s): #modyfikacja z zadania 6
    n=len(Gr)
    d=[float('inf')]*n
    G=[[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(len(Gr[i])):
            G[i][Gr[i][j][0]]=log(Gr[i][j][1])
    d[s]=0
    par=[None]*n
    for i in range(n):
        B=False
        for j in range(n):
            for k in range(n):
                B|=relax(par,d,j,k,G)
    if B: return d,par,False
    return d,par,True

def relax(par,d,i,j,G):
    if d[j]>d[i]+G[i][j]:
        d[j]=d[i]+G[i][j]
        par[j]=i
        return True
    return False

def path(G,start_v,end_v):
    a=Bellman_Ford(G,start_v)
    if not a[2]: return a[0],a[1],"no path - negative cycle"
    k=end_v
    p=[]
    while k!=None:
        p.append(k)
        k=a[1][k]
    if p[-1]!=start_v:
        return a[0],a[1],"no path in this directed graph"
    p.reverse()
    return a[0],a[1],p