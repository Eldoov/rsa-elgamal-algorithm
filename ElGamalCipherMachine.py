# CS789 Cryptography
# El-Gamal Cipher Machine byZuowen Tang
import random
from tools import basicTools
from tools import MRprimalityTest
from tools import BBstepGNstep
from tools import BBSrand
from tools import NRrand
from tools import PRfactorFind


def alice_pub_info(rand_gen, r):
    max, b = 0, 0
    p = MRprimalityTest.getPrime(5, rand_gen)
    for i in range(0, 5):
        if p[i] > max:
            max = p[i]
    p = max

    # generate b, one of the primitive roots
    b = PRfactorFind.pri_root_search(p)

    # generate r as random number if user did not input r
    if r is None:
        r = MRprimalityTest.getPrime(1, rand_gen)
        r = r[0] % p - 1

    # calculate b^r
    br = basicTools.FastExponent(b, r, p)
    print("Public information: Alice's prime number is", p, ", generator is", b,
          ", and public number is ", br, ".")
    print("Alice's secret number is:", r, ", please keep it secret. \n")


def bob_pub_info(p, b, l):
    if l is None:
        l = MRprimalityTest.getPrime(1, 2)
        l = l[0] % p - 1

    bl = basicTools.FastExponent(b, l, p)
    print("Bob's public number is: ", bl)
    print("Bob's secret number is:", l, ", please keep it secret. \n")


def encrypt(brl, message, p):
    return (message * brl) % p


def decrypt(brl_rev, cipher, p):
    return (cipher * brl_rev) % p


def alice():
    choice = None
    while choice is None:
        try:
            choice = int(
                input("Do you wish to (1)Get public info (2)Encrypt a message: "))
        except ValueError:
            print("Invalid input. \n")
            continue
        if choice > 2 or choice < 1:
            print("Invalid input. \n")
            choice = None
            continue
    if choice == 1:
        rand = input("Enter your own secret number?(y/n) :")
        r = None
        while rand == "y" and r is None:
            try:
                r = int(input("Alice's secret number is: "))
            except ValueError:
                print("Invalid input.")
                continue
        if rand == "n":
            r = None
        alice_pub_info(2, r)
    if choice == 2:
        p = None
        while p is None:
            try:
                message = int(input("Enter the message: "))
                bl = int(input("Enter Bob's public number: "))
                r = int(input("Enter Alice's secret number: "))
                p = int(input("Enter the prime number: "))
            except ValueError:
                print("Invalid input. \n")
                continue
        brl = basicTools.FastExponent(bl, r, p)
        cipher = encrypt(brl, message, p)
        print("The ciphertext is ", cipher, "\n")


def bob():
    choice = None
    while choice is None:
        try:
            choice = int(
                input("Do you wish to (1)Get public info (2)Decrypt a message: "))
        except ValueError:
            print("Invalid input. \n")
            continue
        if choice > 2 or choice < 1:
            print("Invalid input. \n")
            continue
    if choice == 1:
        print("Enter Alice's public info below (split with space) ")
        p, b, br = "p", "b", "br"
        while not p.isdigit() or not b.isdigit() or not br.isdigit():
            try:
                p, b, br = input("Prime number, generator, public number: ").split(" ")
            except ValueError:
                print("Invalid input. \n")
                continue
            if not p.isdigit() or not b.isdigit() or not br.isdigit():
                print("Invalid input. \n")
                continue

        # check if p is prime
        if not MRprimalityTest.MillerRabinTest(int(p)):
            print(p, "is not a prime number.\n")
            return
        # check b if primitive root
        if not PRfactorFind.check_root(b, p):
            print(b, "is not a primitive root of", p, "\n")
            return

        rand = None
        while rand is None:
            try:
                rand = input("Enter your own secret number?(y/n) :")
            except ValueError:
                print("Invalid input. \n")
                continue
            if choice != "y" or "n":
                print("Invalid input. \n")
                continue
        l = None
        while rand == "y" and l is None:
            try:
                l = int(input("Bob's secret number is: "))
            except ValueError:
                print("Invalid input.")
                continue
        if rand == "n":
            l = None
        bob_pub_info(int(p), int(b), l)
    elif choice == 2:
        p = None
        while p is None:
            try:
                cipher = int(input("Enter the ciphertext: "))
                br = int(input("Enter Alice's public number: "))
                l = int(input("Enter Bob's secret number: "))
                p = int(input("Enter the prime number: "))
            except ValueError:
                print("Invalid input.")
                continue
        brl = basicTools.FastExponent(br, l, p)
        gcd, x, y = basicTools.gcdExtended(p, brl)
        brl_rev = y % p
        message = decrypt(brl_rev, cipher, p)
        print("The message is ", message, "\n")


