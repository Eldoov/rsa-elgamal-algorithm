# Naor-Reingold Pseudorandom Number Generator
# CS789 Zuowen Tang
import random


def gcd(m, n):
    if m < n:
        x = m
        m = n
        n = x
    if n == 0 or n == 1:
        return abs(n)
    else:
        return gcd(n, (m % n))


def FastExponent(x, e, m, y=1):
    while e != 0:
        if e % 2 == 0:
            x = int((x * x) % m)
            e = int(e / 2)
        else:
            y = int((x * y) % m)
            e = int(e - 1)
    return y


def getA(n, num, x):
    arrplus = 0
    arr0 = [0] * n
    arr1 = [0] * n
    arr = [0] * n
    arrbin = [int(d) for d in str(bin(x))[2:]]
    g = findSq(num)
    for i in range(0, n):
        a = random.randint(1, num)
        b = random.randint(1, num)
        arr0[i] = a
        arr1[i] = b
    for j in range(0, n):
        if arrbin[j] == 0:
            arr[j] = arr0[j]
        if arrbin[j] == 1:
            arr[j] = arr1[j]
    for k in range(0, n):
        arrplus += arr[k]
    res = FastExponent(g, arrplus, num)
    return res


def findSq(num):
    res = 0
    sqrt = 0
    while res != 1:
        sqrt = random.randint(1, num)
        res = gcd(sqrt, num)
    sq = (sqrt ** 2) % num
    return sq


def getB(n):
    array = [0] * (2*n)
    for i in range(0, 2*n):
        rand = random.randint(0, 1)
        array[i] = str(rand)
    res = "".join(array)
    return res


def getBit(n, p, q, x):
    num = getA(n, p*q, x)
    a = str(bin(num)[2:])
    a = a.zfill(2*n)
    b = getB(n)
    array_a = [*a]
    array_b = [*b]
    array_res = [0] * (2*n)
    for i in range(0, 2*n):
        array_res[i] = int(array_a[i]) * int(array_b[i])
    res = (array_res[(2*n)-1])
    return res


def getRand(count):
    array = ["0"] * count
    for i in range(0, count):
        array[i] = str(getBit(6, 47, 37, 43))
    res = "".join(array)
    return res



def RandGen():
    bits = getRand(12)
    rand_num = int(bits, 2)
    return rand_num


# generating 12-bits long number
# n = 6, p = 37, q = 47, x = 43
print(RandGen())



