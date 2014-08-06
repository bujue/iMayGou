factors=[]
def factor(n):
    i=2
    while i<=n:
        if n%i==0:
            factors.append(i)
            n=n/i
        else:
            i=i+1

factor(600851475143)
print max(factors)