def eve():
    p = None
    while p is None:
        try:
            cipher = int(input("Enter the ciphertext: "))
            b = int(input("Enter the generator: "))
            br = int(input("Enter Alice's public number: "))
            bl = int(input("Enter Bob's public number: "))
            p = int(input("Enter the prime number: "))
        except ValueError:
            print("Invalid input.")
            continue

    # check b if primitive root
    if not PRfactorFind.check_root(b, p):
        print(b, "is not a primitive root of", p, "\n")
        return

    # Get private keys
    r = BBstepGNstep.Driver(br, b, p)
    l = BBstepGNstep.Driver(bl, b, p)

    # Crack the ciphertext
    brl = basicTools.FastExponent(br, l, p)
    gcd, x, y = basicTools.gcdExtended(p, brl)
    brl_rev = y % p
    message = decrypt(brl_rev, cipher, p)

    print("Alice's secret number is: ", r)
    print("Bob's secret number is: ", l)
    print("The message is: ", message, "\n")


def Driver():
    while True:
        role = None
        print("-------------------------------------")
        print("-Welcome to El-Gamal Cipher Machine!-")
        while role is None:
            try:
                role = int(input("You are (1)Alice (2)Bob (3)Eve (4)Autorun (0)Quit: "))
            except ValueError:
                print("Invalid input. \n")
                continue
            if role > 4 or role < 0:
                print("Invalid input. \n")
                role = None
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
            autorun()
            continue
        elif role == 0:
            print("\n")
            return


def autorun():
    max, b = 0, 0
    rand_gen = random.randint(1, 2)
    print("\nStarting autorun...")
    print("Generating random prime number...")
    p = MRprimalityTest.getPrime(5, rand_gen)
    for i in range(0, 5):
      if p[i] > max:
        max = p[i]
    p = max

    # generate primitive root b
    b = PRfactorFind.pri_root_search(p)

    # generate r and l as random numbers
    r = MRprimalityTest.getPrime(1, rand_gen)
    r = r[0] % p - 1
    l = MRprimalityTest.getPrime(1, rand_gen)
    l = l[0] % p - 1

    # calculate b^r
    br = basicTools.FastExponent(b, r, p)
    bl = basicTools.FastExponent(b, l, p)
    brl = basicTools.FastExponent(br, l, p)
    gcd, x, y = basicTools.gcdExtended(p, brl)
    brl_rev = y % p

    print("Alice and Bob both agreed on prime number", p, "and the generator", b)
    print("Alice chooses her secret number", r, "and calculates", br)
    print("Bob chooses his secret number", l, "and calculates", bl, "\n")
    print("--------------------------")
    print("The public knowledge are")
    print("Prime number:", p)
    print("The generator:", b)
    print("Alice's public number:", br)
    print("Bob's public number:", bl)
    print("--------------------------")
    print("The private knowledge are")
    print("Alice's secret number:", r)
    print("Bob's secret number:", l)
    print("Alice and Bob both share the key:", brl)
    print("And the multi-inverse of the key:", brl_rev)
    print("--------------------------\n")
    print("Now Alice and Bob can share messages between them.\n")

    if rand_gen == 1:
        message = NRrand.RandGen()
    elif rand_gen == 2:
        message = BBSrand.RandGen()
    print("Alice wants to send the message:", message, "to Bob.")
    cipher = (message * brl) % p
    plain = (cipher * brl_rev) % p
    print("She does the calculation:", message, "*", brl, "mod", p, "=", cipher)
    print("Bob receives the cipher and does the calculation:", cipher, "*", brl_rev, "mod", p, "=", plain)
    print("They successfully exchanged information.\n")

    print("Eve also knows the public information and the ciphertext.")
    print("She will try to crack it without knowing the secret numbers.")
    print("She is trying...(usually under 10 sec with a 24-bit number)")
    r2 = BBstepGNstep.Driver(br, b, p)
    l2 = BBstepGNstep.Driver(bl, b, p)
    plaintext2 = decrypt(brl_rev, cipher, p)
    print("By using Baby-Step&Giant-Step, Eve tries to solve the problem.")
    print("She now has the secret numbers:", r2, "and", l2)
    print("With that, she is able to get the plaintext:", plaintext2, "\n")
    print("Autorun is finished.\n")


# Driver()
