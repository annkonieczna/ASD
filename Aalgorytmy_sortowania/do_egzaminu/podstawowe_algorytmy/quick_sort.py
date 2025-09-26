#Złożoność: 
# best O(n)
# avg. O(nlogn)
# worst O(n^2)

#Wersja Lomuto z partition 

#Idea 
#1. Wybieramy pivot 
#2. Dzielimy tablicę w ten sposób, żeby elementy mniejsze/ większe od pivota znalazły 
# się po odpowiednich stronach tablicy
#3. Rekurencyjnie sortujemy prawą i lewą stronę tablicy (pivot jest już na swoim miejscu)
from random  import randint
def partition(T,p,r):
    k = T[randint(p,r)]
    T[k], T[r] = T[r], T[k] #zamieniamy element na koniec tablicy, gdyż wersja Lomuto zakłada,
    #że pivot jest na końcu 
    x = T[r]
    i = p-1 #zaczynamy przed początkiem tablicy 

    for j in range(p,r): # skanuje wszystkie elementy oprócz pivota.
        if T[j] <= x: 
            i += 1 
            T[i], T[j] = T[j], T[i]
    
    #Po pętli pivot zostaje zamieniony z T[i+1] — 
    # dzięki temu pivot trafia na pierwszą pozycję po bloku elementów <= pivot
    T[i+1],T[r] = T[r], T[i+1]
    return i+1 #pozycja na której mamy pivota


def quicksort(T,p,r):
    if p < r: 
        pivot_index = partition(T,p,r)
        quicksort(T,p,pivot_index - 1) #omijamy pivota, bo jest już na swoim miejscu 
        quicksort(T,pivot_index+1,r)

