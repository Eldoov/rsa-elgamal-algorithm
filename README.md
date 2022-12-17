*BU MET CS789 Cryptography -Fall 2022*

*Final Project by Zuowen Tang*



### <u>To run the program:</u> 

​	Load the entire <u>CipherMachine</u> folder in your IDE and run <u>**main.py**</u>



The default bits of a random number generator are 24 bits. You may try to a larger number for testing; however, this WILL increase the calculation time.



## RSA Cipher Machine

This machine has five functions: (1)**encryption**, (2)**decryption**, (3) **decryption** without a private key, (4) **key generation**, and (5) **autorun**.

By entering numbers, you should be able to choose which function you wish to use. You can choose different pseudorandom number generators for the key generation or use your own key. *There's a very low chance that Naor-Reingold will get stuck; just quit the program and re-enter.*

The autorun function can show how the encryption and decryption go under a random situation. Please check the samples for further details.

Have fun with it.



## El-Gamal Cipher Machine

In this machine, you can be three different roles: (1)**Alice**, (2)**Bob**, (3)**Eve**, or (4)**Autoran**; each fits into traditional roles of computer security. 

As Alice, you can: 

- Generate public information, such as the **prime number** you wish to share with the **generator**, your **public key**, and private information as your **private key**. The machine can generate a pseudorandom number if you don't have one.
- Encrypt a message with your private key and Bob's public key. 

As Bob, you can:

- Generate public information based on info that Alice shared with you, such as your **public key** and **private key**.
- Decrypt a message with your private key and Alice's public key.

As Eve, you can:

- Try to crack Alice's and Bob's private information and their shared ciphertext. You will need all the public information to do this. You will get Alice's and Bob's private keys and the plaintext if everything works well.



The **autorun** function can show how the encryption and decryption go under a random situation. Please check the samples for further details.

***Note:** In autorun, Eve usually spends less than 10 sec to crack a 24-bit random key. With a larger number, Eve will need more time to crack the key and might not success.*



---

### Troubleshooting

I have coded these files under PyCharm IDE and haven't tested them in other IDE, but they should work fine if all files in this folder are left untouched. 

If you have any trouble with them, please let me know; you can also choose to check them on :

- My GitHub page: https://github.com/Eldoov/rsa-elgamal-algorithm

- Replit online IDE for a direct display: https://replit.com/@Eldoov/Cipher-Machine?v=1



Thank you for reading!
