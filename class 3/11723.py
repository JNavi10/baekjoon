import sys

input = sys.stdin.readline

M = int(input())

se = set()
for _ in range(M):
    cmd = input().split()
    match cmd[0]:
        case 'add':
            se.add(int(cmd[1]))
        case 'remove':
            if int(cmd[1]) in se:
                se.remove(int(cmd[1]))
        case 'check':
            if int(cmd[1]) in se:
                print(1)
            else:
                print(0)
        case 'toggle':
            se.remove(int(cmd[1])) if int(cmd[1]) in se else se.add(int(cmd[1]))
        case 'all':
            se = set([i for i in range(1,21)])
        case 'empty':
            se.clear()

