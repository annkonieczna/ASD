from egz1btesty import runtests
from math import inf
def planets( D, C, T, E ):
    n = len(C)
    dp = [[inf]*(E+1) for _ in range(n)]
    dp[0][0] = 0 
    for planet in range(n):
        for fuel in range(E+1): 
            if planet > 0:
                #przelot z planety i-1 do i 
                distance = D[planet] - D[planet-1]
                #jeżeli przed przelotem mieliśmy distance + fuel paliwa, to po przelocie, który zużywa distance 
                #zostało nam fuel 
                #zatem musimy spojrzeć na dp[planet-1][fuel+distance] i przepisujemy ją do wartości dp[plantet][fuel]
                #jeśli jest lepsza 
                if fuel + distance <= E: 
                    dp[planet][fuel] = min(dp[planet][fuel],dp[planet-1][distance+fuel])

            if fuel > 0: 
                    #patrzymy czy opłaca nam się kupić jedną tonę paliwa na tej samej planecie 
                    dp[planet][fuel] = min(dp[planet][fuel],dp[planet][fuel-1] + C[planet])
            else: 
                    #obsługujemy przypadek gdy fuel== 0 i możemy skorzystać z teleportacji 
                    dp[T[planet][0]][fuel] = min(dp[T[planet][0]][fuel],dp[planet][fuel]+T[planet][1])
    return min(dp[n-1])



    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
