li = list(map(int, input().split()))
i = li[0]

if i != 1 and i != 8:
    print('mixed')
elif i == 1:
    for j in range(1, 9):
        if li[j-1] != j:
            print('mixed')
            break
        i += 1
    if i == 9:
        print('ascending')
elif i == 8:
    for j in range(8, 0, -1):
        if li[8-j] != j:
            print('mixed')
            break
        i -= 1
    if i == 0:
        print('descending')
else:
    pass

# Python's == is overloaded to compare value by value unlike C or Java.
"""
li = list(map(int, input().split()))

if li == list(range(1, 9)):
    print('ascending')
elif li == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')
"""