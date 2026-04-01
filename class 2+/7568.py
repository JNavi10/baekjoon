import sys

input = sys.stdin.readline

N = int(input())

li = []
for i in range(N):
    li.append((i,) + tuple(map(int, input().split())))

for a in li:
    count = sum(1 for b in li if b[1] > a[1] and b[2] > a[2])
    print(count + 1, end=' ')