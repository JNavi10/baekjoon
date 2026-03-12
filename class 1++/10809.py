input_str = str(input())

li = [-1] * (ord('z') - ord('a') + 1)

for i in range(len(li)):
    li[i] = input_str.find(chr(i+ord('a')))

for char in li:
    print(char, end =' ')