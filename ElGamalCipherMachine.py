# CS789 Cryptography
# El-Gamal Cipher Machine byZuowen Tang
import random
from tools import basicTools
from tools import MRprimalityTest
from tools import BBstepGNstep


def alice_pub_info(rand_gen, r):
    b = 0
    p = [0]
    while p[0] < 1000:  # get a prime number larger than 100
        p = MRprimalityTest.getPrime(1, rand_gen)
    p = p[0]  # p is a prime number

    # generate b, one of the primitive roots
    for i in range(0, 10):
        if basicTools.gcd(b, p - 1) == 1:  # phi(p) = p-1 since p is a prime number
            break
        else:
            b = random.randint(2, p)

    # generate r as random number if user did not input r
    if r is None:
        r = MRprimalityTest.getPrime(1, rand_gen)
        r = r[0] % p - 1

    # calculate b^r
    br = basicTools.FastExponent(b, r, p)
    print("Public information: Alice's prime number is", p, ", generator is", b, ", and public key is ", br, ".")
    print("Alice's private key is:", r, ", please keep it secret. \n")


def bob_pub_info(p, b, l):
    if l is None:
        l = MRprimalityTest.getPrime(1, 2)
        l = l[0] % p - 1

    bl = basicTools.FastExponent(b, l, p)
    print("Bob's public key is: ", bl)
    print("Bob's private key is:", l, ", please keep it secret. \n")


def encrypt(brl, message, p):
    return (message * brl) % p


def decrypt(brl_rev, cipher, p):
    return (cipher * brl_rev) % p


def alice():
    choice = None
    while choice is None:
        try:
            choice = int(input("Do you wish to (1)Get public info (2)Encrypt a message: "))
        except ValueError or choice != 1 or choice != 2:
            print("Invalid input. \n")
            continue
    if choice == 1:
        r = input("Enter your own random number?(y/n) :")
        if r == "y":
            r = int(input("Alice's random number is: "))
        if r == "n":
            r = None
        alice_pub_info(2, r)
    if choice == 2:
        message = int(input("Enter the message: "))
        bl = int(input("Enter Bob's public key: "))
        r = int(input("Enter Alice's private key: "))
        p = int(input("Enter the prime number: "))
        brl = basicTools.FastExponent(bl, r, p)
        cipher = encrypt(brl, message, p)
        print("The ciphertext is ", cipher, "\n")


def bob():
    choice = None
    while choice is None:
        try:
            choice = int(input("Do you wish to (1)Get public info (2)Decrypt a message: "))
        except ValueError or choice != 1 or choice != 2:
            print("Invalid input. \n")
            continue
    if choice == 1:
        print("Enter Alice's public info below (split with space) ")
        p = None
        while p is None:
            try:
                p, b, br = input("Prime number, generator, public key: ").split(" ")
            except ValueError:
                print("Invalid input. \n")
                continue
        if not MRprimalityTest.MillerRabinTest(int(p)):
            print(p, "is not a prime number.\n")
            return
        l = None
        while l is None:
            try:
                l = input("Enter your own random number?(y/n) :")
            except ValueError or choice != "y" or choice != "y":
                print("Invalid input. \n")
                continue
        if l == "y":
            l = int(input("Bob's random number is: "))
        if l == "n":
            l = None
        bob_pub_info(int(p), int(b), l)
    elif choice == 2:
        cipher = int(input("Enter the ciphertext: "))
        br = int(input("Enter Alice's public key: "))
        l = int(input("Enter Bob's private key: "))
        p = int(input("Enter the prime number: "))
        brl = basicTools.FastExponent(br, l, p)
        gcd, x, y = basicTools.gcdExtended(p, brl)
        brl_rev = y % p
        message = decrypt(brl_rev, cipher, p)
        print("The message is ", message, "\n")


def eve():
    cipher = int(input("Enter the ciphertext: "))
    b = int(input("Enter the generator: "))
    br = int(input("Enter Alice's public key: "))
    bl = int(input("Enter Bob's public key: "))
    p = int(input("Enter the prime number: "))

    # Get private keys
    r = BBstepGNstep.Driver(br, b, p)
    l = BBstepGNstep.Driver(bl, b, p)

    # Crack the ciphertext
    brl = basicTools.FastExponent(br, l, p)
    gcd, x, y = basicTools.gcdExtended(p, brl)
    brl_rev = y % p
    message = decrypt(brl_rev, cipher, p)

    print("Alice's private key is: ", r)
    print("Bob's private key is: ", l)
    print("The secret message is: ", message, "\n")


def Driver():
    while True:
        role = None
        while role is None:
            try:
                print("Welcome to El-Gamal Cipher Machine!")
                role = int(input("You are (1)Alice (2)Bob (3)Eve (4)Quit: "))
            except ValueError or role != 1 or role != 2 or role != 3 or role != 4:
                print("Invalid input. \n")
                continue
        if role == 1:
            alice()
            continue
        elif role == 2:
            bob()
            continue
        elif role == 3:
            eve()
            continue
        elif role == 4:
            print("Quiting...")
            return


Driver()
