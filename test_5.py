def fuc(n):
    product=1
    list=range(1,n+1)
    for i in range(1,n):
        for j in range(i+1,n):
            if list[j]%list[i]==0:
                list[j]/=list[i]
        product*=list[i]
    return product

print fuc(20)
