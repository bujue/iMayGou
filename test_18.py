with open('test_18.txt') as f:
    S = [i.split() for i in f]
    S = [[int(j) for j in i] for i in S]


for i in range(len(S)-1)[::-1]:
    for j in range(i+1):
        S[i][j] += max(S[i+1][j],S[i+1][j+1])

print S[13][12],S[13][13],S[12][12]
print S[0][0]

