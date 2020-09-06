# prime generator, does all primes inclusive of the number, 104743
import time
start = time.process_time()


def prime(upto):
    primenums = [2]
    n = 3
    for m in range(upto):
        for i in range(2, n):
            if n % i != 0:
                l = 'prime'
            else:
                l = 'nprime'
                break
        if l == 'prime':
            (primenums.append(n))
        n += 1
        if primenums[-1] > upto:
            del primenums[-1]
            break
    print(primenums)


prime(10000)
print(f'{time.process_time() - start} seconds')
# normal one
