def power2sum(n):
    power = list(str(2**n))
    return sum(int(i) for i in power)

print power2sum(1000)
