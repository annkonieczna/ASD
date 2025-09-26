# Mamy zbiór monet M = {1, 3, 4, 5}
# T = 7

# Chcemy minimalną liczbą monet o takich norminałach wydać kwotę 7.

# Tablica 1 wymiarowa z inf, oprócz 0 indeksu i potem wybieramy t.j. naszą kwotę.
# Iterujemy po tablicy i będziemy wybirać co raz mniejsze.

# f(x) (z def) = minimalna liczba monet do wydania kwoty x
# f(x) = min { f(x - t) + 1 }
# t - liczba naturalna

# Rekurencja ze spamiętywaniem.


#1 wersja 

# Rekurencja ze spamiętywaniem.

def change(x, M, mem, t): # używamy dicta --> to jest słownik
    if x == 0: return 0
    if x in mem: return mem[x]

    best = float('inf')

    if t <= x:
        tmp = change(x - t) + 1
        if tmp < best:
            best = tmp

    mem[x] = best
    return mem[x]

# bez tablicy wielowymiarowej - na słowniku za to (nie można tak na kolokwium)

def normal_way(M, T):
    inf = float('inf')
    F = [inf] * (T + 1)
    F[0] = 0

    for i in range(1, T + 1):
        for coin in M: # bo to zbiór monet - mogą być wykorzystywane wiele razy
            if coin <= i: # bo jak większy to bez sensu
                F[i] = min(F[i], F[i - coin] + 1)

    return F[T]

M = [1, 3, 10, 5]
T = 7
print(normal_way(M, T))










#druga wersja 
def exchange(coins, amount):
    counts = [amount + 1] * (amount + 1)
    counts[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                counts[i] = min(counts[i], counts[i - coin] + 1)
                
    #print(counts)
                
    return counts[amount] if counts[amount] <= amount else -1

coins = [2, 5]
amount = 2
print(exchange(coins, amount))