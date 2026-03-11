index = 0
max_num = 0
for i in range(1, 10):
    num = int(input())
    if num > max_num:
        index = i
        max_num = num

print(max_num)
print(index)