# CS789 Cryptography - Final project byZuowen Tang
import ElGamalCipherMachine
import RSACipherMachine


def Driver():
    while True:
        choice = None
        while choice is None:
            try:
                print("-------------------------------------")
                print("Which cipher machine you want to try?")
                print("(1)RSA       (2)El-Gamal      (0)Quit")
                choice = int(input())
            except ValueError:
                print("Invalid input!")
                continue
            if choice < 0 or choice > 2:
                print("Invalid input.")
                choice = None
                continue

        if choice == 1:
            RSACipherMachine.Driver()
        elif choice == 2:
            ElGamalCipherMachine.Driver()
        elif choice == 0:
            print("-------------------------------------\n")
            print("Quiting...")
            quit()


Driver()
