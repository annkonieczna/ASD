#Heapsort jest oparty na heapie (kopcu)
# Najczęściej używa się kopca maximum gdzie każdy rodzic ma wartość większe od jego dzieci 

#Złożoność O(nlogn)


#Najpierw piszemy funkcje zwracające indeksy rodziców i dzieci dla wierzchołka o indeksie i 



#Na każdym poziomie liczba węzłów w kopcu binarnym się podwaja(wzory są oparte na 2i).
#liczba węzłów rośnie wykładniczo:

#Sposób na zapamiętanie
#Dzieci są „dwa razy więcej niż rodzic” → 2i + ...
# Lewe dziecko jest pierwsze → +1, prawe drugie → +2
# Rodzic to „w połowie drogi w górę” → (i - 1) // 2



def parent(i):
    return (i-1)//2
def left_kid(i):
    return 2*i+1
def right_kid(i):
    return 2*i+2

#funkcja heapify- naprawia kopiec maksymalny, zakłądając, że dzieci i są już kopcami,
#ale i może być mniejsze od któregoś z dzieci
def heapify(A,i,n):
    l = left_kid(i)
    r = right_kid(i)
    max_index = i #zakładamy, że największy to aktualny węzeł 
    
    #sprawdzamy, czy nie wyszliśmy za tablicę (czy te dzieci istnieją)
    #oraz czy któreś z dzieci ma większą wartość od naszego rodzica 
    if l<n and A[max_index] < A[l]:  # jak zamienimy tu nierówność to mamy kopiec minumim

        max_index = l

    if r<n and A[max_index] < A[r]: 

        max_index = r
    if max_index != i: 
        A[i], A[max_index] = A[max_index], A[i]
        heapify(A,max_index,n) 

#funkcja build_max_heap- buduje kopiec maksymalny z nieuporządkowanej tablicy 
def build_max_heap(T,n):
    #zaczynamy od ostatniego węzła, który nie jest liściem  i idziemy do góry 
    for i in range(parent(n-1),-1,-1):
        heapify(T,i,n)

def heapsort(T):
    n = len(T)
    build_max_heap(T,n)
    #to, że mamy zbudowany kopiec gwarantuje nam tylko to, że największy element(na miejscu T[0]) jest na
    #samej górze więc możemy go zeswapować z ostatnim elementem 

    for i in range(n-1,0,-1):
        T[0], T[i] = T[i], T[0]
        heapify(T,0,i) #naprawiamy bez ostatniego elementu 

T= [2,4,1,33,4,12,-8,17,96,124,5,36,100]
heapsort(T)
print(T)







