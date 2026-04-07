import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    ps = input().strip()

    while True:
        index = ps.find('()')
        
        if index == -1:
            break
        else:
            ps = ps[:index] + ps[index+2:] 

    if ps == '':
        print('YES')
    else:
        print('NO')