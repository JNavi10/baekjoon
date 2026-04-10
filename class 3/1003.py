import sys
input = sys.stdin.readline

T = int(input())

li_0 = [1, 0]
li_1 = [0, 1]

for i in range(2, 41):
    li_0.append(li_0[i-1]+li_0[i-2])
    li_1.append(li_1[i-1]+li_1[i-2])

for _ in range(T):
    N = int(input())
    print(li_0[N], li_1[N])
