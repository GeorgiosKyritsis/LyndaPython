__author__ = 'inamoto21'


def isprime(n):  # Utility Function
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def primes(n = 1):  # Generator Function
    while True:
        if isprime(n):
            yield n  # Returns an iterator object
        n += 1

for n in primes():
    if n > 100: break
    print(n)