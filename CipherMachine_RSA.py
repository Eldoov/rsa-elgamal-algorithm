# CS789 Cryptography
# RSA Cipher Machine by Zuowen Tang

def Encrypt(m,e):
    plaintext = int(input("The plaintext is: "))
    ciphertext = FastExponent(m,plaintext,e)
    print("Ciphertext is: ", int(ciphertext), "\n")
    driver()

def DecryptKey(m,e):
    p, q = FindFac(m)
    print("p is",p,"q is",q)
    phi_n = (p-1)*(q-1)
    print("Phi(n) is :",p,"- 1 *",q,"- 1 =", phi_n)
    d = multiinverse(e, phi_n)
    print("The decrypt key is: ", d)
    return d

def Decrypt(m,e):
    d = DecryptKey(m,e)
    ciphertext = int(input("The ciphertext is: "))
    plaintext = FastExponent(m,ciphertext,d)
    print("The plaintext is: ", plaintext, "\n")
    driver()

def FindFac(x, p=-1, q=-1):
    for y in range(1, x+1):
        res = x / y
        if (int(res)==res and isPrime(int(res)) and isPrime(y)):
            q = y
            p = int(res)
            #print(int(res), isPrime(int(res)))
    return p,q

def isPrime(x, count=0):
    for y in range(1, x+1):
        res = x / y
        if (int(res)==res):
            count += 1
    if (count == 2):
        return True
    else:
        return False

def multiinverse(x, m):
    if (m > x):
        x += m

    for y in range(x+1):
        if((x * y) % m == 1):
            k = int(((x-m) * y - 1)/m)
            res = y
            print("y is:", y, "| k is:", k)
            print(x - m, "*", y, "=", k, "*", m, "+ 1", "\n")
    return res

def FastExponent(m,x,e,y=1):
    print(x,"^",e,"%",m)
    print("x    e    y")
    print("-----------")
    print(x, " ", e, " ", y)
    while (e != 0):
        if (e % 2 == 0):
            x = int((x * x) % m)
            e = int(e / 2)
            print(x, " ", e, " ", y)
        else:
            y = int((x * y) % m)
            e = int(e - 1)
            print(x, " ", e, " ", y)
    return y


def driver():
    while True:
        print("Welcome to RSA cipher machine!")
        print("(1)Encrypt, (2)Decrypt, (3)Get Decrypt Key, (4)Quit")
        choice = int(input("Please select the fuction: "))

        if choice == 1:
            m = int(input("Enter the modulus: "))
            e = int(input("Enter the exponent: "))
            Encrypt(m, e)
        elif choice == 2:
            m = int(input("Enter the modulus: "))
            e = int(input("Enter the exponent: "))
            Decrypt(m, e)
        elif choice == 3:
            m = int(input("Enter the modulus: "))
            e = int(input("Enter the exponent: "))
            DecryptKey(m, e)
        elif choice == 4:
            print("Quiting...")
            return
        else:
            print("Invalid input.")
            continue
        return

# driver
driver()

