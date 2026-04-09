import math

M, N = map(int, input().split())

for i in range(M, N+1):
    divisor = 2
    end = math.sqrt(i)
    not_prime_flag = False
    while divisor <= end:
        if i % divisor == 0:
            not_prime_flag = True
            break
        divisor += 1
    if not not_prime_flag and i != 1:
        print(i)

exit(0)
# It can be sped up trough Sieve of Eratosthenes
# The idea: make a boolean array, mark all multiples of each prime as composite. What's left is prime.
M, N = map(int, input().split())

sieve = [True] * (N + 1)
sieve[0] = sieve[1] = False

for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, N+1, i):
            sieve[j] = False

for i in range(max(M, 2), N + 1):
    if sieve[i]:
        print(i)