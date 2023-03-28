import sys

class Node():
    def __init__(self, id):
        self.id = id
        self.leftMostChild = None
        self.rightSibling = None

def find(u,r):
    if r == None:
        return None
    if r.id == u:
        return r
    p = r.leftMostChild
    while p!= None:
        q = find(u, p)
        if q != None:
            return q
        p = p.rightSibling
    return None

def insert0(v, r):
    if r == None:
        return 
    
    if r.leftMostChild == None:
        r.leftMostChild = Node(v)
        return 

    p = r.leftMostChild
    while p.rightSibling!= None:
        p = p.rightSibling
    p.rightSibling = Node(v)

def insert(v, u):
    p = find(u, r)
    if find(v, r) != None:
        return
    insert0(v, p)

def preOrder(r):
    if r == None:
        return
    print(r.id, end=' ')
    p = r.leftMostChild
    while p!= None:
        preOrder(p)
        p = p.rightSibling

def inOrder(r):
    if r == None:
        return
    p = r.leftMostChild
    inOrder(p)
    print(r.id, end=' ')
    while p != None:
        p = p.rightSibling
        inOrder(p)

def postOrder(r):
    if r == None:
        return

    p = r.leftMostChild
    while p!= None:
        postOrder(p)
        p = p.rightSibling

    print(r.id, end=' ')

L = []
while True:
    l = [x for x in sys.stdin.readline().split()]
    L.append(l)
    if l[0] == '*':
        break
    
for l in L:
    if l[0] == 'MakeRoot':
        r = Node(int(l[1]))
    if l[0] == 'Insert':
        insert(int(l[1]),int(l[2]))
    if l[0] == 'PreOrder':
        preOrder(r)
        print()
    if l[0] == 'InOrder':
        inOrder(r)
        print()
    if l[0] == 'PostOrder':
        postOrder(r)
        print()
