from egz1btesty import runtests

#Mamy 3 opcje: 
#
# def kstrong( T, k):
#   n = len(T)
#   sum = T[0] #zaczynamy wynik od zerowego elementu(przydaje się, gdy wszystkie liczby są ujemne)
#   dp = [[0]*(k+1) for _ in range(n)] # dp[i][j] maksymalna suma j-spójnego podciągu 
#   #kończącego się na i'tym elemencie
#   dp[0][0] = T[0] #baza jeśli nie możemy nic usuwać, wtedy najlepszy podciąg, to po prostu pierwszy element 

#   for i in range(1,n): 
#     #Nie usuwamy i'tego elementu natomiast sprawdzamy czy bardziej opłaca nam się dodać ten element do ciągu 
#     #czy zacząć nowy ciąg od tego elementu 
#     dp[i][0] = max(dp[i-1][0]+T[i],T[i])
#     sum = max(sum,dp[i][0])
#   for kj in range(1,k+1):
#     for i in range(1,n): 
#       #maximum z ( 1. zachowujemy T[i], usuwamy element T[i])
#       dp[i][kj] = max(dp[i-1][kj]+T[i],dp[i-1][kj-1]) #zużywamy jedną delecję
#       sum = max(sum,dp[i][kj])
#   return sum 

#Mamy 3 opcje: 
#Bierzemy i'ty element do naszego ciągu 
#Pomijamy i'ty element i idziemy dalej z naszym ciągiem jeżeli usuięte elementy są < 2 
#Zaczynamy nowy ciąg od i'tego elementu 



from math import inf
def kstrong(T,k):
    n = len(T)
    dp = [[-inf]*(k+1) for _ in range(n)] # dp[i][j] maksymalna suma ciągu jaki udało nam się stworzyć do elementu i usuwając k elementów 
    dp[0][0] = T[0]
    maxi = T[0]
    for i in range(1,n): 
      # sprawdzamy czy bardziej nam się opłaca wziąć nasz element do ciągu czy zacząć nowy ciąg od i'tego elementu 
      dp[i][0] = max(dp[i-1][0]+T[i], T[i])
      # print(dp[i][0])
      maxi = max(maxi,dp[i][0])


    for j in range(1,k+1): 
       for i in range(1,n): 
          dp[i][j] = max(dp[i-1][j-1],dp[i-1][j] + T[i])
          #1.usuwamy  element i'ty, czyli po prostu bierzemy max_sumę z ciągu, który kończył się na i-1 i miał 
          #j-1 usunięć 
          #2. dołączamy T[i] do ciągu, który miał już j usunięć 
          maxi = max(maxi,dp[i][j])
    return maxi
      

# print(kstrong([-20, 5, -1, 10, 2, -8, 10],1))

         

        
















# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )


# O(nk) time complexity


# def kstrong(T, k):
#     n = len(T)
#     dp = [[0 for __ in range(k+1)] for _ in range(n)]
#     answer = T[0]
#     dp[0][0] = T[0]
#     for i in range(1, n):
#         dp[i][0] = max(dp[i-1][0]+T[i], T[i])
#         answer = max(answer, dp[i][0])

#     for kj in range(1, k+1):
#         for i in range(1, n):
#             dp[i][kj] = max(dp[i-1][kj-1], dp[i-1][kj] + T[i])
#             answer = max(answer, dp[i][kj])

#     return answer


# T = [-20, 5, -1, 10, 2, -8, 10]
# k = 1
# print(kstrong(T, k))
