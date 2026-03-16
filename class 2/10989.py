import sys

input = sys.stdin.readline

N = int(input())

li = [0] * 10001

for _ in range(N):
    i = int(input())
    li[i] += 1

for i in range(10001):
    for j in range(li[i]):
        print(i)

## 기적의 오버헤드를 보이는 input function 
## 밑에거도 됨
"""
import sys

input = sys.stdin.readline

N = int(input())

di = dict()
for _ in range(N):
    i = int(input())
    if i not in di:
        di[i] = 1
    else:
        di[i] += 1

for i in sorted(di.keys()):
    for _ in range(di[i]):
        print(i)
"""