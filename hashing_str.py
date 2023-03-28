import sys

class Node(object):
	def __init__(self,k):
		self.key = k 
		self.leftChild = None
		self.rightChild = None
class BST(object):
	def __init__(self):
		self.root = None
	
	#Private functions
	def __Find__(self,k,r):
		if r == None:
			return None
		if r.key == k:
			return r
		if r.key < k:
			return self.__Find__(k,r.rightChild)
		else:
			return self.__Find__(k,r.leftChild)
	def __Insert__(self,k,r):
		if r == None:


	#Public function
	def Find(self,k):
		return self.__Find__(k,self.root)
	def Insert(self,k):
		self.root = self.__Insert__(k,self.root)

def h(k):
	
	return

def Find(k):
	idx = h(k)
	p = BST[idx].Find(k)
	if p != None:
		return 1
	return 0

def Insert(k):


def run():
	while True:
		line = [x for x in sys.stdin.readline().split()]
		if line[0] == '*':
			break
		DB.append(line[0])

	while True:

m = 10000
BST = [None for i in range(m)]
