with open('test_11.txt') as f:
    s=[i.split() for i in f]
s=[[int(j) for j in i] for i in s]
#s=[[int(j) for j in s[i]] for i in range(20)]
#for i in range(20):
   # s[i]=[int(j) for j in s[i]]

max=0
for i in range(20):
    for j in range(17):
        pro=s[i][j]*s[i][j+1]*s[i][j+2]*s[i][j+3]
        if pro>max:
            max=pro
        pro=s[j][i]*s[j+1][i]*s[j+2][i]*s[j+3][i]
        if pro>max:
            max=pro

for i in range(17):
    for j in range(17):
        pro=s[i][j]*s[i+1][j+1]*s[i+2][j+2]*s[i+3][j+3]
        if pro>max:
            max=pro

for i in range(3,20):
    for j in range(17):
        pro=s[i][j]*s[i-1][j+1]*s[i-2][j+2]*s[i-3][j+3]
        if pro>max:
            max=pro

print max
