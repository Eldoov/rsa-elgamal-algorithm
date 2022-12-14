# CS789 Cryptography
# RSA Cipher Machine byZuowen Tang
import random
from tools import basicTools
from tools import MRprimalityTest
from tools import PRfactorFind


def isPrime(val):
    if MRprimalityTest.MillerRabinTest(val):
        print("The modulus cannot be a prime number. \n")
        return True
    else:
        return False


# Encryption Algorithm
def Encrypt(m, e):
    if isPrime(m):
        return
    plaintext = int(input("The plaintext is: "))
    ciphertext = basicTools.FastExponent(plaintext, e, m)  # Use fast exponential to get ciphertext
    print("Ciphertext is: ", int(ciphertext), "\n")


# Algorithm for decryption without private kry (d)
def Crack(m, e):
    if isPrime(m):
        return
    p, q = PRfactorFind.FindFac(m)  # Perform factorization on modulus
    if p == -1 and q == -1:  # The factorization needs to be reinitialized
        print("Quiting...")
        return -1

    phi_n = (p - 1) * (q - 1)
    gcd, x, y = basicTools.gcdExtended(phi_n, e)
    d = y % phi_n
    return d


# Decryption Algorithm
def Decrypt(m, e, with_key):
    if isPrime(m):
        return
    if with_key:
        d = e
    else:
        d = Crack(m, e)  # get decrypt key first
        if d == -1:
            return
    ciphertext = int(input("The ciphertext is: "))

    if basicTools.gcd(ciphertext, m) != 1:
        print("Ciphertext is not relatively prime to the modulus.")
        return

    plaintext = basicTools.FastExponent(ciphertext, d, m)
    print("The plaintext is: ", plaintext, "\n")


# Start the cipher machine
def Driver():
    while True:  # Loop till user quits
        choice = None
        print("-------------------------------------")
        print("   -Welcome to RSA cipher machine!-   ")
        while choice is None:
            try:
                print("(1)Encrypt (2)Decrypt (3)Crack")
                print("(4)Generate Keys (5)Autorun (0)Quit")
                choice = int(input("Please select a function: "))
            except ValueError:
                print("Invalid input. \n")
                continue
            if choice < 0 or choice > 5:
                print("Invalid input. \n")
                choice = None
                continue

        if choice == 0:
            print("\n")
            return
        elif choice == 1:
            m, e = check(1)
            Encrypt(int(m), int(e))
        elif choice == 2:
            m, e = check(2)
            Decrypt(int(m), int(e), True)
        elif choice == 3:
            m, e = check(3)
            Decrypt(int(m), int(e), False)
        elif choice == 4:
            getKey()
        elif choice == 5:
            autorun()


def getKey():
    rand_gen = None
    while rand_gen is None:
        try:
            print("Which Pseudorandom Number Generator you wish to use?")
            print(
                "(1)Naor-Reingold (2)Blum-Blum-Shub (0)python default(only for test)")
            rand_gen = int(input("Please select a generator: "))
        except ValueError:
            print("Invalid input. \n")
            continue
        if rand_gen < 0 or rand_gen > 2:
            print("Invalid input. \n")
            rand_gen = None
            continue
    m, e, d, message = genRandKey(rand_gen)
    print("Your public key is: ( m =", m, ", e =", e, ") and private key is: ( m =", m, ", d =", d, ")")
    print("Your random message is:", message, "\n")
    return m, e


def genRandKey(rand_gen):
    prv_key, pub_key, message = -1, 0, 0
    m, p, q = MRprimalityTest.getModulus(2, rand_gen)
    phi_n = (p - 1) * (q - 1)
    # print(p, "- 1 *", q,"- 1 =", (p - 1) * (q - 1))

    for i in range(0, 10):
        if basicTools.gcd(pub_key, phi_n) == 1:
            break
        else:
            pub_key = random.randint(2, phi_n)

    for i in range(0, 10):
        if basicTools.gcd(message, phi_n) == 1:
            break
        else:
            message = random.randint(1, m)

    gcd, x, y = basicTools.gcdExtended(phi_n, pub_key)
    prv_key = y % phi_n
    # print("pubkey: (", m, ",", pub_key, "), prvkey: (", m, ",", prv_key % phi_n, ")", phi_n)
    return m, pub_key, prv_key % phi_n, message


def check(choice):
    m, e = "m", "e"
    while not m.isdigit() or not e.isdigit():
        try:
            if choice == 1 or choice == 3:
                m, e = input("Enter public key m and e (split with space): ").split(
                    " ")
            else:
                m, e = input("Enter private key m and e (split with space): ").split(
                    " ")
        except ValueError:
            print("Invalid input. \n")
            continue
        if not m.isdigit() or not e.isdigit():
            print("Invalid input. \n")
            continue
    return m, e


def autorun():
    print("\nStarting autorun...")
    print("Generating random keys...")
    rand_gen = random.randint(1, 2)
    m, e, d, message = genRandKey(rand_gen)
    print("Alice's public key is: ( m =", m, ", e =", e, ")")
    print("and private key is: ( m =", m, ", d =", d, ")\n")

    print("Bob wants to send message", message, "to her.")
    print("Bob encrypts the message using Alice's public key.")

    ciphertext = basicTools.FastExponent(message, e, m)  # Use fast exponential to get ciphertext
    print("The ciphertext is", ciphertext, "\n")

    print("Alice receives the ciphertext from Bob and decrypts it with her private key.")
    plaintext = basicTools.FastExponent(ciphertext, d, m)
    print("She gets the plaintext", plaintext, "\n")

    print("Eve also knows the ciphertext Bob sends to Alice;")
    print("however she does not have the private key to decrypt the message.")
    print("She tries to crack it without private key.")
    p, q = PRfactorFind.FindFac(m)  # Perform factorization on modulus
    phi_n = (p - 1) * (q - 1)
    gcd, x, y = basicTools.gcdExtended(phi_n, e)
    d2 = y % phi_n
    print("By calculating the factor of the modulus, Eve finds", p, "and", q)
    print("which are the prime factors of the modulus", m)
    print("Eve now can have Alice's private key (", m, ",", d2, ")")
    print("and thus able to decrypt the message.")
    plaintext2 = basicTools.FastExponent(ciphertext, d2, m)
    print("Eve gets the result:", plaintext2, "\n")
    print("Autorun is finished.\n")


# Driver()
