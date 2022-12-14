"""
Решето Эратосфена

Реализуйте алгоритм решета Эратосфена поиска простых чисел от 1 до n.
Алгоритм обрабатывает числа по очереди, для каждого нового числа проверяя
его делимость на хотя бы одно из уже найденных простых чисел.
"""


def sieve(n: int) -> list:
    """
    Функция принимает число n - верхнюю границу поиска,
    и возвращает массив простых чисел от 1 до n
    """
    primes = []
    k = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            primes.append(i)
        else:
            k = 0
    return primes
