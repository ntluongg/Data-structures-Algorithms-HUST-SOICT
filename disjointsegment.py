
n = int(input())
L = [0 for i in range(n)]
for i in range(n):
	L[i] = [int(j) for j in input().split()]
L.sort(key = lambda x:x[1])

def disjoint():
	count = 1
	M = L[0][1]
	for index in L[1:]:
		if index[0] > M:
			count+=1
			M = index[1]
	print(count)

disjoint()
