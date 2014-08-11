with open('test_13.txt') as f:
    s=[int(i.strip()) for i in f]

print i.strip()
print s
print sum(s)

b='%d'%sum(s)
print b[0:10]
