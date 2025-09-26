# Trzeba korzystać z arytmetyki modulo - odejmowanie/dodawanie liczb na modulo tak samo wpłynie ma podzielność/niepodzielność
# Ten problem można sprowadzić do problemu plecakowego

# f(i, j) = minimalna liczba drzew do i-tego indeksu, jaką było trzeba wyciąć, aby mieć j-tą resztę z dzielenia przez m jabłek
# albo drzewo zostawiamy, albo go wycinamy

# O(n^2)



def orchard(T, m):
    n = len(T)
    F = [[n] * m for _ in range(n)]
    
    F[0][0] = 1 # zawsze mogę usunąć pierwsze drzewo
    F[0][T[0] % m] = 0 # warunek brzegowy - nie wycinam drzew aby otrzymać resztę z 0-drzewa

    for i in range(1, n):
        for j in range(m):
            F[i][j] = min(F[i][j], F[i - 1][j] + 1) # mogę ściąć drzewo

            future_rest = (j + T[i]) % m
            F[i][future_rest] = min(F[i][future_rest], F[i - 1][j])

    return F[n - 1][0]


def orchard(T,m): 

    n = len(T)
    F = [[n]*m for _ in range(n)]

    F[0][0] = 1 
    F[0][T[0]% m] = 0


#Wiemy ile owoców jest na każdym z n drzew 
# Suma owoców musi być podzielna przez m 

#Pytanie: ile drzew musi ściąć, żeby zpełniać warunek konkursu (najmniej) 
#W najgorszym przypadku musi wyciąć wszystkie 

#Tablica T zawiera
# n-elementów, gdzie wartość T[i] to liczba jabłek na i-tym drzewie, a m to liczba, przez którą
# suma owoców na drzewach musi być podzielna.

#Liczba m jest liczbą całkowitą z przedziału [1, 7n].



