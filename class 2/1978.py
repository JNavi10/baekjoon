import math

N = int(input())

li = list(map(int, input().split()))

prime = 0

for i in li:
    if i == 1:
        continue
    sqrt_i = math.sqrt(i)
    divisor = 2
    while divisor < sqrt_i:
        if i % divisor == 0:
            break
        divisor += 1
    if divisor > sqrt_i:
        prime += 1

print(prime)
