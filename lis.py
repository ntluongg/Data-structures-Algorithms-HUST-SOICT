#Dynamic programming
n = int(input())
a = [int(x) for x in input().split()[:n]]
trace = [-1 for i in range(n)]
s = [0 for i in range(n)]
s[0] = 1
selectSubproblem = 0
solution = 0

for i in range(1,n):
	res = 0
	for j in range(0,i):
		if (a[j] < a[i]) and (s[j] > res):
			res = s[j]
			trace[i] = j
	s[i] = res + 1
	if s[i] > solution:
		solution = s[i]
		selectSubproblem = i
print(solution)
#Time complexity: O(n^2)

x = selectSubproblem
l = [a[x]]
while trace[x] != -1:
	l = [a[trace[x]]] + l
	x = trace[x]
print(l)
