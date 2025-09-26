# Dana jest n-elementowa tablica liczb naturalnych T. Dla każdego indeksu i < n, rangą elementu
# na pozycji i określamy liczbę elementów, które w tablicy występują przed elementem i-tym, a ich
# wartość jest mniejsza od T[i].

# Proszę zaimplementować funkcję maxrank(T), która dla tablicy T o rozmiarze n elementów zwróci
# maksymalną rangę pośród wszystkich elementów tablicy.


T = [5,3,9,4]

def maxrank(T):

    n = len(T)
    maxi= -float("inf")
    for i in range(1,n): 
        counter = 0 
        for j in range(i):

            if T[j] < T[i]:
                counter += 1
        if counter > maxi: 
            maxi = counter 


    return maxi 

print(maxrank(T))


    






