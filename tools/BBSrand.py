# Blum-Blum-Shub Pseudorandom Number Generator byZuowen Tang
# BU-MET CS789 Cryptography
import random
from tools import basicTools


def findSeed(num):
    res = 0
    seed = 0
    while res != 1:
        seed = random.randint(1, num)
        res = basicTools.gcd(seed, num)
    return seed


def getBit(n):
    array = [0] * n
    bits_array = ["0"] * n
    seed = findSeed(n)
    s0 = seed
    for i in range(0, n):
        s1 = (s0 ** 2) % n
        s0 = s1
        array[i] = s1
    for j in range(0, n):
        bits_array[j] = array[j] % 2
    res = bits_array[n-1]
    return res


def getRand(count, p, q):
    n = p * q
    array = ["0"] * count
    for i in range(0, count):
        array[i] = str(getBit(n))
    res = "".join(array)
    return res


def RandGen():
    bits = getRand(16, 11, 23)  # getRand(16bit, p, q)
    rand_num = int(bits, 2)
    return rand_num


# generating 16-bit long number
# both p & q are prime numbers that also ≡ 3%4
# In this example, p = 11, q = 23
# print(RandGen())
