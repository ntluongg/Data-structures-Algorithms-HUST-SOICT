import sys

def input():
    [N] = [int(x) for x in sys.stdin.readline().split()]
    A = [int(x) for x in sys.stdin.readline().split()]
    A.insert(0,0)
    return N,A

#Heap sort
def Swap(i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def heapify(i,N):
    L = 2*i
    R = 2*i + 1
    maxInx = i
    if L <= N and A[L] > A[maxInx]:
        maxInx = L
    if R <= N and A[R] > A[maxInx]:
        maxInx = R
    if maxInx != i:
        Swap(i, maxInx)
        heapify(maxInx, N)

def BuildHeap():
    for i in range(N//2,0,-1):
        heapify(i,N)

def HeapSort():
    BuildHeap()
    for i in range(N,1,-1):
        Swap(1,i)
        heapify(1,i-1)

#Merge sort
def Merge(L, M, R):
    i = L
    j = M+1
    
    for k in range(L, R+1):
        if i > M:
            TA[k] = A[j]
            j += 1
        elif j > R:
            TA[k] = A[i]
            i += 1
        else:
            if A[i] < A[j]:
                TA[k] = A[i]
                i += 1
            else:
                TA[k] = A[j]
                j += 1
    
    for k in range(L, R+1):
        A[k] = TA[k]

def MergeSort(L,R):
    if L >= R:
        return
    M = (L+R)//2
    MergeSort(L, M)
    MergeSort(M+1, R)
    Merge(L, M, R)
#

N,A = input()
TA = [0 for i in range(0, N+1)]
#HeapSort()
MergeSort(1,N)
print(A[1:])