import math
x = str(math.factorial(100))
l= 0
total= 0
for i in range(len(x)):
    total+=int(x[l])
    l+=1
print(total)
