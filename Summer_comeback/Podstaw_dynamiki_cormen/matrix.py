#Mamy dany ciąg n macierzy <A1,A2,A3....An> i chcemy obliczyć ich iloczyn 

#Chcemy w tym iloczynie ustawic nawiasowanie 

#Kod zwykłego wymnożenia dwóch macierzy ze sobą: 

#Macierz A musi mieć wymiar pxq i macierz B wymiar qxr
def matrix_multiply(A,B): 
    q1 = len(B) #rows 
    q2 = len(A[0]) #columns 

    if q1 != q2: 
        raise ValueError
    r = len(A) #liczba rzędów macierzy C 
    c = len(B[0]) #liczba kolumn macierzy C  
    C =  [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r): 

        for j in range(c): 
            s = 0
            for k in range(q1): 

                s += A[i][k]*B[k][j]
            C[i][j] = s
                
    
    return C 

A = [[0,1],[2,3],[4,5],[6,5]]
B = [[0,1,2],[2,0,4]]

print(matrix_multiply(A,B))

from math import inf 

#rozwiązanie dynamiczne O(n^3)

def matrix_chain_order(p): 
    #p - ciąg macierzy, w której p[i-1]xp[i] to wymiary macierzy Ai
    n = len(p) - 1
    m = [[0]*n for _ in range(n)]  #m[i][j] minimalny koszt obliczenia Aij
    s = [[0]*n for _ in range(n)] #indeks podzialu, który daje najmniejszy koszt 

    #przechodzimy przez wszystkie możliwości podłańcuchów(ile macierzy mnożymy naraz) (od długości 2 do n)
    for l in range(2,n+1): 
        #następnie przechodzimy przez wszystkie możliwe początki tych łańcuchów w ciągu p 
        for i in range(n-l+1):

            j = i+l-1

            m[i][j] = inf 

            for k in range(i,j): #miejsce w którym dzielimy łańcuch Aij 
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                #m[i][k]- koszt lewego nawiasowania 
                #m[k+1][j] - koszt prawego nawiasowania
                # p[i]*p[k+1]*p[]
                if q < m[i][j]: 
                    m[i][j] = q 
                    s[i][j] = k 
    return m,s 

p = [10, 100, 5, 50]
m, s = matrix_chain_order(p)

print(m[0][2], m)




