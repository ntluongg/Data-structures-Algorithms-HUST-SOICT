class Node(object):
    def __init__(self, id):
        self.id = id
        self.leftMostChild = None
        self.rightSibling = None

def Insert(r, v):
    if r == None:
        return

    if r.leftMostChild == None:
        r.leftMostChild = Node(v)
        return

    p = r.leftMostChild
    while p.rightSibling != None:
        p = p.rightSibling
    p.rightSibling = Node(v)

def Find(u, r):
    #find and return a node having id = u on the tree rooted at r
    # E.g. apply pre-order traversal on the tree for searching
    if r == None:
        return None
    if r.id == u:
        return r
    p = r.leftMostChild
    while p != None:
        q = Find(u, p)
        if q != None: # the node is found
            return q
        p = p.rightSibling
    return None # not found

def InsertNode(v, u):
    p = Find(u, r)
    Insert(p,v)

def printTree(r):
    if r == None:
        return
    print(r.id, end = ': ')
    p = r.leftMostChild
    while p!= None:
        print(p.id,end=' ')
        p = p.rightSibling
    print()

    p = r.leftMostChild
    while p != None:
        printTree(p)
        p = p.rightSibling

def PreOrderTraversal(r):
    if r == None:
        return
    print(r.id,end=' ')
    p = r.leftMostChild
    while p != None:
        PreOrderTraversal(p)
        p = p.rightSibling

def height(r):
    if r == None:
        return 0

    h = 0
    p = r.leftMostChild
    while p != None:
        hp = height(p)
        if h < hp:
            h = hp
        p = p.rightSibling
    return h + 1

def countNodes(r):
    if r == None:
        return 0

    count = 1
    p = r.leftMostChild
    while p != None:
        count = count + countNodes(p)
        p = p.rightSibling
    return count 

def countLeaves(r):
    if r == None:
        return 0

    if r.leftMostChild == None:
        return 1
    
    p = r.leftMostChild
    count = 0
    while p != None:
        count = count + countLeaves(p)
        p = p.rightSibling
    return count

def depth(v,p):
    if p == None:
        return -1
    if p.id == v:
        return 0

    q = p.leftMostChild

    while q != None:
        a = depth(v,q)
        if a > -1:
            return a + 1
        q = q.rightSibling
    return -1

r = Node(10)
Insert(r,11)
InsertNode(1,10)
InsertNode(3,10)
InsertNode(5,11)
printTree(r)
print(height(r))
print(countNodes(r))
print(countLeaves(r))
print(depth(11,r))