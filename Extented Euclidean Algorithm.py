# CS789 Cryptography
# Extended euclidean Algorithm by Zuowen Tang
# x*m + y*n = gcd(m,n)

def gcdExtended(m, n):
	if m == 0:
		return n, 0, 1
	gcd, x1, y1 = gcdExtended(n % m, m)

	x = y1 - (n // m) * x1
	y = x1
	print(n, "* (", y, ") +", m, "* (", x, ") =", gcd)

	return gcd, x, y


m = int(input("Please enter m: "))
n = int(input("Please enter n: "))

gcd, x, y = gcdExtended(m, n)
print("x is",x," and y is", y)
