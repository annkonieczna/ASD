from kolutesty import runtests
#O(nlogn)
# def ice_cream( T ):
#     n = len(T)
#     T.sort(reverse = True)
#     volume = 0
#     time = 0 
#     for i in range(n): 
#         if time < T[i]: 
#             volume += (T[i]-time)
#             time+= 1 
#     return volume 

#O(n)
def ice_cream(T):
    n = len(T)
    if n == 0: 
        return 0 
    m = max(T)
    cnt = [0]*(m+1)
    for i in range(n):
        cnt[T[i]] += 1 
    volume = 0 
    time = 0 
    for j in range(m,0,-1):
        while cnt[j] > 0 and time < n: 
            if j > time: 
                volume += (j-time)
                time += 1 
                cnt[j] -= 1 
            else: 
                return volume 
    return volume


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
