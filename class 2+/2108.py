N = int(input())

li = []
di = dict()
for _ in range(N):
    temp = int(input())
    li.append(temp)
    if temp in di:
        di[temp] += 1
    else:
        di[temp] = 1

# average
print(sum(li)//N)

# median
print(sorted(li)[N//2])

# mode
sorted_dict = dict(sorted(di.items(), key=lambda item: item[1]))
