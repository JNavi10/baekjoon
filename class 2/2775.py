T = int(input())




## 재귀 같은거 쓰는거 아니다
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