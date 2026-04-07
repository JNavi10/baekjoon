N, K = map(int, input().split())

li = [i for i in range(1, N+1)]
index = 0  # start value inclusive
print('<',end='')
while True:
    index += K-1
    while index >= len(li):
        index -= len(li)
    print(li.pop(index), end='')

    if not li:
        break
    print(',', end=' ')
print('>')