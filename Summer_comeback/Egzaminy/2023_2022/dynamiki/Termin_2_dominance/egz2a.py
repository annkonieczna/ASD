from egz2atesty import runtests
#O(n^2)
def dominance(P):
  n = len(P)
  P.sort(key = lambda x: x[0])
  dp = [0]*n
  for i in range(1,n): 
    counter = 0
    for j in range(0,i): 
      if P[i][1] > P[j][1] and P[i][0] > P[j][0] : 
        counter += 1 
    dp[i] = counter 
  return max(dp)



#O(nlogn)
# def dominance(P): 
#   n = len(P)
#   P.sort(key = lambda x: x[0])

from math import inf 
def dominance(P): 
	n = len(P)
	x = [0]*(n+1)
	y = [0]*(n+1)
	for p in P: 
		x[p[0]] += 1
		y[p[1]] += 1 
	for i in range(n-1,-1,-1): 
		x[i] += x[i+1] 
		y[i] += y[i+1]
	min_not_dominated = inf
	for p in P:
        # This counts |x| + |y| + |x ∩ y| Every point with
        # both x and y greater equal will be counted twice. This
        # is not a problem however as the point which dominates
        # most points can't have any point in area |x ∩ y|.
		not_dominated = x[p[0]] + y[p[1]]
		min_not_dominated = min(min_not_dominated, not_dominated)

    # The point dominating most points counted itself twice,
    # because of adding |x ∩ y|, So we need to subtract 1.
	return n - (min_not_dominated + 1)+2
     

    

    





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True)
