from egz2btesty import runtests
from math import inf
def magic( C ):
    n = len(C)
    dp = [-inf]*n  #dp[i] - maksymalna liczba sztabek z jaką udało mi się dojść do komnaty i z komnaty j 
    dp[0] = 0
    for i in range(n): 
        #pierwsza komnata 
        gold = C[i][0] 
        for j in range(1,4): 
            c, index = C[i][j]
            if index == -1: 
                continue
            #pierwszy przypadek w skrzyni znajduje się tyle ile potrzebujemy na podróż
            if gold == c and dp[index] < dp[i]:
                dp[index] = dp[i]
            #drugi przypadek w skrzyni jest nie wystarczająco na naszą podróż
            if gold < c and dp[i] >= c-gold and dp[index] < dp[i]-(c-gold): 
                dp[index] = dp[i]- (c-gold)
            #trzeci przypadek w skrzyni jest za dużo 
            if gold > c and gold-c <=10 and dp[i] + (gold-c) > dp[index]:
                dp[index] = dp[i] + gold-c
    return dp[n-1] if dp[n-1] != -inf else -1
            
            
            
        
        



# zmien all_tests na True zeby uruchomic wszystkie testy
# C = [ [8, [ 6, 3], [ 4, 2], [7, 1]], # 0
# [22, [12, 2], [21, 3], [0,-1]], # 1
# [9, [11, 3], [ 0,-1], [7,-1]], # 2
# [15, [ 0,-1], [ 1,-1], [0,-1]]]
# print(magic(C))
runtests( magic, all_tests = True )
