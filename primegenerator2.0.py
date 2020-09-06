# Find the sum of all the primes below two million. 142913828922
# take a big divisible number
# Python Program to find prime numbers in a range
import time

start = time.process_time()


def approach3(givennumber):
    primes = []
    total = 0
    for possiblePrime in range(2, givennumber + 1):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            total += possiblePrime
            primes.append(possiblePrime)

    return primes


print(approach3(10000000))
print(f'{time.process_time() - start} seconds')
