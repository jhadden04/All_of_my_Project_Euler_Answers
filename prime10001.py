# prime generator, shows which number prime it is e.g. 3 is 2nd prime
import time
start = time.process_time()


def prime(upto):
    total = 1
    primenums = [2, '<---(1)']
    n = 3
    for m in range(upto):

        for i in range(2, n):

            if n % i != 0:
                l = 'prime'
            else:
                l = 'nprime'
                break
        if l == 'prime':
            total += 1
            (primenums.append(n))
            (primenums.append(f'<---({total})'))
        n += 1
    print(primenums)


prime(1500)
print(f'{time.process_time() - start} seconds')
