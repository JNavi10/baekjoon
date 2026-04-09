A = int(input()) % 1000000007
X = int(input())

# index i means (A^(2^i))
powers = [A]
count = 0
val_count = A
while 2**count < X:
    count += 1
    powers.append(powers[-1]**2 % 1000000007)

binary_str = format(X, 'b')

ans = 1
for i, n in enumerate(reversed(binary_str)):
    if n == '1':
        ans *= powers[i]%1000000007

print(ans%1000000007)