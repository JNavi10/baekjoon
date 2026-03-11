num = int(input())

for i in range(1, num+1):
    space = num - i
    for j in range(space):
        print(' ',end='')
    for j in range(i):
        print('*', end='')
    print()