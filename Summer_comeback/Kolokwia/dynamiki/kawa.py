"""
Podziękowania dla: Jakub Kwiecień

Idę po tablicy od prawej strony [O(n)]. Zliczam, ile jest liczb mniejszych po prawej stronie tej
rozważanej i dodaję to do licznika. Na koniec powiększam licznik na rozważanej liczbie o 1, aby
później, w kolejnej iteracji móc ją wziąć pod uwagę jako kolejną liczbę po prawej.

Złożoność: O(n*k)
"""

from kolUtesty import runtests


def kawa(T, k):
    # tu prosze wpisac wlasna implementacje
    n = len(T)

    c = [0] * (k + 1)

    counter = 0

    for i in range(n - 1, -1, -1):
        for j in range(T[i]):
            counter += c[j]
        c[T[i]] += 1
    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kawa, all_tests = True )
#1

def fib(n): 
    fib1 = 0 
    fib2 = 1 
    i = 0 
    for i in range(n-1):
        temp = fib1 
        fib1 = fib2 
        fib2 = temp + fib1 
    return fib2
#2 
from math import inf
def target(T,k): 
    n  = len(T)
    cashe = [[inf]*k for _ in range(n)]

    def recur(i,a): 
        #bierzemy element i
        new_amount = a - T[i] 
        if new_amount == 0: 
            return True 
        elif new_amount <0:
            return False
        
        else:
            recur(i+1,(a - T[i]))
        #nie bierzemy elementu i 
        recur 


def knapsack(T,k): 
    n = len(T)
    dp= [inf]*(k+1)
    dp[0] =0


    for a in range(1,k+1): 
        for c in T:
            if a-c >= 0: 
                dp[a] = min(dp[a],dp[a-c]+1)
    return dp[k]
print(knapsack([1,3,4,5],7))




         

"""
Podziękowania dla: Jakub Karczewski

Tak jak w n * k, ale zamiast tablicy liczników używam drzewa przedziałowego,
aby trzymać informacje o tym, ile jest na dany moment liczb mniejszych
w naszej tablicy po prawej stronie rozważanego elementu.

Złożoność: O(nlogk)
"""

from kolUtesty import runtests


class IntervalAdder:
    def __init__(self, n):
        self.p = 1

        while self.p < n:
            self.p *= 2

        self.T = [0 for _ in range(2 * self.p - 1)]

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get(self, i):
        return self.T[i + self.p - 1]

    def set(self, i, val):
        k = i + self.p - 1

        d = val - self.T[k]

        while k >= 0:
            self.T[k] += d

            k = self.parent(k)

    def sum_helper(self, k, lo, hi, i, j):
        if i == lo and j == hi:
            return self.T[k]

        r = (hi - lo) // 2

        if i > lo + r:
            return self.sum_helper(self.right(k), lo + r + 1, hi, i, j)
        elif j <= lo + r:
            return self.sum_helper(self.left(k), lo, lo + r, i, j)
        else:
            res1 = self.sum_helper(self.left(k), lo, lo + r, i, lo + r)
            res2 = self.sum_helper(self.right(k), lo + r + 1, hi, lo + r + 1, j)

            return res1 + res2

    def sum(self, i, j):
        if i > j:
            return 0

        return self.sum_helper(0, self.p - 1, 2 * self.p - 2, i + self.p - 1, j + self.p - 1)


def kawa(T, k):
    # tu prosze wpisac wlasna implementacje
    n = len(T)

    counter = 0

    ia = IntervalAdder(k + 1)

    for i in range(n - 1, -1, -1):
        counter += ia.sum(0, T[i] - 1)
        ia.set(T[i], ia.get(T[i]) + 1)

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kawa, all_tests = True )





    

