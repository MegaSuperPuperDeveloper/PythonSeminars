# Задача №31. Сделайте программу, последовательность Фибоначчи

def fib(n):
    if n < 3: 
        return n
    return fib(n-1) + fib(n-2)

print(fib(7))