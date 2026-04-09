K = int(input())

li = []
for _ in range(K):
    val = int(input())
    if val == 0:
        li.pop()
    else:
        li.append(val)

print(sum(li))