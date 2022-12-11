# Miller-Rabin Primality Test
# CS789 Zuowen Tang
import random
import NRrand
import BBSrand


def MillerRabinTest(n):
    r = 0
    m = n - 1
    while not ifOdd(m):  # Calculate n-1 = 2^r * m, m is odd
        m = m / 2
        r += 1
    # print((n-1), "= 2^", r, "*", m)
    b = random.randint(1, n - 1)
    # print("b =", b)
    for k in range(0, r):
        if k == 0:
            res = FastExponent(b, m, n)  # Calculate b^m mod n
            # print(res)
            if res == 1 or res == (-1 % n):
                print(n, "is (very likely) a prime number in base", b)
                return True
        else:
            res = FastExponent(b, (2 * k) * m, n)  # Calculate b^(2k*m) mod n
            # print(res)
            if res == (-1 % n):
                print(n, "is (very likely) a prime number in base", b)
                return True
    # print(n, "is a composite number in base", b)
    return False


def ifOdd(val):
    if val % 2 == 0:
        return False
    else:
        return True


def FastExponent(x, e, m, y=1):
    while e != 0:
        if e % 2 == 0:
            x = int((x * x) % m)
            e = int(e / 2)
        else:
            y = int((x * y) % m)
            e = int(e - 1)
    return y


def driver(count):
    while count > 0:
        num = random.randint(1000, 99999)
        # num = NRrand.RandGen()
        # num = BBSrand.RandGen()
        if not ifOdd(num):
            num += 1
        if MillerRabinTest(num) and MillerRabinTest(num) and MillerRabinTest(num):
            print(num, "\n")
            count -= 1


# num = int(input("How many prime numbers you want:"))
driver(2)
