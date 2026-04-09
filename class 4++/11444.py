def fib(n):
    MOD = 1000000007
    if n == 0: return 0

    def mat_mul(A, B):
        return [
            [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
        ]

    powers = [[[1,1],[1,0]]]
    while len(powers) < len(format(n, 'b')):
        powers.append(mat_mul(powers[-1], powers[-1]))

    ans = [[1,0],[0,1]]
    for i, bit in enumerate(reversed(format(n, 'b'))):
        if bit == '1':
            ans = mat_mul(ans, powers[i])

    return ans[0][1] % MOD

n = int(input())
print(fib(n))