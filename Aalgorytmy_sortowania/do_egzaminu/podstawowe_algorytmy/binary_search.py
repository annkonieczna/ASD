#Idea: 
#Binary search działa jedynie na posortowanej liście. 
#Zamiast patrzeć na elementy po kolei parzymy na środkowy element i sprawdzamy, czy jest większy czy mniejszy
#od naszego, większy or our element 
#O(logn)

def binary_search(T, target): 

    n = len(T)

    left = 0 
    right = n-1 
    while left <= right: 
        middle = (right+left) //2 
        if T[middle] == target: 
            return middle
        if T[middle] > target: 
            right = middle - 1
        if T[middle] < target: 
            left = middle +1
    return -1 

arr = [1, 3, 5, 7, 9]
print(binary_search(arr,8))






