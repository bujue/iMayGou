def fun(n):
    if n%2==0:
        return False
    p=3
    while p<n**0.5+1:
        if n%p==0:
            return False
        p+=2
    return True
terms=filter(fun,xrange(2,2000000))
print sum(terms)+2
