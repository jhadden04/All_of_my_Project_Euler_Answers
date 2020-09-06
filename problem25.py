# find the index of the first fibonacci number to have 1000 digits
def fib(num):
    fibonacci = [1, 1]
    for i in range(num-1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        if (len(str(fibonacci[-1])))>= 1000:
            print((len(str(fibonacci[-1]))))
    print(fibonacci)


fib(4782)
# ans = 4782 as first one to cause an error
