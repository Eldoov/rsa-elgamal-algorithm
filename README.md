#BU MET CS789 Cryptography -Fall 2022

*Final Project by Zuowen Tang*


#### Troubleshooting

I have coded these files under PyCharm IDE and haven't tested them in other IDE, but they should work fine if all files in this folder are left untouched. 

If you have any trouble with them, please let me know; you can also choose to check them on:

- my GitHub page: https://github.com/Eldoov/CS789-Algorithms

- Replit online IDE for a direct display: https://replit.com/@Eldoov/Cipher-Machine?v=1



Thank you for reading!

---

## RSA Cipher Machine

This machine has four functions: (1)**encryption**, (2)**decryption**, (3) **decryption** without a private key, and (4) **key generation**.

By entering numbers, you should be able to choose which function you wish to use. You can choose different pseudorandom number generators for key generation or use your own key. *There's a very low chance that Naor-Reingold will get stuck, just quit the program and re-enter.*

Have fun with it.



## El-Gamal Cipher Machine

In this machine, you can be three different roles: (1)**Alice**, (2)**Bob**, or (3)**Eve**; each fits into traditional roles of computer security. 

As Alice, you can: 

- Generate public information, such as the **prime number** you wish to share with the **generator**, your **public key**, and private information as your **private key**. The machine can generate a pseudorandom number if you don't have one.
- Encrypt a message with your private key and Bob's public key. 

As Bob, you can:

- Generate public information based on info that Alice shared with you, such as your **public key** and **private key**.
- Decrypt a message with your private key and Alice's public key.

As Eve, you can:

- Try to crack Alice's and Bob's private information and their shared ciphertext. You will need all the public information to do this. You will get Alice's and Bob's private keys and the plaintext if everything works well.
