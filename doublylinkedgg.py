class Node(object):
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None

class doubly_linked_list(object):
	def __init__(self):
		self.head = None
	
	def push(self,NewVal):
		NewNode = Node(NewVal)
		NewNode.next = self.head
		if self.head is not None:
			self.head.prev = NewNode
		self.head = NewNode
	
	def listprint(self,node):
		while node is not None:
			print(node.data)
			last = node
			node = node.next
		return last.data #return the last element

	def insert(self,prev_node,NewVal):
		if prev_node is None:
			return
		NewNode = Node(NewVal)
		NewNode.next = prev_node.next
		NewNode.prev = prev_node
		if NewNode.next is not None:
			NewNode.next.prev = NewNode

	def append(self,NewVal):
		NewNode = Node(NewVal)
		NewNode.next = None
		if self.head is None:
			NewNode.prev = None
			self.head = NewNode
			return
		last = self.head
		while last.next is not None:
			last = last.next
		last.next = NewNode
		NewNode.prev = last
		return

	#def delete():


dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.listprint(dllist.head)
print("Last element",dllist.listprint(dllist.head))
