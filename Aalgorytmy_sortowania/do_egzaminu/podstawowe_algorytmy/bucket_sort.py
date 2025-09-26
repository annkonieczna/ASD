#Idea: 

#Dzielimy zakres wartości tablicy na kubełki (buckety)
#Rozdzielamy elementy z tablicy do kubełków 
#Sortujemy zawartość każdego kubełka (zazwyczaj stusujemy inne proste sortowanie np insertion sort)
#Łączymy kolejne kubełki w jedną posortowaną listę 

#Główna zaleta: jeśli dane są równomiernie rozłożone i liczba kubełków jest dobrana sensownie,
#  to średni czas jest bliski O(n) (n = liczba elementów). W najgorszym wypadku (wszystko w 
# jednym kubełku) może być O(n²) — więc bucket sort daje największą korzyść przy „dobrym” 
# rozkładzie danych


def bucket_sort(T, bucket_count = None, key = None):
    if not T: 
        return []
    n = len(T)
    if bucket_count is None: 
        bucket_count = n 
    if key is None:
        key = lambda x: float(x)
#nie wiem jakieś dziwne rzeczy 
    

     
