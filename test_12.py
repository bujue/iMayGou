import math
def divisors(n):
    Divisors=0
    integersqrt=int(sqrt(n))
    if sqrt(n)==integersqrt:
        Divisors+=1

    for i in range(1,integersqrt-1):
        if n%i==0:
            Divisors+=2

    return Divisors

def fun():

