n, x = input().split()
x = int(x)
seq = [int(i) for i in input().split()]

for i in seq:
    if i < x:
        print(i, end=' ')