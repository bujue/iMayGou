with open('test_13.txt') as f:
    s=[int(i) for i in f]
print sum(s)

b='%d'%sum(s)
print b[0:10]
