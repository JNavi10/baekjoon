set_int = set()

for i in range(10):
    dividend = int(input())
    set_int.add(dividend%42)

print(len(set_int))