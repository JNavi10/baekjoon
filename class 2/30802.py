# 참가자 수
N = int(input())

# 티셔츠 사이즈 별 신청자 수
li_request_by_size = list(map(int, input().split()))

# T = 주문 가능 티셔츠 묶음 단위, P = 주문 가능 펜 묶음 단위
T, P = map(int, input().split())

# T셔츠 최소 몇 묶음인지. T셔츠는 남아도 됨
t_count = 0
while li_request_by_size:
    target_request = li_request_by_size.pop(0)
    quo = target_request // T
    t_count += quo
    if target_request - quo*T:
        t_count += 1
print(t_count)

# 펜 묶음 몇 묶음, 낱개로 몇 개? 펜은 딱 맞아야 함
print(N // P, N % P)


## pop function is slow because it shifts everything
# math.ceil function does the +1 part
"""
N = int(input())
li_request_by_size = list(map(int, input().split()))
T, P = map(int, input().split())

# math.ceil does the "round up to next bundle" logic
import math
t_count = sum(math.ceil(r / T) for r in li_request_by_size)
print(t_count)

print(N // P, N % P)
"""