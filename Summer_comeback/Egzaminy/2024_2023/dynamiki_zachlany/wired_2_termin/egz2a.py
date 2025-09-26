from egz2atesty import runtests
#if abs(i-j)%2 == 0 nie mogą być połączone 
#warunki: i-j+1 musi być parzyste 
from math import inf

def wired( T ):
  n = len(T)
  dp = [[inf]*n for _ in range(n)] #dp[i][j] - minimalny koszt połączenia wszystkich indeksów od i do j
  
#Kolejność: najpierw rozwiążemy wszystkie przedziały długości 2 (baza), potem 4, 6, … aż do n. 
# podprzedziały są ju# To zapewnia, że gdy liczymy dp[i][j] dla dłuższego przedziału, wszystkie potrzebne krótsze są już policzone.
  for l in range(2,n+1,2): #pętla po długości przedziałów 
    
    for i in range(0,n-l+1):#pętla po lewym końcu przedziału długości l
      j= l+i-1 # prawy przedział 
      for k in range(i+1,j+1,2): #pętla, która wybiera partnera dla naszego pierwszego elementu przedziału 
        #rozpatrujemy pary (i,k) i doliczamy koszty dwóch niezależnych podproblemów 
        dp[i][j] = min(dp[i][j],
                       1+ abs(T[i]-T[k]) + # liczymy koszt przedziału od i do k 
                          (dp[i+1][k-1] if (i+1)<(k-1) else 0)+ #dodajemy do tego koszt przedziału od i+1 do k-1
                          (dp[k+1][j] if k+1 < j else 0)) #dodajemy prawy podprzedział


  return dp[0][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )
