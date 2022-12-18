# Pollard’s Rho Factorization Algorithm byZuowen Tang
# BU-MET CS789 Cryptography
# Initiate x=2 & y=x^2 + 1, return g = gcd((x - y), n) if g != 1
# if g = 1, replace x by (x^2 + 1)%n and y by ((y^2 + 1)^2 + 1)%n, repeat
# in rare case g = n, re-initiate the algorithm
from tools import basicTools
from tools import MRprimalityTest
import random


def isPrime(n):
    if MRprimalityTest.MillerRabinTest(n):
        return True
    else:
        return False


def factor(n):
    x = 2
    y = (x**2) + 1
    for i in range(0, n):
        g = basicTools.gcd((x - y), n)
        if g != 1:
            return g
        elif g == 1:
            x = (x**2 + 1) % n
            y = ((y**2 + 1)**2 + 1) % n
        elif g == n:
            print("The algorithm needs to be reinitialized.")
            return -1


def FindFac(n):
    a = factor(n)
    if a == -1:
        return -1, -1
    b = int(n / a)
    print(a, b)
    return a, b


def FindFacRoot(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    elif n % 5 == 0:
        return 5
    a = factor(n)
    return a


# Find all prime factors
def all_factors(p):
    arr = [0] * 10
    a = p
    for i in range(0, 10):
        if isPrime(a):
            arr[i] = a
            break
        else:
            a = FindFacRoot(p)
            b = p / a
            arr[i] = a
            p = int(b)
            a = p
    return arr


# Primitive Root Search Algorithm
def pri_root_search(p):
    q = all_factors(p-1)
    x1 = [0] * 10

    for i in range(0, 10):
        b = 0
        for j in range(0, 10):
            if basicTools.gcd(b, p - 1) == 1:  # phi(p) = p-1 since p is a prime number
                break
            else:
                b = random.randint(2, p - 1)
        for k in range(len(q)):
            if q[k] != 0:
                x1[k] = int(basicTools.FastExponent(b, ((p - 1) / q[k]), p))
        if 1 not in x1:
            return b
    return -1


def check_root(num, p):
    q = all_factors(p - 1)
    x1 = [0] * 10

    for i in range(len(q)):
        if q[i] != 0:
            x1[i] = int(basicTools.FastExponent(num, ((p - 1) / q[i]), p))
    if 1 not in x1:
        return True
    else:
        return False

