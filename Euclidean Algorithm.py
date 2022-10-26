# CS789 Cryptography
# Educlidean Algorithm by Zuowen Tang
# Theorem 32: For two positive integers m and n ,gcd(m,n) = gcd(n,m%n)
def gcd(m, n):
    if(m < n):
        x = m
        m = n
        n = x
    if (n == 0 or n == 1):
        return abs(n)
    else:
        temp = int(m/n)
        print(m,"=",temp,"*",n,"+",(m % n))
        return gcd(n, (m % n))

#get intput from user
m = int(input("Please enter m: "))
n = int(input("Please enter n: "))

#print result
result = gcd(m, n)
print("The gcd of these two numbers is ", result)
if (result == 1):
    print("These two numbers are relatively prime.")
