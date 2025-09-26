from math import inf
def kstrong(T,k):
    n = len(T)

    dp =[-inf]*(k+1)
    #dp[j] – największa możliwa suma podciągu kończącego się na aktualnej pozycji (np. i),
       # w którym usunięto dokładnie j elementów.
    result = -inf

    for i in range(n): 
        new_dp = [-inf]*(k+1)
        for j in range(k+1): 
            # 1. Dodajemy element i do naszej sumy 
            if dp[j] != inf:
                new_dp[j] = dp[j] + T[i]
            
            #2. Sprawdzamy, czy bardziej nie opłacałoby się nam zacząć nowego ciągu 
            new_dp = max(new_dp[j],T[i])

            #3. Pomijamy element i (najpierw sprawdzając czy możemy)
            if j >0 and dp[j-1] != -inf: 
                new_dp = max(new_dp,new_dp[j-1])

            result = max(result,new_dp)


        dp = new_dp

        #dp to stan z poprzedniego kroku i w tej linijce dajemy znać, że zakończyliśmy analizę dla konkretnego i 
        #i idziemy do kolejnego 

    
    return result



