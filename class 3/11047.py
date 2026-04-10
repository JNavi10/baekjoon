import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin_value_li_ascending = []
for _ in range(N):
    coin_value_li_ascending.append(int(input()))

coin_value_li_descending = sorted(coin_value_li_ascending, reverse=True)

coin_count = 0
index = 0
while K > 0:
    if coin_value_li_descending[index] > K:
        index += 1
    else:
        quotient = K // coin_value_li_descending[index]
        coin_count += quotient
        K -= coin_value_li_descending[index] * quotient
        index += 1

print(coin_count)