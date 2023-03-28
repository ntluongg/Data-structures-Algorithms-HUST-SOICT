class Node(object):
	def __init__(self,id):
		self.id = id
		self.next = None

first = None #pointer to the 1st element of the linked-list

def insertlast(v,f):
#create a new node having id = v
#insert this node at the end of the linked list
#return the pointer to the resulting linked list
	if f == None:
		f = Node(v)
		return f
	last = f
	while last.next != None:
		last = last.next
	q = Node(v)
	last.next = q
	return f #the first is not changed

def printlist(f):
	p = f 
	while p != None:
		print(p.id,end=' ')
		p = p.next
	print()

def insertlastRecursive(v,f): #alternative version 
	if f == None:
		f = Node(v)
		return f
	f.next = insertlastRecursive(v,f.next)
	return f

def insertBefore(v,u,f):
	#f: the pointer to 1st node
	#v: the value id of the new node
	#u: the value id of the current node
	
	#case 1: empty list -> return None
	if f == None:
		return f

	#case 2: 1st node has the value u
	if f.id == u:
		q = Node(v)
		q.next = f
		return q
	#case 3: 
	p = f
	while p.next != None:
		if p.next.id == u:
			break
		p = p.next
	
	if p.next != None:
		q = Node(v)
		q.next = p.next
		p.next = q
		return f	
	else:
		#can't find u -> nothing
		return f

def insertBeforeRecursive(v,u,f):
	if f == None:
		return f
	if f.id == u:
		q = Node(v)
		q.next = f
		return q
	f.next = insertBeforeRecursive(v,u,f.next)
	return f

def remove(v,f):
	#f: pointer to the first node of the list
	# remove the element having id = v
	if f == None:
		return f
	
	if f.id == v:
		return f.next

	p = f
	while p.next != None:
		if p.next.id == v:
			break
		p = p.next

	if p.next != None:
		p.next = p.next.next
		return f
	else:
		return f

def removeRecursive(v,f):
	if f == None:
		return None
	
	if f.id == v:
		return f.next
	
	f.next = removeRecursive(v,f.next)
	return f

def removeAllRecursive(v,f):#remove all elements having id = v
	if f == None:
		return None
	
	if f.id == v:
		f = f.next
		f = removeAllRecursive(f)
		return f

	f.next = removeAllRecursive(v, f.next)
	return f

def sum(f):
	if f == None:
		return 0
	s = 0
	p = f
	while True:
		s = s + p.id
		if p.next == None:
			break
		p = p.next
	return s

def sumRecursive(f):
	if f == None:
		return 0
	return f.id + sumRecursive(f.next)

def countNodes(f):
	if f == None:
		return 0
	c = 0
	p = f
	while True:
		c+=1
		if p.next == None:
			break
		p = p.next
	return c

def countNodesRecursive(f):
	if f == None:
		return 0
	return countNodesRecursive(f.next) + 1

def find(u,f):
	p = f
	while p != None:
		if p.id == u:
			return p #return a pointer to the node
		p = p.next
	return None #return nothing

def findRecursive(u,f):
	if f == None:
		return None
	if f.id == u:
		return f
	return findRecursive(u,f.next)

def insertAfter(v,u,f):
	p = find(u,f)
	if p == None:
		return f
	q = find(v,f)
	if q != None: #node v already exists
		return f
	q = Node(v)
	q.next = p.next
	p.next = q
	return f

def inserAfterRecuresive(v,u,f): 
	#assuming node v is not yet in
	if f == None:
		return None
	if f.id == u:
		p = Node(v)
		p.next = f.next
		f.next = p
		return f
	
	f.next = inserAfterRecuresive(v,u,f.next)
	return f

def reverse(f):
	pp = None
	p = f
	np = None
	while p != None:
		np = p.next
		p.next = pp
		pp = p
		p = np
	return pp

def reverseRecursive(f):
	if (f == None):
		return f
	if (f.next == None):
		return f
	f1 = reverse(f.next)
	f.next.next = f
	f.next = None
	return f1

for i in range(3):
	first = insertlastRecursive(i,first)

printlist(first)
print(sumRecursive(first))
first = insertAfter(3,2,first)
printlist(first)
first = reverse(first)
printlist(first)
first = reverseRecursive(first)
printlist(first)