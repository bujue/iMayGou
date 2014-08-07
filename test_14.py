def chain(n,count=1):
    while n>1:
        count+=1
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    return count

a=0
max=0
for i in range(1000000):
    if chain(i)>max:
        max=chain(i)
        a=i

print a
