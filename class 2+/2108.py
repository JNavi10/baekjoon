import sys

input = sys.stdin.readline

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
print(round(sum(li)/N))

# median
print(sorted(li)[N//2])

# mode
max_freq = max(di.values())
modes = sorted([k for k, v in di.items() if v == max_freq])
print(modes[1] if len(modes) > 1 else modes[0])

# range
print(max(li) - min(li))