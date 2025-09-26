# Pewien podróżnik chce przebyć trasę z punktu A do punktu B. Niestety jego samochód spala dokładnie jeden
# litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie D litrów paliwa. Trasa jest reprezentowana
# jako graf, gdzie wierzchołki to miasta a krawędzie to łączące je drogi. Każda krawędź ma długość w
# kilometrach (przedstawioną jako liczba naturalna). W każdym wierzchołku jest stacja benzynowa, z daną ceną
# za litr paliwa. Proszę podać algorytm znajdujący trasę z punktu A do punktu B o najmniejszym koszcie.


from queue import PriorityQueue
def fuel(G,A,B,D): 

    n = len(G)
    
    P = [[float("inf") for _ in range(D+1)] for _ in range(n)]
    #Graph[v][f] zawiera minimalny koszt dotarcia do miasta v z dokładnie f litrami paliwa.

    # Wartość inf oznacza, że jeszcze nie odwiedziliśmy tego stanu.
    #Tablica Graph ma za zadanie przechowywać minimalne koszty dotarcia do każdego miasta z określoną 
    # ilością paliwa w baku. Jest to sposób na śledzenie wszystkich możliwych stanów podróży w kontekście:
    d = [float('inf')]*n

    q = PriorityQueue()
    #q: Kolejka priorytetowa, która będzie przechowywać stany w postaci krotek 
    # (koszt, ilość paliwa, miasto).
    q.put((0,0,A))
    # zaczynamy w mieście start z 0 litrami paliwa i kosztem 0

    while q.not_empty(): 

        c,f,v = q.get() # wydobywamy najtańszy stan z kolejki (koszt, paliwo, miasto)
        
        if d[v] > c: 
            d[v] = c
        for i in range(D + 1 - f):  # próbujemy dobić paliwo do pełna, aż do D litrów

            pass









