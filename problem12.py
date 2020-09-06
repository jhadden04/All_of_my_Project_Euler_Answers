# Python Program to find the factors of a number

# This function computes the factor of the argument passed
from itertools import chain, cycle, accumulate  # last of which is Python 3 only


def print_factors(n):
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2, 4]))):
            if c * c > n: break
            if n % c: continue
            d, p = (), c
            while not n % c:
                n, p, d = n // c, p * c, d + (p,)
            yield (d)
        if n > 1: yield ((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a * b for a in r for b in e]
    return len(r)
n= 0
number = 0
triangle_number= []
for i in range(1000000):
    number = number + i
    triangle_number.append(number)
while print_factors(triangle_number[n])<=500:
    print(print_factors(triangle_number[n]))
    n+=1
print(triangle_number[n])