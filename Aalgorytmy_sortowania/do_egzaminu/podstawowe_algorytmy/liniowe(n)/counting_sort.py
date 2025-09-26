#Idea: 
#Counting sort sortuje tablicę o rozmiarze n, w której występują liczby z zakresu od [0, k]. 
#Wykorzystuje ideę sum prefixowych (Dla tablicy A[0..n-1] suma prefiksowa w indeksie i to suma wszystkich 
# elementów od początku do i włącznie)

#Złożoność: 
#O(n+k)

#Kiedy używać counting sort?
# Gdy elementy są liczbami całkowitymi w małym względnym zakresie (k ≲ c·n).

# Gdy potrzebujesz stabilnego sortowania (np. jako część radix sort).
# Nie używaj, gdy kluczy jest bardzo dużo (np. 32-bitowe liczby losowe 
# bez dodatknego przetwarzania) — pamięć rośnie z k

from random import randint

def counting_sort(T,n,k):
    B = [0]*n #tablica wynikowa, w której będziemy wpisywać  posortowane liczby(wynik)
    C = [0]*(k+1) #tablica liczników(k=1, bo uwzględniamy zarówno 0 jak i k)

    #Ile jest liczb równych konkretnej liczbie z przedziału od 0 do k 
    for i in range(n): 
        C[T[i]]+= 1 
    #Zamieniamy C na tablicę sum prefixowych 
    for j in range(1,k+1): 
        C[j] += C[j-1]

    #Chcemy teraz umieścić każdy element z tablicy T w odpowiednim miejscu w tablicy B 
    #korzystając z sum prefiksowych w tablicy C 

    #Po drugiej pętli C[v] mówi: ile elementów w całej tablicy jest ≤ v.
    # Z tego wynika, że ostatnia (najwyższa) pozycja przeznaczona
    # dla wartości v w tablicy B to indeks C[v] - 1 (bo indeksy zaczynają się od 0).
    #Gdy umieścimy jeden element v na tej pozycji, musimy zarezerwować kolejne (wcześniejsze)
    #  miejsce dla następnego wystąpienia v. Robimy to przez C[v] -= 1 — teraz C[v] wskazuje 
    # „następne wolne miejsce” dla wartości v (czyli pozycję tuż przed poprzednią).
    # Iteracja od końca (n-1 do 0) gwarantuje stabilność: jeśli w T są dwie równe wartości v
    #  i pierwsza występuje wcześniej, to w B ta wcześniejsza zostanie wpisana wcześniej niż ta,
    #  która występowała pózniej (czyli zachowujemy kolejność elementów o równym kluczu).

    for i in range(n-1,-1,-1):


        B[C[T[i]] - 1] = T[i]
        C[T[i]] -= 1 

    return B 

T = [randint(0, 100) for _ in range(20)]
print(counting_sort(T, len(T), 100))


    


