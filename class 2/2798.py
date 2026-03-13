from itertools import combinations

N, M = map(int, input().split())
li = list(map(int, input().split()))

ans = float('-inf')

for combo in combinations(li, 3):
    total = sum(combo)
    if abs(total - M) < abs(ans - M) and not total > M:
        ans = total
        if ans == M:
            break

print(ans)

## itertools has combinations functions
## float('-inf') is guaranteed to be worse than any valid answer