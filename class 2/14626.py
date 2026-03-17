broken_ISBN = input()

sum = 0
broken_index = -1
for i, char in enumerate(broken_ISBN):
    if char == '*':
        broken_index = i
        char = 0
    if i % 2 == 1:
        sum += 3 * int(char)
    else:
        sum += int(char)

last_digit = sum % 10
if last_digit == 0:
    print(0)
elif broken_index % 2 == 0:
    print(10-last_digit)
else:
    for i in range(10):
        if i * 3 % 10 == 10-last_digit:
            print(i)
