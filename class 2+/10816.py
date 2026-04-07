N = int(input())

di = dict()

for i in map(int, input().split()):
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

M = int(input())

for i in map(int, input().split()):
    if i in di:
        print(di[i], end= ' ')
    else:
        print(0, end=' ')