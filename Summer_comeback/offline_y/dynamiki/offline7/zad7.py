from zad7testy import runtests
from math import inf

def orchard(T, m):
    n= len(T)
    dp = [[inf]*m for _ in range(n)]
    #dp[i][j] minimalna ilość drzew, które wycieliśmy dochodząc do indeksu i z resztą z dzielenia j
    dp[0][0]=1
    dp[0][T[0]%m] = 0

    for i in range(1,n):
        for j in range(m): 
            if dp[i-1][j] != inf: 
                #wycinamy drzewo 
                dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
                #nie wycinamy drzewa 
                new_r = (j+T[i])%m
                dp[i][new_r] = min(dp[i][new_r],dp[i-1][j])
        
    return dp[n-1][0]
print(orchard([2,2,7,5,1,14,7], 7))





from math import inf 
def orchard(T,m): 
    n = len(T)
    dp = [[inf]*(m) for i in range(n)] #dp[i][j] - minimum wyciętych drzew dochodząc do drzewa i z resztą j
    dp[0][0] = 1
    dp[0][T[0]%m] = 0 
    for i in range(1,n):
        for j in range(m): 
            if dp[i-1][j] != inf: 
                #wycinamy drzewo 
                dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
                # nie wycinamy drzewa 
                new_r = (j + T[i])%m
                dp[i][new_r] = min(dp[i][new_r],dp[i-1][j])

    return dp[n-1][0]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
# print((7-14%7)%7)
