import sys

input = sys.stdin.readline

N = int(input())

li = []
for i in range(N):
    li.append((i,) + tuple(input().split()))

li = [(i[0], int(i[1]), i[2]) for i in li]
li.sort(key=lambda x: x[1])

for i in li:
    print(i[1], i[2])