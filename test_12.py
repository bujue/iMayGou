import math
a=1
b=1
def divisors(n):
    Divisors=0
    integersqrt=int(math.floor(math.sqrt(n)))

    if math.sqrt(n)==integersqrt:
        Divisors+=1

    for i in range(1,integersqrt):
        if n%i==0:
            Divisors+=2

    return Divisors


while b < 500:
    a+=1
    m=a*(a+1)/2
    b=divisors(m)


print a*(a+1)/2



