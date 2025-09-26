from egz3btesty import runtests

from collections import deque
#O(n)
# def kunlucky(T, k):
#   n = len(T)
#   is_unlucky = [False]*(n+1)
#   i = k 
#   nu = 1
#   while i <= n: 
#     is_unlucky[i] = True 
#     i = 7+ i + (i%nu)
#     nu += 1 
#   q = deque()
#   max_len,L =  0, 0
#   for j in range(n): 
#     if is_unlucky[T[j]]:
#       q.append(j)
#       if len(q) == 3:
#         L = q.popleft() + 1 
#     max_len = max(max_len, j -L+1)
      
    
#   return max_len
# #O(n^2)
# def kunlucky(T,k): 
#   n = len(T)
#   is_unlucky = [False]*(n+1)
#   i = k 
#   nu = 1
#   max_len = 0 
#   while i <= n: 
#     is_unlucky[i] = True 
#     i = 7+ i + (i%nu)
#     nu += 1 
#   for i in range(n): 
#     count_unlucky = 0 
#     for j in range(i,n):
#       if is_unlucky[T[j]]: 
#         count_unlucky+= 1 
#         if count_unlucky == 3:
#           break  
           
#       max_len = max(max_len,j-i +1)
#   return max_len

from collections import deque 
def kunlucky(T,k): 
    n = len(T)
    maxi = max(T)
    is_unlucky = [False]*(maxi+1)
    x = k 
    i = 1 
    while x <= maxi: 
        is_unlucky[x] = True 
        temp = x
        x = temp + (temp % i) + 7 
        i += 1 
    # print(is_unlucky)
    maxi = 0 
    l = 0 
    q = deque()
    for i in range(n): 
        if not is_unlucky[T[i]]:
            maxi = max(maxi,(i-l+1))
        else: 
            if len(q) < 2: 
                q.append(i)
            else:
                l = q.popleft() + 1 
                q.append(i)
                maxi = max(maxi,(i-l+1))
    return maxi 
            
            
            
        
        
        
  
#   return 
# print(kunlucky([11, 10, 19, 19, 17, 16, 3, 9, 6, 14, 13, 8, 2, 13, 11, 12, 5, 5, 5],3))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True)
