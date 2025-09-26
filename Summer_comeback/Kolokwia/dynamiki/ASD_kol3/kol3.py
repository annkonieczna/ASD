

from kol3testy import runtests
from math import inf 

def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])
    dp = [[inf]*m for _ in range(n)]
    for i in range(n-1,-1,-1): 
        for j in range(m-1,-1,-1): 
            #jesteśmy w ostatnim wierszu 
            if i == n-1: 
                sum_row = C[i][j] 
                if sum_row <=s: 
                    dp[i][j] = 0 
                    continue
            if j == m-1: 
                sum_colum = C[i][j] 
                if sum_colum <=s: 
                    dp[i][j] = 0 
                    continue
            #dodajemy wiersz
            sum_row = C[i][j] - (C[i+1][j] if i+1 <n else 0)
            sum_colum = C[i][j] - (C[i][j+1] if j+1 <m else 0)
            if sum_row <= s: 
                dp[i][j] = min(dp[i][j],1+dp[i+1][j])
            if sum_colum <=s: 
                dp[i][j] = min(dp[i][j], 1+ dp[i][j+1])
    return dp[0][0] if dp[0][0] != inf else -1

            

# def parkiet(B, C, s):
#     m = len(B)
#     n = len(B[0])
    
#     cnt1 = 0
#     i = 0
#     j = 0
#     while True:
#         if i == m - 1 and j == n - 1:
#             break
        
#         if i < m - 1 and j < n - 1:
#             if C[i][j] - C[i][j + 1] <= s:
#                 cnt1 += 1
#                 j += 1
#             elif C[i][j] - C[i + 1][j] <= s:
#                 cnt1 += 1
#                 i += 1  
                        
#         elif j < n - 1:
#             if C[i][j] - C[i][j + 1] <= s:
#                 cnt1 += 1
#                 j += 1     
                        
#         elif i < m - 1:
#             if C[i][j] - C[i + 1][j] <= s:
#                 cnt1 += 1
#                 i += 1
                        
#         if (i == m - 1 or j == n - 1) and C[i][j] <= s:
#             break
    
#     cnt2 = 0
#     i = 0
#     j = 0
#     while True:
#         if i == m - 1 and j == n - 1:
#             break
        
#         if i < m - 1 and j < n - 1:
#             if C[i][j] - C[i + 1][j] <= s:
#                 cnt2 += 1
#                 i += 1 
#             elif C[i][j] - C[i][j + 1] <= s:
#                 cnt2 += 1
#                 j += 1
                             
#         elif i < m - 1:
#             if C[i][j] - C[i + 1][j] <= s:
#                 cnt2 += 1
#                 i += 1    
                            
#         elif j < n - 1:
#             if C[i][j] - C[i][j + 1] <= s:
#                 cnt2 += 1
#                 j += 1             
                        
#         if (i == m - 1 or j == n - 1) and C[i][j] <= s:
#             break
                   
#     return min(cnt1, cnt2)

runtests(parkiet, all_tests = True)
