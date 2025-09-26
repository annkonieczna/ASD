from egz3btesty import runtests
#O(n^2)
def uncool( P ):
  n = len(P)

  for i in range(n): 
    for j in range(i+1,n): 
      a,b = P[i]
      c,d  = P[j]
      #zawieranie się 
      if (a <= c and d <= b) or (c <=a and b<=d): 
        continue
      #rozłączne
      if (b <c) or (d < a): 
        continue
      return (i,j)




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
