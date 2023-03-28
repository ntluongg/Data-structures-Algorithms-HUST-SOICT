import sys
class Node():
    def __int__(self, k):
        self.key = k
        self.rightChild = None
        self.leftChild = None
    
def find(u, r):
    if r == None:
        return r
    if r.key == u:
        return r
    p = find(u, r.leftChild)
    if p != None:
        return p
    return find(u, r.rightChild)

def addLeft(v, u):
    global r
    p = find(u, r)
    if p == None:
        return
    q = find(v, r)
    if q != None:
        return 
    q = Node(v)
    if p.leftChild != None:
        return
    p.leftChild = q

def addRight(v, u):
    global r
    p = find(u, r)
    if p == None:
        return
    q = find(v, r)
    if q != None:
        return 
    q = Node(v)
    if p.rightChild != None:
        return
    p.rightChild = q
    