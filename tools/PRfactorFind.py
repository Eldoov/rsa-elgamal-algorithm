# Pollard’s Rho Factorization Algorithm byZuowen Tang
# BU-MET CS789 Cryptography
# Initiate x=2 & y=x^2 + 1, return g = gcd((x - y), n) if g != 1
# if g = 1, replace x by (x^2 + 1)%n and y by ((y^2 + 1)^2 + 1)%n, repeat
# in rare case g = n, re-initiate the algorithm
from tools import basicTools
from tools import MRprimalityTest


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
    return a, b

