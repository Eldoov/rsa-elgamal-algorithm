# Miller-Rabin Primality Test byZuowen Tang
# BU-MET CS789 Cryptography
import random
from tools import basicTools
from tools import BBSrand
from tools import NRrand


def MillerRabinTest(n):
    r = 0
    m = n - 1
    while not basicTools.ifOdd(m):  # Calculate n-1 = 2^r * m, m is odd
        m = m / 2
        r += 1
    # print((n-1), "= 2^", r, "*", m)
    b = random.randint(1, n - 1)
    for k in range(0, r):
        if k == 0:
            res = basicTools.FastExponent(b, m, n)  # Calculate b^m mod n
            if res == 1 or res == (-1 % n):
                # print(n, "is (very likely) a prime number in base", b)
                return True
        else:
            res = basicTools.FastExponent(b, (2 * k) * m, n)  # Calculate b^(2k*m) mod n
            if res == (-1 % n):
                # print(n, "is (very likely) a prime number in base", b)
                return True
    # print(n, "is a composite number in base", b)
    return False


def getPrime(count, rand):
    array = [0] * count
    while count > 0:
        if rand == 0:
            num = random.randint(1000, 10000)
        elif rand == 1:
            num = NRrand.RandGen()
        elif rand == 2:
            num = BBSrand.RandGen()
        else:
            return array
        if not basicTools.ifOdd(num):
            num += 1
        if MillerRabinTest(num) and MillerRabinTest(num) and MillerRabinTest(num):
            array[count - 1] = num
            count -= 1
    return array


def getModulus(count, rand):
    arr = getPrime(count, rand)
    a = arr[0]
    b = arr[1]
    # print(a, "*", b, "=", a*b)
    return a * b, a, b

# num = int(input("How many prime numbers you want:"))
# change 2 to other numbers in order to get more or less prime numbers
# print(getModulus(2))
