from egzP5atesty import runtests 
from math import inf

#Maksymalny prostokąt w histogramie 

#O(n^2)

# def inwestor ( T ):
    # n = len(T)
    # best = 0 
    # dp = [[0]*n for _ in range(n)] #dp[i][j]-minimalna wartość dla przedziału (i,j)
    # for i in range(n): 
    #     dp[i][i] = T[i]
    #     best = max(best,dp[i][i])

    # for l in range(2,n+1):
    #     for i in range(n-l+1): 
    #         j = i + l -1
    #         dp[i][j] = min(T[j],dp[i][j-1])
    #         area = j - i +1
    #         best = max(best,area*dp[i][j])

    # return best 
#O(n) z użyciem stosu
#Chcemy dla każdego elementu z tablicy T znać indeks elementu po prawej i po lewej stronie, który jest mniejszy 
#od naszego elementu 
from collections import deque 
def inwestor(T): 
    n = len(T)
    q = deque()
    q.extend([-1,0])
    area = 0 
    L = [-1]*n
    R = [n]*n
    for i in range(1,n):
        #przypadek, gdy nasz element na stacku jest większy niż i'ty element 
        while q[-1] != -1 and T[q[-1]] > T[i]:
            R[q[-1]] = i 
            q.pop()
        #jeżeli poprzedni element był równy naszemu, to jego najmniejszy element po lewej stronie staje się naszym
        if T[i] == T[i-1]: 
            L[i] = L[i-1]
        #Jeśli nie są one równe, to najmniejszy element po lewej stronie staje się tym samym elementem 
        else: 
            L[i] = q[-1]
                
        q.append(i)

    for j in range(n): 
        area = max(area, T[j]*(R[j]-L[j]-1))
    return area

        


        







# print(inwestor([2, 1, 5, 6, 2, 3]))






runtests ( inwestor, all_tests=True)