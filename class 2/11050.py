N, K = map(int, input().split())

def factorial(i: int):
    if i <= 1:
        return 1
    return i * factorial(i-1)

print(factorial(N)//factorial(K)//factorial(N-K))
