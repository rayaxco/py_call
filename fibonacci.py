def fibonacci(number):
    a=0
    b=1
    for i in range(number):
        yield a
        temp=a
        a=b
        b=temp+a

f=fibonacci(20)
for i in range(20):
    print(i,'::',next(f))
