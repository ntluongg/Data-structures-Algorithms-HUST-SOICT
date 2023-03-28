l = list()

while True:
    line = str(input())
    if line == '#':
        break
    c = line.split()
    if c[0] == 'PUSH':
        l.append(int(c[1]))
    else:
        if len(l) > 0:
            popped = l.pop(0)
            print(popped)
        else:
            print('NULL')
