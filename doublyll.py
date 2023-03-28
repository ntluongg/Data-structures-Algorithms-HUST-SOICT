class Node(object):
    def __init__(self,value):
        self.prev = None
        self.next = None
        self.value = value

def findFromLeft(u,first,last):
    p = first
    while p != None:
        if p.value == u:
            return p
        p = p.next
    return None

def printLeft2Right(first,last):
    p = first
    while p != None:
        print(p.value,end=' ')
        p = p.next
    print()

def printRight2Left(first,last):
    p = last
    while p != None:
        print(p.value,end=' ')
        p = p.prev
    print()

def insertBefore(v,u,first,last):
    if first == None:
        return first,last
    q = Node(v)
    p = findFromLeft(u,first,last)
    if p != None:
        pp = p.prev
        if pp == None:
            q.next = p
            first = q
            p.prev = q
        else:
            q.prev = pp
            q.next = p
            pp.next = q
            p.prev = q
    return first,last

def removeNode(v,first,last):
    p = findFromLeft(v,first,last)
    if p != None:
        if p.prev == None:
            p = first.next
            p.prev = None
            return p, last
        elif p.next == None:
            p = last.prev
            p.next = None
            return first,p
        pp = p.prev
        pn = p.next
        pp.next = pn
        pn.prev = pp
    return first,last

#create nodes
head = Node(0)
first = Node(1)
second = Node(2)
tail = Node(3)

#link nodes
head.next = first
first.prev = head
first.next = second
second.prev = first
second.next = tail
tail.prev = second

printLeft2Right(head,tail)

head,tail = insertBefore(10,0,head,tail)
head,tail = insertBefore(100,3,head,tail)
printLeft2Right(head,tail)

head,tail = insertBefore(999,10000,head,tail)
printLeft2Right(head,tail)