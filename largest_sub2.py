# max sub sequence but in dynamic programming
n = int(input())

a = [int(i) for i in input().split()]

s = [0 for  i in range(n)]

s[0] = a[0]

for i in range(1,n):
	if s[i-1] > 0:
		s[i] = s[i-1] + a[i]
	else:
		s[i] = a[i]
#Time complexity: O(n) 
print(max(s))