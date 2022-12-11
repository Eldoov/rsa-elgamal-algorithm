# Pollard’s Rho Factorization Algorithm
# CS789 Zuowen Tang


def gcd(m, n):
    if n == 0:
        return abs(m)
    else:
        return gcd(n, (m % n))


def factor(n):
    x = 2
    y = (x**2) + 1
    for i in range(0, n):
        g = gcd((x - y), n)
        if g != 1:
            return g
        elif g == 1:
            x = (x**2 + 1) % n
            y = ((y**2 + 1)**2 + 1) % n
        elif g == n:
            print("The algorithm needs to be reinitialized.")
            return


def Driver(n):
    a = factor(n)
    b = int(n / a)
    print(a, "*", b, "=", n)


Driver(10303)
