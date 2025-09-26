from egz3btesty import runtests
# na każdym etapie podróży wojownik może podjąć 3 wybory, pójść w prawo do góry lub w dół, jeśli nie opuści przez
#to zakresu tablicy ani nie napotka znaku z hashtagiem
from math import inf
# def maze( L ):
#     n = len(L)
#     dp = [[-inf]*n for _ in range(n)] #maksymalna liczba odwiedzonch komnat dochodząc do komnaty (i,j)
#     dp[0][0] = 0 
#     if L[0][0] == '#' or L[n-1][n-1] == '#':
#         return -1
    
#     #Zaczynamy kolumnami dlatego, że jak spojrzymy na ten problem, w ten sposób, że albo poruszamy się 
#     # w górę i w dół do kolejnych rzędów albo idziemy w prawo do nowej kolumny i nigdy nie możemy wrócić 
#     #do poprzedniej 
#     for c in range(1,n):
#         #idziemy w prawo z poprzedniej kolumny 
#         for r in range(n): 
#             if L[r][c] != '#':
#                 if dp[r][c-1] != -inf: 
#                     dp[r][c] = max(dp[r][c-1]+1,dp[r][c])
#         #idziemy do dołu 
#         for r in range(1,n):
#             if L[r][c] != '#':
#                 if dp[r-1][c] != -inf: 
#                     dp[r][c] = max(dp[r][c], dp[r-1][c]+1)
#         #idziemy do góry 
#         for r in range(n-2,-1,-1):
#             if L[r][c] != '#':
#                 if dp[r+1][c] != -inf: 
#                     dp[r][c] = max(dp[r][c], dp[r+1][c]+1)
#         # print(dp)

#     return dp[n-1][n-1] if dp[n-1][n-1] != -inf else -1

# L = ['....', '..#.', '..#.', '....']
# print(maze(L))

def maze( L ):
    n = len( L )
    DPG = [[-1 for _ in range( n )] for __ in range( n )] # w górę
    DPD = [[-1 for _ in range( n )] for __ in range( n )] # w dół

    if( L[0][0] == '#' or L[n-1][n-1] == '#' ): return -1

    DPG[0][0], DPD[0][0] = 0,0

    for row in range(1,n):
        if L[row][0] == '#': break
        DPD[row][0] = DPD[row-1][0]+1

    for col in range( 1,n ):
        for row in range(n):
            if L[row][col] == '#': continue
            if DPG[row][col-1] == -1 and DPD[row][col-1] == -1: continue
            val = max(DPG[row][col-1], DPD[row][col-1]) + 1
            DPG[row][col] = val
            DPD[row][col] = val
        for row in range(n):
            if L[row][col] == '#': continue
            if DPG[row][col-1] == -1 and DPD[row][col-1] == -1 : continue
            row1, row2 = row-1,row+1
            while row1 >=0:
                if L[row1][col] == '#': break
                DPG[row1][col] = max(DPG[row1][col], DPG[row1+1][col]+1)
                row1 -=1
            while row2 <n:
                if L[row2][col] == '#': break
                DPD[row2][col] = max(DPD[row2][col], DPD[row2-1][col]+1)
                row2 +=1
        
    if DPG[n-1][n-1] == -1 and DPD[n-1][n-1] == -1: return -1
    return max(DPG[n-1][n-1], DPD[n-1][n-1])



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
