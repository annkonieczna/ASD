#Idea: 

#Merge sort - jest to sortowaie przez scalanie 
#Rekurencyjny algorytm oparty na zasadzie dziel i zwyciężaj (divide and conquer)

#Działanie: 
    #1. Dziel - dzielimy tablicę na poł, aż uzyskamy jednoelementowe podtablice 
    #2. Zwyciężaj (scalaj) - scalaj ze sobą mniejsze posortowane talice w większe w sposób uporządkowany 


def merge(T,b,m,e):
    #b-indeks wskazujący na pierwszy element (beginning)
    #m-middle
    #e-end     
    #liczymy długość podtablic 
    l1 = m - b + 1 
    l2 = e - m
    #Tworzymy lewą i prawą podtablicę poprzez slicing  
    L = T[b:m+1]
    R = T[m+1:e+1]
    #mamy sobie fajniutkie 2 tablice 

    #Następnie scalamy dwie posortowane tablice 
    i,j = 0,0
    k = b 
    # i - wskaźnik w tablicy L
    #j - wskaźnik w tablicy R
    #k - wskaźnik w tablicy T, w którą będziemy wpisywać wyniki 

    #dopóki mamy elementy w obu listach: 
    while i < l1 and j <l2: 
        #porównujemy L[i] z R[j]
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1 

        else: 
            T[k] = R[j]
            j += 1 
        
        k += 1 
    while i < l1: 
        T[k] = L[i]
        i+= 1 
        k+= 1 
    while j < l2: 
        T[k] = R[j]
        j+= 1 
        k+= 1

def merge_sort(T,b,e):

    #przypadek bazowy, przy 1 elemntowej tablicy 
    if b>=e: 
        return 
    #wyznaczamy środek fragmentu 
    
    m = (b+e) // 2 
    #sortujemy osobno prawą i lewą stronę wywołując rekurencyjnie tę funkcję 

    merge_sort(T,b,m)
    merge_sort(T,m+1,e)
    #następnie scalamy dwie połowy 
    merge(T,b,m,e)

def sort(T): 
    n = len(T)
    merge_sort(T,0,n-1)


T = [5, 2, 8, 1]
sort(T)
print(T)


    
    