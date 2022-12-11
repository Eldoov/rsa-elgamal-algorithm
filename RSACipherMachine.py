# CS789 Cryptography
# RSA Cipher Machine by Zuowen Tang

def Encrypt(m, e):
    plaintext = int(input("The plaintext is: "))
    ciphertext = FastExponent(m, plaintext, e)
    print("Ciphertext is: ", int(ciphertext), "\n")
    Driver()


def DecryptKey(m, e):
    p, q = FindFac(m)
    print("p is", p, "q is", q)
    phi_n = (p-1)*(q-1)
    print("Phi(n) is :", p, "- 1 *", q, "- 1 =", phi_n)
    d = multi_inverse(e, phi_n)
    print("The decrypt key is: ", d)
    return d


def Decrypt(m, e):
    d = DecryptKey(m, e)
    ciphertext = int(input("The ciphertext is: "))
    plaintext = FastExponent(m, ciphertext, d)
    print("The plaintext is: ", plaintext, "\n")
    Driver()


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


def FindFac(n):
    a = factor(n)
    b = int(n / a)
    return a, b


def multi_inverse(x, m):
    if m > x:
        x += m
    for y in range(x+1):
        if(x * y) % m == 1:
            k = int(((x-m) * y - 1)/m)
            res = y
            print("y is:", y, "| k is:", k)
            print(x - m, "*", y, "=", k, "*", m, "+ 1", "\n")
    return res


def FastExponent(m, x, e, y=1):
    while e != 0:
        if e % 2 == 0:
            x = int((x * x) % m)
            e = int(e / 2)
        else:
            y = int((x * y) % m)
            e = int(e - 1)
    return y


def Driver():
    while True:
        print("Welcome to RSA cipher machine!")
        print("(1)Encrypt, (2)Decrypt, (3)Get Decrypt Key, (4)Quit")
        choice = int(input("Please select a function: "))
        if choice == 4:
            print("Quiting...")
            return
        elif choice != 1 or 2 or 3:
            print("Invalid input. \n")
            continue
        else:
            m = int(input("Enter the modulus: "))
            e = int(input("Enter the exponent: "))
        if choice == 1:
            Encrypt(m, e)
        elif choice == 2:
            Decrypt(m, e)
        elif choice == 3:
            DecryptKey(m, e)


Driver()

