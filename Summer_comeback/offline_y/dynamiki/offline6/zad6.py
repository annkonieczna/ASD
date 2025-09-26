from zad6testy import runtests
from math import inf
# def parking(X,Y):
#   n = len(X)
#   m = len(Y)
#   k = max(max(Y),max(X))
#   T = [None]*(k+1)
#   dp = [[inf]*m for _ in range(n)]
#   #min suma przypisania i+1 biurowców X[0]....X[i] przy założeniu, że biurowiec X[i] jest przypisany Y[j]

#   dp[0][0] = abs(X[0]-Y[0])
#   for p in range(m): 
#       dp[0][p] = abs(X[0]-Y[p])
#       dp[0][p] = min(dp[0][p],dp[0][p-1])
#       #dp[0][p] - minimum przypisania pierwszego biurowca, do któregoś z parkingów 
#   for s in range(1,n):
      
#       for p in range(s,m):
#         pass
          
  

# X = [3, 6, 10, 14]
# Y = [1, 4, 5, 10, 11, 13, 17]
# print(parking(X,Y))
# import math

# def parking(X, Y):
#     n = len(X)
#     m = len(Y)
#     f = [[math.inf for __ in range(m)] for _ in range(n)]

#     f[0][0] = abs(X[0] - Y[0])
#     for p in range(1, m):
#         f[0][p] = abs(X[0] - Y[p])
#         f[0][p] = f[0][p-1] if f[0][p-1] < f[0][p] else f[0][p]

#     for s in range(1, n):
#         for p in range(s, m):
#             f[s][p] = min(f[s-1][p-1] + abs(X[s] - Y[p]), f[s][p-1])
            
#     return f[n-1][m-1]



def parking(X,Y): 
    n = len(X)
    m = len(Y)
    field = [[inf]*m for _ in range(n)]
    field[0][0] = abs(X[0]-Y[0])
    #inicjalizujemy przypisanie pierwszego biurowca do każdego z parkingów 
    for p in range(1,m): 
        field[0][p] = abs(X[0]-Y[p])
        field[0][p] = min(field[0][p],field[0][p-1])
    for b in range(1,n):
        for p in range(1,m):
            field[b][p] =min(field[b-1][p-1] + abs(X[b] - Y[p]), field[b][p-1])
    return field[n-1][m-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
