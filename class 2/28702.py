val = -1
num_index = None
for i, num in enumerate(range(3)):
    in_val = input()

    if not num_index and in_val not in ['Fizz', 'Buzz', 'FizzBuzz']:
        num_index = i
        val = int(in_val)
        break

while i < 3:
    i += 1
    val += 1

if val % 5 == 0 and val % 3 == 0:
    print('FizzBuzz')
elif val % 5 == 0:
    print('Buzz')
elif val % 3 == 0:
    print('Fizz')
else:
    print(val)
