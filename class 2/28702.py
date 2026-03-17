li = [0]*4

num_found = False
for i in range(3):
    in_val = input()

    if not num_found and in_val not in ['Fizz', 'Buzz', 'FizzBuzz']:
        li[i] = int(in_val)
        num_found = True
    else:
        li[i] = li[i-1] + 1
last_num = li[3]
mod3