#october 31st 22 
#Divide an conquer example
a = [1,2,3,4,-1,-4,81]

def maxLeft(L,R):
	res = a[R]
	s = 0
	i = R
	while i>=L:
		s = s + a[i]
		res = max(res,s)
		i = i - 1
	return res

def maxRight(L,R):
	res = a[L]
	s = 0
	i = L
	while i<=R:
		s = s + a[i]
		res = max(res,s)
		i = i + 1
	return res

def maxSeq(L,R):
	if L==R:
		return a[L]
	m = (L+R)//2
	mL = maxSeq(L,m)
	mR = maxSeq(m+1,R)
	mLR = maxLeft(L,m) + maxRight(m+1,R)
	return max(mL,mR,mLR)
#time complexity: 
print(maxSeq(0,len(a)-1))