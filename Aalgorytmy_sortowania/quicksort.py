#quicksort używając max O(logn) pamięci 


def partition(T,l,r): 
    pivot = T[r]
    pointer = l-1

    for i in range(l,r):
        if T[i] <= pivot:
            pointer += 1
            T[i], T[pointer] = T[pointer], T[i]
    
    T[r],T[pointer + 1] = T[pointer +1], T[r]
    return pointer + 1

def quicksort(t,l,r): 
    while l<r: 
        pivot = partition(T,l,r)
        if pivot - l < r -pivot:
            quicksort(T,l,pivot-1)
            l = pivot + 1
        else: 
            quicksort(T,pivot +1,r)
            r = pivot -1

T = [1,3,5,3,2,7,8]

print(T)

quicksort(T,0,len(T)-1)
print(T)

