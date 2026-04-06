import sys

input = sys.stdin.readline

N = int(input())

li_a = set()
for ele in map(int, input().split()):
    li_a.add(ele)

M = int(input())
for val in map(int, input().split()):
    if val in li_a:
        print(1)
    else:
        print(0)