from math import inf 


def kunlucky(T, k):
    n = len(T)
    max_in_T = T[0]

    for num in T:
        max_in_T = max(max_in_T, num)
    is_unlucky = [False]*(max_in_T+1)

    xi = k
    i = 1
    while xi<=max_in_T:
        is_unlucky[xi] = True
        xi = xi + (xi%i) + 7
        i+=1
    
    l = 0
    count_unlucky = 0
    max_len = 0

    for r in range(n):
        if is_unlucky[T[r]]:
            count_unlucky+=1

        while count_unlucky > 2:
            if is_unlucky[T[l]]:
                count_unlucky -= 1
            l+=1
        max_len = max(max_len, r-l+1)

    return max_len

# zmien all_tests na True zeby uruchomic wszystkie testy


T = [11, 10, 19, 19, 17, 16, 3, 9, 6, 14, 13, 8, 2, 13, 11, 12, 5, 5, 5]
k = 3
        
    




