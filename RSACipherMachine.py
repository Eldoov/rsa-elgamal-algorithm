# CS789 Cryptography
# RSA Cipher Machine byZuowen Tang
import random

from tools import basicTools
from tools import MRprimalityTest
from tools import PRfactorFind


# Encryption Algorithm
def Encrypt(m, e):
    plaintext = int(input("The plaintext is: "))
    ciphertext = basicTools.FastExponent(plaintext, e, m)  # Use fast exponential to get ciphertext
    print("Ciphertext is: ", int(ciphertext), "\n")


# Algorithm for decryption without private kry (d)
def Crack(m, e):
    p, q = PRfactorFind.FindFac(m)  # Perform factorization on modulus

    if p == -1 and q == -1:  # The factorization needs to be reinitialized
        print("Quiting...")
        return 0

    phi_n = (p - 1) * (q - 1)
    gcd, x, y = basicTools.gcdExtended(phi_n, e)
    d = y % phi_n
    return d


# Decryption Algorithm
def Decrypt(m, e, with_key):
    if with_key:
        d = e
    else:
        d = Crack(m, e)  # get decrypt key first
    ciphertext = int(input("The ciphertext is: "))
    plaintext = basicTools.FastExponent(ciphertext, d, m)
    print("The plaintext is: ", plaintext, "\n")


# Start the cipher machine
def Driver():
    while True:  # Loop till user quits
        choice = None
        while choice is None:
            try:
                print("Welcome to RSA cipher machine!")
                print("(1)Encrypt, (2)Decrypt, (3)Crack, (4)Quit")
                choice = int(input("Please select a function: "))
            except ValueError or choice != 1 or choice != 2 or choice != 3:
                print("Invalid input. \n")
                continue
        if choice == 4:
            print("Quiting...")
            return
        elif 0 < choice < 4:
            if choice == 1:
                m, e = randMod(None, 1)
                Encrypt(m, e)
            elif choice == 2:
                m, e = randMod("n", 2)
                Decrypt(m, e, True)
            elif choice == 3:
                m, e = randMod("n", 3)
                Decrypt(m, e, False)


def randMod(rand_mod, choice):
    while rand_mod is None:
        try:
            rand_mod = input("Do you want to generate a pair of keys (y/n)? ")
        except ValueError or rand_mod != "y" or rand_mod != "n":
            print("Invalid input. \n")
            continue

    if rand_mod == "y":
        rand_gen = None
        while rand_gen is None:
            try:
                print("Which Pseudorandom Number Generator you wish to use?")
                print("(1)Naor-Reingold (2)Blum-Blum-Shub (0)python default(only for test)")
                rand_gen = int(input("Please select a generator: "))
            except ValueError or rand_gen != 0 or rand_gen != 1 or rand_gen != 2:
                print("Invalid input. \n")
                continue
        m, e, d = genRandKey(rand_gen)
        print("Your public key is: (", m, e, ") and private key is: (", m, d, ")")
        return m, e

    while rand_mod == "n":
        try:
            if choice == 1 or choice == 2:
                m, e = input("Enter private key (split with space): ").split(" ")
                m, e = int(m), int(e)
            if choice == 3:
                m, e = input("Enter public key (split with space): ").split(" ")
                m, e = int(m), int(e)
            return m, e
        except ValueError:
            print("Invalid input. \n")
            continue


def genRandKey(rand_gen):
    prv_key, pub_key = -1, 0
    count = 0
    m, p, q = MRprimalityTest.getModulus(2, rand_gen)
    phi_n = (p - 1) * (q - 1)
    # print(p, "- 1 *", q,"- 1 =", (p - 1) * (q - 1))

    for i in range(0, 10):
        if basicTools.gcd(pub_key, phi_n) == 1:
            break
        else:
            pub_key = random.randint(2, phi_n)

    gcd, x, y = basicTools.gcdExtended(phi_n, pub_key)
    prv_key = y % phi_n
    # print("pubkey: (", m, ",", pub_key, "), prvkey: (", m, ",", prv_key % phi_n, ")", phi_n)
    return m, pub_key, prv_key % phi_n


Driver()
