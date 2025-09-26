#Idea 
#Sortowanie przez wstawianie.
#Działa podobnie jak porządkowanie kart do gry: bierzesz następny element (kartę), 
# porównujesz go z już posortowaną częścią po lewej i „wstawiasz” go w odpowiednie miejsce, 
# przesuwając większe elementy o jedno miejsce w prawo

#Złożoność:
#  O(n) w najlepszym 
#O(n^2) w najgorszym

def insertion_sort(T): 

    n = len(T)

    if n <= 1:
        return T 
    for i in range(1,n): #elementy na lewo od i są już zawsze posortowane 
        key = T[i] #element, który chcemy wstawić 
        j = i-1 #zaczynam porównywać z elementem, który jest obok 
        while j >= 0 and T[j] > key: 
            T[j+1] = T[j]
            j -= 1 
        T[j+1] = key
    return T

T = [0, -15, 2, 8, 12, 24, -90, 112, 5]
print(insertion_sort(T))


