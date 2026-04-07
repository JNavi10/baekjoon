import sys

input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    args = input().split()

    match args[0]:
        case 'push':
            val = int(args[1])
            queue.append(val)
        case 'pop':
            print(queue.pop(0)) if queue else print(-1)
        case 'size':
            print(len(queue))
        case 'empty':
            print(1) if not queue else print(0)
        case 'front':
            print(queue[0]) if queue else print(-1)
        case 'back':
            print(queue[-1]) if queue else print(-1)
        