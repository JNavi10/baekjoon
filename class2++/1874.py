import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])
li = [int(input_data[i+1]) for i in range(n)]

stack = []
li_index = 0
count = 1
out = []
really = set()

while True:
    if li[li_index] not in really:
        if count == li[li_index]:
            stack.append(count)
            really.add(count)
            out.append('+')

            pop_val = stack.pop()
            really.remove(pop_val)
            out.append('-')

            count+=1
            li_index+=1
        elif count < li[li_index]:
            stack.append(count)
            really.add(count)
            out.append('+')
            count+=1
        else: 
            out = ['NO']
            break
    else:
        pop_val = stack.pop()
        really.remove(pop_val)
        out.append('-')
        while pop_val != li[li_index]:
            pop_val = stack.pop()
            really.remove(pop_val)
            out.append('-')
        li_index+=1

    if li_index == n:
        if stack:
            out = ['NO']
        break

print('\n'.join(out))

