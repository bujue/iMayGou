def fun():
    a=3
    b=5
    c=a+b
    sum=2
    while c<=4000000:
        sum=sum+c
        a=c+b
        b=a+c
        c=a+b
    return sum

print fun()
