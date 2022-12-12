# Tools for cipher machine
# by Zuowen Tang


def ifOdd(val):
    if val % 2 == 0:
        return False
    else:
        return True


# Euclidean algorithm for GCD
# For two positive integers m and n ,gcd(m,n) = gcd(n,m%n)
def gcd(m, n):
    if n == 0:
        return abs(m)
    else:
        return gcd(n, (m % n))


# Multiplicative inverse algorithm
# y is a multiplicative inverse of x % m if (xy)%m = 1
def multi_inverse(x, m):
    res = -1
    for y in range(1, m):
        if (x * y) % m == 1:
            res = y
    return res


# Fast Exponentiation Algorithm
# (x^e)%m = 0log(e)
def FastExponent(x, e, m, y=1):
    while e != 0:
        if e % 2 == 0:
            x = int((x * x) % m)
            e = int(e / 2)
        else:
            y = int((x * y) % m)
            e = int(e - 1)
    return y


# Extended euclidean Algorithm
# x*m + y*n = gcd(m,n)
def gcdExtended(m, n):
    if m == 0:
        return n, 0, 1
    gcd, x1, y1 = gcdExtended(n % m, m)
    x = y1 - (n // m) * x1
    y = x1
    return gcd, x, y

