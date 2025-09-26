from egzP4atesty import runtests 
def bin_search(A,l,r,key):
    while r-l> 1: #kończy, gdy mamy jakieś 2 elementy 
        m = (r+l)//2
        if A[m] > key: 
            r = m 
        else:
            l = m 
    return r 

def lis(T): 
    n = len(T)
    S = []
    S.append(T[0])
    for i in range(1,n): 
        if T[i] >= S[len(S)-1]: #ostatni element S
            S.append(T[i])
        else: 
            S[bin_search(S,-1,len(S)-1,T[i])] = T[i]
    return len(S)

def mosty(T): 
    T.sort(key = lambda x: (x[0],x[1]))
    T2 = [T[i][1] for i in range(len(T))]
    return lis(T2)
    


        #bierzemy naszą kolejną krawęź do naszego pociągu 

        #pomijamy naszą krawędź i kontynuujemy 

        #zaczynamy dowy ciąg od naszej krawędzi 
        
# def mosty ( T ):
#     T.sort(key = lambda x : (x[0],x[1]))
#     n = len(T)
#     dp = [1]*n
#     for i in range(1,n):
#         for j in range(0,i): #przeglądamy wszystkie wcześniejsze mosty 
#             if T[i][1] > T[j][1]:
#                 dp[i] = max(dp[i],dp[j] + 1) 
    
#     return max(dp)
runtests ( mosty, all_tests=True)

