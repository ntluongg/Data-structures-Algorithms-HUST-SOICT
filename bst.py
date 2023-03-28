class Node():
    def __init__(self,inputKey):
        self.key = inputKey
        self.leftChild = None
        self.rightChild = None
    
def insert(r, k):
    if r == None:
        return Node(k)
    if r.key == k:
        return r
    elif r.key < k:
        r.rightChild = insert(r.rightChild, k)
    else:
        r.leftChild = insert(r.leftChild, k)
    return r

def search(r, k):
    if r == None:
        return None
    if r.key == k:
        return r
    elif r.key < k:
        return search(r.rightChild, k)
    else:
        return search(r.leftChild, k)
    
def findMin(r):
    if r == None:
        return None
    lmin = findMin(r.leftChild)
    if lmin != None:
        return lmin
    return r

def delete(r, k):
    if r == None:
        return None
    if r.key < k:
        r.rightChild = delete(r.rightChild, k)
    elif r.key > k:
        r.leftChild = delete(r.leftChild, k)
    else: # when r.key == k
        if r.rightChild != None and r.leftChild != None:
            p = findMin(r.rightChild)
            r.key = p.key
            r.rightChild = delete(r.rightChild, p.key)
        else:
            if r.rightChild == None:
                r = r.leftChild
            else:
                r = r.rightChild
    return r

def inOrder(r):
    if r == None:
        return
    inOrder(r.leftChild)
    print(r.key, end=' ')
    inOrder(r.rightChild)



r = Node(20)
r = insert(r, 10)
r = insert(r, 25)
r = insert(r, 15)
r = insert(r, 22)
r = insert(r, 5)
inOrder(r)
print()

#Find Node
p = search(r, 22)
if p == None:
    print('Cant find node')
else:
    print(p.key)

print(findMin(r).key)

r = delete(r, 5)
print(findMin(r).key)