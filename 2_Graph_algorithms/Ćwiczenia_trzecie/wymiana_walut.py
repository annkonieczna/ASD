# Dana jest tabela kursów walut. Dla każdych dwóch walut 'x' oraz 'y' wpis K[x][y] oznacza ile trzeba
# zapłacić waluty 'x' żeby otrzymać jednostkę waluty 'y'. Proszę zaproponować algorytm, który sprawdza
# czy istnieje taka waluta 'z', że za jednostkę 'z' można uzyskać więcej niż jednostkę 'z' przez serię
# wymian walut.

#dodajemy sztuczny wierzchołek 

from math import log10 
def Bellman_Ford(K): 
    n = len(K)

    


    Graph = [[-log10(K[i][j]) for j in range(n)] for i in range(n)]

    for start in range(n): 
        d = [float('inf')]*n
        d[start] = 0 

        for _ in range(n-1): #relaksacja krawędzi n-1 razy

            for u in range(n): 

                for v in range(n): 

                    if d[v] > d[u] +  Graph[u][v]: 

                        d[v] = d[u] + Graph[u][v]
        #sprawdzanie ujemnego cyklu 

        for u in range(n): 

            for v in range(n): 
                if d[u] + Graph[u][v] < d[v]:
                    return True
                
        return False
    


 


# Dana jest tabela kursów walut. Dla każdych dwóch walut 'x' oraz 'y' wpis K[x][y] oznacza ile trzeba
# zapłacić waluty 'x' żeby otrzymać jednostkę waluty 'y'. Proszę zaproponować algorytm, który sprawdza
# czy istnieje taka waluta 'z', że za jednostkę 'z' można uzyskać więcej niż jednostkę 'z' przez serię
# wymian walut.


from math import log10 

def exchange(K): 

    n = len(K)

    Graph = [[-log10(K[i][j] for j in range(n))] for i in range(n)]

    
    for start in range(n): 

        d = [float('inf')]*n
        d[start] = 0 

        
        for _ in range(n-1): 

            for u in range(n): 
                for v in range(n): 

                    if d[v] > d[u] + Graph[u][v]: 

                        d[v] = d[u] + Graph[u][v]

        for u in range(n): 

            for v in range(n): 

                if d[v] > d[u] + Graph[u][v]: 
                    return True 
        
        return False 
    





















