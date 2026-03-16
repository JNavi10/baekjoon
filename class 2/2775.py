T = int(input())

def make_floor_above(floor_below:list[int]):
    floor_above = []

    total = 0
    for i in floor_below:
        total += i
        floor_above.append(total)

    return floor_above

for _ in range(T):
    # k층
    k = int(input())
    # n호
    n = int(input())
    # 밑층 arr 1층으로 초기화
    bottom_arr = [i for i in range(1, n+1)]
    if k == 0:
        print(bottom_arr[n-1])
        continue

    curr_floor = 0
    while curr_floor != k:
        # 위층 array 생성
        bottom_arr = make_floor_above(bottom_arr)
        curr_floor += 1
    
    print(bottom_arr[n-1])



## 재귀 같은거 쓰는거 아니다. DP 쓰세요
"""
def head_count(floor_num, room_num):
    if floor_num == 0:
        return room_num
    if room_num == 1:
        return 1
    else:
        total = head_count(floor_num, room_num-1) + head_count(floor_num-1, room_num)
    return total

for _ in range(T):
    # k층
    k = int(input())
    # n호
    n = int(input())
    print(head_count(k,n))

"""