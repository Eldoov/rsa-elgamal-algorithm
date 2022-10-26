# CS789 Cryptography
# Baby-step Giant-step Algorithm by Zuowen Tang
import math
# b^l ≡ a % n, find l
# l = log(base:b)a

def multiinverse(x, m):
    count = 0
    if (m > x):
        x += m
    for y in range(x+1):
        if((x * y) % m == 1 and count == 0):
            res = y
            k = int(((x - m) * y - 1) / m)
            print(x - m, "*", y, "=", k, "*", m, "+ 1")
            count += 1
    return res

def fastpower(x, e, m):
    y = 1
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

a = int(input("a:"))
b = int(input("b:"))
n = int(input("n:")) # assume n is a prime number

size = n-1
m = math.sqrt(size)

if (m == int(m)):
    m = int(m)
else:
    m = int(m+1)

print("m is",m)

# initiate arrays for algorithm
bbstep = [-1] * m
gnstep = [-1] * m

# Baby-step
print("    Baby Step    ")
print("------------------")
for j in range(m):
    b1 = (b ** j)%n
    print("j=",j," | ",b,"^",j,"=",b1)
    bbstep[j] = b1

print(bbstep, "\n")

inv = multiinverse(b,n)
print("The multi inverse of",b,"mod",n,"is:", inv)
print("Calculate", inv,"^",m,"mod",n,"to find c")
c = fastpower(inv, m, n)
print("c is", c, "\n")

# Giant-step
print("    Giant Step:    ")
print("--------------------")
for i in range(m):
    x = a * (c ** i)%n
    print("i =",i," |  x =",(c ** i),"*",a,"=",x)
    gnstep[i] = x

print(gnstep,"\n")

count = 0
l = 0
for k in range(m):
    for h in range(m):
        if(bbstep[k] == gnstep[h]):
            print("j =",k,"and i =", h)
            #print(bbstep[k],gnstep[h])
            count += 1
            l = (h*m)+k
            print("l =", h, "*", m, "+", k, "=",l)

print("\nThere is/are total", count,"of match(es).")
print("l is",l)
print(b,"^",l,"≡", a, "mod", n)
