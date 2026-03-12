T = int(input())

for i in range(T):
    # 층, 층당 방 수, 몇번쨰 손님 
    H, W, N = map(int, input().split())
    # 층수
    floor_num = N % H
    # 호실
    half_room_num = N // H + 1 # +1 because half_room_num starts at 1
    # 맨 윗층 별도 처리
    if floor_num == 0:
        floor_num = H
        half_room_num -= 1
    # combine
    print(str(floor_num*100+half_room_num))

# 나눠지는 값 dividend가 0으로 시작하는지 1로 시작하는지 확인
# 나눗셈, 나머지는 기본적으로 0베이스라서 0으로 시작해야 edge-case 처리를 안함
"""
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    N -= 1  # shift to 0-indexed
    floor_num = N % H + 1      # +1 to shift back
    room_num = N // H + 1      # +1 to shift back
    print(floor_num * 100 + room_num)
"""