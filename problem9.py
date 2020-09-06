
a=8
b=15
c= 17
for i in range(10):
    print(a, b, c)
    if a+b+c==1000 and a**2+ b**2== c**2:
        print(f'a= {a} b= {b} c= {c} success')
        break
    else:
        a*=5
        b*=5
        c*=5


print(a*b*c)

