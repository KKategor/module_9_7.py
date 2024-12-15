# Task Декораторы в Python



def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        print(n)
        k = 0
        for j in range(1, n):
            if (n % j == 0):
                k += 1
        if k <= 2:
            print('Простое')
        else:
            print('Составное')
    return wrapper

@is_prime
def sum_three(a, b , c):
    return a + b + c
result = sum_three(2, 3, 6)
