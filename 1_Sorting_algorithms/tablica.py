# Sortujemy n elementową tablicę, która ma liczby ze zbioru ).... N^2-1



def counting_sort(T, key_func):
    N = len(T)
    count = [0] * N

    for num in T:
        digit = key_func(num)
        count[digit] += 1

    for i in range(1, N):
        count[i] += count[i - 1]

    sorted_array = [0] * N

    for num in T:
        digit = key_func(num)
        count[digit] -= 1
        sorted_array[count[digit]] = num

    return sorted_array

def sort(T):
    N = len(T)

    T = counting_sort(T, lambda x: x % N)

    T = counting_sort(T, lambda x: x // N)

    return T