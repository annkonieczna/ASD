#n kubełków z lodami 
# W każdym kubełku pewna objętość lodów 
#Zjedzenie jednego kubełka zajmuje jedną minutę 
#Z upływem każdej minuty topi się jedna jednostka 
#Element T[i] to początkowa objętość lodów w i-tym kubełku

#Aby zjeść jak najwięcej lodów, musimy zaczynać od kubełków z największą objętością

#Posortować kubełki malejąco według objętości lodów (counting sortem)

def ice__cream(T):

    if not T: return 0 

    max_val = max(T)

    buckets = (max_val+1)*[]
    #Tworzymy tablicę (buckets) długości max_val + 1,
    #w której indeks i oznacza liczbę kubełków mających dokładnie i jednostek lodów.

    for vol in T: 

        buckets[vol] += 1 
    
    total = 0 

    minute = 0 

    for vol in range(max_val,0,-1): 

        #To tak, jakbyśmy przeglądali kubełki od tych z największą ilością lodów do najmniejszych.

        #Dlaczego? Chcemy najpierw zjadać największe kubełki, zanim zbyt wiele się z nich roztopi.

        while buckets[vol] > 0: 

            curr = vol - minute 
            if curr <= 0: 
                return total
            if curr > 0:

                total += curr 
                minute += 1 
                buckets[vol] -= 1 
    
    return total 

