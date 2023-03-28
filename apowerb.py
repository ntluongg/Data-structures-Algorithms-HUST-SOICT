#Divide and conquer
a,b = map(int,input().split())

def solution(): #print out (a^b) mod (10^9+7)
	print(power(a,b))

def power(a,b): #T(n) = log(n)
	if b==0:
		return 1
	x = power(a,b//2)
	remainder = a**(b%2) % (1000000007)
	return ((x**2)*remainder) % (1000000007)
	#(a x b) mod m = ((a mod m) x (b mod m)) mod m 

solution()