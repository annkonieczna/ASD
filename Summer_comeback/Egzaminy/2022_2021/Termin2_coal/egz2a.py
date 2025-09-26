from egz2atesty import runtests
from math import inf
#O(n^2)
def coal( A, T ):
    n = len(A)
    D= [0]*n 
    k = 0
    index = [None]*n
    D[0] = A[0]
    index[0] = k

    for i in range(1,n):
        f = False
        for j in range(0,i): 
            if D[j] + A[i] <= T: 
                D[j] += A[i]
                f = True
                index[i] = j
                # print(i,D[j],index[i])
                break
        if not f: 
            if D[k] +A[i] <=T:
                D[k] += A[i]
                index[i] = k 
                # print(D[k],index[i]) 
            else: 
                k+=1
                D[k] += A[i]
                index[i] = k
                # print(i,D[k],index[i])
                
    return index[n-1]

#O(nlogn)

def binsearch(T,target):
    l = 0 
    


    pass

def coal(A,T): 
    n = len(A)
    D = [(T,None)]*n
    for i in range(n): 
        D[i][1] = i
    index = [None]*n
    D[0] -= A[0]
    l = 0 
    for i in range(1,n): 
        k = binsearch(D[:l])
        if k == False: 
            if D[l][0]- A[i] <= 0:
                D[l][0] -= A[i]
                index[i] = l
            else: 
                D[l+1][0] -= A[i]
                l += 1 
                index[i] = l
        else:
            index[i] = k
            D[k][0] -= A[i]
    return index[n-1]




                


# A      = [1, 6, 2, 10, 8, 7, 1]
# A      = [2, 7, 6, 7, 6, 3, 10, 9, 2, 7]
# T      = 10            
# print(coal(A,T))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
