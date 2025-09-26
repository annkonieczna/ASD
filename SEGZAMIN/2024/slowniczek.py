def fib(n):

    cache = {0:0,1:1}

    def fib_aux(n):

        if n in cache: 
            return cache[n]
        else:
            cache[n] = fib_aux(n-1) + fib_aux(n-2)
            return cache[n]
    
    return fib_aux(n)


print(fib(100))







