from kolutesty import runtests

def projects(n, L):
  G = [[] for _ in range(n)]
  projects_before = [0]*n #ile projektów musi być wykonanych przed naszym
  for p,q in L: 
    G[q].append(p)
    projects_before[p] += 1 

  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = False )
