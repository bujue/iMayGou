def Fibo(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return Fibo(n-1)+Fibo(n-2)

n=0
sum=0
while Fibo(n)<4000000:
    if Fibo(n)%2==0:
        sum=sum+Fibo(n)
    n=n+1

print sum

