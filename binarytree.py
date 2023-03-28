class Node(object):
    def __init__(self,id):
        self.id = id
        self.leftChild = None
        self.rightChild = None
    
def preOrder(r):
    if r == None:
        return
    print(r.id, end= ' ')
    preOrder(r.leftChild)
    preOrder(r.rightChild)

def inOrder(r):
    if r == None:
        return
    inOrder(r.leftChild)
    print(r.id, end=' ')
    inOrder(r.rightChild)

def postOrder(r):
    if r == None:
        return
    postOrder(r.leftChild)
    postOrder(r.rightChild)
    print(r.id, end=' ')

def find(u,r):
    if r == None:
        return None
    if r.id == u:
        return r
    q = find(u,r.leftChild)
    if q != None:
        return q
    return find(u,r.rightChild)

def addLeftChild(v,u):
#create new node with id = v
    p = find(u,r)
    if p == None:
        return
    q = find(v,r)
    if q != None:
        return
    if p.leftChild != None:
        return
    q = Node(v)
    p.leftChild = q

def addRightChild(v,u):
    p = find(u,r)
    if p == None:
        return
    q = find(v,r)
    if q != None:
        return
    if p.rightChild != None:
        return
    q = Node(v)
    p.rightChild = q

def height(r):
    if r == None:
        return 0
    
    h1 = height(r.rightChild)
    h2 = height(r.leftChild)
    return max(h1,h2) + 1
    
def countLeaves(r):
    if r == None:
        return 0
    if r.leftChild == None and r.rightChild == None:
        return 1
    return countLeaves(r.leftChild) + countLeaves(r.rightChild)

r = Node(3)
addLeftChild(5,3)
addRightChild(1,3)
addLeftChild(4,5)
addRightChild(9,5)
addLeftChild(8,1)
addLeftChild(7,8)
addRightChild(2,8)
inOrder(r)
print()
print(countLeaves(r))