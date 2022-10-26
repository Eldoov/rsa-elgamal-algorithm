# CS789 Cryptography
# Primitive Root Search Algorithm by Zuowen Tang

def primrootsearch(p):
    q = FindFac(p-1)
    print(q)
    x1 = [0] * 10
    for b in range(1, p - 1):
        for i in range(len(q)):
            if (q[i] != 0):
                x1[i] = int(fastpower(b, ((p - 1)/q[i]), p))
        if 1 not in x1:
            print(b)


def fastpower(x, e, m):
    y = 1
    while (e != 0):
        if (e % 2 == 0):
            x = int((x * x) % m)
            e = int(e / 2)
        else:
            y = int((x * y) % m)
            e = int(e - 1)
    return y

def isPrime(x, count=0):
    for y in range(1, x+1):
        res = x / y
        if (int(res)==res):
            count += 1
    if (count == 2):
        return True
    else:
        return False

def FindFac(x):
    primedivisor = [0] * 10
    i = 0
    for y in range(1, x+1):
        res = x / y
        if (int(res)==res and isPrime(int(res))):
            print(int(res))
            primedivisor[i] = int(res)
            i += 1
    return(primedivisor)

p = int(input("Enter a prime number p:"))
if isPrime(p):
    primrootsearch(p)
else:
    print(p,"is not a prime number.")