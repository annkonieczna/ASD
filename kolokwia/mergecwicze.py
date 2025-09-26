# dla tablilcy 

def merge(left,right): 

    nowa_tablica = []

    i = j = 0 

    while i < len(left) and j < len(right): 

        if right[i] < left[j]: 

            nowa_tablica.append(right[i])
        
    nowa_tablica.append(left or right)


def merge_sort(A): 

    middle = 
    
    left = mergesort(A[:middle])
