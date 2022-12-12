# CS789 Cryptography
# Baby-step Giant-step Algorithm by Zuowen Tang
import math
from tools import basicTools
# b^l ≡ a % n, find l
# l = log(base:b)a


def Driver(a, b, n):
    size = n - 1
    m = math.sqrt(size)
    if m == int(m):
        m = int(m)
    else:
        m = int(m + 1)

    # initiate arrays for algorithm
    bbstep = [-1] * m
    gnstep = [-1] * m

    # Baby-step
    for j in range(m):
        b1 = (b ** j) % n
        bbstep[j] = b1
    inv = basicTools.multi_inverse(b, n)
    c = basicTools.FastExponent(inv, m, n)

    # Giant-step
    for i in range(m):
        x = a * (c ** i) % n
        gnstep[i] = x
    count = 0
    l = 0
    for k in range(m):
        for h in range(m):
            if bbstep[k] == gnstep[h]:
                count += 1
                l = (h * m) + k
    return l


# print(Driver(3305, 1785, 21773))