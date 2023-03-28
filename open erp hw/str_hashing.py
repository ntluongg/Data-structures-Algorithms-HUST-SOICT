import sys

def main():
    global m
    [n,m] = [int(x) for x in sys.stdin.readline().split()]
    S = []
    for i in range(n):
        [s] = sys.stdin.readline().split()
        S.append(s)
    for s in S:
        print(h(s))

def h(s):
    global m
    h = 0
    l = len(s)
    for i in range(l):
        h = h + (ord(s[i])*256**(l - 1 - i))%m
    return h%m

if __name__ == '__main__':
    main()