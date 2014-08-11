S = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
D = [0,3,6,6,5,5,5,7,6,6]
H = 7

letters = 11
for i in range(1,1000):
    c = i%10
    b = (i%100-c)/10
    a = (i%1000-b*10-c)/100

    if a != 0:
        letters += S[a]+H
        if b != 0 or c !=0:
            letters +=3

    if b == 0 or b == 1:
        letters += S[b*10+c]
    else:
        letters += D[b]+S[c]

print letters





