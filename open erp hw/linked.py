class Node(object):
    def __init__(self,value = None):
        self.value = value
        self.next = None

def addlast(k):
    global first

    if first == None:
        first = Node(k)
    if first.value == k:
        return
    p = first
    while p.next != None:
        p = p.next
        if p.value == k:
            return
    q = Node(k)
    p.next = q

def found(k):
    global first
    p = first

    while p!= None:
        if p.value == k:
            return True
        p = p.next
    return False

def addfirst(k):
    global first
    if found(k):
        return 

    q = Node(k)
    q.next = first
    first = q

def printlist():
    global first

    p = first
    while p != None:
        print(p.value,end = ' ')
        p = p.next
    print()

def addbefore(u,v):
    global first
    
    if found(u):
        return

    p = first
    q = Node(u)
    if first == None:
        return
    if first.value == v:
        q.next = first
        first = q
        return
    while (p.next!= None) and (p.next.value != v)  :
        p = p.next
    if p.next == None:
        return
    elif p.next.value == v:
        q.next = p.next
        p.next = q

def addafter(u,v):
    global first

    if found(u):
        return

    p = first
    while (p!= None) and (p.value != v)  :
        p = p.next
    if p == None:
        return
    elif p.value == v:  
        q = Node(u)
        q.next = p.next
        p.next = q

def remove(k):
    global first
    if first == None:
        return
    
    if first.value == k:
        first = first.next
        return

    p = first
    while p.next != None:
        if p.next.value == k:
            break
        p = p.next
    if p.next == None:
        return
    else:
        p.next = p.next.next
    
def reverse():
    global first
    pp = None
    p = first
    np = None
    while p != None:
        np = p.next
        p.next = pp
        pp = p
        p = np
    first = pp


n = input()
first = None
for i in input().split():
    addlast(int(i))
while True:
    l = str(input())
    if l != '#':
        c = l.split()
        if c[0] == 'addlast':
            addlast(int(c[1]))
        elif c[0] == 'addfirst':
            addfirst(int(c[1]))
        elif c[0] == 'addbefore':
            addbefore(int(c[1]),int(c[2]))
        elif c[0] == 'addafter':
            addafter(int(c[1]),int(c[2]))
        elif c[0] == 'remove':
            remove(int(c[1]))
        else:
            reverse()
    else:
        break
printlist()