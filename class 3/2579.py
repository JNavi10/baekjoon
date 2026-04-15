import sys
sys.stdin.readline


def max_sum_stairs_with_restraint(stairs):
    # 0: 1칸 움직여서 도착
    # 1: 2칸 움직여서 도착
    # 2: 이전칸에서 2칸 움직여서 도착 못함
    sums = [[0, 0] for _ in range(len(stairs))]

    for i in range(len(stairs)):
        if i == 0:
            sums[i][0] = stairs[i]
            # 2칸 움직여서 도착 못함
            # 스킵하여 변동 없음
        elif i == 1:
            sums[i][0] = sums[i-1][0] + stairs[i]
            sums[i][1] = stairs[i]
        else:
            sums[i][0] += sums[i-1][1] + stairs[i]
            sums[i][1] += max(sums[i-2][0]+stairs[i], sums[i-2][1]+stairs[i])

    return max(sums[-1])

if __name__ == "__main__":
    num_stairs = int(input())

    stairs = []
    for _ in range(num_stairs):
        stairs.append(int(input()))
    print(max_sum_stairs_with_restraint(stairs))