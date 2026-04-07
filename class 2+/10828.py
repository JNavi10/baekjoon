import sys

input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    args = input().split()

    match args[0]:
        case 'push':
            val = int(args[1])
            stack.append(val)
        case 'pop':
            print(stack.pop()) if stack else print(-1)
        case 'size':
            print(len(stack))
        case 'empty':
            print(1) if not stack else print(0)
        case 'top':
            print(stack[-1]) if stack else print(-1)
        