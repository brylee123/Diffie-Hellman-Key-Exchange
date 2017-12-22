import math
import random
import getpass

def primeGen():
	prime = []
	count = 3
	while len(prime) < 1000:	# First 1000 prime numbers
		isprime = True
		for x in range(2, int(math.sqrt(count) + 1)):
			if count % x == 0: 
				isprime = False
				break
		if isprime:
			prime.append(count)
		count += 1
	return prime

def isInt(s):
	try:
		return int(s)
	except ValueError:
		return isInt(getpass.getpass("Not an integer, Try again: "))

if __name__ == "__main__":
	prime = primeGen()

	g = random.choice(prime)
	prime.remove(g)
	p = random.choice(prime)

	print("Shared g value:", g)
	print("Shared p value:", p)

	a = isInt(getpass.getpass("Hidden \"a\" value: "))
	b = isInt(getpass.getpass("Hidden \"b\" value: "))

	#print(a, b)
	A = (g**a)%p
	B = (g**b)%p

	print("##################################################\n")
	print("Calculation of shared key with \033[0;31m\"a\"\033[0m:\n")
	print("User assigned value of \033[0;31m\"a\"\033[0m is\033[0;31m", a, "\033[0m")


	print("Formula: A = g^a mod p")

	# Actual Calculation of A
	print(str(g)+"^"+str(a)+" mod "+str(p)+" =", A, "= A")

	# Received B
	print("Received \"B\" value")
	print("shared_key_a = B^a mod p")
	shared_key_a = (B**a)%p
	print(str(B)+"^"+str(a)+" mod "+str(p)+" =", shared_key_a)
	print("Shared Key Calculated from \"a\" is:", shared_key_a)

	print("\n##################################################\n")
	print("Calculation of shared key with \033[0;34m\"b\"\033[0m:\n")
	print("User assigned value of \033[0;34m\"b\"\033[0m is\033[0;34m", b, "\033[0m")


	print("Formula: B = g^b mod p")
	
	# Actual Calculation of B
	print(str(g)+"^"+str(b)+" mod "+str(p)+" =", B, "= B")

	# Received A
	print("Received \"A\" value")
	print("shared_key_b = A^b mod p")
	shared_key_b = (A**b)%p
	print(str(A)+"^"+str(b)+" mod "+str(p)+" =", shared_key_b)
	print("Shared Key Calculated from \"b\" is:", shared_key_b)

	print("\n##################################################\n")


	if shared_key_a == shared_key_b:
		print("This prompt should always print if shared_key_a is equal to shared_key_b. (Which is always)\n\n\n")



