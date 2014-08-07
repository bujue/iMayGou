import time
'''
def fun(n):
    i=2
    while i<n:
        if n%i==0:
            return False
        else:
            i+=1
    return True
'''

def fun(n):
    if n%2==0:
        return False
    p=3
    while p<n**0.5+1:
        if n%p==0:
            return False
        p+=2
    return True

def term(i):
    x=2
    index=1
    while index !=i:
        x+=1
        if fun(x)==True:
            index+=1
    return x

start=time.time()
prime=term(10001)
elapsed=(time.time()-start)

print "found %s in %s seconds"%(prime,elapsed)

