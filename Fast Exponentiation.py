# Fast Exponentiation Algorithm by Zuowen Tang

# (x^e)%m = 0log(e)
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

print("(x^e)%m")
x = int(input("Enter x: "))
e = int(input("Enter e: "))
m = int(input("Enter m: "))
fastpower(x,e,m)




