def solution():
	global count
	print(''.join(x))
	count +=1

def check(k,v):
	if k==0:
		return True
	if x[k-1] == "1" and v == "1":
		return False
	return True

def trai(k):
	for i in range(2):
		if check(k,str(i)):
			x[k] = str(i)
			if k == n-1 :
				solution()
			else:
				trai(k+1)

count = 0
x = list()
n = int(input())
for i in range(n):
	x.append(-1)
trai(0)
print(count)