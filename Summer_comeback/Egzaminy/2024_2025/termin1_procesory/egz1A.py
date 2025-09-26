from egz1Atesty import runtests
from collections import deque 
# def battle(P,K,R):
#     #robimy jedną tablice wszystkiego
#     n = len(K)
#     m = len(P)
#     T = [None]*(4*m+4*n) #Puste fragmenty mają w tablicy -2 
#     for i in range(n): 
#         T[K[i]] = (K[i],R[i])

#     for j in range(m): 
#         T[P[j]] = (P[j],-1) #procesory mają 0 
#     counter= 0 
#     q = deque()
#     for i in range(len(T)): 
#         if T[i] == None: 
#             continue
#         pos,marker = T[i]
#         if marker <0:
#             while q: #procesor
#                 last_pos,last_marker = q.pop() #nasza ostatnia katapulta 
#                 #stos LIFO gwarantuje, że katapulty są sprawdzane malejąco indeksami
#                 # #Ale uwaga: to oznacza, że nie sięgnie żadnego procesora jeszcze dalej 
#                 # w prawo (bo wszystkie następne procesory będą miały pos jeszcze większe).
#                 #Dlatego taka katapulta jest bezużyteczna i możemy ją wyrzucić ze stosu na zawsze. 

#                 if last_pos + last_marker >= pos: 
#                     counter += 1 
#                     break 
#         else: 
#             q.append((pos,marker))
#     return counter 
        

            

def battle(P, K, R):
    n = len(K)
    m = len(P)
    markers = [None for _ in range(4*n + 4*m)]
    for i in range(m):
        markers[P[i]] = 0
    for i in range(n):
        markers[K[i]] = R[i]

    answer = 0
    stack = deque()

    for i in range(4*n + 4*m):
        if markers[i] is not None and markers[i] > 0:
            stack.append((i, markers[i]))
        elif markers[i] == 0:
            while stack:
                pos, r = stack.pop()
                if r >= i-pos:
                    answer += 1
                    break

    return answer

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True )