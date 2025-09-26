#Cieżarówka chce przejechać z punktu a do punktu b 

# Są punkty boczne i punkty przesiadkowe 

# Jest dwóch kierowców - J i M 

# Z punktu A rusza J 

#Kierowcy muszą się najpóźniej zamianiać na 3 punkcie przesiadkowym od ostatniej zmiany 

#Marian ma być za kierownicą w przypadku mijania jak najmniejszej liczby punktów kontrolnych 


def process_input(P): 

    n = len(P)

    P = [(P[0][i], P[1][i], i) for i in range(n)]

    P.sort()

    checkpoints= [0] # Liczba punktów kontrolnych do punktu przesiadki o indeksie i 
    transfer_indexes_map = [-1]
    controls_counter = 0 

    for x, is_transfer, i in P: 

        if is_transfer:

            checkpoints.append(controls_counter)
            transfer_indexes_map.append(i)

        else: 
            controls_counter += 1 
        
    checkpoints.append(controls_counter)
    transfer_indexes_map.append(-1)

    return checkpoints, transfer_indexes_map

from math import inf


M = 0
J = 1


def process_input(P):
    n = len(P)

    P = [(P[i][0], P[i][1], i) for i in range(n)]
    P.sort()

    checkpoints = [0] # Liczba punktów kontrolnych do punktu przesiadki o indeksie `i`
    transfers_indexes_map = [-1] # Mapa indeksów z naszych indeksów, na oryginalne.
    controls_counter = 0

    for x, is_transfer, i in P:
        if is_transfer:
            checkpoints.append(controls_counter)
            transfers_indexes_map.append(i)
        else:
            controls_counter += 1

    checkpoints.append(controls_counter)
    transfers_indexes_map.append(-1)

    return checkpoints, transfers_indexes_map

def drivers(P,B): 
    
    checkpoints, transfer_indexes_map = process_input(P)
    n = len(checkpoints)


    #dp[i][M] – minimalna liczba punktów kontrolnych, 
    #które Marian przejedzie zaczynając od punktu przesiadkowego i, jeśli on teraz prowadzi.

    #dp[i][J] – analogicznie, dla Jacka.
    dp = [[inf,inf] for _ in range(n)]
    sol = [[-1,-1] for _ in range(n)]

    #sol[i][M] – który przystanek wybrano jako następny dla Mariana (do rekonstrukcji rozwiązania).
    # sol[i][J] – to samo dla Jacka.
    




def drivers(P, _):
    # Przetworzenie danych

    checkpoints, transfers_indexes_map = process_input(P)
    n = len(checkpoints)

    # Dynamic Programming

    dp = [[inf, inf] for _ in range(n)]
    sol = [[-1, -1] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for k in range(1, 4):
            alt_m = dp[i + k][J] + (checkpoints[i + k] - checkpoints[i]) if i + k < n \
                    else checkpoints[n - 1] - checkpoints[i]

            if alt_m < dp[i][M]:
                dp[i][M] = alt_m
                sol[i][M] = i + k

            alt_j = dp[i + k][M] if i + k < n \
                    else 0

            if alt_j < dp[i][J]:
                dp[i][J] = alt_j
                sol[i][J] = i + k

    # Odczytanie wyniku

    ans = []
    driver = J
    stop = sol[0][driver]

    while stop < n and transfers_indexes_map[stop] > -1:
        ans.append(transfers_indexes_map[stop])
        driver = M if driver == J else J
        stop = sol[stop][driver]

    return ans

