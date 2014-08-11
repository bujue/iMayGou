s=[]
def route(n):
    for i in range(1,n+2):
        s.append(range(i))
    print s

    for i in range(1,n+1):
        s[0][0]=1
        s[i][0]=1
        for j in range(1,i):
            s[i][j]=s[i][j-1]+s[i-1][j]
        s[i][i]=2*s[i][i-1]
    return s[n][n]

print route(2)





