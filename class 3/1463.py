N = int(input())

count = 0

se = set([N])

while 1 not in se:
    temp_set = set()
    for i in se:
        temp_set.add(i-1)
        if i%3==0:
            temp_set.add(i//3)
        if i%2==0:
            temp_set.add(i//2)
    count += 1
    se = temp_set

print(count)