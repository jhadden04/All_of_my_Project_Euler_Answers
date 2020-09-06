# sum of digits of 2**1000
num = str((2**10000))
# print(num)
x = 0
total = 0
for i in range(len(num)):
    total += int(num[x])
    x += 1
print(total)